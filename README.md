# 界面精炼 · UI Refinery

**中文** | [English](README.en.md)

一个按任务范围工作的 Codex UI skill：探索视觉方向，统一界面规范，补齐相关交互状态，并用真实截图和操作结果精修。

本仓库包含从 `distinctive-ai-design` 改名后的增强版本，以及选自 Emil Kowalski 设计工程经验的按需参考。名称与调用方式为 **`ui-refinery`**。来源及第三方许可见 [NOTICE](NOTICE.md)。

## 什么时候使用

- 创建或重新设计具体的网页、桌面应用、移动应用或游戏界面。
- 沿用现有产品规范完善页面、组件、交互与状态反馈。
- 检查并改善信息层级、动效、数据边界或移动网页体验。
- 针对具体界面或截图提出设计评审和修改建议。

仅按当前请求和交付物判断适用范围。后端、脚本、配置、文档、代码解释及仓库分析未涉及界面目标时，不添加 UI 设计、截图或审美要求。阅读、安装和维护 skill 本身也不启动设计流程。

## 安装

让支持 `skill-installer` 的 Codex 执行：

```text
使用 skill-installer 安装 https://github.com/CrazyHandin/ui-refinery 仓库根目录的 skill，名称为 ui-refinery，放入当前 Codex 的用户级 skills 目录。
```

也可以克隆到本机的用户级 skill 目录，例如：

```sh
mkdir -p ~/.agents/skills
git clone https://github.com/CrazyHandin/ui-refinery.git ~/.agents/skills/ui-refinery
```

Windows PowerShell 示例：

```powershell
git clone https://github.com/CrazyHandin/ui-refinery.git "$env:USERPROFILE\.agents\skills\ui-refinery"
```

目标目录应尚不存在；已有安装时先检查本地修改。项目级安装可放入 `.agents/skills/ui-refinery`。若当前环境尚未识别更新，可新建会话或重启 Codex。

不需要设置“所有对话必须执行 UI 设计”的全局规则。自动发现应以本 skill 的具体适用范围为准。

## 使用

新界面或方向探索：

```text
使用 $ui-refinery 为我的桌面工具设计设置页。
主要任务是快速找到并调整常用选项，沿用现有技术栈。
先提出三个不同的信息组织方向，允许你选定最合适的一项并实施。
用相关状态和真实运行截图检查结果，说明未验证的部分。
```

局部修复：

```text
使用 $ui-refinery 修复这个对话框在窄窗口中遮挡确认按钮的问题。
保留现有视觉规范，只调整相关布局和交互，验证主操作与焦点路径。
```

新设计可以探索多个方向；已有方向直接沿用；局部问题使用精简流程。用户只要概念时，交付概念和依据，不扩展为实现任务。

## 主要能力

| 能力 | 方法 |
| --- | --- |
| 任务分流 | 根据新设计、产品扩展、局部修改或纯概念选择流程长度 |
| 视觉一致性 | 优先复用已有字体、间距、语义颜色、控件和状态规范 |
| 交互完整性 | 按本次操作覆盖相关加载、空数据、失败恢复和成功反馈 |
| 真实评审 | 查看运行截图，优先修正最影响理解和操作的问题，并复查 |
| 减法精修 | 移除无用途装饰和重复说明，保留必要状态和操作线索 |

## 按需参考

| 参考 | 何时读取 |
| --- | --- |
| [软件 UI 实现](references/software-ui.md) | 产品结构、设计变量、交互状态和相关窗口适配 |
| [截图评审与媒体](references/review-and-media.md) | 视觉精修、评审证据与有明确用途的媒体 |
| [动效与交互质感](references/motion-and-polish.md) | 实际新增、调整或诊断动效与反馈 |
| [真实数据与界面边界](references/ui-data-stress.md) | 长文本、缺失字段、数量边界及相关布局问题 |
| [移动网页体验](references/mobile-web.md) | 移动 Web/PWA 的触摸、滚动、安全区与软键盘 |
| [Skill 效果验证](references/skill-evaluation.md) | 修改 skill 或明确比较不同版本的效果 |

只加载本次任务需要的参考。独立评审、浏览器、真机和媒体生成取决于当前工具与任务授权；缺少证据时如实说明。静态截图不能证明动画流畅、交互正确或完整无障碍符合性。

## 验证

```sh
python -m pip install -r tests/requirements.txt
python -X utf8 tests/validate_skill.py
python -X utf8 -m unittest discover -s tests -p 'test_*.py' -v
```

[验证方案](docs/VALIDATION.md)说明结构检查与可选端到端复现。结构和自动化测试通过不能证明视觉效果提升；实际 UI 生成、截图精修、性能和真机体验需要分别验证。

`docs/` 中早期记录保留改名前的名称和来源，用于追溯。它们不代表当前仓库已经执行过记录中的上游 CI。

## 来源

本版本基于 [houxin0010/distinctive-ai-design](https://github.com/houxin0010/distinctive-ai-design) 修改，保留其对 Anshu Chimala 文章的来源说明。新增参考选择性改编自 [emilkowalski/skills 的固定版本](https://github.com/emilkowalski/skills/tree/a81dbca07f2217b7103e510c0f13f8d5b017afc9)，并保留对应的 [MIT 许可](references/licenses/emilkowalski-MIT.txt)。完整说明见 [NOTICE](NOTICE.md)。
