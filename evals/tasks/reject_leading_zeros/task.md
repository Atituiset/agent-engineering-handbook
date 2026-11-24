## Goal
`Durations.parse` 拒绝带前导零的数字：`"01h"`、`"1h05m"`、`"00s"` 都应报错；单独一个 `0`（如 `"0s"`、`"1h0m"`）仍然合法。

## Context
- 代码：`src/main/java/example/durations/Durations.java`；测试：`src/test/java/example/durations/DurationsTest.java`
- 规则见 AGENTS.md

## Constraints
- 报错方式和现有错误一致（`DurationException`）
- 不改公共 API，不加依赖

## Done when
- 新增正反两类测试用例
- `bash scripts/verify.sh` 输出 `verify: OK`
