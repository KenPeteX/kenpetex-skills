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
