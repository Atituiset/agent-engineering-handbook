# 落地起步套件 · TypeScript

《驾驭 Agent 实践手册》[第 15 章「落地起步套件」](https://atituiset.github.io/agent-engineering-handbook/handbook/15-starter-kit)的 TypeScript 版本。这个分支的根目录就是一个完整、可直接 clone 的项目：一个很小但真实的库（把 `1h30m` 这样的时长解析成秒数），加上让编码智能体「改完必须过检查」的全套配置。

手册里「把规则变成检查」的原则，在这里对应到具体文件：

```text
规则写在哪            谁来执行                   本仓库中的文件
-----------------    -----------------------    ------------------------------------------
告诉智能体怎么做      智能体读取（可能不遵守）    AGENTS.md、CLAUDE.md、.cursor/rules/project.mdc
改完必须过的检查      你、智能体、CI 同一条命令   scripts/verify.sh
提交前自动拦截        git pre-commit 钩子         .pre-commit-config.yaml
编辑时自动拦截        Claude Code hooks           .claude/settings.json + scripts/guard-protected.sh
宣布完成前强制验证    Claude Code Stop hook       scripts/stop-verify.sh
合并前最终裁判        GitHub Actions              .github/workflows/ci.yml
怎样跑验证（按需）    智能体按需加载的 skill      .agents/skills/verify/（.claude/skills/ 为同内容副本）
```

## 目录

```text
.
├── AGENTS.md                     # 唯一的规则源：命令、边界、非标准约定、坑点
├── CLAUDE.md                     # 只有一行 @AGENTS.md，让 Claude Code 读同一份
├── .cursor/rules/project.mdc     # Cursor 规则，alwaysApply，指向 AGENTS.md
├── .agents/skills/verify/SKILL.md  # verify skill（Codex、Gemini CLI、Copilot、Cursor、OpenCode 读这里）
├── .claude/skills/verify/SKILL.md  # 同内容副本（Claude Code 只读 .claude/skills/），verify.sh 检查两者一致
├── .claude/settings.json         # hooks：拦截受保护文件、编辑后格式化、完成前跑 verify
├── .pre-commit-config.yaml       # prettier / eslint / tsc / vitest
├── .github/workflows/ci.yml      # CI 只做一件事：bash scripts/verify.sh
├── scripts/
│   ├── verify.sh                 # 格式 → lint → 类型 → 测试 → 构建 → skill 副本一致
│   ├── guard-protected.sh        # PreToolUse hook：受保护文件一律拦截（exit 2）
│   └── stop-verify.sh            # Stop hook：verify 不过就不许结束（exit 2）
├── package.json / package-lock.json  # 依赖与工具版本全部锁定
├── tsconfig.json / tsconfig.build.json  # strict + noUncheckedIndexedAccess
├── eslint.config.js              # typescript-eslint strictTypeChecked，任何 error 都失败
├── src/                          # 示例库
└── test/                         # vitest
```

## 前置工具

| 工具                                    | 本仓库实测版本（2026-11-20，Debian 13） | 说明                                                                                                                     |
| --------------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Node.js / npm                           | 24.22.1 / 11.21.1                       | 要求 Node ≥ 20；CI 用 Node 22                                                                                            |
| typescript / eslint / typescript-eslint | 6.0.3 / 10.15.0 / 8.73.0                | 由 `package-lock.json` 锁定                                                                                              |
| vitest / prettier                       | 5.1.1 / 3.10.1                          | 同上，不需要全局安装                                                                                                     |
| pre-commit                              | 4.7.0                                   | 需要 Python：`uv tool install pre-commit` 或 `pipx install pre-commit`；只想用 Node 生态的话，可改用 husky，检查命令不变 |
| git、bash                               | 系统自带                                | `scripts/*.sh` 需要 bash                                                                                                 |

## 演练：从复制模板到让智能体完成一个小任务

下面每一步的「预期输出」都摘自真实运行结果。标注「需在你的编辑器/CLI 中执行」的步骤依赖智能体本身，无法在脚本里自动复现，我们只验证了它周围的检查。

### 第 1 步：复制模板

```bash
git clone --branch starter/typescript --single-branch \
  https://github.com/Atituiset/agent-engineering-handbook.git my-durations
cd my-durations
rm -rf .git && git init -b main && git add -A && git commit -m "init from starter kit"
npm ci
```

### 第 2 步：跑一次 verify，确认基线是绿的

```bash
bash scripts/verify.sh
```

预期输出（vitest 的时间戳与耗时每次不同）：

```text
==> format (prettier --check)
Checking formatting...
All matched files use Prettier code style!

==> lint (eslint)

==> types (tsc --noEmit)

==> tests (vitest run)

 RUN  v5.1.1 /path/to/my-durations

 Test Files  1 passed (1)
      Tests  14 passed (14)

==> build (tsc -p tsconfig.build.json)

==> skill copies in sync (.agents/skills == .claude/skills)

verify: OK
```

> eslint 和 tsc 通过时不输出任何内容，这是正常的。没有 `node_modules` 时 verify.sh 会先执行 `npm ci`。

### 第 3 步：装上 pre-commit

```bash
uv tool install pre-commit      # 或 pipx install pre-commit
pre-commit install
pre-commit run --all-files
```

预期输出：

```text
pre-commit installed at .git/hooks/pre-commit
prettier --check.........................................................Passed
eslint...................................................................Passed
tsc --noEmit.............................................................Passed
vitest run...............................................................Passed
```

### 第 4 步：确认 hook 脚本能拦住受保护文件

Claude Code 在每次 Edit/Write 前把调用信息以 JSON 传给 `scripts/guard-protected.sh`。脚本本身可以手动测：

```bash
echo '{"tool_name":"Write","tool_input":{"file_path":"/x/eslint.config.js"}}' | scripts/guard-protected.sh; echo "exit=$?"
```

预期输出：

```text
blocked: /x/eslint.config.js is protected (CI, checks, dependency and tool config). Ask a human to change it.
exit=2
```

**需在你的 CLI 中执行**：在 Claude Code 里输入 `/hooks`，确认 PreToolUse、PostToolUse、Stop 三个 hook 已加载。其他工具（Codex、Cursor 等）的 hook 机制各不相同，本套件只附了 Claude Code 版；在别的工具里，pre-commit 和 CI 这两道检查照样生效。

### 第 5 步：让智能体完成一个小任务（需在你的编辑器/CLI 中执行）

把下面这段任务说明（格式取自手册 [第 11 章 §3](https://atituiset.github.io/agent-engineering-handbook/handbook/11-checklists#_3-任务说明模板)）交给智能体：

```markdown
## Goal

parseDuration 支持 d（天）这个单位，例如 "1d2h" = 93600。

## Context

- 代码：src/parse.ts；测试：test/parse.test.ts
- 规则见 AGENTS.md

## Constraints

- 单位仍须按降序出现、每个最多一次（"1h1d" 应报错）
- 不改导出，不加依赖

## Done when

- 新增正反两类测试用例
- bash scripts/verify.sh 输出 verify: OK，并把最后几行贴进总结
```

### 第 6 步：看检查能拦住什么（真实失败输出）

为了确认检查真的有效，我们手工模拟了一个「不守规矩」的改动：把 `d` 加到单位表**末尾**（顺序错了），再顺手导出一个参数没写类型的 `totalDays(text)`。eslint 首先拦下：

```text
==> lint (eslint)

/path/to/my-durations/src/parse.ts
  53:8   error  Missing return type on function                                         @typescript-eslint/explicit-function-return-type
  54:35  error  Unsafe argument of type `any` assigned to a parameter of type `string`  @typescript-eslint/no-unsafe-argument

✖ 2 problems (2 errors, 0 warnings)
```

即使 lint 被绕过，类型检查也会拦住同一个问题：

```text
$ npx --no-install tsc --noEmit
src/parse.ts(53,27): error TS7006: Parameter 'text' implicitly has an 'any' type.
```

删掉 `totalDays` 之后，测试揭示了真正的逻辑错误（`d` 排在 `s` 后面，`1d2h` 被判为乱序）：

```text
==> tests (vitest run)
 FAIL  test/parse.test.ts > parseDuration > parses 1d2h as 93600 seconds
DurationError: unit "h" repeated or out of order in "1d2h"
 ❯ parseDuration src/parse.ts:44:13
      Tests  1 failed | 15 passed (16)
```

同一状态下，Stop hook（`scripts/stop-verify.sh`）返回 `exit=2`，不让智能体宣布完成；pre-commit 也拒绝提交：

```text
$ git commit -m "add days"
prettier --check.........................................................Passed
eslint...................................................................Passed
tsc --noEmit.............................................................Passed
vitest run...............................................................Failed
```

### 第 7 步：正确的改动，verify 通过

正确做法是把 `d` 放在单位表最前面，并补上正反用例。第一次运行时，格式检查还拦下了一行过长的测试代码：

```text
==> format (prettier --check)
Checking formatting...
[warn] test/parse.test.ts
[warn] Code style issues found in the above file. Run Prettier with --write to fix.
```

执行 `npm run format`（Claude Code 的 PostToolUse hook 会在每次编辑后自动做这一步）之后：

```text
==> format (prettier --check)
All matched files use Prettier code style!

==> lint (eslint)

==> types (tsc --noEmit)

==> tests (vitest run)
 Test Files  1 passed (1)
      Tests  18 passed (18)

==> build (tsc -p tsconfig.build.json)

==> skill copies in sync (.agents/skills == .claude/skills)

verify: OK
```

提交时 pre-commit 四项全部 Passed。最终 diff：

```diff
 const UNIT_SECONDS: ReadonlyMap<string, number> = new Map([
+  ["d", 86400],
   ["h", 3600],
```

```diff
     ["1h1m1s", 3661],
+    ["1d", 86400],
+    ["1d2h", 93600],
   ])("parses %s as %i seconds", (text, expected) => {
...
-  it.each(["", "h", "10", "1x", "1m1h", "1h1h", " 1h", "1h "])("rejects %j", (text) => {
-    expect(() => parseDuration(text)).toThrow(DurationError);
-  });
+  it.each(["", "h", "10", "1x", "1m1h", "1h1h", " 1h", "1h ", "1h1d", "1d1d"])(
+    "rejects %j",
+    (text) => {
+      expect(() => parseDuration(text)).toThrow(DurationError);
+    },
+  );
```

### 第 8 步：推到 GitHub，让 CI 做最终裁判

`.github/workflows/ci.yml` 在 push 和 pull request 时运行：装 Node 22、`npm ci`，然后只执行 `bash scripts/verify.sh`，和本地是同一条命令。在仓库 **Settings → Branches** 里把 `ci / verify` 设为必需检查，智能体就无法绕过它合并（手册 [第 12 章示例 A](https://atituiset.github.io/agent-engineering-handbook/handbook/12-quality-cicd#example-a)）。

我们在本地用全新 clone 跑了与 CI 相同的命令（`npm ci && bash scripts/verify.sh`），结果通过；GitHub 托管 runner 上的实际运行结果请以该分支的 Actions 页面为准。

## Skills 与 MCP

本套件自带的 skill 只有一个 `verify`：手册 [第 13 章 §0.2](https://atituiset.github.io/agent-engineering-handbook/handbook/13-skills-catalog#starter-set) 的「最小组合」建议个人先自己写一个 verify skill。下面的命令都在本机实际跑过：

```bash
# 以下两个工具是 Python 写的，用 uv 安装
# 校验 skill 格式（agentskills/agentskills 的参考实现 skills-ref；其 README 注明仅供演示，不建议用于生产）
uv tool install "git+https://github.com/agentskills/agentskills#subdirectory=skills-ref"
skills-ref validate .agents/skills/verify
# → Valid skill: .agents/skills/verify

# 安全扫描（NVIDIA/SkillSpector；--no-llm 只做静态规则扫描）
uv tool install --python 3.13 git+https://github.com/NVIDIA/skillspector.git
skillspector scan .agents/skills/verify/ --no-llm
# → Score 0/100 · Severity LOW · Recommendation SAFE · No security issues detected.
```

想参考社区 skill 时，用 [vercel-labs/skills](https://github.com/vercel-labs/skills) 先列出再挑一个装，装完先扫描、再读：

```bash
npx skills add obra/superpowers --list          # 列出可选 skill，不安装
npx skills add mattpocock/skills --skill tdd -a claude-code -y
# → ✓ tdd (copied) → ./.claude/skills/tdd ；同时生成 skills-lock.json（记录来源 commit 与内容哈希）
skillspector scan .claude/skills/tdd --no-llm
# → Score 0/100 · Recommendation SAFE（静态扫描结果，不能代替人工阅读）
```

第 13 章把 obra/superpowers、mattpocock/skills、anthropics/skills 标为「参考」：读懂后改写成自己的版本，不要整包安装。扫描为 SAFE 只说明静态规则没有命中，不等于安全（第 13 章 §6、第 09 章）。

**MCP**：本套件默认不配置任何 MCP 服务器。手册 [第 07 章「CLI vs MCP」](https://atituiset.github.io/agent-engineering-handbook/handbook/07-harness-tools#cli-vs-mcp) 的取舍是：内部工具优先做成 CLI（这里就是 `scripts/verify.sh`）；需要认证、跨应用或厂商已提供的集成再用 MCP，而每加一个服务器都会扩大攻击面。真要接入时，从第 13 章所列的厂商官方来源选（例如 AWS 的 [agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws)、Cloudflare 的 [skills](https://github.com/cloudflare/skills) 插件），并先用 `skillspector` 的 MCP 扫描或 [Tencent/AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard) 检查。

## 用到你自己的项目

1. 复制 `scripts/`、`.pre-commit-config.yaml`、`.github/workflows/ci.yml`、`.claude/`、`.agents/`、`.cursor/`、`CLAUDE.md`。
2. 重写 `AGENTS.md`：只写模型读不到、猜不到的东西（命令、边界、非标准约定、坑点），控制在 100 行以内（手册 [第 02 章 §3](https://atituiset.github.io/agent-engineering-handbook/handbook/02-context-engineering#_3-写法-一份好的-agents-md-包含什么)）。
3. 合并 `tsconfig.json`、`eslint.config.js`、`.prettierrc.json` 到你的配置；老项目一次开不了 `strictTypeChecked` 时，先对新目录开，逐步扩大。
4. 改 `scripts/guard-protected.sh` 里的 `PROTECTED_REGEX`，把你的 CI、迁移脚本、架构测试加进去。
5. 把你最重要的 3–5 条架构规则写成测试或 lint 规则，加进 `scripts/verify.sh`（手册 [第 04 章 §4](https://atituiset.github.io/agent-engineering-handbook/handbook/04-architecture-constraints#_4-工具箱-把架构规则变成检查)）。

## 已知限制

- 智能体本身的行为（第 5 步）无法在脚本里复现；我们验证的是它周围的检查：verify.sh、pre-commit、hook 脚本、CI 的等价命令。
- `.claude/settings.json` 的 hook 配置按 Claude Code 文档的格式编写，脚本已手动测试；在 Claude Code 里实际触发的情况请用第 4 步的 `/hooks` 自行确认。
- `CLAUDE.md` 用 `@AGENTS.md` 导入同一份规则；Cursor 的 `.mdc` 规则同样用 `@AGENTS.md` 引用。如果你用的工具版本不支持这种引用，就把 AGENTS.md 的内容直接复制过去。
