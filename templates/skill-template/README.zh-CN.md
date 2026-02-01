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
