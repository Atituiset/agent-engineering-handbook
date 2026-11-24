# 落地起步套件 · C++

《驾驭 Agent 实践手册》[第 15 章「落地起步套件」](https://atituiset.github.io/agent-engineering-handbook/handbook/15-starter-kit)的 C++ 版本。这个分支的根目录就是一个完整、可直接 clone 的项目：一个很小但真实的库（把 `1h30m` 这样的时长解析成秒数），加上让编码智能体「改完必须过检查」的全套配置。

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
├── .pre-commit-config.yaml       # clang-format + scripts/verify.sh
├── .github/workflows/ci.yml      # CI 只做一件事：bash scripts/verify.sh
├── .github/workflows/evals.yml   # 智能体评测：mock 智能体跑 evals/，低于基线就失败
├── evals/                        # 评测任务、隐藏测试和 harness（见 evals/README.md）
├── scripts/
│   ├── verify.sh                 # 格式 → 构建(-Werror) → clang-tidy → ctest → skill 副本一致
│   ├── guard-protected.sh        # PreToolUse hook：受保护文件一律拦截（exit 2）
│   └── stop-verify.sh            # Stop hook：verify 不过就不许结束（exit 2）
├── CMakeLists.txt                # C++20，-Wall -Wextra -Wpedantic -Wconversion -Wshadow -Werror
├── .clang-format / .clang-tidy   # clang-tidy 的 WarningsAsErrors: "*"
├── include/durations/ src/       # 示例库
├── tests/                        # doctest 测试，由 ctest 运行
└── third_party/doctest/          # doctest 2.5.3 单头文件（MIT），构建不需要联网
```

## 前置工具

| 工具 | 本仓库实测版本（2026-11-20，Debian 13） | 说明 |
| --- | --- | --- |
| CMake | 3.31.6 | 要求 ≥ 3.20 |
| GCC | 14.2.0 | 任何支持 C++20 指定初始化器的 GCC/Clang 均可 |
| clang-format | 19.1.7 | 版本不同，格式结果可能不同；CI 用 `pipx install clang-format==19.1.7` 固定版本 |
| clang-tidy | 19.1.7（系统包）/ 19.1.0.1（PyPI 包） | 两种来源都实测通过；CI 用 `pipx install clang-tidy==19.1.0.1` |
| pre-commit | 4.7.0 | 需要 Python：`uv tool install pre-commit` 或 `pipx install pre-commit` |
| git、bash | 系统自带 | `scripts/*.sh` 需要 bash |

## 演练：从复制模板到让智能体完成一个小任务

下面每一步的「预期输出」都摘自真实运行结果。标注「需在你的编辑器/CLI 中执行」的步骤依赖智能体本身，无法在脚本里自动复现，我们只验证了它周围的检查。

### 第 1 步：复制模板

```bash
git clone --branch starter/cpp --single-branch \
  https://github.com/Atituiset/agent-engineering-handbook.git my-durations
cd my-durations
rm -rf .git && git init -b main && git add -A && git commit -m "init from starter kit"
```

### 第 2 步：跑一次 verify，确认基线是绿的

```bash
bash scripts/verify.sh
```

预期输出：

```text
==> format (clang-format --dry-run --Werror)

==> configure + build (cmake, -Werror)
[ 25%] Building CXX object CMakeFiles/durations.dir/src/parse.cpp.o
[ 50%] Linking CXX static library libdurations.a
[ 50%] Built target durations
[ 75%] Building CXX object CMakeFiles/durations_tests.dir/tests/test_parse.cpp.o
[100%] Linking CXX executable durations_tests
[100%] Built target durations_tests

==> static analysis (clang-tidy, warnings are errors)
[1/2] Processing file /path/to/my-durations/src/parse.cpp.
18766 warnings generated.
[2/2] Processing file /path/to/my-durations/tests/test_parse.cpp.
67118 warnings generated.

==> tests (ctest)
1/1 Test #1: durations_tests ..................   Passed    0.01 sec

100% tests passed, 0 tests failed out of 1

==> skill copies in sync (.agents/skills == .claude/skills)

verify: OK
```

> 「N warnings generated」是 clang-tidy 在系统头文件里发现、但按配置不报告的警告，数量随编译器和标准库版本变化，不是失败。只有带 `error:` 的行才会让这一步失败。

### 第 3 步：装上 pre-commit

```bash
uv tool install pre-commit      # 或 pipx install pre-commit
pre-commit install
pre-commit run --all-files
```

预期输出：

```text
pre-commit installed at .git/hooks/pre-commit
clang-format --dry-run --Werror..........................................Passed
build + clang-tidy + ctest (scripts/verify.sh)...........................Passed
```

### 第 4 步：确认 hook 脚本能拦住受保护文件

Claude Code 在每次 Edit/Write 前把调用信息以 JSON 传给 `scripts/guard-protected.sh`。脚本本身可以手动测：

```bash
echo '{"tool_name":"Edit","tool_input":{"file_path":"/x/.clang-tidy"}}' | scripts/guard-protected.sh; echo "exit=$?"
```

预期输出：

```text
blocked: /x/.clang-tidy is protected (CI, checks, dependency and tool config). Ask a human to change it.
exit=2
```

**需在你的 CLI 中执行**：在 Claude Code 里输入 `/hooks`，确认 PreToolUse、PostToolUse、Stop 三个 hook 已加载。其他工具（Codex、Cursor 等）的 hook 机制各不相同，本套件只附了 Claude Code 版；在别的工具里，pre-commit 和 CI 这两道检查照样生效。

### 第 5 步：让智能体完成一个小任务（需在你的编辑器/CLI 中执行）

把下面这段任务说明（格式取自手册 [第 11 章 §3](https://atituiset.github.io/agent-engineering-handbook/handbook/11-checklists#_3-任务说明模板)）交给智能体：

```markdown
## Goal
durations::parse_duration 支持 d（天）这个单位，例如 "1d2h" = 93600。

## Context
- 代码：src/parse.cpp、include/durations/parse.hpp；测试：tests/test_parse.cpp
- 规则见 AGENTS.md

## Constraints
- 单位仍须按降序出现、每个最多一次（"1h1d" 应报错）
- 不新增公共函数，不加依赖

## Done when
- 新增正反两类测试用例
- bash scripts/verify.sh 输出 verify: OK，并把最后几行贴进总结
```

### 第 6 步：看检查能拦住什么（真实失败输出）

为了确认检查真的有效，我们手工模拟了一个「不守规矩」的改动：把 `d` 加到单位表**末尾**（顺序错了），再顺手加一个返回 `int` 的 `total_days()`。`-Wconversion -Werror` 首先在编译阶段拦下：

```text
==> configure + build (cmake, -Werror)
/path/to/my-durations/src/parse.cpp:75:69: error: conversion from ‘int64_t’ {aka ‘long int’} to ‘int’ may change value [-Werror=conversion]
   75 | int total_days(std::string_view text) { return parse_duration(text) / 86400; }
cc1plus: all warnings being treated as errors
```

智能体常见的「修法」是加一个 C 风格强制转换把警告压下去，编译器这次放行了，但 clang-tidy 接着拦下：

```text
==> static analysis (clang-tidy, warnings are errors)
/path/to/my-durations/src/parse.cpp:75:48: error: C-style casts are discouraged; use static_cast [google-readability-casting,-warnings-as-errors]
   75 | int total_days(std::string_view text) { return (int)(parse_duration(text) / 86400); }
      |                                                ^~~~~
```

去掉这个函数之后，测试揭示了真正的逻辑错误（`d` 排在 `s` 后面，`1d2h` 被判为乱序）：

```text
==> tests (ctest)
/path/to/my-durations/tests/test_parse.cpp:19: ERROR: CHECK( parse_duration("1d2h") == 93600 ) THREW exception: "unknown, repeated or out-of-order unit 'h' in "1d2h""
[doctest] test cases:  2 |  1 passed | 1 failed | 0 skipped
The following tests FAILED:
	  1 - durations_tests (Failed)
```

同一状态下，Stop hook（`scripts/stop-verify.sh`）返回 `exit=2`，不让智能体宣布完成；pre-commit 也拒绝提交：

```text
$ git commit -m "add days"
clang-format --dry-run --Werror..........................................Passed
build + clang-tidy + ctest (scripts/verify.sh)...........................Failed
```

### 第 7 步：正确的改动，verify 通过

正确做法是把 `d` 放在单位表最前面，并补上正反用例。第一次运行时，格式检查还拦下了没按 clang-format 换行的测试代码：

```text
==> format (clang-format --dry-run --Werror)
tests/test_parse.cpp:23:33: error: code should be clang-formatted [-Wclang-format-violations]
    for (std::string_view text :
                                ^
```

执行 `find include src tests -name '*.cpp' -o -name '*.hpp' | xargs clang-format -i`（Claude Code 的 PostToolUse hook 会在每次编辑后自动做这一步）之后：

```text
==> format (clang-format --dry-run --Werror)

==> configure + build (cmake, -Werror)
[100%] Built target durations_tests

==> static analysis (clang-tidy, warnings are errors)
[1/2] Processing file /path/to/my-durations/src/parse.cpp.
18766 warnings generated.
[2/2] Processing file /path/to/my-durations/tests/test_parse.cpp.
67118 warnings generated.

==> tests (ctest)
1/1 Test #1: durations_tests ..................   Passed    0.00 sec

100% tests passed, 0 tests failed out of 1

==> skill copies in sync (.agents/skills == .claude/skills)

verify: OK
```

提交时 pre-commit 两项全部 Passed。最终 diff：

```diff
-constexpr std::array<Unit, 3> kUnits{{
+constexpr std::array<Unit, 4> kUnits{{
+    {.symbol = 'd', .seconds = 86400},
     {.symbol = 'h', .seconds = 3600},
```

```diff
     CHECK(parse_duration("1h1m1s") == 3661);
+    CHECK(parse_duration("1d") == 86400);
+    CHECK(parse_duration("1d2h") == 93600);
 }
...
-    for (std::string_view text :
-         {"", "h", "10", "1x", "1m1h", "1h1h", " 1h", "1h ", "99999999999999999999s"}) {
+    for (std::string_view text : {"", "h", "10", "1x", "1m1h", "1h1h", " 1h", "1h ", "1h1d", "1d1d",
+                                  "99999999999999999999s"}) {
```

### 第 8 步：推到 GitHub，让 CI 做最终裁判

`.github/workflows/ci.yml` 在 push 和 pull request 时运行：用 pipx 装固定版本的 clang-format 19.1.7 与 clang-tidy 19.1.0.1，然后只执行 `bash scripts/verify.sh`，和本地是同一条命令。在仓库 **Settings → Branches** 里把 `ci / verify` 设为必需检查，智能体就无法绕过它合并（手册 [第 12 章示例 A](https://atituiset.github.io/agent-engineering-handbook/handbook/12-quality-cicd#example-a)）。

我们在本地用 PyPI 上同版本的 clang-format / clang-tidy 包，在全新 clone 里跑了与 CI 相同的命令，结果通过；GitHub 托管 runner（ubuntu-24.04 自带 CMake 与 GCC）上的实际运行结果请以该分支的 Actions 页面为准。

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

## 智能体评测（evals/）

`scripts/verify.sh` 只回答“这一次改动对不对”；要回答“换了模型、提示词或规则之后，智能体是变好还是变差”，需要评测（手册[第 16 章](https://atituiset.github.io/agent-engineering-handbook/handbook/16-agent-evals)）。`evals/` 是一套最小实现：3 个任务（2 个回归、1 个能力），每个任务跑多次，在不含 `evals/` 的副本里让智能体工作，再在干净副本里跑隐藏测试和 `verify.sh` 判分，报告 pass@k、pass^k 和 Wilson 95% 区间，并由 `.github/workflows/evals.yml` 和 `evals/baseline.json` 比较、回归即失败。默认用离线 mock 智能体，CI 不需要模型密钥。

```bash
python3 evals/run_evals.py run --trials 5 --k 1 3 5 --out evals/results.json
python3 evals/run_evals.py gate --baseline evals/baseline.json --current evals/results.json --k 3
```

本地实测（2026-11-25，mock 智能体）：回归集 8/10 次通过，pass^3 = 0.550；能力集 3/5，pass@3 = 1.000。故意调低 mock 成功率后门禁失败，回归集 pass^3 0.550 → 0.050；让 mock 在失败时改 `scripts/verify.sh`，隔离判分记下 4 次违规、门禁失败，而只在它自己目录里跑 verify 的对照判分是 15/15 全部“通过”。这些数字只说明 harness 能工作，不代表任何真实模型；接入真实智能体的方法见 [evals/README.md](evals/README.md)。

## 用到你自己的项目

1. 复制 `scripts/`、`.pre-commit-config.yaml`、`.github/workflows/ci.yml`、`.claude/`、`.agents/`、`.cursor/`、`CLAUDE.md`。
2. 重写 `AGENTS.md`：只写模型读不到、猜不到的东西（命令、边界、非标准约定、坑点），控制在 100 行以内（手册 [第 02 章 §3](https://atituiset.github.io/agent-engineering-handbook/handbook/02-context-engineering#_3-写法-一份好的-agents-md-包含什么)）。
3. 把 `CMakeLists.txt` 里的警告选项、`.clang-format`、`.clang-tidy` 合并到你的工程；老项目一次清不完 clang-tidy 的发现时，先只对改动的文件运行（例如 `git diff --name-only` 过滤），再逐步扩大。
4. 改 `scripts/guard-protected.sh` 里的 `PROTECTED_REGEX`，把你的 CI、迁移脚本、架构测试加进去。
5. 把你最重要的 3–5 条架构规则写成测试或 lint 规则，加进 `scripts/verify.sh`（手册 [第 04 章 §4](https://atituiset.github.io/agent-engineering-handbook/handbook/04-architecture-constraints#_4-工具箱-把架构规则变成检查)）。

## 已知限制

- 智能体本身的行为（第 5 步）无法在脚本里复现；我们验证的是它周围的检查：verify.sh、pre-commit、hook 脚本、CI 的等价命令。
- `.claude/settings.json` 的 hook 配置按 Claude Code 文档的格式编写，脚本已手动测试；在 Claude Code 里实际触发的情况请用第 4 步的 `/hooks` 自行确认。
- `CLAUDE.md` 用 `@AGENTS.md` 导入同一份规则；Cursor 的 `.mdc` 规则同样用 `@AGENTS.md` 引用。如果你用的工具版本不支持这种引用，就把 AGENTS.md 的内容直接复制过去。
