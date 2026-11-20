# 15 · 落地起步套件：可直接 clone 的 Python / TypeScript / C++ 模板

[[toc]]

## 要点

- **前 14 章讲「该做什么」，这一章给「拿来就能跑的东西」。** 手册仓库里有三个独立分支 `starter/python`、`starter/typescript`、`starter/cpp`，每个分支的根目录都是一个完整的小项目，可以直接 clone 后当模板用。
- **核心只有一条命令：`scripts/verify.sh`。** 智能体、人、pre-commit、Claude Code 的 Stop hook 和 GitHub Actions 跑的都是它：格式、lint、类型检查（C++ 为 `-Werror` 编译加 clang-tidy）、测试。本地绿就等于 CI 绿。
- **每个分支都在本机实测过。** 2026-11-20 在 Debian 13 上，三个分支的 verify.sh 都从 git bundle clone 出的干净副本跑通；我们还故意改坏代码，确认 lint、类型检查、测试、格式检查、pre-commit 和 hook 脚本都会拦住（§4 摘录了真实输出）。
- **智能体本身的行为没法用脚本复现。** 「把任务交给智能体」这一步标为「需在你的编辑器/CLI 中执行」；我们验证的是它周围的检查。GitHub 托管 runner 上的 CI 结果，以各分支 Actions 页面为准。
- **规则文件只是「建议」，检查才是「必须」**（[第 04 章](./04-architecture-constraints)）。所以 AGENTS.md 写得很短，真正的约束放在 verify.sh、hook、pre-commit 和 CI 里。

> 想先知道该读什么、先做什么，见 [一页纸推荐](./00-one-page)；skill 在全书里的定位见 [第 13 章 §0](./13-skills-catalog#book-view)。这一章把其中「立即可做」的几件事做成了文件。

## 1. 三个分支 {#branches}

| 分支 | 示例项目 | 检查链（全部在 `scripts/verify.sh`） | 链接 |
| --- | --- | --- | --- |
| `starter/python` | uv + pytest 的小库 | ruff format → ruff check → mypy --strict → pytest | [tree/starter/python](https://github.com/Atituiset/agent-engineering-handbook/tree/starter/python) |
| `starter/typescript` | Node ESM + vitest 的小库 | prettier → eslint（typescript-eslint strictTypeChecked）→ tsc --noEmit → vitest → tsc build | [tree/starter/typescript](https://github.com/Atituiset/agent-engineering-handbook/tree/starter/typescript) |
| `starter/cpp` | CMake + ctest + doctest 的小库 | clang-format → `-Werror` 编译 → clang-tidy（警告即错误）→ ctest | [tree/starter/cpp](https://github.com/Atituiset/agent-engineering-handbook/tree/starter/cpp) |

三个示例项目做的是同一件事：把 `1h30m` 这样的时长解析成秒数，错误输入抛出专门的异常。功能故意选得很小，好让注意力集中在周围的检查上。

复制模板（以 Python 为例，另两个分支把分支名换掉即可）：

```bash
git clone --branch starter/python --single-branch \
  https://github.com/Atituiset/agent-engineering-handbook.git my-project
cd my-project
rm -rf .git && git init -b main && git add -A && git commit -m "init from starter kit"
bash scripts/verify.sh        # 最后一行应为 verify: OK
```

这三个分支和 `main` 没有共同历史（orphan 分支），只包含示例项目本身；文档站的构建与部署只用 `main`，互不影响。

## 2. 书里的方法对应到哪个文件 {#mapping}

| 书里的要求 | 对应文件 | 出处 |
| --- | --- | --- |
| 测试、lint、类型检查、构建一条命令跑通 | `scripts/verify.sh` | [11 §1](./11-checklists#_1-新仓库接入智能体-第一周清单)、[04 §9](./04-architecture-constraints#_9-让代码库对智能体可读、可跑) |
| 约 100 行以内的 AGENTS.md：命令、边界、非标准约定、坑点 | `AGENTS.md`（三个分支都不到 40 行） | [02 §3](./02-context-engineering#_3-写法-一份好的-agents-md-包含什么)、[11 §2](./11-checklists#_2-agents-md-模板) |
| 多个工具共用一份规则 | `CLAUDE.md` 只有一行 `@AGENTS.md`；`.cursor/rules/project.mdc` 也指向 AGENTS.md | [13 §3](./13-skills-catalog#compat) |
| 格式化与 lint 用 hook 自动执行 | `.claude/settings.json` 的 PostToolUse；`.pre-commit-config.yaml` | [07 §3](./07-harness-tools#_3-hooks-把「必须」变成确定性) |
| 受保护文件禁止智能体修改 | `scripts/guard-protected.sh`（PreToolUse，命中即 exit 2） | [04 §5](./04-architecture-constraints#_5-保护检查本身)、[11 §1](./11-checklists#_1-新仓库接入智能体-第一周清单) |
| 宣布完成前强制跑测试 | `scripts/stop-verify.sh`（Stop hook，verify 不过就 exit 2） | [07 §3](./07-harness-tools#_3-hooks-把「必须」变成确定性)、[05 §6](./05-verification#_6-防作弊与升级) |
| CI 是独立的最终裁判 | `.github/workflows/ci.yml` 只执行 `bash scripts/verify.sh` | [12 Q03](./12-quality-cicd#q03)、[12 示例 A](./12-quality-cicd#example-a) |
| 先自己写一个 verify skill | `.agents/skills/verify/SKILL.md`（`.claude/skills/` 下为同内容副本，verify.sh 检查两者一致） | [13 §0.2](./13-skills-catalog#starter-set)、[05 §8](./05-verification#_8-评测-为团队的-harness-建回归) |
| 工具版本锁定，本地与 CI 一致 | `uv.lock`、`package-lock.json`；C++ 在 CI 里用 pipx 固定 clang-format 19.1.7 与 clang-tidy 19.1.0.1 | [12 Q10](./12-quality-cicd#q10) |

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

## 4. 实测结果：通过与被拦住 {#results}

运行环境：2026-11-20，Debian 13；uv 0.13.8，Node.js 24.22.1，CMake 3.31.6，GCC 14.2.0，clang-format / clang-tidy 19.1.7，pre-commit 4.7.0。每个分支都从 git bundle clone 到干净目录再运行。

### 4.1 基线全部通过 {#results-pass}

| 分支 | verify.sh 结果 | pre-commit run --all-files |
| --- | --- | --- |
| python | ruff format 8 files already formatted；ruff check All checks passed；mypy Success；pytest 14 passed；`verify: OK` | 4 项 Passed |
| typescript | prettier 通过；eslint、tsc 无输出；vitest 14 passed；tsc build 通过；`verify: OK` | 4 项 Passed |
| cpp | clang-format 无违规；`-Werror` 编译通过；clang-tidy 无 error；ctest 100% tests passed；`verify: OK`（系统包 LLVM 19.1.7 与 PyPI 包 clang-tidy 19.1.0.1 各跑一次，都通过） | 2 项 Passed |

完成演练任务（支持 `d` 单位）之后：Python 18 passed，TypeScript 18 passed，C++ ctest 100% 通过，三者都是 `verify: OK`。

### 4.2 故意改坏，确认会被拦住 {#results-fail}

我们手工模拟了一个「不守规矩」的改动：把 `d` 加到单位表**末尾**（顺序错了，`1d2h` 会被判为乱序），再顺手加一个偷懒的辅助函数。下面是 verify.sh 的真实输出摘录，每次修掉一个问题再跑：

| 分支 | 第一道拦截 | 第二道拦截 | 最后由测试拦住的逻辑错误 |
| --- | --- | --- | --- |
| python | ruff：`F401 'os' imported but unused` | mypy：`error: Function is missing a type annotation [no-untyped-def]` | pytest：`DurationError: unit 'h' repeated or out of order in '1d2h'`，`1 failed, 15 passed` |
| typescript | eslint：`Missing return type on function`、`Unsafe argument of type 'any'`，`2 problems (2 errors)` | tsc：`error TS7006: Parameter 'text' implicitly has an 'any' type.` | vitest：`DurationError: unit "h" repeated or out of order in "1d2h"`，`1 failed / 15 passed` |
| cpp | GCC：`conversion from 'int64_t' to 'int' may change value [-Werror=conversion]` | 用 C 风格转换压掉警告后，clang-tidy：`C-style casts are discouraged; use static_cast [google-readability-casting,-warnings-as-errors]` | doctest：`CHECK( parse_duration("1d2h") == 93600 ) THREW exception`，ctest `1 tests failed` |

同一状态下的其他关口：

- **Stop hook**：三个分支的 `scripts/stop-verify.sh` 都返回 `exit=2`，并输出 `scripts/verify.sh failed: fix the problems above before finishing.`
- **pre-commit**：`git commit` 被拒，Python 和 TypeScript 是测试那一项 `Failed`，C++ 是 `build + clang-tidy + ctest (scripts/verify.sh) ... Failed`。
- **受保护文件**：`guard-protected.sh` 对 `scripts/verify.sh`、`eslint.config.js`、`.clang-tidy` 都输出 `blocked: ... is protected` 并返回 `exit=2`。
- **格式**：正确改动第一次运行时，三个分支都因为一行过长的测试代码被格式检查拦下（ruff format / prettier / clang-format），格式化后通过。

C++ 那一行值得多看一眼：编译器警告被一个 `(int)` 强制转换「修好」了，这和 [第 10 章反模式 8](./10-anti-patterns#_8-让变更能修改评判它的检查) 记录的「为编译通过跳过检查」（[CN06](/sources/chinese#cn06)）是同一类行为。只有编译器一层的话，它就混过去了，第二层静态分析才把它拦下。这也是 [第 04 章](./04-architecture-constraints) 主张多层检查的原因。

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
3. 把工具配置合并到你的项目。老项目一次开不了最严档位（`mypy --strict`、`strictTypeChecked`、全量 clang-tidy）时，先对新模块或改动文件开，再逐步扩大。
4. 改 `scripts/guard-protected.sh` 里的 `PROTECTED_REGEX`，把你的 CI、迁移脚本、架构测试加进去。
5. 把最重要的 3–5 条架构规则写成测试或 lint 规则，加进 `scripts/verify.sh`（[04 §4](./04-architecture-constraints#_4-工具箱-把架构规则变成检查)）。
6. 在 GitHub 把 `ci / verify` 设为必需检查。没有这一步，前面几层都能被绕过。

## 7. 已知限制与未验证项 {#limits}

| 项目 | 状态 |
| --- | --- |
| verify.sh、pre-commit、hook 脚本（三种语言） | **已在本机实测**，通过和被拦住的情况都有 |
| CI 工作流 | 本机用全新 clone 跑了等价命令（verify.sh）并通过；**GitHub 托管 runner 上的运行未在本章写作时验证**，以各分支 Actions 页面为准 |
| `.claude/settings.json` 中的 hook 在 Claude Code 里实际触发 | **未验证**：脚本本身已手动测试，配置按 Claude Code 文档的格式编写；请在 Claude Code 里用 `/hooks` 确认 |
| `CLAUDE.md` 的 `@AGENTS.md` 导入、Cursor `.mdc` 的 `@AGENTS.md` 引用 | **未在编辑器里验证**；若你的工具版本不支持，把 AGENTS.md 内容直接复制过去 |
| 智能体完成任务（演练第 5 步） | **需在你的编辑器/CLI 中执行**；README 里的「正确改动」是按任务说明手工完成的参考答案 |
| 其他工具（Codex、Cursor、Gemini CLI 等）的 hook | 未提供；这些工具里只有 pre-commit 与 CI 两层生效 |
| pre-commit 在 TypeScript、C++ 项目里需要 Python | 已注明；只用 Node 生态的团队可以换成 husky，检查命令不变 |

## 与传统软件工程认知的对比 {#compare}

| 传统认知 | 在这套模板里 | 为什么这样选 |
| --- | --- | --- |
| 项目模板（cookiecutter、create-xxx）主要提供目录结构和依赖 | 模板的重点是检查链：一条 verify 命令，加上 hook、pre-commit、CI 三处复用 | 智能体会照着仓库里已有的东西写；没有检查，结构很快会走样（[第 04 章](./04-architecture-constraints)） |
| 编码规范写在 CONTRIBUTING 里，靠评审把关 | 规范写进 lint、类型检查和受保护文件列表，AGENTS.md 只剩命令和少量约定 | 规则文件遵不遵守由模型决定（[AN01](/sources/anthropic#an01)）；能机械判定的就交给工具 |
| CI 是团队设施，本地检查可以宽松一些 | 本地、hook、CI 跑同一个脚本，工具版本锁定 | 智能体要靠能在本地运行的验证闭环自证（[12 Q02](./12-quality-cicd#q02)）；本地与 CI 跑同一条命令，「本地绿」才有意义 |
| 警告可以先放着 | `-Werror`、clang-tidy 警告即错误、eslint `--max-warnings=0` | 智能体会用压掉警告的方式「修好」问题（§4.2 的 C 风格转换），只有零容忍才能逼它改代码 |

## 本章小结 {#summary}

- 三个 orphan 分支 `starter/python`、`starter/typescript`、`starter/cpp`，各自是一个能直接 clone 的完整项目。
- 唯一的完成标准是 `bash scripts/verify.sh` 输出 `verify: OK`。智能体、人、pre-commit、Stop hook 和 CI 都跑这一条命令。
- 实测：三个分支基线全部通过；一个故意写错的改动，被 lint、类型检查（或 `-Werror`）、clang-tidy、测试、格式检查、pre-commit 和 Stop hook 逐层拦下。
- 没验证的部分已经如实标出：GitHub runner 上的 CI 运行、Claude Code 里实际触发 hook、各编辑器对 `@AGENTS.md` 的支持，以及智能体本身的行为。
- 下一步：按 §6 套用到你自己的项目，把 `ci / verify` 设为必需检查，再按 [一页纸推荐](./00-one-page#do-now) 逐项补齐其余几件事。
