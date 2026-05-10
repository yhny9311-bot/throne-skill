# Throne Skill

面向风景园林、城市生态、遥感规划、生态网络、街景语义与空间公平研究的科研王朝式工作流 Skill。

Throne Skill 不是普通的论文润色提示词，也不是自动写论文机器。它的目标是把一堆论文、一个模糊选题或一组数据，逐步转化为可执行、可解释、可写作、可审查的科研方案。

核心链条是：

```text
论文 PDF
-> 文献卡片
-> 方法矩阵
-> 研究缺口
-> 创新路径
-> 变量体系
-> 数据清单
-> 实验 SOP
-> 论文骨架
-> 图表规范
-> 引文核查
-> 投稿初稿准备
```

## 适用场景

Throne Skill 适合以下任务：

- 下载了很多论文，但不知道从哪里读起，也不知道如何把方法拆出来复用。
- 想把多篇论文中的数据、变量、模型、指标和创新点整理成表格。
- 有一个风景园林或城市生态方向，但不知道怎样形成可投稿的研究问题。
- 需要把一个研究方向转化为变量表、数据清单、实验步骤和工具路线。
- 需要设计遥感、GIS、GEE、PLUS、InVEST、Circuitscape、街景语义等研究流程。
- 想参考高水平期刊论文的结构、引言逻辑、讨论逻辑和标题层级，但不想抄句子。
- 投稿前需要检查图表规范、引用真实性、方法合理性和潜在抄袭风险。

重点支持方向包括：

- 城市热环境与地表温度驱动因素
- 绿地公平性与公园可达性
- 街景语义、视觉绿量与感知评价
- 生态网络、廊道、阻力面与网络韧性
- 生态系统服务与权衡协同
- PLUS / InVEST / Circuitscape / Linkage Mapper 等空间模型
- 城市标度、复杂系统与超线性规律
- 风景园林设计表达、技术路线图和论文图表规范

## 核心思想

Throne Skill 使用“王朝 / 三省六部 / 寺监”的隐喻组织科研流程，但它不是角色扮演。

这些名称只是工作流标签，用来强制不同任务产出不同的科研材料：

| 机构 | 真实功能 |
|---|---|
| 中书省 | 文献解构、研究问题提炼、方法拼合、创新路径生成 |
| 尚书省 | 变量设计、数据清单、实验 SOP、工具链、可行性推演 |
| 翰林院 | 论文骨架、引言漏斗、讨论结构、安全仿写 |
| 锦衣卫 | 幻觉检查、逻辑检查、创新性审查、抄袭风险审查 |
| 国子监 | 核心概念解释、新手引导、方法启蒙 |
| 钦天监 | 遥感、GIS、GEE、LST、夜光、GeoAI |
| 工部 | PLUS、InVEST、生态网络、空间模拟、模型工程 |
| 太常寺 | 图表规范、地图规范、期刊制图标准 |
| 尚宝司 | DOI、BibTeX、引文真实性和引用风险核查 |

输出应该是表格、矩阵、SOP、清单、论文结构和审查意见，而不是古风套话。

## 触发命令

你可以直接使用以下命令：

| 命令 | 启动模块 | 用途 |
|---|---|---|
| `上朝：文献解构` | 中书省 | 上传论文后拆文献、建方法矩阵、找缺口、给选题 |
| `入学：概念启蒙` | 国子监 | 解释复杂网络、MGWR、SEM、超线性标度等概念 |
| `观天：遥感方案` | 钦天监 | 设计 GEE、LST、NDVI、夜光、街景语义等遥感/GIS流程 |
| `兴工：实验推演` | 尚书省 + 工部 | 生成变量表、数据清单、模型路线、实验 SOP 和 Plan B |
| `开笔：论文骨架` | 翰林院 | 生成题目、摘要逻辑、引言漏斗、讨论结构和句型模板 |
| `定礼：图表规范` | 太常寺 | 检查论文图、地图、配色、图例、输出格式 |
| `用印：引文核查` | 尚宝司 | 检查 DOI、BibTeX、引用真实性和引用支撑关系 |
| `会审：全局质检` | 锦衣卫 | 审查创新性、可行性、逻辑断裂、幻觉和抄袭风险 |

## 使用示例

### 1. 文献解构

```text
上朝：文献解构。

我的研究方向是“城市热环境、绿地公平性与复杂网络耦合研究”。
这些是我下载的 30 篇文献。
请中书省先拆文献，生成文献卡片、方法组件矩阵、研究缺口和 3-5 个可行研究路径。
所有关键判断请标注证据来源。
```

期望输出：

- 单篇文献结构卡片
- 跨文献方法矩阵
- 可迁移方法组件
- 研究缺口
- 3-5 个创新路径
- 锦衣卫质检按语

### 2. 实验推演

```text
批红第二个方案。

兴工：实验推演。
请尚书省、工部和钦天监把它转成完整实验 SOP，包括变量表、数据清单、GEE/GIS/Python 工具路线、稳健性检验和 Plan B。
```

期望输出：

- 变量操作化表
- 数据清单
- 方法链
- 标准操作流程
- 工具路线
- 方法合理性说明
- 替代方案与风险

### 3. 论文骨架

```text
开笔：论文骨架。

请翰林院参考我上传的两篇 Landscape and Urban Planning 文章，
拆解它们的引言和讨论结构，然后生成我的论文题目、摘要逻辑、引言漏斗、方法标题、结果标题和讨论小标题。
只模仿结构，不模仿原句。
```

期望输出：

- 题目备选
- Highlights
- 摘要结构
- 引言漏斗
- 章节标题体系
- 讨论种子结构
- 安全仿写提示
- 防抄袭检查

## 证据标签

Throne Skill 要求关键判断标注来源，避免 AI 把猜测包装成事实。

| 标签 | 含义 |
|---|---|
| `[来自文献]` | 直接来自用户上传或已读取的论文 |
| `[来自用户材料]` | 来自用户给出的笔记、数据、目标或说明 |
| `[方法推断]` | 基于学科方法知识做出的合理推断 |
| `[待验证假设]` | 可能成立，但还需要数据或文献验证 |
| `[写作建议]` | 写作结构、表达方式或段落组织建议 |

铁律：

- 不编造文献。
- 不编造 DOI。
- 不编造结果。
- 不在没有证据表、变量表和方法链之前直接写完整论文。
- 模仿论文结构，不复制原文句子。

## 文件结构

```text
throne-skill/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── court/
│   ├── zhongshu_literature_deconstruction.md
│   ├── shangshu_experimental_sop.md
│   ├── hanlin_writing_skeleton.md
│   ├── jinyiwei_quality_gate.md
│   ├── guozijian_concept_bootcamp.md
│   ├── qintianjian_remote_sensing_gis.md
│   ├── gongbu_spatial_simulation.md
│   ├── taichangsi_figure_standard.md
│   └── shangbaosi_citation_check.md
├── references/
│   ├── landscape_method_library.md
│   ├── concept_glossary.md
│   └── evidence_labels.md
├── templates/
│   ├── literature_card_template.md
│   ├── method_matrix_template.md
│   ├── variable_table_template.md
│   ├── sop_template.md
│   ├── manuscript_skeleton_template.md
│   ├── discussion_seed_template.md
│   └── quality_gate_template.md
├── tool_registry/
│   └── github_officials.yaml
├── examples/
│   └── urban_heat_prompt.md
└── scripts/
    └── matrix_to_csv.py
```

## 关键文件说明

- `SKILL.md`：Skill 总纲。包含触发条件、工作流、证据规则和按需加载路径。
- `court/`：各部门的具体工作规则。
- `references/landscape_method_library.md`：风景园林专属方法库，是本 Skill 与通用科研助手的核心区别。
- `references/concept_glossary.md`：核心概念启蒙库。
- `templates/`：文献卡片、方法矩阵、变量表、SOP、论文骨架和质检模板。
- `tool_registry/github_officials.yaml`：可选外部工具注册表，不代表这些工具已经安装。
- `scripts/matrix_to_csv.py`：把 Markdown 表格转换为 CSV 的轻量脚本。

## 安装到 Codex

把本仓库克隆或复制到 Codex 技能目录：

```powershell
git clone https://github.com/yhny9311-bot/throne-skill.git "$env:USERPROFILE\.codex\skills\throne-skill"
```

之后即可在对话中使用：

```text
Use $throne-skill ...
```

或直接使用中文触发命令：

```text
上朝：文献解构。
```

## 设计原则

1. **从角色扮演改成角色化工作流**  
   保留王朝隐喻，但输出必须是科研材料。

2. **从万能科研改成风景园林专用**  
   内置城市热环境、绿地公平性、生态网络、街景语义、生态系统服务、PLUS、复杂网络等方法库。

3. **从 GitHub 项目堆砌改成工具注册表**  
   外部项目只作为可选工具，不写死为必需依赖。

4. **从自动写论文改成证据驱动写作**  
   先证据、变量、方法、SOP，再写作结构，最后才进入正文表达。

## 当前状态

这是第一版可用版本，重点完成：

- 主 Skill 触发与路由
- 三省主流程
- 国子监、钦天监、工部、太常寺、尚宝司外围模块
- 风景园林方法库
- 证据标签体系
- GitHub 工具注册表
- 常用输出模板
- 基础表格转换脚本

后续可以继续扩展：

- 更多真实案例
- Zotero / BibTeX / PDF 批处理脚本
- GEE 模板脚本
- 论文图表检查脚本
- 期刊风格库
- 中文核心期刊与 SCI 期刊写作风格对照
