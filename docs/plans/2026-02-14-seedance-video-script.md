# Seedance Video Script Skill Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 创建一个帮助用户为 Seedance 2.0 平台生成高质量视频提示词的 Claude Skill，支持 6 种场景和交互式优化。

**Architecture:** 使用 SKILL.md 作为主入口（<500行核心流程），templates/ 存储可复用的 Prompt 模板，references/ 存储详细参考文档。采用渐进式加载策略，仅在需要时加载参考文档。

**Tech Stack:** Claude Skill format (SKILL.md + bundled resources), Handlebars-style template syntax ({{variable}}), Markdown

---

## Task 1: 创建 skill 目录结构

**Files:**
- Create: `seedance-video-script/SKILL.md`
- Create: `seedance-video-script/templates/portrait.txt`
- Create: `seedance-video-script/templates/scenery.txt`
- Create: `seedance-video-script/templates/action-copy.txt`
- Create: `seedance-video-script/templates/story.txt`
- Create: `seedance-video-script/templates/edit.txt`
- Create: `seedance-video-script/references/scenarios.md`
- Create: `seedance-video-script/references/optimization.md`
- Create: `seedance-video-script/references/workflow.md`

**Step 1: 创建主目录**

```bash
mkdir -p seedance-video-script/templates seedance-video-script/references
```

**Step 2: 验证目录结构**

Run: `ls -la seedance-video-script/`
Expected: directories `templates/` and `references/` exist

**Step 3: 提交**

```bash
git add seedance-video-script/
git commit -m "feat(skill): create seedance-video-script directory structure"
```

---

## Task 2: 编写 SKILL.md - Frontmatter 和欢迎语

**Files:**
- Modify: `seedance-video-script/SKILL.md`

**Step 1: 创建 SKILL.md 文件并写入 frontmatter**

Write the following content to `seedance-video-script/SKILL.md`:

```markdown
---
name: seedance-video-script
description: 为 Seedance 2.0 平台生成高质量视频提示词。支持6种场景（人像、风景、动作复刻、剧情短片、视频编辑、自定义），提供交互式Prompt生成与优化，包含角色稳定、运镜复刻、音频同步等核心功能。触发词："Seedance 2.0 提示词生成"、"Seedance"、"视频脚本"、"Seedance prompt"。
---

# Seedance 2.0 提示词生成助手

## 欢迎与场景引导

当用户触发本技能时，首先展示欢迎语并引导场景选择：

```
你好！我是 Seedance 2.0 专属提示词助手，可帮你生成适配文生视频/图生视频/多镜头叙事的高质量 Prompt，支持角色稳定、运镜复刻、音频同步等核心需求。

请先选择你要创作的场景（输入序号即可）：
1. 唯美人像短视频（≤15秒，图生视频为主）
2. 氛围感风景视频（≤15秒，无角色/简单动态）
3. 动作复刻视频（图+视频参考，复刻运镜/动作）
4. 剧情短片（＞15秒，多镜头叙事）
5. 视频编辑/延长（基于现有视频修改/续拍）
6. 自定义需求（可详细描述）
```

## 灵活工作流

本技能支持灵活的交互模式：

### 模式 1: 直接输入（推荐）
用户直接描述需求，系统自动识别场景并跳过不必要提问。

**场景检测关键词**：
- "人像" → 场景 1（唯美人像）
- "风景" → 场景 2（氛围感风景）
- "复刻/动作" → 场景 3（动作复刻）
- "剧情/故事" → 场景 4（剧情短片）
- "延长/编辑/修改" → 场景 5（视频编辑）

### 模式 2: 场景选择
用户从 6 个场景中选择，然后按场景分层提问。

## 场景识别与信息采集

根据用户输入的场景，从 `references/scenarios.md` 读取对应场景的变量定义和提问列表。

**变量填充规则**：
- 时长默认值：6 秒
- 画质默认值：4K 超高清
- 约束默认值：面部稳定不扭曲、动作自然
- 音频默认值：根据场景自动推断

**参考素材标注**：
- 图片：@Image1, @Image2, ...
- 视频：@Video1, @Video2, ...
- 音频：@Audio1, @Audio2, ...
```

**Step 2: 验证文件创建**

Run: `cat seedance-video-script/SKILL.md | head -30`
Expected: YAML frontmatter with name and description fields

**Step 3: 提交**

```bash
git add seedance-video-script/SKILL.md
git commit -m "feat(skill): add SKILL.md frontmatter and welcome message"
```

---

## Task 3: 创建 portrait.txt 模板

**Files:**
- Create: `seedance-video-script/templates/portrait.txt`

**Step 1: 创建唯美人像短视频模板**

Write the following content to `seedance-video-script/templates/portrait.txt`:

```text
{{#if 参考图}}基于@Image1保持{{角色特征}}一致，{{/if}}{{核心动作}}，{{镜头运镜}}，{{场景&光影}}，治愈清新风格，4K超高清，面部稳定不扭曲、人体比例正常、动作自然不僵硬，{{音频}}，{{时长}}秒丝滑无卡顿
```

**Step 2: 验证文件创建**

Run: `cat seedance-video-script/templates/portrait.txt`
Expected: Template with Handlebars-style variables

**Step 3: 提交**

```bash
git add seedance-video-script/templates/portrait.txt
git commit -m "feat(template): add portrait video prompt template"
```

---

## Task 4: 创建 scenery.txt 模板

**Files:**
- Create: `seedance-video-script/templates/scenery.txt`

**Step 1: 创建氛围感风景视频模板**

Write the following content to `seedance-video-script/templates/scenery.txt`:

```text
{{核心场景}}，{{动态效果}}，{{镜头运镜}}，{{色调&氛围}}，4K超高清，无模糊/无闪烁/无重影，{{音频}}，{{时长}}秒无缝过渡
```

**Step 2: 验证文件创建**

Run: `cat seedance-video-script/templates/scenery.txt`
Expected: Template with Handlebars-style variables

**Step 3: 提交**

```bash
git add seedance-video-script/templates/scenery.txt
git commit -m "feat(template): add scenery video prompt template"
```

---

## Task 5: 创建 action-copy.txt 模板

**Files:**
- Create: `seedance-video-script/templates/action-copy.txt`

**Step 1: 创建动作复刻视频模板**

Write the following content to `seedance-video-script/templates/action-copy.txt`:

```text
{{#if 角色参考图}}@Image1中的{{角色特征}}作为主体，{{/if}}{{#if 动作参考视频}}复刻@Video1的{{核心要求}}，{{/if}}{{镜头运镜}}，{{额外风格}}，4K超高清，动作连贯不僵硬、面部稳定不扭曲，{{#if 音频参考}}@Audio1卡点节奏，{{/if}}{{时长}}秒无抖动
```

**Step 2: 验证文件创建**

Run: `cat seedance-video-script/templates/action-copy.txt`
Expected: Template with Handlebars-style variables and conditional logic

**Step 3: 提交**

```bash
git add seedance-video-script/templates/action-copy.txt
git commit -m "feat(template): add action copy video prompt template"
```

---

## Task 6: 创建 story.txt 模板

**Files:**
- Create: `seedance-video-script/templates/story.txt`

**Step 1: 创建剧情短片（多镜头）模板**

Write the following content to `seedance-video-script/templates/story.txt`:

```text
# 总约束
{{#if 核心角色参考图}}基于{{核心角色参考图}}保持{{核心角色特征}}一致，{{/if}}全片面部稳定不扭曲、场景无缝过渡，4K超高清，{{统一风格}}，{{音频}}，总时长{{总时长}}秒

# 分镜Prompt
{{#each 分镜列表}}
Shot {{序号}}（{{时间区间}}）：{{景别}}，{{运镜}}，{{剧情内容}}，{{环境音}}，动作缓慢自然
{{/each}}
```

**Step 2: 验证文件创建**

Run: `cat seedance-video-script/templates/story.txt`
Expected: Template with Handlebars-style variables and loop logic

**Step 3: 提交**

```bash
git add seedance-video-script/templates/story.txt
git commit -m "feat(template): add story video prompt template"
```

---

## Task 7: 创建 edit.txt 模板

**Files:**
- Create: `seedance-video-script/templates/edit.txt`

**Step 1: 创建视频编辑/延长模板**

Write the following content to `seedance-video-script/templates/edit.txt`:

```text
{{#if 操作类型==延长}}将@Video1延长{{新增时长}}秒。{{具体要求}}，4K超高清，动作自然连贯，{{音频}}{{/if}}
{{#if 操作类型==替换/修改}}修改@Video1：{{具体要求}}，保留原视频运镜&节奏，4K超高清，面部稳定不扭曲，{{音频}}{{/if}}
```

**Step 2: 验证文件创建**

Run: `cat seedance-video-script/templates/edit.txt`
Expected: Template with Handlebars-style variables and conditional logic

**Step 3: 提交**

```bash
git add seedance-video-script/templates/edit.txt
git commit -m "feat(template): add video edit prompt template"
```

---

## Task 8: 编写 references/scenarios.md

**Files:**
- Create: `seedance-video-script/references/scenarios.md`

**Step 1: 创建场景详细说明文档**

Write the following content to `seedance-video-script/references/scenarios.md`:

```markdown
# 场景详细说明与变量定义

## 场景 1: 唯美人像短视频

### 提问列表
1. 参考素材：是否上传参考图？（是/否，若为"是"，需标注@Image1）
2. 角色特征：年龄/人种/发型/服装（例：28岁亚裔女性，棕色卷发，米色风衣）
3. 核心动作：需缓慢/自然的连续动作（例：林间缓慢行走，微风拂发，微微低头浅笑）
4. 场景&光影：例（海边黄昏/林间清晨，暖橙光影/丁达尔光效）
5. 镜头运镜：例（中景+缓慢推镜/近景+轻微环绕）
6. 时长：5-15秒（默认6秒）
7. 音频：环境音/背景音乐（例：风吹树叶声/轻柔钢琴）

### 变量定义
| 变量名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| 参考图 | 布尔 | false | 是否有角色参考图 |
| 角色特征 | 文本 | - | 年龄/人种/发型/服装描述 |
| 核心动作 | 文本 | - | 连续缓慢动作描述 |
| 镜头运镜 | 文本 | - | 景别+运镜方式 |
| 场景&光影 | 文本 | - | 环境+光线效果 |
| 音频 | 文本 | - | 环境音/背景音乐 |
| 时长 | 数字 | 6 | 生成时长（秒） |

### 示例
**输入**：28岁亚裔女性，棕色卷发，米色风衣，林间缓慢行走，微风拂发，中景+缓慢推镜，海边黄昏暖橙光影，8秒，风吹树叶声
**输出**：基于@Image1保持28岁亚裔女性棕色卷发米色风衣一致，林间缓慢行走，微风拂发，微微低头浅笑，中景+缓慢推镜，海边黄昏暖橙光影，治愈清新风格，4K超高清，面部稳定不扭曲、人体比例正常、动作自然不僵硬，风吹树叶声，8秒丝滑无卡顿

---

## 场景 2: 氛围感风景视频

### 提问列表
1. 核心场景：例（海边日落/山间晨雾/城市雨夜）
2. 动态效果：缓慢的画面变化（例：海浪轻拍沙滩/云雾缓缓流动/雨滴滑落玻璃）
3. 镜头运镜：例（缓慢横移/全景缓慢拉升/固定镜头）
4. 色调&氛围：例（暖橙治愈/冷调高级/赛博朋克霓虹）
5. 时长：5-15秒（默认6秒）
6. 音频：环境音（例：海浪声/雨声/鸟鸣）

### 变量定义
| 变量名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| 核心场景 | 文本 | - | 自然/城市场景描述 |
| 动态效果 | 文本 | - | 缓慢画面变化描述 |
| 镜头运镜 | 文本 | - | 景别+运镜方式 |
| 色调&氛围 | 文本 | - | 色彩+情绪描述 |
| 音频 | 文本 | - | 环境音描述 |
| 时长 | 数字 | 6 | 生成时长（秒） |

---

## 场景 3: 动作复刻视频

### 提问列表
1. 参考素材：
   - 角色参考图：是否上传？（是/否，标注@Image1）
   - 动作/运镜参考视频：是否上传？（是/否，标注@Video1）
   - 音频参考：是否上传卡点音频？（是/否，标注@Audio1）
2. 核心要求：需复刻的具体内容（例：复刻@Video1的舞蹈动作+环绕运镜）
3. 角色约束：需保持的特征（例：面部一致/服装一致）
4. 镜头运镜：补充运镜描述
5. 时长：5-15秒（默认6秒）
6. 额外风格：例（赛博朋克光影/复古胶片质感）

### 变量定义
| 变量名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| 角色参考图 | 布尔 | false | 是否有角色参考图 |
| 角色特征 | 文本 | - | 角色描述 |
| 动作参考视频 | 布尔 | false | 是否有动作参考视频 |
| 核心要求 | 文本 | - | 复刻的动作/运镜描述 |
| 镜头运镜 | 文本 | - | 补充运镜描述 |
| 额外风格 | 文本 | - | 视觉风格描述 |
| 音频参考 | 布尔 | false | 是否有音频参考 |
| 时长 | 数字 | 6 | 生成时长（秒） |

---

## 场景 4: 剧情短片（多镜头）

### 提问列表
1. 总时长：15-30秒
2. 核心角色：参考图标注+特征（例：@Image2，30岁亚裔女性，黑色短发）
3. 核心剧情：简单叙事逻辑（例：阁楼翻旧相册→回忆童年→合相册）
4. 统一风格：光影+色调+氛围（例：王家卫暖橙青色调/治愈清新风格）
5. 音频：背景音乐+环境音（例：轻柔钢琴+木箱吱呀声）
6. 分镜偏好：是否需要指定每段镜头

### 变量定义
| 变量名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| 核心角色参考图 | 文本 | - | @ImageX 标注 |
| 核心角色特征 | 文本 | - | 角色描述 |
| 统一风格 | 文本 | - | 光影+色调+氛围 |
| 音频 | 文本 | - | 背景音乐+环境音 |
| 总时长 | 数字 | - | 总时长（秒） |
| 分镜列表 | 数组 | - | 包含序号、时间区间、景别、运镜、剧情、环境音 |

---

## 场景 5: 视频编辑/延长

### 提问列表
1. 参考素材：原视频标注（@Video1）
2. 操作类型：延长/角色替换/添加元素/修改运镜
3. 具体要求：
   - 延长：需新增时长+新增内容
   - 替换/修改：需修改的具体部分
4. 音频：是否保留原音频/新增音效

### 变量定义
| 变量名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| 操作类型 | 文本 | - | 延长/替换/修改 |
| 新增时长 | 数字 | - | 延长秒数 |
| 具体要求 | 文本 | - | 延长内容/修改内容 |
| 音频 | 文本 | - | 保留原音频/新增音效 |

---

## 场景 6: 自定义需求

### 提问列表
请详细描述你的创作需求，建议包含以下维度（可按需补充）：
1. 素材类型：参考图/视频/音频（标注@素材名）
2. 主体&动作：角色/物体+具体动态
3. 镜头&运镜：景别+运动方式
4. 场景&光影：环境+光线效果
5. 风格&氛围：视觉风格+情绪氛围
6. 时长&音频：生成时长+声音要求
7. 特殊约束：角色稳定/动作连贯/无抖动等
```

**Step 2: 验证文件创建**

Run: `head -50 seedance-video-script/references/scenarios.md`
Expected: Scenario definitions with variable tables

**Step 3: 提交**

```bash
git add seedance-video-script/references/scenarios.md
git commit -m "feat(reference): add scenarios documentation with variable definitions"
```

---

## Task 9: 编写 references/optimization.md

**Files:**
- Create: `seedance-video-script/references/optimization.md`

**Step 1: 创建优化建议库文档**

Write the following content to `seedance-video-script/references/optimization.md`:

```markdown
# 优化建议库

## 维度 1: 角色一致性问题

| 问题表现 | 核心原因 | Prompt 优化建议 |
|----------|----------|----------------|
| 角色变脸/面部扭曲 | 未标注角色参考+无稳定约束 | 1. 新增"基于@ImageX保持面部/服装一致"<br>2. 补充"面部稳定不扭曲、人体比例正常"<br>3. 避免复杂多人互动，聚焦单角色 |
| 角色动作僵硬/漂浮 | 动作描述模糊/过于剧烈 | 1. 将"跳舞/跑跳"改为"缓慢转身/轻轻抬手"<br>2. 新增"动作自然不僵硬、无漂浮/无重影"<br>3. 补充"物理真实感，头发/衣物自然飘动" |

**优化关键词检测**：
- "变脸"、"扭曲"、"不像"、"换脸"、"脸不一样"

---

## 维度 2: 运镜&画面流畅度问题

| 问题表现 | 核心原因 | Prompt 优化建议 |
|----------|----------|----------------|
| 画面抖动/运镜混乱 | 运镜描述模糊/要求复杂 | 1. 明确运镜词："缓慢推镜/平稳跟拍/无抖动"<br>2. 避免"快速切换/复杂环绕"，改为"轻微环绕/缓慢横移"<br>3. 新增"丝滑无卡顿/无缝过渡" |
| 景别混乱（忽近忽远） | 未指定景别 | 1. 补充景别词："近景/中景/全景/特写"<br>2. 分镜中标注每段景别 |

**优化关键词检测**：
- "抖动"、"卡顿"、"不流畅"、"晃"、"晕"

---

## 维度 3: 音频同步问题

| 问题表现 | 核心原因 | Prompt 优化建议 |
|----------|----------|----------------|
| 音频与动作不同步 | 未标注音频参考+无卡点约束 | 1. 新增"@AudioX卡点动作节奏"<br>2. 补充"音效同步动作，背景音乐渐强/渐弱"<br>3. 明确音频类型："仅保留环境音/添加电子乐卡点" |
| 无音效/音效违和 | 未指定音频需求 | 1. 精准描述音频："海浪声+轻柔钢琴"而非"好听的音乐"<br>2. 补充"环境音匹配场景" |

**优化关键词检测**：
- "不同步"、"没声音"、"音频对不上"、"无声"、"音效"

---

## 维度 4: 画质&风格问题

| 问题表现 | 核心原因 | Prompt 优化建议 |
|----------|----------|----------------|
| 画面模糊/细节丢失 | 无画质约束+参考素材模糊 | 1. 新增"4K超高清/细节丰富/锐度清晰"<br>2. 补充"无模糊/无重影/无闪烁"<br>3. 提示用户上传2K+参考素材 |
| 风格漂移（中途变风格） | 风格描述模糊 | 1. 将"好看/很美"改为"日系清新/王家卫暖橙青色调"<br>2. 总约束中标注"全片风格统一，无漂移"<br>3. 补充风格参考："in the style of 韦斯·安德森" |

**优化关键词检测**：
- "模糊"、"画质差"、"不清楚"、"风格不对"、"不像风格"

---

## 维度 5: 时长&节奏问题

| 问题表现 | 核心原因 | Prompt 优化建议 |
|----------|----------|----------------|
| 短时长（<10秒）动作不完整 | 动作描述过多 | 1. 精简动作：保留1-2个核心缓慢动作<br>2. 分镜拆分：将复杂动作拆分为多段短镜头 |
| 长时长（>15秒）画面卡顿 | 无分镜约束+动作复杂 | 1. 按10秒/段拆分分镜，标注时间区间<br>2. 每段分镜仅描述1个核心动作<br>3. 新增"场景无缝过渡/一镜到底" |

**优化关键词检测**：
- "太短"、"太长"、"节奏不对"、"动作没做完"、"卡"

---

## 优化映射规则

### 用户反馈关键词 → 优化维度

| 用户反馈 | 优化维度 | 优先级 |
|---------|---------|-------|
| 变脸/扭曲/不像 | 角色一致性 | 高 |
| 抖动/卡顿/不流畅/晃 | 运镜&画面流畅度 | 高 |
| 不同步/没声音 | 音频同步 | 中 |
| 模糊/画质差 | 画质&风格 | 中 |
| 太短/太长/节奏不对 | 时长&节奏 | 低 |

### 优化应用流程

1. 用户反馈问题 → 提取关键词
2. 从优化建议库查找对应维度的解决方案
3. 将解决方案应用到原 Prompt
4. 展示优化后的 Prompt 和优化点说明（3-5条）
5. 询问用户是否需要进一步调整

### 通用优化建议（当无法匹配具体维度时）

如果无法匹配具体维度，应用以下通用优化：
1. 新增"4K超高清"
2. 新增"面部稳定不扭曲"
3. 新增"动作自然不僵硬"
4. 新增"无模糊/无重影/无闪烁"
5. 新增"丝滑无卡顿/无缝过渡"
```

**Step 2: 验证文件创建**

Run: `head -50 seedance-video-script/references/optimization.md`
Expected: Optimization tables with keyword mappings

**Step 3: 提交**

```bash
git add seedance-video-script/references/optimization.md
git commit -m "feat(reference): add optimization library with keyword mappings"
```

---

## Task 10: 编写 references/workflow.md

**Files:**
- Create: `seedance-video-script/references/workflow.md`

**Step 1: 创建工作流程文档**

Write the following content to `seedance-video-script/references/workflow.md`:

```markdown
# 完整工作流程

## 1. 欢迎与场景引导

### 欢迎语模板
```
你好！我是 Seedance 2.0 专属提示词助手，可帮你生成适配文生视频/图生视频/多镜头叙事的高质量 Prompt，支持角色稳定、运镜复刻、音频同步等核心需求。

请先选择你要创作的场景（输入序号即可）：
1. 唯美人像短视频（≤15秒，图生视频为主）
2. 氛围感风景视频（≤15秒，无角色/简单动态）
3. 动作复刻视频（图+视频参考，复刻运镜/动作）
4. 剧情短片（＞15秒，多镜头叙事）
5. 视频编辑/延长（基于现有视频修改/续拍）
6. 自定义需求（可详细描述）
```

### 场景检测关键词
- "人像" → 场景 1
- "风景" → 场景 2
- "复刻"、"动作" → 场景 3
- "剧情"、"故事" → 场景 4
- "延长"、"编辑"、"修改" → 场景 5

---

## 2. 需求采集

### 按场景分层提问

参考 `references/scenarios.md` 中每个场景的提问列表，逐个提问收集信息。

### 变量默认值
- 时长：6 秒
- 画质：4K 超高清
- 约束：面部稳定不扭曲、动作自然
- 音频：根据场景自动推断

---

## 3. Prompt 生成反馈

### 输出模板
```
根据你的需求，为你生成适配 Seedance 2.0 的 Prompt 如下：

【最终 Prompt】
[生成的完整Prompt内容]

【使用说明】
1. 复制上述 Prompt 至 Seedance 2.0 输入框；
2. 确保上传的素材与 Prompt 中标注的@Image1/@Video1等一一对应；
3. 新手建议先按生成时长的50%测试（例：需求10秒先试5秒），确认效果后再调整。

是否需要优化该 Prompt？（是/否，若为"是"，请说明优化方向：如角色更稳定/运镜更丝滑/风格更突出等）
```

---

## 4. 优化交互 & 结束语

### 优化反馈模板
```
【优化反馈】
根据你的优化需求，调整后的 Prompt 如下：

[优化后的Prompt]

【核心优化点】
1. [优化维度1]：[具体优化内容]
2. [优化维度2]：[具体优化内容]

是否需要进一步调整？（是/否）
```

### 结束语模板
```
本次 Prompt 生成完成！如需创作其他类型视频，可再次触发"Seedance 2.0 提示词生成"，祝你创作顺利～
```

---

## 5. 输出格式

### 最终 Prompt 输出
**格式**：纯文本（无 Markdown）
**内容**：替换变量后的完整 Prompt

### 使用说明输出
**格式**：Markdown 列表
**内容**：3 条使用建议

### 优化反馈输出
**格式**：Markdown
**内容**：优化后的 Prompt + 3-5 条核心优化点

---

## 6. 完整对话示例

### 示例 1: 唯美人像视频

**用户**：我要做一个海边日落的人像视频

**助手**：
检测到关键词"人像"，选择场景 1：唯美人像短视频

请补充以下信息：
1. 参考素材：是否上传参考图？（是/否）
2. 角色特征：年龄/人种/发型/服装
3. 核心动作：需缓慢/自然的连续动作
4. 场景&光影：海边黄昏（已提供）
5. 镜头运镜：景别+运镜方式
6. 时长：5-15秒（默认6秒）
7. 音频：环境音/背景音乐

**用户**：是，有参考图，25岁亚裔女性，黑色长发，白色连衣裙，缓慢转身面向大海，特写+缓慢推镜，8秒，海浪声

**助手**：
```
根据你的需求，为你生成适配 Seedance 2.0 的 Prompt 如下：

【最终 Prompt】
基于@Image1保持25岁亚裔女性黑色长发白色连衣裙一致，缓慢转身面向大海，特写+缓慢推镜，海边黄昏暖橙光影，治愈清新风格，4K超高清，面部稳定不扭曲、人体比例正常、动作自然不僵硬，海浪声，8秒丝滑无卡顿

【使用说明】
1. 复制上述 Prompt 至 Seedance 2.0 输入框；
2. 确保上传的素材与 Prompt 中标注的@Image1/@Video1等一一对应；
3. 新手建议先按生成时长的50%测试（例：需求10秒先试5秒），确认效果后再调整。

是否需要优化该 Prompt？
```

### 示例 2: 优化反馈

**用户**：角色有点变脸

**助手**：
```
【优化反馈】
根据你的优化需求，调整后的 Prompt 如下：

基于@Image1保持25岁亚裔女性黑色长发白色连衣裙，面部特征完全一致，缓慢转身面向大海，特写+缓慢推镜，海边黄昏暖橙光影，治愈清新风格，4K超高清，面部稳定不扭曲、五官比例正常、无变形，动作自然不僵硬，海浪声，8秒丝滑无卡顿

【核心优化点】
1. 角色一致性：强化"面部特征完全一致"约束，新增"五官比例正常、无变形"
2. 聚焦主体：移除多余描述，聚焦角色稳定性

是否需要进一步调整？（是/否）
```
```

**Step 2: 验证文件创建**

Run: `head -50 seedance-video-script/references/workflow.md`
Expected: Complete workflow documentation with examples

**Step 3: 提交**

```bash
git add seedance-video-script/references/workflow.md
git commit -m "feat(reference): add workflow documentation with examples"
```

---

## Task 11: 完成 SKILL.md 的主体内容

**Files:**
- Modify: `seedance-video-script/SKILL.md`

**Step 1: 完成 SKILL.md 的完整内容**

Append the following content to `seedance-video-script/SKILL.md`:

```markdown
## 模板加载与变量填充

根据选择的场景，从 `templates/` 目录读取对应的模板文件：

| 场景 | 模板文件 |
|-----|---------|
| 1. 唯美人像 | templates/portrait.txt |
| 2. 氛围感风景 | templates/scenery.txt |
| 3. 动作复刻 | templates/action-copy.txt |
| 4. 剧情短片 | templates/story.txt |
| 5. 视频编辑 | templates/edit.txt |

**变量替换规则**：
- 布尔条件：`{{#if 条件}}...{{/if}}` - 仅在条件为真时包含内容
- 循环生成：`{{#each 列表}}...{{/each}}` - 遍历数组生成内容
- 文本替换：`{{变量名}}` - 直接替换为对应文本

**默认值策略**：
- 时长：6 秒
- 画质：4K 超高清
- 约束：面部稳定不扭曲、动作自然
- 音频：根据场景自动推断

## Prompt 生成与输出

### 输出格式

**最终 Prompt**（纯文本，无 Markdown）：
```
基于@Image1保持28岁亚裔女性棕色卷发米色风衣一致，林间缓慢行走...
```

**使用说明**（Markdown 列表）：
```
【使用说明】
1. 复制上述 Prompt 至 Seedance 2.0 输入框；
2. 确保上传的素材与 Prompt 中标注的@Image1/@Video1等一一对应；
3. 新手建议先按生成时长的50%测试...
```

## 优化交互流程

### 触发条件
当用户反馈需要优化时（如"角色变脸"、"画面抖动"等），执行优化流程。

### 优化步骤
1. 从用户反馈中提取关键词
2. 从 `references/optimization.md` 读取对应的优化建议
3. 将优化建议应用到原 Prompt
4. 展示优化后的 Prompt 和核心优化点（3-5条）
5. 询问是否需要进一步调整

### 优化关键词映射
| 关键词 | 优化维度 |
|--------|---------|
| 变脸/扭曲/不像 | 角色一致性 |
| 抖动/卡顿/不流畅 | 运镜&画面流畅度 |
| 不同步/没声音 | 音频同步 |
| 模糊/画质差 | 画质&风格 |
| 太短/太长/节奏不对 | 时长&节奏 |

## 参考文档引用

**何时读取参考资料**：
- `references/scenarios.md` - 信息采集时，按场景读取变量定义
- `references/optimization.md` - 用户反馈优化需求时，读取优化建议库
- `references/workflow.md` - 需要参考完整对话示例时

## 技术规范

**SKILL.md 长度限制**：< 500 行
**模板语法**：Handlebars 风格 `{{变量名}}`
**输出格式**：纯文本 Prompt + Markdown 说明
**语言**：中文

## 设计原则

1. **简洁性**：SKILL.md 保持精简，详细内容放在 references/
2. **渐进式加载**：元数据 → SKILL.md → references/（按需加载）
3. **灵活性**：支持自由输入和结构化提问两种模式
4. **交互性**：优化流程采用交互式确认，而非自动执行
5. **可维护性**：模板和参考文档分离，便于更新
```

**Step 2: 验证文件完整性**

Run: `wc -l seedance-video-script/SKILL.md`
Expected: Line count < 500

**Step 3: 提交**

```bash
git add seedance-video-script/SKILL.md
git commit -m "feat(skill): complete SKILL.md with template loading and optimization flow"
```

---

## Task 12: 验证 Skill 结构

**Files:**
- Test: `seedance-video-script/`

**Step 1: 验证目录结构**

Run: `tree seedance-video-script/` 或 `find seedance-video-script/ -type f`
Expected:
```
seedance-video-script/
├── SKILL.md
├── templates/
│   ├── portrait.txt
│   ├── scenery.txt
│   ├── action-copy.txt
│   ├── story.txt
│   └── edit.txt
└── references/
    ├── scenarios.md
    ├── optimization.md
    └── workflow.md
```

**Step 2: 验证 SKILL.md frontmatter**

Run: `head -5 seedance-video-script/SKILL.md`
Expected: YAML frontmatter with `name` and `description` fields

**Step 3: 验证模板文件**

Run: `ls seedance-video-script/templates/` 和 `cat seedance-video-script/templates/*.txt`
Expected: 5 template files with Handlebars syntax

**Step 4: 验证参考文档**

Run: `ls seedance-video-script/references/` 和 `head -20 seedance-video-script/references/*.md`
Expected: 3 reference files with valid markdown

**Step 5: 提交**

```bash
git add seedance-video-script/
git commit -m "chore(skill): verify seedance-video-script structure"
```

---

## Task 13: 更新项目文档

**Files:**
- Modify: `docs/plans/2026-02-14-seedance-video-script-design.md`
- Modify: `README.md` (可选)
- Modify: `README.zh-CN.md` (可选)

**Step 1: 更新设计文档状态**

修改 `docs/plans/2026-02-14-seedance-video-script-design.md` 的状态为"实施完成"

**Step 2: 提交**

```bash
git add docs/plans/2026-02-14-seedance-video-script-design.md
git commit -m "docs(design): update seedance-video-script design status to completed"
```

---

## Task 14: 推送到远程仓库

**Files:**
- Push: feature/seedance-video-script branch

**Step 1: 推送到远程**

```bash
git push -u origin feature/seedance-video-script
```

**Step 2: 验证推送成功**

Run: `git log --oneline -5`
Expected: Latest commits pushed to remote

**Step 3: 报告完成**

输出：实施完成，Skill 已创建在 `seedance-video-script/` 目录，代码已推送到 `feature/seedance-video-script` 分支。
