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
