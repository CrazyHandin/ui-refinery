# Emil 设计工程参考整合

> 历史记录：本文保留改名前的名称、调用示例与当时验证范围。当前 skill 已更名为 `ui-refinery`，使用方式见 [README](../README.md)；原项目 CI 链接不代表本仓库已经运行相同检查。

日期：2026-10-31（Asia/Shanghai）。对本机已优化的 `distinctive-ai-design` 增补按需参考，保持名称、调用提示和现有全局调用规则。

## 来源与版本

源仓库：[emilkowalski/skills](https://github.com/emilkowalski/skills/tree/a81dbca07f2217b7103e510c0f13f8d5b017afc9)。固定提交为 `a81dbca07f2217b7103e510c0f13f8d5b017afc9`，从同一 GitHub ZIP 快照读取选定文件，使用 ZIP 中的提交注释记录版本。

选择了设计工程、动画实现、动画性能、mobile-native、break-ui、边界样例目录、UI cheatsheet 和 LICENSE 共 8 份源文件。各文件及原归档的 SHA-256 见 [来源清单](emil-source-manifest.json)。原仓库的开场白、自动触发元数据和强制输出格式未合并；只整理适合当前工作流的经验，并保留 [MIT 许可](../references/licenses/emilkowalski-MIT.txt)。

## 按需参考

| 参考 | 使用时机 | 具体内容 |
| --- | --- | --- |
| [动效与交互质感](../references/motion-and-polish.md) | 实际新增、调整或诊断动效与反馈 | 动效用途、频率、参数起点、连续操作与取消、减少动态效果、性能证据 |
| [真实数据与界面边界](../references/ui-data-stress.md) | 有数据界面的相关边界问题或专门检查 | 字段约束、可信边界、测试数据入口、布局原因、同条件复查与检查/修复范围 |
| [移动网页体验](../references/mobile-web.md) | 移动浏览器或 PWA 的触摸、滚动、视口和输入问题 | 按能力处理交互、保留缩放、局部手势、安全区、软键盘、模拟环境与真机证据 |

主入口仅增加具体任务与参考的对应表，不要求每个 UI 任务加载全部细节。没有安装整套上游 skills，也没有新增付费服务或项目依赖。

## 适配重点

- 动效按用途和使用频率判断，时长作为可调整起点；未采用全局禁止键盘触发动效或必须使用固定曲线的做法。
- 性能结论需要复现和测量；CSS/WAAPI 加速及 Motion 的属性处理依赖版本、API 与浏览器，不能只凭属性名断言。对照了 [Motion 官方性能文档](https://motion.dev/docs/performance)。
- 保留缩放与原生输入能力；滚动、文字选择和手势改为局部按症状处理。软键盘不等同于动态视口单位已解决的问题，对照了 [MDN：VisualViewport](https://developer.mozilla.org/en-US/docs/Web/API/VisualViewport)、[touch-action](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/touch-action)及[视口长度单位](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)。
- 普通修改只使用少量相关边界，专门检查才扩大覆盖；不强制每次创建数据切换面板。用户已要求修复时按授权完成，不额外停下等待确认。
- 未将 CSS 方案用于原生平台，也未把作者的库偏好变成项目必须安装的清单。

## 实际验证与限制

| 检查 | 结果 | 范围 |
| --- | --- | --- |
| skill-creator quick_validate.py | PASS | 元数据、名称和未完成占位检查 |
| 仓库 validate_skill.py | PASS | 必要文件、YAML、名称和 Markdown 相对文件引用 |
| unittest 完整测试 | PASS，25 项 | 原有静态与负向检查、完整参考复制、来源哈希及已有目录保护 |
| 来源与许可 | 已记录并核对 | 固定快照、各源文件哈希、随包许可与引用路径；参考不依赖在线下载才能阅读 |
| 适用范围与执行习惯 | 已做文本自查 | 局部修复、高频键盘交互、数据检查/修复、移动 Web 与原生平台的分流；并非独立模型测试 |
| 实际 UI 生成、视觉 A/B、动画性能与真机体验 | NOT VERIFIED | 本次整理 skill，未生成或测试具体产品 UI；不能由上述测试推断视觉提升比例 |

测试使用已有工作目录内的 Python 3.12.10 与隔离依赖，临时文件也位于工作目录。主 skill 不依赖这些测试工具运行。

## 维护

继续调用 `$distinctive-ai-design`。以后更新上游参考时，对照固定提交和官方实现文档复核；保留本地任务分流与用户偏好。历史本地优化见 [上一轮记录](LOCAL_UPDATE_2026-10-31.md)。
