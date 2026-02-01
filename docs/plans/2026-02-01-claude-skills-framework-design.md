# Claude Skills Framework Design

## Overview

A production-ready framework for managing a personal Claude Code skills library with modular design, semantic versioning, and flexible installation options.

## Directory Structure

```
kenpetex-skills/                    # Root directory
├── skills/                         # All skills storage
│   ├── skill-1/                    # Skill 1 (independent)
│   │   ├── SKILL.md               # Skill definition (required)
│   │   ├── README.md              # Skill documentation (recommended)
│   │   ├── README.zh-CN.md        # Chinese documentation (recommended)
│   │   ├── package.json           # npm configuration (required)
│   │   ├── VERSION                # Skill version (required)
│   │   ├── CHANGELOG.md           # Changelog (recommended)
│   │   ├── scripts/               # Skill-specific scripts
│   │   └── ...                    # Other skill files
│   └── skill-2/                    # Skill 2 (independent)
│       └── ...
├── scripts/                        # Global utility scripts
│   ├── commit-helper.py           # Conventional Commits generator
│   ├── version-manager.py         # Version management tool
│   └── install.sh                 # Installation script
├── .claude-plugin/                 # Claude Code plugin config (optional)
│   └── marketplace.json           # Marketplace configuration
├── VERSION                         # Root version number
├── README.md                       # Root documentation (English)
├── README.zh-CN.md                 # Root documentation (Chinese)
├── CHANGELOG.md                    # Root changelog
└── .gitignore                      # Git ignore rules
```

## Skill Internal Structure

```
skill-name/
├── SKILL.md                       # Required - Claude Code skill definition
├── README.md                      # Recommended - English documentation
├── README.zh-CN.md                # Recommended - Chinese documentation
├── package.json                   # Required - npm package config
├── VERSION                        # Required - Independent skill version
├── CHANGELOG.md                   # Recommended - Skill changelog
├── scripts/                       # Optional - Skill-specific scripts
│   ├── main.py                    # Main execution logic
│   └── utils.py                   # Helper functions
├── templates/                     # Optional - Template files
├── references/                    # Optional - Reference materials
└── .gitignore                     # Optional - Skill-specific ignores
```

## SKILL.md Specification

```yaml
---
name: skill-name
description: |
  Skill description in English
  技能描述（支持中文）
  Triggers: "keyword1", "keyword2", "/command"
---
```

## package.json Specification

```json
{
  "name": "@kenpetex/skill-name",
  "version": "1.0.0",
  "description": "Skill description",
  "bin": {
    "skill-name": "./scripts/main.py"
  },
  "files": [
    "SKILL.md",
    "README.md",
    "README.zh-CN.md",
    "scripts/",
    "VERSION"
  ],
  "keywords": ["claude-code", "skill"],
  "author": "kenpetex",
  "license": "MIT"
}
```

## Version Control

### Version Format

**Root version** (`VERSION` file):
```
1.2.0
```

**Skill version** (`skill-name/VERSION` file):
```
2.1.3
```

### Pre-release Format

```
1.0.0-alpha.1   # Internal testing
1.0.0-beta.2    # Public testing
1.0.0-rc.3      # Release candidate
```

### SemVer Rules

- **MAJOR**: Incompatible API changes
- **MINOR**: Backward-compatible functionality additions
- **PATCH**: Backward-compatible bug fixes

### version-manager.py Commands

```bash
# View current version
python scripts/version-manager.py status

# Update root version
python scripts/version-manager.py bump major  # 1.0.0 -> 2.0.0
python scripts/version-manager.py bump minor  # 1.2.0 -> 1.3.0
python scripts/version-manager.py bump patch  # 1.2.3 -> 1.2.4

# Update specific skill version
python scripts/version-manager.py bump skill-name major
python scripts/version-manager.py bump skill-name minor --pre-release beta

# Generate CHANGELOG.md
python scripts/version-manager.py changelog
```

## Conventional Commits Workflow

### commit-helper.py Functionality

```bash
# Main command
python scripts/commit-helper.py

# Execution flow:
# 1. Analyze git diff to identify change type and scope
# 2. Generate commit message in Conventional Commits format
# 3. Display for user confirmation
# 4. Execute git commit after confirmation
```

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Auto-identified Commit Types

| Type | Description | Trigger Conditions |
|------|-------------|-------------------|
| `feat` | New feature | New files or new functionality code |
| `fix` | Bug fix | Bug fixes or error corrections |
| `docs` | Documentation | Only changes to .md files |
| `style` | Code formatting | Formatting-only changes |
| `refactor` | Refactoring | Code refactoring (non-feature, non-fix) |
| `chore` | Build/tool | Config files, scripts changes |
| `perf` | Performance | Performance-related changes |

### Scope Auto-identification

- Root directory changes → `root`
- `skills/skill-name/` changes → `skill-name`
- Multiple skill changes → `multiple`

### Example Output

```
🔍 Detected changes:

Modified:
  - skills/my-skill/README.md
  - VERSION

📝 Generated commit message:

---
docs(root): update VERSION and add skill documentation

Update root version to 1.0.0 and add README for my-skill.
---

Confirm commit? (y/n)
```

## Installation Methods

### Method 1: npm packages (npx)

Each skill is published as an independent npm package:

```bash
# Install individual skill
npx @kenpetex/skill-name

# Or install globally
npm install -g @kenpetex/skill-name
```

### Method 2: Manual Installation to Claude Code

```bash
# Use provided installation script
./scripts/install.sh

# Or manually copy to Claude plugin directory
cp -r skills/skill-name ~/.claude/skills/skill-name
```

### install.sh Commands

```bash
# List all available skills
./scripts/install.sh list

# Install all skills
./scripts/install.sh all

# Install specific skill
./scripts/install.sh skill-name

# Uninstall skill
./scripts/install.sh uninstall skill-name

# Update installed skills
./scripts/install.sh update
```

### .claude-plugin/marketplace.json

```json
{
  "name": "kenpetex-skills",
  "version": "1.0.0",
  "description": "Personal Claude Skills Library by kenpetex",
  "plugins": [
    {
      "name": "skill-name",
      "version": "1.0.0",
      "description": "Skill description",
      "source": "skills/skill-name"
    }
  ]
}
```

## README.md Specification

### Root README.md (English)

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
| [skill-1](skills/skill-1/) | 1.2.0 | Skill description |
| [skill-2](skills/skill-2/) | 2.1.0 | Skill description |

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

### Root README.zh-CN.md (Chinese)

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
| [skill-1](skills/skill-1/) | 1.2.0 | 技能描述 |
| [skill-2](skills/skill-2/) | 2.1.0 | 技能描述 |

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

## Skill README Specification

### Skill README.md (English)

```markdown
# Skill Name

Concise description of what this skill does.

## Overview

A more detailed description of the skill's purpose and capabilities.

[🇨🇳 中文文档](./README.zh-CN.md)

## Features

- Feature 1
- Feature 2

## Installation

### npm

```bash
npx @kenpetex/skill-name
```

### Manual

```bash
cp -r ~/.claude/skills/skill-name ~/.claude/skills/
```

## Usage

Detailed usage examples and instructions.

## FAQ

Common questions and answers.

## License

MIT License
```

### Skill README.zh-CN.md (Chinese)

```markdown
# Skill Name

技能简短描述

## 概述

更详细的技能描述，说明技能的目的和能力。

[English](./README.md)

## 功能

- 功能1
- 功能2

## 安装

### npm

```bash
npx @kenpetex/skill-name
```

### 手动

```bash
cp -r ~/.claude/skills/skill-name ~/.claude/skills/
```

## 使用

详细的使用示例和说明。

## FAQ

常见问题和解答。

## 许可证

MIT License
```

## File Naming Conventions

| Language | Standard Naming |
|----------|----------------|
| English (default) | `README.md` |
| 简体中文 | `README.zh-CN.md` |
| 繁体中文 | `README.zh-TW.md` |
| 日语 | `README.ja.md` |
| 韩语 | `README.ko.md` |

## Tool Scripts

### commit-helper.py

```python
#!/usr/bin/env python3
"""
Auto-generate Conventional Commits compliant commit messages
"""

def analyze_changes():
    """Analyze git diff, identify change type and scope"""
    # 1. Get list of changed files
    # 2. Identify scope based on file paths
    # 3. Identify type based on change content
    pass

def generate_commit_message(type, scope, changes):
    """Generate commit message"""
    # 1. Generate subject line
    # 2. Generate body (if needed)
    # 3. Display for user confirmation
    pass
```

### version-manager.py

```python
#!/usr/bin/env python3
"""
Version management tool, following SemVer specification
"""

def bump_version(version, type, pre_release=None):
    """Bump version number"""
    # Support major/minor/patch and pre-release tags
    pass

def update_changelog(old_version, new_version):
    """Generate CHANGELOG.md"""
    pass
```

### install.sh

```bash
#!/bin/bash
"""
Skill installation/uninstallation/update script
"""

# Commands:
# list       - List all skills
# all        - Install all skills
# <name>     - Install specific skill
# uninstall  - Uninstall skill
# update     - Update installed skills
```

## Implementation Priorities

1. Create base directory structure
2. Implement root README files (English + Chinese)
3. Implement version-manager.py
4. Implement commit-helper.py
5. Implement install.sh
6. Create skill template
7. Add .gitignore
8. Initial commit

## Notes

- All documentation must be bilingual (English + Chinese)
- Version numbers follow SemVer strictly
- Commit messages follow Conventional Commits
- Each skill is fully independent with its own package.json
- Both npm and manual installation are supported
