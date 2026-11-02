# UI Refinery 改名与发布检查

日期：2026-11-03（Asia/Shanghai）。当前维护名称为 `ui-refinery`，仓库为 [CrazyHandin/ui-refinery](https://github.com/CrazyHandin/ui-refinery)。

## 改名范围

- 同步 skill 元数据、展示名称、默认调用、README 示例、测试名称契约和端到端夹具路径。
- 保留已有的任务范围修正：仅在当前任务明确涉及具体界面目标时应用；非 UI 和 skill 维护任务不附加设计要求。
- 新安装示例指向本仓库根目录，不再指向上游原版。
- 保留原项目来源、固定版本的 Emil 参考与完整第三方许可，见 [NOTICE](../NOTICE.md)。早期验证记录保留历史名称并增加上下文说明。
- 修复文档校验器将 PowerShell `$env:USERPROFILE` 误识别为 skill 名称的问题，并增加相应回归案例；错误的 skill 调用仍会被检查出来。

## 实际本地验证

环境：Windows、Python 3.12.10；隔离测试依赖为 PyYAML 6.0.3、markdown-it-py 4.0.0、mdurl 0.1.2。

| 检查 | 结果 | 范围 |
| --- | --- | --- |
| skill-creator quick_validate.py | PASS | 元数据、命名、未完成占位 |
| tests/validate_skill.py | PASS | 必要文件、严格 YAML、默认调用、文档调用和本地相对引用 |
| unittest 完整测试 | PASS，26 项 | 原有结构和负向检查、夹具参考完整性、来源哈希、已有目录保护及 PowerShell 文档回归 |
| UI 生成、视觉对照、性能与真机体验 | NOT VERIFIED | 本次改名并发布 skill，未运行具体产品 UI 验证 |

初次检查发现 PowerShell 示例误报，修正后重新运行结构检查和完整测试并通过。本文只记录实际本地检查，不预写远程 CI 结果；GitHub Actions 的实际状态见[工作流运行](https://github.com/CrazyHandin/ui-refinery/actions/workflows/smoke.yml)。

复现步骤和可选端到端验收见 [验证方案](VALIDATION.md)。
