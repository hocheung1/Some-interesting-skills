# Some-interesting-skills

## Modern U.S. Military Story Collector

An evidence-first, runnable Python project for collecting modern U.S. military human-interest story leads and reusable photo leads. The collector treats publication safety as a product requirement: it records provenance, blocks unsupported claims, and keeps photo identity verification distinct from copyright/licence verification.

### Research safeguards

- **Modern by default:** only 1990–present material is in scope. World War II and Vietnam require an explicit opt-in.
- **Core facts:** need both an official/primary record and a truly independent second publisher. Reprints, syndication, mirrors, and recycled press releases do not count.
- **Photos:** must retain the original asset page, caption, photographer, date, rights status, and separate identity evidence for the depicted person.
- **No padding:** the target is 5–10 verified photos, but fewer are reported when evidence is insufficient.
- **Honest uncertainty:** conflicts remain attributed instead of being guessed away; S/A/B/C/D grades control whether an item may enter the final narrative.

## 使用教程：怎样正确提问

安装后，在 Codex 中直接说明你要研究的对象、时间范围和交付内容即可。默认研究范围是 **1990 年至今**；如要研究更早时期，必须明确写出授权范围。

### 通用提问模板

```text
请使用 modern-us-military-story-collector 研究【人物姓名／单位／事件关键词】。

时间范围：【例如 2003–2012；默认 1990 年至今】
目标：核验其真实经历，并写成一份中文人物故事报告。
照片：寻找最多 10 张、目标 5–10 张可用照片；每张必须单独核验人物身份和版权。
侧重点：【例如救援经历、获奖记录、服役单位、某次行动】
输出：提供证据台账、验证结果和最终 Markdown 报告；保留冲突与未通过核验的材料。
```

### 可直接复制的提问示例

**完整人物故事**

```text
请使用 modern-us-military-story-collector 研究【人物姓名】在【年份】至【年份】期间的真实美军服役经历，重点核验【事件或奖项】。请用中文交付人物故事、证据台账和验证结果；照片目标 5–10 张，但绝不以未核验照片凑数。每条核心事实需要官方/一手来源与独立第二来源，所有冲突均保留。
```

**从事件寻找人物**

```text
请使用 modern-us-military-story-collector 寻找与【事件关键词，例如“2017 年飓风救援中的美国海岸警卫队医护人员”】有关的真实人物故事。范围限 1990 年至今。先给我可核验的人物候选和来源，不要把线索当事实；确认后再生成报告和照片清单。
```

**只做照片核验**

```text
请使用 modern-us-military-story-collector 核验【人物姓名】的照片素材。请只保留能提供原始网页、完整 caption、摄影师、日期、人物身份依据和独立版权/许可依据的照片；输出最多 10 张，并列出所有被排除图片及原因。
```

**允许研究更早战争（必须明确）**

```text
请使用 modern-us-military-story-collector 研究【人物姓名】的越战经历。我明确授权将默认年代范围扩展到 1965–1975；其余事实、独立来源、照片身份和版权核验规则保持不变。
```

### 避免这样提问

- “找一个感人的美军故事，多配一些图。”——缺少人物、事件或时间锚点，且“多配图”容易形成凑数压力。
- “证明【结论】是真的。”——应改为请求核验该结论并保留相反证据。
- “所有政府网站照片都能用。”——版权必须逐张核验，不能按网站域名推断。

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
