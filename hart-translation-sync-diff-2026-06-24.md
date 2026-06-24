---
layout: page
title: Hart Translation Sync Diff 2026-06-24
---

# Hart Translation Sync Diff 2026-06-24

이 문서는 `source-library`의 Hart *The Concept of Law* 번역 최종
정책어 검산 변경분을 `HartConcept` 공개 번역 surface에 반영한 기록이다.

## 기준

- 원천 리포: `source-library`
- 원천 커밋: `4e72c40 Audit Hart translation terminology`
- 원천 경로:
  `sources/inbox/hart-concept-law-2026-06-02/source-surfaces/`
- 반영 리포: `HartConcept`
- 반영 경로:
  - `TRANSLATIONS/CHAPTERS/`
  - `Summary/`
  - `Terms/`

## 반영 범위

이번 동기화는 공개 독자 surface에 직접 연결되는 파일들로 제한했다.

- 번역 본문 및 전후문:
  `TRANSLATIONS/CHAPTERS/`
- 강독용 요약:
  `Summary/summary_02.md`, `Summary/summary_05.md`
- 용어 노트:
  `Terms/00-philosphical_terms.md`부터 `Terms/04-rule-skeptic.md`

`source-library` 내부의 번역 정책 문서, ledger, memory seed, 문단별 감사
리포트는 working master의 연속성 surface로 보고 이 공개 repo에는 별도로
복제하지 않았다.

## 주요 반영 원칙

- `offence` / `offender`는 자동으로 `범죄` / `행위자`로 옮기지 않고
  문맥상 `위반행위` / `위반자`로 정리했다.
- `admissions`는 `recognition`과 섞이지 않도록 `시인`으로 분리했다.
- `virtue`는 `미덕`, `merit` / `merits`는 `이점` / `이점들`로 구분했다.
- `regular` / `regularity` 계열은 `정기적`이나 `규칙성`이 아니라
  `반복적으로 일양적인` / `반복적 일양성` 계열을 유지했다.
- `source`는 `원천`, `foundation`은 `토대`로 분리했다.
- `power` / `competence`는 법적 권한/권능 문맥과 비법적 능력 문맥을
  구분했다.
- `customarily`, `defining feature`, `claim`, `suggest`, `conclusive`,
  `affirmative`, `indication` 등 정책어의 최종 회귀 검산 결과를 반영했다.

## 검산

동기화 후 다음을 확인했다.

- `source-library`의 대응 `translation`, `summary`, `terms` surface와
  `HartConcept` 공개 surface가 checksum 기준으로 일치한다.
- `git diff --check`가 통과했다.
- 다음 위험어 회귀 검색에서 잔여 적중이 없었다:
  `범죄(offence)`, `범죄행위(offence)`, `행위자(offender)`,
  `인정(admissions)`, `장점`, `정기적`, `규칙성`, `공무원`, `공직자`,
  `법원(法源)`, `정의적 특징`, `법철학(jurisprudence)`.
