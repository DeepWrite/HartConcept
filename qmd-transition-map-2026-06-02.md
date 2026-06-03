# HartConcept QMD Transition Map

Date: 2026-06-02

## Decision

Use `source-library` as the master/work/provenance layer for the 2026 summer
Hart translation work. Use `HartConcept` as the public release surface: the
course site may temporarily expose the original and translation during the
course window, but it should show only finished class-facing snapshots.

Do not create a separate term repo yet. Do not move the existing public
Markdown, Jekyll, or TeX/B5 files before the 2026-06-17 print-ready deadline.
Instead, route new work through the source-library packet and teaching export.

## Why This Is the Right Shape

- The current `HartConcept` repository is public and already carries the
  class-facing Hart site, original-text pages, and translation pages. That is
  useful during the course, but it is not the right place for correction
  registers, production dashboards, private source handling, or B5 working
  files.
- The existing Markdown-to-TeX/B5 translation pipeline is fragile but usable.
  With a 2026-06-17 print deadline, preserving it and making the source rule
  explicit is safer than converting the whole book pipeline at once.
- The Jekyll course-site surface is old and still carries template residue, but
  it is the existing public route for temporary original/translation access.
  Keep it stable as a release surface.
- The workspace is moving toward QMD/Quarto for current writing, production
  dashboards, and publishable document surfaces. That does not make TeX the
  authoring source for translation prose.

## Active Lanes

| Lane | Path | Status | Rule |
| --- | --- | --- | --- |
| Korean translation master/work source | `source-library/sources/inbox/hart-concept-law-2026-06-02/source-surfaces/translation/CHAPTERS/` | active authoring source | Edit translation prose here first. Accepted changes flow outward to B5 and public release snapshots. |
| Original-text working surface | `source-library/sources/inbox/hart-concept-law-2026-06-02/source-surfaces/original/` | source/provenance candidate | Use for alignment and source identity clarification before public release updates. |
| 2026 summer QMD workflow surface | `source-library/exports/teaching/hart-concept-2026-summer/workflow/qmd-2026-summer/` | private dashboard | Use for schedule, correction register, translation production dashboard, and assistant-facing status. |
| B5 generated print layer | `source-library/exports/teaching/hart-concept-2026-summer/b5/trans-chapters/sections/`, `source-library/exports/teaching/hart-concept-2026-summer/b5/trans-chapters/main-b5-small.tex` | derived/build | Regenerate section TeX from source-library Markdown. Direct TeX edits only for layout/build fixes, and mirror text fixes back to Markdown. |
| Public release surface | `HartConcept/OriginalText/`, `HartConcept/TRANSLATIONS/`, numbered site pages | released snapshot | Keep class-facing original/translation access here during the course window. Do not use this as the work master. |
| Prior summer version | `source-library/exports/teaching/hart-concept-2026-summer/b5/trans-chapters/sections/2025-summer-version/` | archive comparison | Use for comparison and provenance. Do not treat as current source. |
| Winter 2026 PDFs and current generated sections | `TEX/trans-chapters/` | baseline evidence | Use the final winter print version as the baseline for the third version. |
| Jekyll course site | root numbered `.md` files and `_config.yml` | public release route | Keep stable and update only with finished course-facing snapshots. |

## Archive Rule

Before 2026-06-17, "archive" means marking, routing, and preserving. It does
not mean moving files that the public Jekyll site or existing TeX build may
still reference.

After the print-ready PDF is delivered, a bounded archive pass can move or copy
old artifacts into an explicit archive tree and leave forwarding notes from old
paths.

## Template Repo Judgment

Do not create a new template repo for Hart on 2026-06-02.

Recommended sequence:

1. Build this term's QMD surface inside the source-library teaching export.
2. Use it through the 2026-06-17 translation deadline and the 2026 summer term.
3. After the term, extract a reusable template only if at least two future uses
   are visible:
   - another classics-reading course site,
   - another translation-backed seminar,
   - or a reusable `reading-seminar-course-kit` distinct from `deepwrite-course-kit`.

`deepwrite-course-kit` is relevant as a model for separating reusable shells
from term-specific work, but it is currently writing-course oriented and still
Jekyll-shaped. Hart should not be folded into it unless the reusable layer is
made more general.

## Third Translation Production Rule

The 2026 third translation version should be treated as a controlled revision of
the winter 2026 print baseline.

Minimum workflow:

1. Lock baseline file paths and identify the current printed winter PDF.
2. Intake the user's major correction list as a dated correction register.
3. Apply accepted changes to the source-library Markdown translation source
   files.
4. Regenerate the TeX section files from the source-library Markdown source.
5. Run a terminology and problem-translation audit across all chapters.
6. Render B5 candidate PDF.
7. Check quotation marks, footnote numbering, page breaks, chapter order, and
   Korean readability.
8. Deliver print-ready PDF by 2026-06-17.
9. Copy only finished class-facing snapshots into `HartConcept` for public
   course access.

## Secretary Handling

The assistant should treat 2026-06-17 as the real deadline. The calendar shows
2026-06-18 to 2026-06-21 as blocked or low-production days, and the course opens
on 2026-06-24.
