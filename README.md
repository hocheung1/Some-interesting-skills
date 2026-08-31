# Some-interesting-skills

## Modern U.S. Military Story Collector

An evidence-first, runnable Python project for collecting modern U.S. military human-interest story leads and reusable photo leads. The collector treats publication safety as a product requirement: it records provenance, blocks unsupported claims, and keeps photo identity verification distinct from copyright/licence verification.

### Research safeguards

- **Modern by default:** only 1990–present material is in scope. World War II and Vietnam require an explicit opt-in.
- **Core facts:** need both an official/primary record and a truly independent second publisher. Reprints, syndication, mirrors, and recycled press releases do not count.
- **Photos:** must retain the original asset page, caption, photographer, date, rights status, and separate identity evidence for the depicted person.
- **No padding:** the target is 5–10 verified photos, but fewer are reported when evidence is insufficient.
- **Honest uncertainty:** conflicts remain attributed instead of being guessed away; S/A/B/C/D grades control whether an item may enter the final narrative.

## Quick start

```bash
python -m pip install -e .[dev]
us-story-collector validate examples/story-candidate.json
us-story-collector report examples/story-candidate.json --output report.md
python -m unittest discover -s tests -v
```

The example deliberately includes excluded records, demonstrating that unsupported material does not enter the final fact body.

## 在 Codex 中快速安装

### 推荐：直接在 Codex 对话框安装

在 Codex 新任务中发送以下一句话即可，无需手动复制文件或打开终端：

```text
请使用 skill-installer 从 GitHub 仓库 hocheung1/Some-interesting-skills 的根目录安装 skill，命名为 modern-us-military-story-collector。
```

安装完成后，新开一个 Codex 任务即可使用 `modern-us-military-story-collector`。

### 备用：PowerShell 安装

如果需要在本机直接安装，可在 Windows PowerShell 中运行：

```powershell
$skill = Join-Path $env:USERPROFILE '.codex\skills\modern-us-military-story-collector'; git clone --depth 1 https://github.com/hocheung1/Some-interesting-skills.git $skill
```

已安装时，进入该目录更新即可：

```powershell
git -C (Join-Path $env:USERPROFILE '.codex\skills\modern-us-military-story-collector') pull --ff-only
```

## Repository layout

- `SKILL.md` — evidence-collection operating procedure.
- `src/` — source discovery, validation, photo checks, reports, and CLI.
- `schemas/` — JSON Schema for research ledgers.
- `config/` — DVIDS and official-site discovery configuration.
- `examples/` — reviewable sample input.
- `docs/` — research protocol and grading rubric.
- `tests/` — offline regression tests.

See [docs/research-protocol.md](docs/research-protocol.md) for the full editorial and provenance rules.
