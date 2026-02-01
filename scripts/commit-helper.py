#!/usr/bin/env python3
"""
Auto-generate Conventional Commits compliant commit messages.
Analyzes git diff to identify change type and scope.
"""

import os
import subprocess
import sys
from pathlib import Path


# Mapping of file patterns to scope
SCOPE_PATTERNS = {
    r'^VERSION$': 'root',
    r'^README\.md$': 'root',
    r'^README\.zh-CN\.md$': 'root',
    r'^CHANGELOG\.md$': 'root',
    r'^\.gitignore$': 'root',
    r'^scripts/': 'scripts',
    r'^docs/': 'docs',
    r'^skills/([^/]+)/': lambda m: m.group(1),
}

# Mapping of change types based on file changes
TYPE_RULES = {
    # New feature
    'new_feature': {
        'patterns': [r'skills/[^/]+/'],
        'type': 'feat',
    },
    # Documentation
    'documentation': {
        'patterns': [r'\.md$', r'^docs/'],
        'type': 'docs',
    },
    # Chore/Build
    'chore': {
        'patterns': [r'\.json$', r'\.sh$', r'^scripts/'],
        'type': 'chore',
    },
}


def run_git_command(command):
    """Run a git command and return its output."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent.parent
        )
        return result.stdout.strip(), result.returncode
    except Exception as e:
        return str(e), 1


def get_changed_files():
    """Get list of changed files (staged and unstaged)."""
    # Staged files
    output, _ = run_git_command('git diff --name-only --cached')
    staged = set(output.split('\n')) if output else set()

    # Unstaged files
    output, _ = run_git_command('git diff --name-only')
    unstaged = set(output.split('\n')) if output else set()

    return staged | unstaged


def get_file_diff(file_path):
    """Get diff for a specific file."""
    output, _ = run_git_command(f'git diff --cached {file_path} 2>/dev/null || git diff {file_path}')
    return output


def identify_scope(file_path):
    """Identify scope based on file path."""
    import re

    for pattern, scope in SCOPE_PATTERNS.items():
        match = re.search(pattern, file_path)
        if match:
            if callable(scope):
                return scope(match)
            return scope

    return None


def identify_type(changed_files):
    """Identify commit type based on changed files."""
    import re

    # Check if only documentation files were changed
    doc_files = [f for f in changed_files if f.endswith('.md')]
    if len(doc_files) == len(changed_files):
        return 'docs'

    # Check for new files
    for file_path in changed_files:
        output, _ = run_git_command(f'git ls-files --error-unmatch {file_path} 2>/dev/null')
        if output:  # File exists in git
            continue
        # New file
        if 'skills/' in file_path:
            return 'feat'

    # Check for configuration/package files
    for file_path in changed_files:
        if file_path in ['VERSION', '.gitignore'] or 'package.json' in file_path:
            return 'chore'

    return 'chore'  # Default


def generate_subject(scope, type, changed_files):
    """Generate commit subject."""
    file_count = len(changed_files)

    if type == 'docs':
        if scope == 'root':
            return "update documentation"
        else:
            return f"update {scope} documentation"

    elif type == 'feat':
        if file_count == 1:
            return f"add {scope} skill"
        else:
            return "add new skills"

    elif type == 'chore':
        if 'VERSION' in changed_files:
            return "update version"
        elif scope == 'root':
            return "update project configuration"
        else:
            return f"update {scope} configuration"

    return "update project"


def generate_body(scope, type, changed_files):
    """Generate commit body (if needed)."""
    body_parts = []

    # List changed files
    if changed_files:
        body_parts.append("\nChanged files:")
        for file_path in sorted(changed_files):
            body_parts.append(f"  - {file_path}")

    return '\n'.join(body_parts) if body_parts else None


def generate_commit_message():
    """Generate a Conventional Commits message."""
    changed_files = get_changed_files()

    if not changed_files:
        print("No changes detected. Nothing to commit.")
        return None

    # Identify scope - use 'multiple' if multiple scopes detected
    scopes = set()
    for file_path in changed_files:
        scope = identify_scope(file_path)
        if scope:
            scopes.add(scope)

    if len(scopes) == 0:
        scope = 'root'
    elif len(scopes) == 1:
        scope = scopes.pop()
    else:
        scope = 'multiple'

    # Identify type
    commit_type = identify_type(changed_files)

    # Generate subject and body
    subject = generate_subject(scope, commit_type, changed_files)
    body = generate_body(scope, commit_type, changed_files)

    # Build full message
    message = f"{commit_type}({scope}): {subject}"

    if body:
        message += body

    return message


def confirm_and_commit(message):
    """Ask user to confirm and execute commit."""
    print("\n" + "=" * 60)
    print("Generated commit message:")
    print("=" * 60)
    print(message)
    print("=" * 60)

    # Check if files are staged
    output, _ = run_git_command('git diff --name-only --cached')
    staged = set(output.split('\n')) if output else set()

    changed = get_changed_files()

    if len(changed) != len(staged):
        print(f"\nWarning: Only {len(staged)} of {len(changed)} files are staged.")
        print("Run 'git add .' to stage all changes before committing.")

    response = input("\nCommit these changes? (y/n): ").strip().lower()

    if response == 'y':
        # Stage all changes if not already staged
        run_git_command('git add -A')

        # Split message into lines for multi-line commit
        lines = message.split('\n')
        # Escape quotes and other special characters in commit message
        escaped_lines = [line.replace('"', '\\"') for line in lines]

        # Commit with multi-line message
        if len(escaped_lines) == 1:
            commit_cmd = f'git commit -m "{escaped_lines[0]}"'
        else:
            # First line is subject, rest is body
            subject = escaped_lines[0]
            body = escaped_lines[1:]
            # Join body lines with newline characters for git
            body_str = '\\n'.join(body)
            commit_cmd = f'git commit -m "{subject}" -m "{body_str}"'

        output, code = run_git_command(commit_cmd)

        if code == 0:
            print("\n✅ Commit successful!")
            return True
        else:
            print(f"\n❌ Commit failed: {output}")
            return False
    else:
        print("Commit cancelled.")
        return False


def main():
    """Main entry point."""
    message = generate_commit_message()

    if message:
        confirm_and_commit(message)


if __name__ == "__main__":
    main()
