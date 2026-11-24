## Goal
`Durations.parse` 支持 `d`（天）这个单位，例如 `"1d2h"` = 93600 秒。

## Context
- 代码：`src/main/java/example/durations/Durations.java`；测试：`src/test/java/example/durations/DurationsTest.java`
- 规则见 AGENTS.md

## Constraints
- 单位仍须按降序出现、每个最多一次（`"1h1d"`、`"1d1d"` 应报错）
- 不改公共 API，不加依赖

## Done when
- 新增正反两类测试用例
- `bash scripts/verify.sh` 输出 `verify: OK`
