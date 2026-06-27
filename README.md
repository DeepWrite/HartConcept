# HartConcept

`HartConcept` is the public release surface for the SNU classics-reading course
on H. L. A. Hart's *The Concept of Law* and for the class-facing Korean teaching
translation used during the course window.

## Current Public Surface

- Temporary original / translation publication pages:
  `08-book-original.md`, `09-book-translation.md`, `OriginalText/`,
  `TRANSLATIONS/`
- Living errata page for the locked 2026 summer printed translation:
  `TRANSLATIONS/translation-errata-2026-summer.md`
- Course-facing Jekyll / Just the Docs pages:
  `_config.yml`, `index.md`, `03-syllabus.md`, `04-lectures.md`,
  `05-assignments.md`, `15-ai-policy.md`, and related numbered markdown pages.
- Final public release snapshots:
  copied deliberately from `source-library` only after a release decision.

## Internal Work Surfaces

Correction logs, sync diffs, QMD transition maps, production notes, and other
private workflow records do not belong in this public course-site repo. Keep
them in the private work/master layer and copy only finished class-facing
snapshots into `HartConcept`.

## Repeat Offering Publication Tiers

This site is designed to survive repeated offerings of the Hart course, not only
the 2026 summer section. Class materials should therefore be separated by public
function before publication.

| Tier | Examples | Rule |
| --- | --- | --- |
| Always-public reading tools | argument-analysis toolkit, common terms, presentation template, chapter pre-guides that do not give answers | May stay public across offerings. Keep them as reading lenses, not answer keys. |
| Current-course public records | section syllabus, AI policy, group assignments, print errata for a named course edition | Publish only when useful for the current course window. Archive or hide from navigation before the next offering if the record is section-specific. |
| Post-class public review | model presentations, completed argument guides, anonymized representative questions and reading corrections | Release only after the relevant class or presentation has occurred. Do not expose them as pre-class aids for future students unless deliberately reclassified. |
| Enrolled-only or internal materials | name-bearing student questions, classroom response notes, lecture transcript intake, grading-sensitive diagnosis | Do not publish on GitHub Pages as-is. Use source-library for internal records and eTL or another access-controlled surface for enrolled-student-only release. |

Student question responses may become public only after names and evaluation
traces are removed and the material is rewritten as thematic representative
questions. Raw or name-bearing versions belong in `source-library`.

## Legacy Surfaces

- Generated B5 / TeX translation layer:
  `TEX/trans-chapters/`
- Earlier summer translation slice:
  `TEX/trans-chapters/sections/2025-summer-version/`

`HartConcept/TRANSLATIONS/` and `HartConcept/OriginalText/` remain public-course
release snapshots, not the working master. They may be temporarily published
during the course, but should be updated only from an approved release bundle.

Treat TeX/B5 files in this repo as legacy or released build artifacts. Current
B5 production work belongs outside this public site repo until a release
decision is made.

The locked `2026년 6월 여름계절학기 인쇄본` is recorded in source-library's
print-lock baseline, not published from this site repo. Do not restore the B5
PDFs here; publish later corrections through source-library and the public
errata page.

## 2026 Summer Deadlines

- Translation third version print-ready target: 2026-06-17.
- Blocked / low-production period: 2026-06-18 to 2026-06-21.
- Course start: 2026-06-24.
- Course end: 2026-07-27.
