# Claude Skills Framework Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a production-ready Claude Skills library framework with modular design, semantic versioning, and flexible installation.

**Architecture:** Monorepo-style structure with independent skills in `skills/` directory, shared utility scripts for version management and commit generation, support for both npm and manual installation.

**Tech Stack:** Python 3, Bash, npm/Node.js, Git

---

## Task 1: Create Base Directory Structure

**Files:**
- Create: `skills/` (directory)
- Create: `scripts/` (directory)
- Create: `docs/` (directory)
- Create: `templates/` (directory)

**Step 1: Create all directories**

```bash
mkdir -p skills scripts docs templates
```

**Step 2: Verify directories created**

```bash
ls -la
```
Expected: See `skills/`, `scripts/`, `docs/`, `templates/` directories

**Step 3: Commit**

```bash
git add skills/ scripts/ docs/ templates/
git commit -m "chore: create base directory structure"
```

---

## Task 2: Create Root README.md (English)

**Files:**
- Create: `README.md`

**Step 1: Create README.md**

```markdown
# Kenpetex Skills

A curated collection of reusable Claude Code skills for enhancing development workflows.

## Overview

This repository contains production-ready Claude Code skills designed to streamline development processes and improve productivity. Each skill encapsulates specific capabilities and workflows, allowing teams to leverage them in their daily Claude Code sessions.

[🇨🇳 中文文档](./README.zh-CN.md)

## Features

- **Modular Design**: Each skill is independently installable and versioned
- **Production Ready**: Thoroughly tested and documented
- **Flexible Installation**: Support for both npm packages and manual installation
- **Semantic Versioning**: Follows SemVer for predictable updates

## Installation

### npm packages

```bash
# Install all skills
npm install @kenpetex/skills

# Install individual skill
npx @kenpetex/skill-name
```

### Manual Installation

```bash
./scripts/install.sh all
```

## Usage

After installation, use skills directly in Claude Code. Each skill includes detailed documentation and usage examples.

## Available Skills

| Skill | Version | Description |
|-------|---------|-------------|
| <!-- Skills will be listed here --> |

## Version Management

This repository follows Semantic Versioning (SemVer):

- **MAJOR**: Incompatible API changes
- **MINOR**: Backward-compatible functionality additions
- **PATCH**: Backward-compatible bug fixes

## License

MIT License

## Contributing

Contributions are welcome! Please submit issues and pull requests.
```

**Step 2: Verify file created**

```bash
cat README.md | head -10
```
Expected: Shows "# Kenpetex Skills"

**Step 3: Commit**

```bash
git add README.md
git commit -m "docs: add root README.md (English)"
```

---

## Task 3: Create Root README.zh-CN.md (Chinese)

**Files:**
- Create: `README.zh-CN.md`

**Step 1: Create README.zh-CN.md**

```markdown
# Kenpetex Skills

精心设计的 Claude Code 技能集合，用于提升开发工作效率。

## 概述

本仓库包含生产级别的 Claude Code 技能，旨在简化开发流程并提高生产力。每个技能封装了特定的能力和工作流，可以在 Claude Code 中直接使用。

[English](./README.md)

## 特性

- **模块化设计**：每个技能可独立安装和版本控制
- **生产就绪**：经过充分测试和文档化
- **灵活安装**：支持 npm packages 和手动安装两种方式
- **语义化版本**：遵循 SemVer 规范，更新可预测

## 安装

### npm packages

```bash
# 安装所有技能
npm install @kenpetex/skills

# 安装单个技能
npx @kenpetex/skill-name
```

### 手动安装

```bash
./scripts/install.sh all
```

## 使用

安装后，在 Claude Code 中直接使用即可。每个技能都包含详细的文档和使用示例。

## 可用技能

| 技能 | 版本 | 描述 |
|------|------|------|
| <!-- 技能将在此列出 --> |

## 版本管理

本仓库遵循语义化版本控制（SemVer）：

- **MAJOR**：不兼容的 API 变更
- **MINOR**：向后兼容的功能性新增
- **PATCH**：向后兼容的问题修复

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！
```

**Step 2: Verify file created**

```bash
cat README.zh-CN.md | head -10
```
Expected: Shows "# Kenpetex Skills"

**Step 3: Commit**

```bash
git add README.zh-CN.md
git commit -m "docs: add root README.zh-CN.md (Chinese)"
```

---

## Task 4: Create Root VERSION File

**Files:**
- Create: `VERSION`

**Step 1: Create VERSION file**

```bash
echo "0.1.0" > VERSION
```

**Step 2: Verify file content**

```bash
cat VERSION
```
Expected: `0.1.0`

**Step 3: Commit**

```bash
git add VERSION
git commit -m "chore: initialize root VERSION to 0.1.0"
```

---

## Task 5: Create Root CHANGELOG.md

**Files:**
- Create: `CHANGELOG.md`

**Step 1: Create CHANGELOG.md**

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project structure
- Base documentation (English & Chinese)
- Version management framework

## [0.1.0] - 2025-02-01

### Added
- Initial release of Claude Skills framework
```

**Step 2: Verify file created**

```bash
cat CHANGELOG.md | head -15
```
Expected: Shows "# Changelog"

**Step 3: Commit**

```bash
git add CHANGELOG.md
git commit -m "docs: add root CHANGELOG.md"
```

---

## Task 6: Create .gitignore

**Files:**
- Create: `.gitignore`

**Step 1: Create .gitignore**

```text
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
ENV/
env/

# Node
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
package-lock.json
yarn.lock

# Claude Code
.claude/cache/
.claude/tmp/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/

# Temporary files
*.tmp
temp/
tmp/
```

**Step 2: Verify file created**

```bash
cat .gitignore | head -5
```
Expected: Shows "# Python"

**Step 3: Commit**

```bash
git add .gitignore
git commit -m "chore: add .gitignore"
```

---

## Task 7: Create version-manager.py

**Files:**
- Create: `scripts/version-manager.py`

**Step 1: Create version-manager.py**

```python
#!/usr/bin/env python3
"""
Version management tool following SemVer specification.
Supports bumping MAJOR, MINOR, PATCH and pre-release versions.
"""

import re
import sys
from pathlib import Path


class Version:
    """Semantic Version class following SemVer 2.0.0."""

    SEMVER_REGEX = re.compile(
        r'^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)'
        r'(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)'
        r'(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?'
        r'(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$'
    )

    def __init__(self, version_string):
        self.version_string = version_string
        self.major, self.minor, self.patch, self.pre_release, self.build = self._parse(version_string)

    def _parse(self, version_string):
        """Parse version string into components."""
        match = self.SEMVER_REGEX.match(version_string)
        if not match:
            raise ValueError(f"Invalid SemVer version: {version_string}")

        major = int(match.group(1))
        minor = int(match.group(2))
        patch = int(match.group(3))
        pre_release = match.group(4) or None
        build = match.group(5) or None

        return major, minor, patch, pre_release, build

    def bump(self, bump_type, pre_release=None):
        """Bump version according to type."""
        if bump_type == 'major':
            self.major += 1
            self.minor = 0
            self.patch = 0
        elif bump_type == 'minor':
            self.minor += 1
            self.patch = 0
        elif bump_type == 'patch':
            self.patch += 1
        else:
            raise ValueError(f"Invalid bump type: {bump_type}")

        if pre_release:
            self.pre_release = self._get_pre_release_with_increment(pre_release)
        else:
            self.pre_release = None

        return str(self)

    def _get_pre_release_with_increment(self, pre_release_type):
        """Generate pre-release version with increment."""
        if self.pre_release and self.pre_release.startswith(pre_release_type):
            # Increment existing pre-release number
            parts = self.pre_release.split('.')
            if len(parts) > 1 and parts[-1].isdigit():
                parts[-1] = str(int(parts[-1]) + 1)
                return '.'.join(parts)
        return f"{pre_release_type}.1"

    def __str__(self):
        version = f"{self.major}.{self.minor}.{self.patch}"
        if self.pre_release:
            version += f"-{self.pre_release}"
        if self.build:
            version += f"+{self.build}"
        return version


def get_root_version():
    """Get root VERSION file content."""
    version_file = Path(__file__).parent.parent / "VERSION"
    return version_file.read_text().strip()


def get_skill_version(skill_name):
    """Get skill VERSION file content."""
    version_file = Path(__file__).parent.parent / "skills" / skill_name / "VERSION"
    return version_file.read_text().strip()


def update_root_version(new_version):
    """Update root VERSION file."""
    version_file = Path(__file__).parent.parent / "VERSION"
    version_file.write_text(new_version + "\n")


def update_skill_version(skill_name, new_version):
    """Update skill VERSION file."""
    version_file = Path(__file__).parent.parent / "skills" / skill_name / "VERSION"
    version_file.write_text(new_version + "\n")


def list_skills():
    """List all skills in the skills directory."""
    skills_dir = Path(__file__).parent.parent / "skills"
    if not skills_dir.exists():
        return []

    skills = []
    for skill_dir in skills_dir.iterdir():
        if skill_dir.is_dir() and not skill_dir.name.startswith('.'):
            version_file = skill_dir / "VERSION"
            if version_file.exists():
                version = version_file.read_text().strip()
                skills.append((skill_dir.name, version))

    return sorted(skills)


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python version-manager.py status")
        print("  python version-manager.py list")
        print("  python version-manager.py bump <major|minor|patch> [--pre-release <alpha|beta|rc>]")
        print("  python version-manager.py bump <skill-name> <major|minor|patch> [--pre-release <alpha|beta|rc>]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "status":
        root_version = get_root_version()
        print(f"Root version: {root_version}")

        skills = list_skills()
        if skills:
            print("\nSkills:")
            for skill_name, version in skills:
                print(f"  {skill_name}: {version}")

    elif command == "list":
        skills = list_skills()
        print("Available skills:")
        for skill_name, version in skills:
            print(f"  {skill_name} ({version})")

    elif command == "bump":
        if len(sys.argv) < 3:
            print("Error: Missing arguments")
            print("Usage: python version-manager.py bump <major|minor|patch> [--pre-release <type>]")
            print("       python version-manager.py bump <skill-name> <major|minor|patch> [--pre-release <type>]")
            sys.exit(1)

        # Check if first argument is a skill name
        skills = [s[0] for s in list_skills()]
        if sys.argv[2] in skills:
            skill_name = sys.argv[2]
            bump_type = sys.argv[3]
            current_version = get_skill_version(skill_name)
            update_func = update_skill_version
            prefix = f"{skill_name}"
        else:
            skill_name = None
            bump_type = sys.argv[2]
            current_version = get_root_version()
            update_func = update_root_version
            prefix = "Root"

        # Parse pre-release option
        pre_release = None
        if "--pre-release" in sys.argv:
            idx = sys.argv.index("--pre-release")
            if idx + 1 < len(sys.argv):
                pre_release = sys.argv[idx + 1]

        # Validate bump_type
        if bump_type not in ["major", "minor", "patch"]:
            print(f"Error: Invalid bump type '{bump_type}'. Use major, minor, or patch.")
            sys.exit(1)

        # Validate pre_release type
        if pre_release and pre_release not in ["alpha", "beta", "rc"]:
            print(f"Error: Invalid pre-release type '{pre_release}'. Use alpha, beta, or rc.")
            sys.exit(1)

        # Bump version
        version = Version(current_version)
        new_version = version.bump(bump_type, pre_release)
        update_func(skill_name, new_version)

        print(f"{prefix} version: {current_version} -> {new_version}")

    else:
        print(f"Error: Unknown command '{command}'")
        sys.exit(1)


if __name__ == "__main__":
    main()
```

**Step 2: Make script executable**

```bash
chmod +x scripts/version-manager.py
```

**Step 3: Test status command**

```bash
python scripts/version-manager.py status
```
Expected: `Root version: 0.1.0`

**Step 4: Test list command**

```bash
python scripts/version-manager.py list
```
Expected: `Available skills:` (no skills yet)

**Step 5: Commit**

```bash
git add scripts/version-manager.py
git commit -m "feat: add version-manager.py with SemVer support"
```

---

## Task 8: Create commit-helper.py

**Files:**
- Create: `scripts/commit-helper.py`

**Step 1: Create commit-helper.py**

```python
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

        # Commit
        output, code = run_git_command(f'git commit -m "{message.replace(chr(10), "\\n")}"')

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
```

**Step 2: Make script executable**

```bash
chmod +x scripts/commit-helper.py
```

**Step 3: Test with no changes**

```bash
python scripts/commit-helper.py
```
Expected: `No changes detected. Nothing to commit.`

**Step 4: Commit**

```bash
git add scripts/commit-helper.py
git commit -m "feat: add commit-helper.py for Conventional Commits"
```

---

## Task 9: Create install.sh

**Files:**
- Create: `scripts/install.sh`

**Step 1: Create install.sh**

```bash
#!/bin/bash
# Skill installation/uninstallation/update script

set -e

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
SKILLS_DIR="$PROJECT_ROOT/skills"
CLAUDE_SKILLS_DIR="$HOME/.claude/skills"
CLAUDE_PLUGINS_DIR="$HOME/.claude/plugins"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Functions
print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

list_skills() {
    print_info "Available skills:"
    echo ""

    if [ ! -d "$SKILLS_DIR" ]; then
        print_warning "No skills directory found."
        return 1
    fi

    local count=0
    for skill_dir in "$SKILLS_DIR"/*/; do
        if [ -d "$skill_dir" ]; then
            skill_name=$(basename "$skill_dir")
            version_file="$skill_dir/VERSION"

            if [ -f "$version_file" ]; then
                version=$(cat "$version_file")
                echo "  • $skill_name (v$version)"
                ((count++))
            fi
        fi
    done

    if [ $count -eq 0 ]; then
        print_warning "No skills found."
    fi

    echo ""
}

install_skill() {
    local skill_name="$1"
    local skill_source="$SKILLS_DIR/$skill_name"
    local skill_dest="$CLAUDE_SKILLS_DIR/$skill_name"

    # Check if skill exists
    if [ ! -d "$skill_source" ]; then
        print_error "Skill '$skill_name' not found in $SKILLS_DIR"
        return 1
    fi

    # Check if skill has SKILL.md
    if [ ! -f "$skill_source/SKILL.md" ]; then
        print_error "Skill '$skill_name' does not have a SKILL.md file"
        return 1
    fi

    print_info "Installing '$skill_name'..."

    # Create destination directory
    mkdir -p "$CLAUDE_SKILLS_DIR"

    # Copy skill directory
    cp -r "$skill_source" "$skill_dest"

    # Make scripts executable
    find "$skill_dest/scripts" -type f -name "*.py" -exec chmod +x {} \; 2>/dev/null || true
    find "$skill_dest/scripts" -type f -name "*.sh" -exec chmod +x {} \; 2>/dev/null || true

    print_success "Installed '$skill_name' to $skill_dest"
}

install_all() {
    print_info "Installing all skills..."

    if [ ! -d "$SKILLS_DIR" ]; then
        print_error "No skills directory found."
        return 1
    fi

    local installed=0
    local failed=0

    for skill_dir in "$SKILLS_DIR"/*/; do
        if [ -d "$skill_dir" ]; then
            skill_name=$(basename "$skill_dir")

            if install_skill "$skill_name"; then
                ((installed++))
            else
                ((failed++))
            fi
        fi
    done

    echo ""
    print_success "Installation complete: $installed installed, $failed failed"
}

uninstall_skill() {
    local skill_name="$1"
    local skill_dest="$CLAUDE_SKILLS_DIR/$skill_name"

    if [ ! -d "$skill_dest" ]; then
        print_warning "Skill '$skill_name' is not installed."
        return 0
    fi

    print_info "Uninstalling '$skill_name'..."
    rm -rf "$skill_dest"
    print_success "Uninstalled '$skill_name'"
}

update_skill() {
    local skill_name="$1"

    print_info "Updating '$skill_name'..."
    uninstall_skill "$skill_name"
    install_skill "$skill_name"
}

update_all() {
    print_info "Updating all installed skills..."

    if [ ! -d "$CLAUDE_SKILLS_DIR" ]; then
        print_warning "No skills directory found in $CLAUDE_SKILLS_DIR"
        return 0
    fi

    local updated=0
    local failed=0

    for skill_dir in "$CLAUDE_SKILLS_DIR"/*/; do
        if [ -d "$skill_dir" ]; then
            skill_name=$(basename "$skill_dir")

            if [ -d "$SKILLS_DIR/$skill_name" ]; then
                if update_skill "$skill_name"; then
                    ((updated++))
                else
                    ((failed++))
                fi
            else
                print_warning "Skipping '$skill_name' - not found in source"
            fi
        fi
    done

    echo ""
    print_success "Update complete: $updated updated, $failed failed"
}

show_help() {
    cat << EOF
Kenpetex Skills Installation Script

Usage: $0 <command> [skill-name]

Commands:
  list           List all available skills
  all            Install all skills
  <skill-name>   Install a specific skill
  uninstall      Uninstall a specific skill
  update         Update a specific skill
  update-all     Update all installed skills
  help           Show this help message

Examples:
  $0 list
  $0 all
  $0 my-skill
  $0 uninstall my-skill
  $0 update my-skill
  $0 update-all

EOF
}

# Main
main() {
    if [ $# -eq 0 ]; then
        show_help
        exit 0
    fi

    case "$1" in
        list)
            list_skills
            ;;
        all)
            install_all
            ;;
        uninstall)
            if [ -z "$2" ]; then
                print_error "Please specify a skill name to uninstall"
                echo "Usage: $0 uninstall <skill-name>"
                exit 1
            fi
            uninstall_skill "$2"
            ;;
        update)
            if [ -z "$2" ]; then
                print_error "Please specify a skill name to update"
                echo "Usage: $0 update <skill-name>"
                exit 1
            fi
            update_skill "$2"
            ;;
        update-all)
            update_all
            ;;
        help|--help|-h)
            show_help
            ;;
        *)
            # Assume it's a skill name to install
            install_skill "$1"
            ;;
    esac
}

main "$@"
```

**Step 2: Make script executable**

```bash
chmod +x scripts/install.sh
```

**Step 3: Test list command**

```bash
./scripts/install.sh list
```
Expected: Shows available skills list (currently empty)

**Step 4: Test help command**

```bash
./scripts/install.sh help
```
Expected: Shows help message

**Step 5: Commit**

```bash
git add scripts/install.sh
git commit -m "feat: add install.sh script for skill management"
```

---

## Task 10: Create Skill Template

**Files:**
- Create: `templates/skill-template/SKILL.md`
- Create: `templates/skill-template/README.md`
- Create: `templates/skill-template/README.zh-CN.md`
- Create: `templates/skill-template/package.json`
- Create: `templates/skill-template/VERSION`
- Create: `templates/skill-template/CHANGELOG.md`
- Create: `templates/skill-template/.gitignore`
- Create: `templates/skill-template/scripts/main.py`
- Create: `templates/skill-template/scripts/__init__.py`

**Step 1: Create template directory**

```bash
mkdir -p templates/skill-template/scripts
```

**Step 2: Create SKILL.md**

```bash
cat > templates/skill-template/SKILL.md << 'EOF'
---
name: skill-template
description: |
  Skill description in English.
  技能描述（支持中文）。
  Triggers: "keyword1", "keyword2", "/command"
---

# Skill Template

A template for creating new Claude Code skills.

## Overview

This is a template skill that demonstrates the structure and conventions for creating new Claude Code skills.

[🇨🇳 中文文档](./README.zh-CN.md)

## Features

- Feature 1
- Feature 2

## Usage

Describe how to use this skill.

## Implementation

Describe the implementation details.
EOF
```

**Step 3: Create README.md**

```bash
cat > templates/skill-template/README.md << 'EOF'
# Skill Template

A template for creating new Claude Code skills.

## Overview

This template provides the standard structure and conventions for creating new skills in the Kenpetex Skills library.

[🇨🇳 中文文档](./README.zh-CN.md)

## Features

- Standard skill structure following Claude Code specifications
- Pre-configured package.json for npm publishing
- Bilingual documentation (English & Chinese)
- Semantic versioning support

## Usage

### Using the Template

1. Copy this template to a new skill directory
2. Replace placeholders with your skill-specific content
3. Update SKILL.md with skill description and triggers
4. Implement your skill logic in `scripts/main.py`
5. Test and document thoroughly

### File Structure

```
skill-name/
├── SKILL.md               # Claude Code skill definition
├── README.md              # English documentation
├── README.zh-CN.md        # Chinese documentation
├── package.json           # npm package configuration
├── VERSION                # Skill version
├── CHANGELOG.md           # Changelog
├── scripts/
│   ├── main.py           # Main skill logic
│   └── __init__.py       # Python package init
└── .gitignore            # Skill-specific ignores
```

## Installation

### npm

```bash
npx @kenpetex/skill-name
```

### Manual

```bash
./scripts/install.sh skill-name
```

## Development

### Running the Skill

```bash
python scripts/main.py
```

### Testing

Add tests following TDD principles:
1. Write failing test
2. Run test to verify it fails
3. Write minimal implementation
4. Run test to verify it passes
5. Refactor and commit

## License

MIT License
EOF
```

**Step 4: Create README.zh-CN.md**

```bash
cat > templates/skill-template/README.zh-CN.md << 'EOF'
# Skill Template

用于创建新 Claude Code 技能的模板。

## 概述

此模板提供了在 Kenpetex Skills 库中创建新技能的标准结构和约定。

[English](./README.md)

## 特性

- 遵循 Claude Code 规范的标准技能结构
- 预配置的 package.json 用于 npm 发布
- 双语文档（英文和中文）
- 语义化版本控制支持

## 使用

### 使用模板

1. 将此模板复制到新的技能目录
2. 用技能特定的内容替换占位符
3. 使用技能描述和触发器更新 SKILL.md
4. 在 `scripts/main.py` 中实现技能逻辑
5. 测试并完整文档

### 文件结构

```
skill-name/
├── SKILL.md               # Claude Code 技能定义
├── README.md              # 英文文档
├── README.zh-CN.md        # 中文文档
├── package.json           # npm 包配置
├── VERSION                # 技能版本
├── CHANGELOG.md           # 变更日志
├── scripts/
│   ├── main.py           # 主技能逻辑
│   └── __init__.py       # Python 包初始化
└── .gitignore            # 技能特定忽略规则
```

## 安装

### npm

```bash
npx @kenpetex/skill-name
```

### 手动

```bash
./scripts/install.sh skill-name
```

## 开发

### 运行技能

```bash
python scripts/main.py
```

### 测试

遵循 TDD 原则添加测试：
1. 编写失败的测试
2. 运行测试验证失败
3. 编写最小实现
4. 运行测试验证通过
5. 重构并提交

## 许可证

MIT License
EOF
```

**Step 5: Create package.json**

```bash
cat > templates/skill-template/package.json << 'EOF'
{
  "name": "@kenpetex/skill-template",
  "version": "0.1.0",
  "description": "Skill template for creating new Claude Code skills",
  "bin": {},
  "files": [
    "SKILL.md",
    "README.md",
    "README.zh-CN.md",
    "scripts/",
    "VERSION"
  ],
  "keywords": [
    "claude-code",
    "skill",
    "template"
  ],
  "author": "kenpetex",
  "license": "MIT"
}
EOF
```

**Step 6: Create VERSION**

```bash
echo "0.1.0" > templates/skill-template/VERSION
```

**Step 7: Create CHANGELOG.md**

```bash
cat > templates/skill-template/CHANGELOG.md << 'EOF'
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial skill template
EOF
```

**Step 8: Create .gitignore**

```bash
cat > templates/skill-template/.gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so

# Logs
*.log

# Temporary files
*.tmp
temp/
tmp/
EOF
```

**Step 9: Create scripts/__init__.py**

```bash
cat > templates/skill-template/scripts/__init__.py << 'EOF'
"""Skill initialization module."""

__version__ = "0.1.0"
EOF
```

**Step 10: Create scripts/main.py**

```bash
cat > templates/skill-template/scripts/main.py << 'EOF'
#!/usr/bin/env python3
"""
Main skill execution logic.

This module contains the primary logic for the skill.
"""

import sys
import argparse


def main():
    """Main entry point for the skill."""
    parser = argparse.ArgumentParser(description="Skill description")
    parser.add_argument("--version", action="version", version="skill-template 0.1.0")

    args = parser.parse_args()

    # Implement skill logic here
    print("Skill executed successfully!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
EOF
```

**Step 11: Make main.py executable**

```bash
chmod +x templates/skill-template/scripts/main.py
```

**Step 12: Verify template structure**

```bash
find templates/skill-template -type f | sort
```
Expected:
```
templates/skill-template/.gitignore
templates/skill-template/CHANGELOG.md
templates/skill-template/README.md
templates/skill-template/README.zh-CN.md
templates/skill-template/SKILL.md
templates/skill-template/VERSION
templates/skill-template/package.json
templates/skill-template/scripts/__init__.py
templates/skill-template/scripts/main.py
```

**Step 13: Commit**

```bash
git add templates/
git commit -m "feat: add skill template with standard structure"
```

---

## Task 11: Create Root CHANGELOG.md (Update with Implementation)

**Files:**
- Modify: `CHANGELOG.md`

**Step 1: Update CHANGELOG.md with implementation details**

```bash
cat > CHANGELOG.md << 'EOF'
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project structure
- Base documentation (English & Chinese)
- Version management framework with SemVer support
- Conventional Commits auto-generation
- Skill installation/management script
- Skill template for new skills

## [0.1.0] - 2025-02-01

### Added
- Initial release of Claude Skills framework
- Modular skill library architecture
- Bilingual documentation support
- Semantic versioning for root and individual skills
- Automatic Conventional Commits generation
- Flexible installation (npm + manual)
- Comprehensive skill template
EOF
```

**Step 2: Verify update**

```bash
cat CHANGELOG.md
```

**Step 3: Commit**

```bash
git add CHANGELOG.md
git commit -m "docs: update CHANGELOG.md with implementation details"
```

---

## Task 12: Update Root VERSION to 0.1.0

**Files:**
- Modify: `VERSION`

**Step 1: Update VERSION file**

```bash
python scripts/version-manager.py bump patch
```
Expected: `Root version: 0.1.0 -> 0.1.1`

**Step 2: Verify version**

```bash
cat VERSION
```
Expected: `0.1.1`

**Step 3: Commit**

```bash
git add VERSION
git commit -m "chore: bump root version to 0.1.1"
```

---

## Task 13: Verify Project Structure

**Files:**
- Verify: Complete project structure

**Step 1: Display final project structure**

```bash
tree -L 3 -a --dirsfirst 2>/dev/null || find . -type f -o -type d | grep -v ".git" | sort
```

Expected structure:
```
.
├── CHANGELOG.md
├── README.md
├── README.zh-CN.md
├── VERSION
├── docs/
│   └── plans/
│       ├── 2025-02-01-claude-skills-framework-design.md
│       └── 2025-02-01-claude-skills-framework-implementation.md
├── scripts/
│   ├── commit-helper.py
│   ├── install.sh
│   └── version-manager.py
├── skills/
└── templates/
    └── skill-template/
        ├── .gitignore
        ├── CHANGELOG.md
        ├── README.md
        ├── README.zh-CN.md
        ├── SKILL.md
        ├── VERSION
        ├── package.json
        └── scripts/
            ├── __init__.py
            └── main.py
```

**Step 2: Test all scripts**

```bash
echo "=== Testing version-manager.py ==="
python scripts/version-manager.py status
python scripts/version-manager.py list

echo -e "\n=== Testing install.sh ==="
./scripts/install.sh help
./scripts/install.sh list

echo -e "\n=== Testing commit-helper.py ==="
echo "# Test" > test.md
git add test.md
python scripts/commit-helper.py
```

**Step 3: Cleanup test file**

```bash
rm -f test.md
```

**Step 4: Final commit**

```bash
python scripts/commit-helper.py
```

---

## Implementation Complete

The Claude Skills Framework is now fully implemented with:

- ✅ Base directory structure
- ✅ Bilingual documentation (English & Chinese)
- ✅ Version management with SemVer support
- ✅ Conventional Commits auto-generation
- ✅ Skill installation/management script
- ✅ Comprehensive skill template
- ✅ Git ignore rules
- ✅ Changelog documentation

### Next Steps

1. Create new skills using the template in `templates/skill-template/`
2. Publish skills to npm (optional)
3. Add tests for skills
4. Document individual skill usage

### Usage Examples

```bash
# List all skills
./scripts/install.sh list

# Create a new skill
cp -r templates/skill-template skills/my-new-skill
cd skills/my-new-skill
# Edit files to implement your skill

# Install a skill
./scripts/install.sh my-new-skill

# Update version
cd ../..
python scripts/version-manager.py bump my-new-skill minor

# Commit changes
python scripts/commit-helper.py
```
