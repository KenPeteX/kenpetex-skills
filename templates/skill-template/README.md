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
