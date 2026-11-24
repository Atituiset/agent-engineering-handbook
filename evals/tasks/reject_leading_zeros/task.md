## Goal
`ParseDuration` 拒绝带前导零的数字：`"01h"`、`"1h05m"`、`"00s"` 都应报错；单独一个 `0`（如 `"0s"`、`"1h0m"`）仍然合法。

## Context
- 代码：`durations.go`；测试：`durations_test.go`
- 规则见 AGENTS.md

## Constraints
- 报错方式和现有错误一致（`ErrInvalid`）
- 不改公共 API，不加依赖

## Done when
- 新增正反两类测试用例
- `bash scripts/verify.sh` 输出 `verify: OK`
