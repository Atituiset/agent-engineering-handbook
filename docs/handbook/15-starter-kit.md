# 15 · 落地起步套件：可直接 clone 的七种语言模板

[[toc]]

## 要点

- **前 14 章讲「该做什么」，这一章给「拿来就能跑的东西」。** 手册仓库里有七个独立分支：`starter/python`、`starter/typescript`、`starter/cpp`、`starter/java`、`starter/rust`、`starter/c`、`starter/go`。每个分支的根目录都是一个完整的小项目，可以直接 clone 后当模板用。
- **核心只有一条命令：`scripts/verify.sh`。** 智能体、人、pre-commit、Claude Code 的 Stop hook 和 GitHub Actions 跑的都是它：格式、lint、类型检查（编译型语言为 `-Werror` 编译或等价的严格模式，再加静态分析）、测试。本地绿就等于 CI 绿。
- **每个分支都在本机实测过。** 2026-11-20 在 Debian 13 上，七个分支的 verify.sh 都从 git bundle clone 出的干净副本跑通；我们还故意改坏代码，确认类型或转换检查、lint、测试、格式检查、pre-commit、Stop hook 和受保护文件拦截都会生效（§4 摘录了真实输出）。Python、TypeScript、C++、Rust、C、Go 六个分支的 GitHub Actions 也已实际跑通。Java 分支在 GitHub 上的第一次运行失败了：wrapper 下载 Maven 时出错，而 verify.sh 把报错过滤掉了（经过见 §7）。修复后的运行结果以该分支 Actions 页面为准。
- **智能体本身的行为没法用脚本复现。** 「把任务交给智能体」这一步标为「需在你的编辑器/CLI 中执行」；我们验证的是它周围的检查。
- **规则文件只是「建议」，检查才是「必须」**（[第 04 章](./04-architecture-constraints)）。所以 AGENTS.md 写得很短，真正的约束放在 verify.sh、hook、pre-commit 和 CI 里。

> 想先知道该读什么、先做什么，见 [一页纸推荐](./00-one-page)；skill 在全书里的定位见 [第 13 章 §0](./13-skills-catalog#book-view)。这一章把其中「立即可做」的几件事做成了文件。

## 1. 七个分支 {#branches}

| 分支 | 示例项目 | 检查链（全部在 `scripts/verify.sh`） | 链接 |
| --- | --- | --- | --- |
| `starter/python` | uv + pytest 的小库 | ruff format → ruff check → mypy --strict → pytest | [tree/starter/python](https://github.com/Atituiset/agent-engineering-handbook/tree/starter/python) |
| `starter/typescript` | Node ESM + vitest 的小库 | prettier → eslint（typescript-eslint strictTypeChecked）→ tsc --noEmit → vitest → tsc build | [tree/starter/typescript](https://github.com/Atituiset/agent-engineering-handbook/tree/starter/typescript) |
| `starter/cpp` | CMake + ctest + doctest 的小库 | clang-format → `-Werror` 编译 → clang-tidy（警告即错误）→ ctest | [tree/starter/cpp](https://github.com/Atituiset/agent-engineering-handbook/tree/starter/cpp) |
| `starter/java` | JDK 21 + Maven wrapper + JUnit 5 的小库 | Spotless（google-java-format）→ javac `-Xlint:all -Werror` + Error Prone → JUnit 5 | [tree/starter/java](https://github.com/Atituiset/agent-engineering-handbook/tree/starter/java) |
| `starter/rust` | cargo 库 crate，工具链由 rust-toolchain.toml 固定 | cargo fmt --check → cargo clippy（pedantic，`-D warnings`）→ cargo test | [tree/starter/rust](https://github.com/Atituiset/agent-engineering-handbook/tree/starter/rust) |
| `starter/c` | C17 + CMake + ctest + Unity 的小库 | clang-format → `-Werror -Wconversion` 编译 → clang-tidy（含转换类与魔数检查）→ ctest | [tree/starter/c](https://github.com/Atituiset/agent-engineering-handbook/tree/starter/c) |
| `starter/go` | Go 模块，staticcheck 与 goimports 以 go.mod 的 tool 依赖固定 | gofmt + goimports → go vet → staticcheck → go test -race | [tree/starter/go](https://github.com/Atituiset/agent-engineering-handbook/tree/starter/go) |

七个示例项目做的是同一件事：把 `1h30m` 这样的时长解析成秒数，错误输入抛出专门的异常（C 和 Go 返回错误码或 error 值，Rust 返回 `Result`）。功能故意选得很小，好让注意力集中在周围的检查上。

复制模板（以 Python 为例，其他分支把分支名换掉即可）：

```bash
git clone --branch starter/python --single-branch \
  https://github.com/Atituiset/agent-engineering-handbook.git my-project
cd my-project
rm -rf .git && git init -b main && git add -A && git commit -m "init from starter kit"
bash scripts/verify.sh        # 最后一行应为 verify: OK
```

这七个分支和 `main` 没有共同历史（orphan 分支），只包含示例项目本身；文档站的构建与部署只用 `main`，互不影响。

## 2. 书里的方法对应到哪个文件 {#mapping}

| 书里的要求 | 对应文件 | 出处 |
| --- | --- | --- |
| 测试、lint、类型检查、构建一条命令跑通 | `scripts/verify.sh` | [11 §1](./11-checklists#_1-新仓库接入智能体-第一周清单)、[04 §9](./04-architecture-constraints#_9-让代码库对智能体可读、可跑) |
| 约 100 行以内的 AGENTS.md：命令、边界、非标准约定、坑点 | `AGENTS.md`（七个分支都不到 40 行） | [02 §3](./02-context-engineering#_3-写法-一份好的-agents-md-包含什么)、[11 §2](./11-checklists#_2-agents-md-模板) |
| 多个工具共用一份规则 | `CLAUDE.md` 只有一行 `@AGENTS.md`；`.cursor/rules/project.mdc` 也指向 AGENTS.md | [13 §3](./13-skills-catalog#compat) |
| 格式化与 lint 用 hook 自动执行 | `.claude/settings.json` 的 PostToolUse；`.pre-commit-config.yaml` | [07 §3](./07-harness-tools#_3-hooks-把「必须」变成确定性) |
| 受保护文件禁止智能体修改 | `scripts/guard-protected.sh`（PreToolUse，命中即 exit 2） | [04 §5](./04-architecture-constraints#_5-保护检查本身)、[11 §1](./11-checklists#_1-新仓库接入智能体-第一周清单) |
| 宣布完成前强制跑测试 | `scripts/stop-verify.sh`（Stop hook，verify 不过就 exit 2） | [07 §3](./07-harness-tools#_3-hooks-把「必须」变成确定性)、[05 §6](./05-verification#_6-防作弊与升级) |
| CI 是独立的最终裁判 | `.github/workflows/ci.yml` 只执行 `bash scripts/verify.sh` | [12 Q03](./12-quality-cicd#q03)、[12 示例 A](./12-quality-cicd#example-a) |
| 先自己写一个 verify skill | `.agents/skills/verify/SKILL.md`（`.claude/skills/` 下为同内容副本，verify.sh 检查两者一致） | [13 §0.2](./13-skills-catalog#starter-set)、[05 §8](./05-verification#_8-评测-为团队的-harness-建回归) |
| 工具版本锁定，本地与 CI 一致 | `uv.lock`、`package-lock.json`、Maven wrapper + pom.xml、`rust-toolchain.toml`、go.mod 的 `tool` 依赖；C/C++ 在 CI 里用 pipx 固定 clang-format 19.1.7 与 clang-tidy 19.1.0.1 | [12 Q10](./12-quality-cicd#q10) |

检查分四层，越往下越难绕过：

```text
层          触发时机                  文件                                   能否被智能体绕过
---------   -----------------------   ------------------------------------   ------------------------------
规则文件    每次会话开始              AGENTS.md / CLAUDE.md / .mdc           能：遵守与否由模型决定
编辑 hook   每次 Edit/Write 前后      .claude/settings.json + scripts/*.sh   较难：受保护文件直接拦截（仅 Claude Code）
提交 hook   git commit                .pre-commit-config.yaml                能：--no-verify 可跳过
CI          push / pull request       .github/workflows/ci.yml               不能：设为必需检查后无法合并
```

所以最后一层必须开：在 GitHub 仓库 **Settings → Branches** 把 `ci / verify` 设为必需检查（[第 12 章示例 A](./12-quality-cicd#example-a)）。

## 3. 演练：从复制模板到让智能体完成一个小任务 {#walkthrough}

每个分支的 README 都有一份完整的 8 步演练，每一步附真实运行输出。步骤相同：

```text
1  复制模板（git clone --branch starter/<lang>）
2  跑 verify，确认基线是绿的
3  装 pre-commit，pre-commit run --all-files 全部 Passed
4  手动测 hook 脚本：改受保护文件 → exit 2；改源码 → exit 0
5  把任务说明交给智能体：支持 d（天）这个单位       ← 需在你的编辑器/CLI 中执行
6  看检查能拦住什么：一个「不守规矩」的改动被逐层拦下
7  正确的改动：verify: OK，pre-commit 全部 Passed
8  推到 GitHub，把 ci / verify 设为必需检查
```

任务说明用 [第 11 章 §3](./11-checklists#_3-任务说明模板) 的模板，Done when 写明「`bash scripts/verify.sh` 输出 `verify: OK`，并把最后几行贴进总结」。这样完成标准是机器可判定的，而不是智能体自己说了算。

- Python 演练：[starter/python/README.md](https://github.com/Atituiset/agent-engineering-handbook/blob/starter/python/README.md)
- TypeScript 演练：[starter/typescript/README.md](https://github.com/Atituiset/agent-engineering-handbook/blob/starter/typescript/README.md)
- C++ 演练：[starter/cpp/README.md](https://github.com/Atituiset/agent-engineering-handbook/blob/starter/cpp/README.md)
- Java 演练：[starter/java/README.md](https://github.com/Atituiset/agent-engineering-handbook/blob/starter/java/README.md)
- Rust 演练：[starter/rust/README.md](https://github.com/Atituiset/agent-engineering-handbook/blob/starter/rust/README.md)
- C 演练：[starter/c/README.md](https://github.com/Atituiset/agent-engineering-handbook/blob/starter/c/README.md)
- Go 演练：[starter/go/README.md](https://github.com/Atituiset/agent-engineering-handbook/blob/starter/go/README.md)

## 4. 实测结果：通过与被拦住 {#results}

运行环境：2026-11-20，Debian 13。每个分支都从 git bundle clone 到干净目录再运行；Java、Go 的验证还用了空的本地 Maven 仓库和 Go 模块缓存，确认从零下载依赖也能通过；Java 另外用与 GitHub runner 相同的 Temurin 21.0.13+9 重跑了一遍。

| 分支 | 工具与版本（本机实测） | CI 里怎么固定 |
| --- | --- | --- |
| python | uv 0.13.8；ruff 0.17.6、mypy 2.4.1、pytest 9.2.0 | `uv.lock` |
| typescript | Node.js 24.22.1；TypeScript 6.0.3、eslint 10.15.0、typescript-eslint 8.73.0、vitest 5.1.1、prettier 3.10.1 | `package-lock.json`；CI 用 Node 22 |
| cpp | CMake 3.31.6、GCC 14.2.0、clang-format / clang-tidy 19.1.7、doctest 2.5.3 | pipx 安装 clang-format 19.1.7、clang-tidy 19.1.0.1 |
| java | OpenJDK 21.0.13（Debian）与 Temurin 21.0.13+9、Maven 3.9.16（wrapper）、Spotless 3.11.0、google-java-format 1.36.0、Error Prone 2.53.0、JUnit 5.14.4 | wrapper + pom.xml；CI 用 `actions/setup-java@v5` 装 Temurin 21，并缓存依赖和 wrapper 下载的 Maven |
| rust | rustup 1.29.3；rustc / cargo 1.100.0、clippy 0.1.100、rustfmt 1.11.0 | `rust-toolchain.toml`；CI 先 `rustup toolchain install 1.100.0` |
| c | CMake 3.31.6、GCC 14.2.0、clang-format / clang-tidy 19.1.7、Unity 2.7.0 | 同 cpp |
| go | Go 1.27.3、staticcheck 0.8.2、golang.org/x/tools 0.53.0（goimports） | go.mod 的 `tool` 依赖；CI 用 `actions/setup-go` 固定 1.27.3 |

所有分支的 pre-commit 都是 4.7.0。

### 4.1 基线全部通过 {#results-pass}

| 分支 | verify.sh 结果 | pre-commit run --all-files |
| --- | --- | --- |
| python | ruff format 8 files already formatted；ruff check All checks passed；mypy Success；pytest 14 passed；`verify: OK` | 4 项 Passed |
| typescript | prettier 通过；eslint、tsc 无输出；vitest 14 passed；tsc build 通过；`verify: OK` | 4 项 Passed |
| cpp | clang-format 无违规；`-Werror` 编译通过；clang-tidy 无 error；ctest 100% tests passed；`verify: OK`（系统包 LLVM 19.1.7 与 PyPI 包 clang-tidy 19.1.0.1 各跑一次，都通过） | 2 项 Passed |
| java | spotless:check、Error Prone 编译无输出；`tests passed: 15`；`verify: OK` | 2 项 Passed |
| rust | cargo fmt、clippy 通过；`test result: ok. 2 passed`（两个表驱动测试，共 15 条用例）；`verify: OK` | 3 项 Passed |
| c | clang-format 无违规；`-Werror -Wconversion` 编译通过；clang-tidy 无 error；ctest 100% tests passed；`verify: OK`（系统包与 PyPI 包 LLVM 各跑一次） | 2 项 Passed |
| go | gofmt、goimports、go vet、staticcheck 无输出；`ok  example.com/durations`；`verify: OK` | 4 项 Passed |

完成演练任务（支持 `d` 单位）之后：Python 18 passed，TypeScript 18 passed，Java `tests passed: 19`，Rust 2 个测试函数通过，C++、C 的 ctest 与 Go 的 `go test -race` 全部通过，七个分支都是 `verify: OK`。

### 4.2 故意改坏，确认会被拦住 {#results-fail}

我们手工模拟了一个「不守规矩」的改动：把 `d` 加到单位表**末尾**（顺序错了，`1d2h` 会被判为乱序），再顺手加一个偷懒的辅助函数。下面是 verify.sh 的真实输出摘录，每次修掉一个问题再跑：

| 分支 | 第一道拦截（多为类型或转换） | 第二道拦截（压掉第一道之后） | 最后由测试拦住的逻辑错误 |
| --- | --- | --- | --- |
| python | ruff：`F401 'os' imported but unused` | mypy：`error: Function is missing a type annotation [no-untyped-def]` | pytest：`DurationError: unit 'h' repeated or out of order in '1d2h'`，`1 failed, 15 passed` |
| typescript | eslint：`Missing return type on function`、`Unsafe argument of type 'any'`，`2 problems (2 errors)` | tsc：`error TS7006: Parameter 'text' implicitly has an 'any' type.` | vitest：`DurationError: unit "h" repeated or out of order in "1d2h"`，`1 failed / 15 passed` |
| cpp | GCC：`conversion from 'int64_t' to 'int' may change value [-Werror=conversion]` | 用 C 风格转换压掉警告后，clang-tidy：`C-style casts are discouraged; use static_cast [google-readability-casting,-warnings-as-errors]` | doctest：`CHECK( parse_duration("1d2h") == 93600 ) THREW exception`，ctest `1 tests failed` |
| java | javac：`incompatible types: possible lossy conversion from long to int` | 用 `(int)` 强转后，Error Prone：`[UnusedMethod] Method 'totalDays' is never used.` + `warnings found and -Werror specified` | JUnit：`DurationsTest.parsesValidDurations:24 » Duration unknown, repeated or out-of-order unit 'h' in "1d2h"`，`Tests run: 17, ... Errors: 1` |
| rust | rustc：`error[E0308]: mismatched types ... expected 'u32', found 'u64'` | 用 `as u32` 后，clippy 报 5 个 error，包括 `casting 'u64' to 'u32' may truncate the value`（cast_possible_truncation）和 `used 'unwrap()' on a 'Result' value` | `assertion 'left == right' failed: input "1d2h"`，`1 passed; 1 failed` |
| c | GCC 一次两处：`conversion from 'int64_t' to 'int' may change value [-Werror=conversion]`，`ignoring return value of 'durations_parse' declared with attribute 'warn_unused_result'` | 检查返回值并用 `(int)` 强转后，clang-tidy：`86400 is a magic number; consider replacing it with a named constant [readability-magic-numbers]` | Unity：`test_parses_valid_durations:FAIL: Expected 0 Was 3:1d2h`，ctest `1 tests failed` |
| go | go vet 的类型检查：`cannot use s / 86400 (value of type int64) as int value in return statement` | 用 `int(...)` 转换后，staticcheck：`func totalDays is unused (U1000)` | `--- FAIL: TestParseDurationValid/1d2h ... unknown, repeated or out-of-order unit 'h' in "1d2h"` |

同一状态下的其他关口：

- **Stop hook**：七个分支的 `scripts/stop-verify.sh` 都返回 `exit=2`，并输出 `scripts/verify.sh failed: fix the problems above before finishing.`
- **pre-commit**：`git commit` 被拒。Python、TypeScript、Rust、Go 是测试那一项 `Failed`；C++、C 是 `build + clang-tidy + ctest (scripts/verify.sh) ... Failed`；Java 是 `compile (Error Prone, -Werror) + JUnit (scripts/verify.sh) ... Failed`。
- **受保护文件**：`guard-protected.sh` 对 `scripts/verify.sh`、`eslint.config.js`、`.clang-tidy`、`pom.xml`、`Cargo.toml`、`tests/.clang-tidy`、`go.sum` 都输出 `blocked: ... is protected` 并返回 `exit=2`。
- **格式**：正确改动第一次运行时，七个分支都被格式检查拦下一次（过长的行或缺空格；ruff format、prettier、clang-format、google-java-format、rustfmt、gofmt），格式化后通过。

C++、Java、Rust、C、Go 这几行值得多看一眼：类型或转换错误都被一个强制转换「修好」了，这和 [第 10 章反模式 8](./10-anti-patterns#_8-让变更能修改评判它的检查) 记录的「为编译通过跳过检查」（[CN06](/sources/chinese#cn06)）是同一类行为。只有编译器一层的话，它就混过去了，第二层静态分析才把它拦下。这也是 [第 04 章](./04-architecture-constraints) 主张多层检查的原因。

要如实说明的是，第二层拦下的并不总是强转本身：C++ 的 clang-tidy 和 Rust 的 clippy 直接指出了强转（`google-readability-casting`、`cast_possible_truncation`）；Java 和 Go 拦下的是「函数没人调用」，C 拦下的是魔数。我们为 C 启用的 clang-tidy 检查没有对 `(int)` 强转报错，C 分支 README 里写明了这一点。

### 4.3 skill 工具实测 {#results-skills}

| 命令 | 结果 |
| --- | --- |
| `skills-ref validate .agents/skills/verify` | `Valid skill: .agents/skills/verify` |
| `skillspector scan .agents/skills/verify/ --no-llm` | `Score 0/100 · Severity LOW · Recommendation SAFE · No security issues detected.` |
| `npx skills add obra/superpowers --list` | 列出 15 个可选 skill，不安装 |
| `npx skills add mattpocock/skills --skill tdd -a claude-code -y` | 装到 `./.claude/skills/tdd`，生成 `skills-lock.json`（记录来源 commit 与 `computedHash`） |
| `skillspector scan .claude/skills/tdd --no-llm` | `Score 0/100 · Recommendation SAFE` |

`--no-llm` 只做静态规则扫描。SAFE 只说明静态规则没有命中，不等于安全，引入前仍要人工阅读（[第 13 章 §6](./13-skills-catalog#security)、[第 09 章](./09-security)）。skills-ref 的 README 注明它是演示用的参考实现，不建议用于生产。

## 5. Skills 与 MCP 怎么配 {#skills-mcp}

起步套件的选择全部来自 [第 13 章 §0.2 推荐起步组合](./13-skills-catalog#starter-set)，没有引入新来源：

| 组件 | 套件里的做法 | 安装命令（已实测） |
| --- | --- | --- |
| 自己写的 verify skill | 每个分支自带 `.agents/skills/verify/`，内容就是「跑 verify.sh、修代码不修检查」 | 无需安装 |
| 规范校验：[agentskills/agentskills](https://github.com/agentskills/agentskills) | 改 skill 后手动或在 CI 里跑 | `uv tool install "git+https://github.com/agentskills/agentskills#subdirectory=skills-ref"` |
| 安全扫描：[NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | 引入任何第三方 skill 前先扫 | `uv tool install --python 3.13 git+https://github.com/NVIDIA/skillspector.git` |
| 跨工具安装：[vercel-labs/skills](https://github.com/vercel-labs/skills) | 先 `--list` 再按名字装一个；`skills-lock.json` 提交进仓库 | `npx skills add <owner/repo> --skill <name> -a <agent>` |
| 参考：[obra/superpowers](https://github.com/obra/superpowers)、[mattpocock/skills](https://github.com/mattpocock/skills)、[anthropics/skills](https://github.com/anthropics/skills) | 第 13 章标为「参考」：读懂后改写成自己的，不要整包安装 | 同上，用 `--list` 浏览 |

**MCP 默认一个都不配。** [第 07 章「CLI vs MCP」](./07-harness-tools#cli-vs-mcp) 的取舍是：内部工具优先做成 CLI，人和智能体都能用，也能测试，套件里的 `scripts/verify.sh` 就是这样一个 CLI。需要认证、跨应用或厂商已提供的集成时再接 MCP，每加一个服务器都会扩大攻击面。真要接入时，从第 13 章所列厂商官方来源选（例如 [aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws)、[cloudflare/skills](https://github.com/cloudflare/skills)），接入前按 [第 09 章 §3](./09-security#_3-供应链-新的攻击面) 审查。

## 6. 套用到已有项目 {#adopt}

1. 复制 `scripts/`、`.pre-commit-config.yaml`、`.github/workflows/ci.yml`、`.claude/`、`.agents/`、`.cursor/`、`CLAUDE.md`。
2. 重写 `AGENTS.md`：只写模型读不到、猜不到的东西，控制在 100 行以内（[02 §3](./02-context-engineering#_3-写法-一份好的-agents-md-包含什么)）。
3. 把工具配置合并到你的项目。老项目一次开不了最严档位（`mypy --strict`、`strictTypeChecked`、全量 clang-tidy、clippy pedantic、Error Prone 加 `-Werror`）时，先对新模块或改动文件开，再逐步扩大。
4. 改 `scripts/guard-protected.sh` 里的 `PROTECTED_REGEX`，把你的 CI、迁移脚本、架构测试加进去。
5. 把最重要的 3–5 条架构规则写成测试或 lint 规则，加进 `scripts/verify.sh`（[04 §4](./04-architecture-constraints#_4-工具箱-把架构规则变成检查)）。
6. 在 GitHub 把 `ci / verify` 设为必需检查。没有这一步，前面几层都能被绕过。

## 7. 已知限制与未验证项 {#limits}

| 项目 | 状态 |
| --- | --- |
| verify.sh、pre-commit、hook 脚本（七种语言） | **已在本机实测**，通过和被拦住的情况都有 |
| CI 工作流 | Python、TypeScript、C++、Rust、C、Go：**GitHub Actions 已实际运行并通过**（2026-11-20）。Java：第一次运行失败（见下一行），修复后的运行**在本节写作时尚未验证**，以该分支 Actions 页面为准 |
| Java 分支第一次 CI 失败 | 日志只有 `==> format (spotless:check, google-java-format)` 和 `Process completed with exit code 1`，这一步只用了约 0.2 秒。CI 里没有缓存，`./mvnw` 要先用 wget 下载 Maven；当时的 verify.sh 为了突出编译警告，只打印以 `[WARNING]`/`[ERROR]` 开头的行，wrapper 的 `wget: Failed to fetch ...` 不是这种格式，被过滤掉了。0.2 秒不够下载并启动 Maven，所以失败的只能是下载这一步；本机让下载地址返回 403，得到完全相同的「只有标题、退出码 1」。下载为什么失败，日志里没有留下证据（Maven Central 会对共享 IP 返回 403/429，这是可能的原因之一，未证实）。修复：verify.sh 失败时原样打印 wrapper 和 Maven 的全部输出；CI 换成 `setup-java@v5`（单独缓存 wrapper 下载的 Maven），并设 `MVNW_VERBOSE=true`，再失败时日志会显示 wget 的 HTTP 状态。教训：**给检查脚本的输出做过滤，会连同你没预料到的错误一起藏起来**；失败时宁可多打印 |
| Rust 的 `cargo deny` | **未配置、未实测**：示例 crate 没有第三方依赖 |
| Java 的 google-java-format 版本 | 固定为 1.36.0：1.37.0 经 Spotless 3.11.0 调用时在本机报错（单独运行 jar 正常），原因未深究 |
| C 的显式强转 | 我们启用的 clang-tidy 检查没有报 `(int)` 强转，只能靠 AGENTS.md 的约定、测试和评审 |
| `.claude/settings.json` 中的 hook 在 Claude Code 里实际触发 | **未验证**：脚本本身已手动测试，配置按 Claude Code 文档的格式编写；请在 Claude Code 里用 `/hooks` 确认 |
| `CLAUDE.md` 的 `@AGENTS.md` 导入、Cursor `.mdc` 的 `@AGENTS.md` 引用 | **未在编辑器里验证**；若你的工具版本不支持，把 AGENTS.md 内容直接复制过去 |
| 智能体完成任务（演练第 5 步） | **需在你的编辑器/CLI 中执行**；README 里的「正确改动」是按任务说明手工完成的参考答案 |
| 其他工具（Codex、Cursor、Gemini CLI 等）的 hook | 未提供；这些工具里只有 pre-commit 与 CI 两层生效 |
| pre-commit 在 Python 以外的项目里也需要 Python | 已注明；不想引入 Python 的团队可以换成该语言生态的钩子工具（例如 husky），检查命令不变 |

## 与传统软件工程认知的对比 {#compare}

| 传统认知 | 在这套模板里 | 为什么这样选 |
| --- | --- | --- |
| 项目模板（cookiecutter、create-xxx）主要提供目录结构和依赖 | 模板的重点是检查链：一条 verify 命令，加上 hook、pre-commit、CI 三处复用 | 智能体会照着仓库里已有的东西写；没有检查，结构很快会走样（[第 04 章](./04-architecture-constraints)） |
| 编码规范写在 CONTRIBUTING 里，靠评审把关 | 规范写进 lint、类型检查和受保护文件列表，AGENTS.md 只剩命令和少量约定 | 规则文件遵不遵守由模型决定（[AN01](/sources/anthropic#an01)）；能机械判定的就交给工具 |
| CI 是团队设施，本地检查可以宽松一些 | 本地、hook、CI 跑同一个脚本，工具版本锁定 | 智能体要靠能在本地运行的验证闭环自证（[12 Q02](./12-quality-cicd#q02)）；本地与 CI 跑同一条命令，「本地绿」才有意义 |
| 警告可以先放着 | `-Werror`、clang-tidy 警告即错误、eslint `--max-warnings=0`、javac `-Werror`、clippy `-D warnings` | 智能体会用压掉警告的方式「修好」问题（§4.2 的各种强制转换），只有零容忍才能逼它改代码 |

## 本章小结 {#summary}

- 七个 orphan 分支 `starter/python`、`starter/typescript`、`starter/cpp`、`starter/java`、`starter/rust`、`starter/c`、`starter/go`，各自是一个能直接 clone 的完整项目。
- 唯一的完成标准是 `bash scripts/verify.sh` 输出 `verify: OK`。智能体、人、pre-commit、Stop hook 和 CI 都跑这一条命令。
- 实测：七个分支基线全部通过；一个故意写错的改动，被类型或转换检查、lint 或静态分析、测试、格式检查、pre-commit 和 Stop hook 逐层拦下，受保护文件的修改被 hook 脚本拒绝。
- 没验证的部分已经如实标出：Java 分支修复后在 GitHub runner 上的 CI 运行、Claude Code 里实际触发 hook、各编辑器对 `@AGENTS.md` 的支持，以及智能体本身的行为。
- 下一步：按 §6 套用到你自己的项目，把 `ci / verify` 设为必需检查，再按 [一页纸推荐](./00-one-page#do-now) 逐项补齐其余几件事。
