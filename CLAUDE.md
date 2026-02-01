# Kenpetex Skills - Claude Code Guidelines

> 本文件定义了本项目开发流程和规范，Claude Code 在执行任务时必须遵守。
> This file defines development workflow and standards that Claude Code must follow when executing tasks.

---

## 1. New Task Development Workflow

**所有新功能开发任务必须遵循此流程：**

### Step 1: 需求探索
```
Use superpowers:brainstorming skill
```
- 逐个提问细化需求
- 探索不同的实现方案
- 呈现设计并获取确认

### Step 2: 计划编写
```
Use superpowers:writing-plans skill
```
- 创建详细的实现计划
- 计划保存到 `docs/plans/YYYY-MM-DD-<feature-name>.md`

### Step 3: 计划执行
```
Use superpowers:executing-plans skill
```
- 按计划逐个任务执行
- 每个任务完成后验证

---

## 2. Task Completion Self-Check Workflow

**任何任务（新功能或修复）完成后，必须执行以下步骤：**

### 2.1 质量评估（量化）

检查清单：
- [ ] 项目结构完整性检查
  - [ ] 必需目录存在（`skills/`、`scripts/`、`docs/`、`templates/`）
  - [ ] 必需文件存在（`VERSION`、`README.md`、`README.zh-CN.md`）

- [ ] 脚本语法正确性
  - [ ] Python 脚本：`python3 -m py_compile` 检查
  - [ ] Bash 脚本：`bash -n` 检查

- [ ] 文档内容准确性
  - [ ] 中英文档内容一致
  - [ ] 日期正确（北京时间）
  - [ ] 无错别字和格式错误

- [ ] 核心功能测试
  - [ ] `scripts/version-manager.py status` 正常
  - [ ] `scripts/install.sh help` 正常
  - [ ] `scripts/commit-helper.py` 语法正确

### 2.2 查漏补缺

系统性检查方法：
1. **全局搜索问题关键字**
   ```bash
   grep -r "2025" .    # 检查日期错误
   grep -r "TODO" .     # 检查未完成项
   ```

2. **对比设计文档**
   - 检查 `docs/plans/` 中的设计文档
   - 验证所有设计点是否实现

3. **文件完整性验证**
   - 列出项目目录结构
   - 确认所有必需文件存在

### 2.3 问题修复流程

**发现任何问题，必须遵循完整流程：**

#### 第 1 步：定位问题
- 确定问题出现的具体位置（文件名、行号）
- 使用工具辅助定位（grep、日志、错误信息）

#### 第 2 步：分析原因
- 分析问题存在的根本原因
- 检查依赖关系、数据流、逻辑错误

#### 第 3 步：设计方案
- 给出明确的修复方案
- 考虑方案的副作用和影响范围

#### 第 4 步：执行修复
- 实施修复方案
- 修改时保持代码风格一致

#### 第 5 步：验证结果
- 确认问题已解决
- 运行相关测试

#### 第 6 步：回归检查
- 检查修复是否引入新问题
- 执行质量评估（2.1 节）

### 2.4 提交代码到远程

```bash
# 使用自动化工具提交
python scripts/commit-helper.py
```

- 工具会自动：staging + commit + push
- 确认输出显示 "Push successful!"

---

## 3. Bug Fix Workflow

**Bug 修复任务独立于新任务流程，遵循以下步骤：**

### Step 1: 定位问题
- 描述问题现象
- 使用工具定位具体位置

### Step 2: 分析原因
- 分析根本原因
- 理解问题上下文

### Step 3: 设计方案
- 给出修复方案
- 考虑边界情况

### Step 4: 执行修复
- 实施修复代码
- 保持代码风格一致

### Step 5: 验证结果
- 确认问题解决
- 回归测试

### Step 6: 质量检查
- 执行 2.1 节质量评估
- 执行 2.2 节查漏补缺

### Step 7: 提交代码
```bash
python scripts/commit-helper.py
```

---

## 4. Documentation Standards

### 4.1 语气和用词

| ✅ 专业 | ❌ 口语化 |
|---------|----------|
| "验证功能正确性" | "看看功能对不对" |
| "分析问题根因" | "搞清楚问题在哪" |
| "实施修复方案" | "试着修一下" |
| "遵循规范" | "按这个来弄" |

### 4.2 中英双语规则

**所有文档更新必须遵循：**

| 操作类型 | 英文文档 | 中文文档 |
|---------|----------|---------|
| 新增技能 | `README.md` | `README.zh-CN.md` |
| 修改功能 | 同步更新 | 同步更新 |
| 删除技能 | 同步更新 | 同步更新 |
| 版本变更 | 同步更新 | 同步更新 |

### 4.3 文件命名规范

| 语言 | 标准命名 |
|------|----------|
| 英文（默认）| `README.md` |
| 简体中文 | `README.zh-CN.md` |
| 繁体中文 | `README.zh-TW.md` |
| 日语 | `README.ja.md` |
| 韩语 | `README.ko.md` |

---

## 5. Date Rules

**所有日期必须使用北京时间**

- 格式：`YYYY-MM-DD`
- 示例：`2026-02-01`
- 应用范围：
  - `CHANGELOG.md` 中的版本日期
  - `docs/plans/` 文件名中的日期
  - 提交信息中的日期（如有）

**获取当前北京时间的方法：**
```bash
# macOS
date "+%Y-%m-%d"

# Linux
date +%Y-%m-%d
```

---

## 6. Quick Reference

### 常用命令

```bash
# 检查日期一致性
grep -r "2025" .

# Python 语法检查
python3 -m py_compile scripts/*.py

# Bash 语法检查
bash -n scripts/*.sh

# 提交代码（自动推送）
python scripts/commit-helper.py

# 版本管理
python scripts/version-manager.py status
python scripts/version-manager.py bump major|minor|patch
```

### 检查清单速查

**任务完成前必须确认：**

- [ ] 质量评估完成（2.1 节）
- [ ] 查漏补缺完成（2.2 节）
- [ ] 如有问题，按流程修复（2.3 节）
- [ ] 代码已提交到远程（2.4 节）
- [ ] 文档已同步更新（中英）
- [ ] 日期使用北京时间
- [ ] 文档语气专业无口语化

---

## 7. AI Compliance

**Claude Code 在每次任务开始时：**
1. 必须先阅读本 `CLAUDE.md` 文件
2. 理解所有规范和流程
3. 任务执行过程中严格遵守
4. 任务完成时执行检查清单

**用户在每次会话开始时：**
- 可以说："阅读项目规范"
- Claude Code 会自动加载 `CLAUDE.md`
- 确认理解和遵守规范
