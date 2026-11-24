## Goal
`parse_duration` 允许相邻的 `<数字><单位>` 之间有一个或多个空格，例如 `"1h 30m"` = 5400 秒。

## Context
- 代码：`src/durations/parse.py`；测试：`tests/test_parse.py`
- 规则见 AGENTS.md

## Constraints
- 开头、结尾的空格仍然报错（`" 1h"`、`"1h "`）
- 数字和单位之间不能有空格（`"1 h"` 报错）；只认空格，制表符照样报错
- 单位顺序规则不变；不改公共 API，不加依赖

## Done when
- 新增正反两类测试用例
- `bash scripts/verify.sh` 输出 `verify: OK`
