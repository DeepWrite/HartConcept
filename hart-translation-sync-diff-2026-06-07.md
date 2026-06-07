---
layout: page
title: Hart Translation Sync Diff 2026-06-07
---

# Hart Translation Sync Diff 2026-06-07

이 문서는 `source-library`의 Hart *The Concept of Law* 번역 proofreading 변경분을 `HartConcept` 번역 챕터 md 파일에 반영하면서, 기존 `HartConcept` 파일 대비 무엇이 바뀌었는지 대조하기 위해 작성한 목록이다.

## 기준

- 원천 리포: `source-library`
- 원천 커밋: `3e0d51a Refine Hart translation proofreading`
- 원천 경로: `sources/inbox/hart-concept-law-2026-06-02/source-surfaces/translation/CHAPTERS/`
- 반영 리포: `HartConcept`
- 반영 경로: `TRANSLATIONS/CHAPTERS/`
- 대조 기준: `HartConcept`의 기존 tracked 파일과 위 원천 커밋에서 가져온 반영본

## 변경 파일 요약

| 순번 | 파일 | 변경 규모 | 성격 |
| --- | --- | ---: | --- |
| 1 | `FRONTMATTER/04_2012_INTRODUCTION.md` | +33 / -33 | Green의 2012 Introduction 본문 용어 정리 및 영어 주석 번역 |
| 2 | `FRONTMATTER/forTex.md` | +33 / -33 | 위 Introduction의 TeX 결합용 파일 동일 정리 |
| 3 | `chapter_1-translation.md` | +12 / -12 | `idea`, `conception`, `notion`, `virtue`, `duty` 계열 정리 |
| 4 | `chapter_2-translation.md` | +8 / -8 | 장 제목, Austin 분석, `subordinate`, `power` 계열 정리 |
| 5 | `chapter_3-translation.md` | +14 / -14 | `comply`, `conform`, `subordinate`, 게임 규칙 비유 용어 정리 |
| 6 | `chapter_4-translation.md` | +20 / -20 | `compliance`, `power`, 주권자 구상, 주석 번역 및 오탈자 정리 |
| 7 | `chapter_5-translation.md` | +31 / -31 | `duty`와 `obligation`, `conception`/`notion`, `refer` 계열 정리 |
| 8 | `chapter_6-translation.md` | +14 / -14 | 장 제목, `superior`/`subordinate`, `assumed`/`postulated`, `source` 정리 |
| 9 | `chapter_7-translation.md` | +22 / -22 | 개방적 구조, 위임 권한, 의회 계속성/승계, `source` 정리 |
| 10 | `chapter_8-translation.md` | +8 / -8 | 정의와 도덕 장의 `conformity`, `duty`/`obligation`, 복종 표현 정리 |
| 11 | `chapter_9-translation.md` | +8 / -9 | 법과 도덕 장의 `conformity`, `merit or demerit`, 주석 번역 및 오탈자 정리 |
| 12 | `chapter_10-translation.md` | +5 / -5 | 국제법 장의 `reference`, `assumption`, `conform` 계열 정리 |
| 13 | `chapter_11-POSTSCRIPT-translation.md` | +19 / -19 | 후기의 `duty`, `conformity`, `source`, `premisses` 계열 정리 |

## 공통 변경 원칙

이번 변경은 문체적 윤문보다 Hart 법철학 용어의 계열 정합성을 맞추는 데 가깝다.

- `conform`, `conformity`는 문맥상 단순 복종이나 순응보다 기준과의 관계를 드러내야 하므로 대체로 `부합`, `부합하다`로 정리했다.
- `comply`, `compliance`는 요건 충족, 이행, 준수 등 문맥별 기능에 맞춰 분리했다.
- `duty`는 `책무`, `obligation`은 `의무` 중심으로 분리했다.
- `source`, `source of law`는 `근원`이나 `법원`보다 `원천`, `법의 원천` 계열로 맞췄다.
- `subordinate`는 `하위`보다 권위 관계를 드러내는 `종속된`으로 정리했다.
- `idea`, `conception`, `notion`, `concept`는 모두 `개념`으로 평탄화하지 않고, `관념`, `구상`, `개념적 파악`, `개념`을 문맥별로 나눴다.
- 남아 있던 영어 주석 문장은 한국어 서지 문장으로 옮겼다.

## 파일별 대조 목록

### 1. `FRONTMATTER/04_2012_INTRODUCTION.md`

- `대상자(subjects)` -> `수범자(subjects)`
- `따라야 한다(ought to conform)` -> `부합해야 한다(ought to conform)`
- `부응하거나`, `일치(conformity)` -> `부합하거나`, `부합(conformity)`
- `법원(supreme source of law)` -> `법의 원천(supreme source of law)`
- `권한(power)`, `사회 권한` -> `권력(power)`, `사회적 권력(social power)`
- `의무 부과` -> `책무부과`
- `근원(source)` -> `원천(source)`
- 영어 주석 문장 다수를 한국어 서지 문장으로 번역했다. 예: `See eg. ...` -> `예컨대 ... 참조.`
- `Hart calls his position 'soft' positivism...` 주석을 한국어로 번역하고 `inclusive positivism`의 이유를 명시했다.
- `Normative`가 도덕적 평가가 아니라 규범 관련성을 뜻한다는 설명 주석을 한국어화했다.

### 2. `FRONTMATTER/forTex.md`

이 파일은 `04_2012_INTRODUCTION.md`의 TeX 결합용 표면이므로 같은 변경이 반영되었다.

- `대상자(subjects)` -> `수범자(subjects)`
- `conform`, `conformity` 계열 -> `부합` 계열
- `source`, `source of law` 계열 -> `원천`, `법의 원천`
- `power`, `social power` 계열 -> `권력`, `사회적 권력`
- 영어 주석 문장 -> 한국어 서지 문장

### 3. `chapter_1-translation.md`

- `인식` -> `관념(idea)`
- `대해 성찰하고 이를 명시화` -> `대한 우리의 구상(conception)을 성찰하고 명시화`
- `순응한다면` -> `이에 응한다면`
- `'그렇게하지않을수없게함(oblige)'` 표현을 띄어쓰기와 의미가 드러나도록 정리했다.
- `의무, 권리, 책임` -> `의무(obligations), 책무(duties), 권리(rights)`
- `개념` -> `관념(idea)`, `구상`, `개념적 파악(notion)` 등으로 문맥별 분리
- `덕목` -> `미덕(virtue)`
- `강제 규칙 개념` -> `강행 규칙(mandatory rule)의 관념(idea)`
- `지칭/참조하는(refer)` -> `지칭하는(refer)`
- `가정`, `전제` 계열 일부 -> `상정(supposition)`, `가정(tacit assumption)`, `설정해 둔(postulated)`
- 영어 주석 `He adds 'and morals'.` -> `그는 ‘and morals’를 덧붙인다.`

### 4. `chapter_2-translation.md`

- 장 제목 `다양성(Varieties...)` -> `여러 유형들(Varieties...)`
- `뒷받침되는` -> `유지되는`
- `법의 개념` -> `법이라는 관념(idea of law)`
- `생각(notion)` -> `개념적 파악(notion)`
- `오스틴의 분석은 여러 결점에도 불구하고 하나의 장점을 지닌다` -> `오스틴 분석의 미덕(virtue)은, 그 결점들이 무엇이든 간에...`
- `하위(subordinate)` -> `종속된(subordinate)`
- `최고와 하위` -> `최고 요소와 종속`
- `권한(power)` -> `능력(power)`으로 조정된 지점이 있다.
- `공직자` -> `공무담당자`
- 영어 주석 일부를 한국어로 번역했다. 예: `Addressed to the community at large` 관련 설명.

### 5. `chapter_3-translation.md`

- `comply` 계열 중 형식 요건 문맥: `준수` -> `충족`
- `조항을 준수하지 않은` -> `조항의 요건을 충족하지 못한`
- `규칙의 준수에 부응하거나 부응하지` -> `규칙에 부합하거나 부합하지`
- `하위 입법 기관` -> `종속된 입법기관`
- `순응` -> `규칙 부합 행위`
- `공무담당자들((심판...)` -> `공식 역할자들(심판...)`
- `공무원적` -> `공식`
- `규칙들이 준수되기를`, `명령들이 준수되기를` -> `규칙들에 복종하기를`, `명령들에 복종하기를`
- 장 제목 `다양성(The...)` -> `여러 유형들(The...)`
- 영어 주석 `See above, p. 2.` -> `위 2쪽 참조.`

### 6. `chapter_4-translation.md`

- 오탈자: `검토없이` -> `검토 없이`, `상상속의` -> `상상 속의`, `한계을` -> `한계를`
- `준수(compliance)` -> 문맥상 `이행(compliance)` 또는 `준수`
- `순응` -> `부합`
- `규칙의 관념` -> `규칙이라는 개념적 파악`
- `권한(power)`/`권력(power)` 계열을 문맥별로 재배치했다. 법적 능력과 주권적 권위 문맥에서 `권한`과 `권력`을 구분했다.
- `주권자에 대한 개념` -> `주권자 구상`
- `생각` -> `개념적 파악`
- 영어 주석을 한국어로 번역했다. 예: `See p. 19 above.` -> `위 19쪽 참조.`

### 7. `chapter_5-translation.md`

- `개념화하는 방식` -> `보는 구상`
- `의무 부과` -> `책무를 부과하는`
- `공무원` -> `공무담당자`
- `순응` -> `부합`
- `의무(duties)` -> `책무(duties)`
- `의무나 권리` -> `책무(duties)나 의무(obligations)`
- `책무(duty)의 개념` -> `책무(duty)에 대한 개념적 파악`
- `의무의 개념` -> `의무라는 관념`
- `생각(the notion)` -> `개념적 파악(the notion)`
- `참조/언급할(refer)` -> `참조할(refer)` 또는 문맥상 `부를(refer)`
- `합치`, `순응` -> `부합`
- `의무(obligation)를 ... 오해하도록` -> `의무(obligation)에 관한 오도적 구상...`으로 문장 구조를 정리했다.
- `행위 주체가 수행해야`, `부과되어야 하는` -> `주체에게서 이행되어야`, `그 주체가 부담하는`

### 8. `chapter_6-translation.md`

- 장 제목 `기초`, `법체계를 기초하는 것들` -> `토대들`, `법체계의 토대들`
- `개념` 계열 -> `관념`, `구상`, `개념적 파악`으로 분리
- `상위(superior)` -> `우위의(superior)`
- `하위(subordinate)` -> `종속된(subordinate)`
- `일단가정된다(assumed)`, `공리로전제된다(postulated)` -> `가정된다(assumed)`, `공준으로 설정된다(postulated)`
- `규칙을 준수하는`, `규칙을 준수하지` -> `규칙에 부합하는`, `규칙에 부합하지`
- `순응하다(conform)` -> `부합하다(conform)`
- `올바른(correction...)` -> `올바른(correct...)`
- `법원(law source)` -> `법의 원천(sources of law)`
- `공무원들` -> `공무담당자들`
- `인식된` -> `수용된`

### 9. `chapter_7-translation.md`

- `관념`, `개념` 계열을 `구상`, `관념`, `개념적 파악`으로 분리
- `standard)을 준수해야` -> `standard)에 부합해야`
- `위임 입법적 결정(delegated power)` -> `위임된 규칙제정 권한(delegated power)의 행사`
- `결정이나 그 결정에 대한 예측의 개념` -> `결정과 결정 예측이라는 개념적 파악`
- `규칙의 개념` -> `규칙이라는 개념적 파악`
- `규칙 준수` -> `그 규칙에의 부합`
- `의무`, `임무` -> `책무(duty)`
- `비-공무담당자(non-official)` -> `비공식 참여자(non-official)`
- `하위` -> `종속된`
- 의회 연속성 문맥: `후속` -> `승계`, `지속적` -> `계속적`, `후속 의회들` -> `잇따른 의회들(successive parliaments)`
- `권능` -> `능력들`
- `근원` -> `원천들`
- `그러한 권한` -> `그렇게 판시할 권위(authority)`
- 오탈자: `득점를` -> `득점을`, `득점는` -> `득점은`

### 10. `chapter_8-translation.md`

- `법에 대한 순응(conformity)` -> `법에의 부합(conformity)`
- `의무의` -> 문맥별로 `책무(rights and duties of compensation)의`, `의무(obligations)의`
- `순응(conformity)` -> `부합(conformity)`
- `권총강도` -> `강도`
- `의무의 이행` -> `의무에 부합하는 행위`
- `법률의 준수처럼` -> `법에 대한 복종처럼`
- `규칙들의 준수` -> `규칙들에 부합하는 것`
- `준수가 요구된다` -> `부합을 요구하는 ... 뒷받침된다`로 문장 연결을 정리했다.

### 11. `chapter_9-translation.md`

- `준수/합치(a conformity)` -> `부합(a conformity)`
- `conviction)위에` -> `conviction) 위에`
- `언급` -> `참조`
- `순응(compliance)` -> `준수(compliance)`
- `순응*해야` -> `부합*해야`
- `정의나 도덕에 대한 신중한 부합을 결코 덜 요구하지 않는다` -> `정의나 도덕에 신중하게 부합할 수 있다`
- `준수(conformity)할` -> `그에 부합(conformity)할`
- 오탈자: `부정의(inquity)` -> `부정의(iniquity)`
- `장점(merit) 여부` -> `장점이나 단점(merit or demerit)`
- 영어 주석 `See the judgment of 27 July 1949...` -> 한국어 서지 문장으로 번역했다.

### 12. `chapter_10-translation.md`

- `관념(conception)` -> `구상(conception)`
- `규칙들을 근거로 하여` -> `규칙들에 참조하여`
- 오탈자: `필수적인(nnecessary)` -> `필수적인(necessary)`
- `그에 따라` 문장을 `그것에 참조하여 ... 그것에 힘입어 ...`로 정리해 `reference to`의 기능을 살렸다.
- `규칙들로 하여금 구성하게 한다` -> `규칙들이 구성한다`
- `전제(assumption)`, `전제` -> `가정(assumption)`, `가정`
- `순응해야` -> `준수해야`

### 13. `chapter_11-POSTSCRIPT-translation.md`

- `의무(duty/duties)` 계열 -> `책무(duty/duties)` 계열
- `의무를` -> 문맥상 `책무(legal duties)를`, `책무를`
- `개념화들(conceptions)` -> `구상들(conceptions)`
- `정합성(conformity)` -> `부합(conformity)`
- `전제들(premisses)` -> `전제명제들(premisses)`
- `준수(conformity)` -> `부합(conformity)`
- `의무 부여` -> `책무 설정`
- `출처(authoritative source)` -> `원천(authoritative source)`
- `근원을 구성하는 자료(source...)` -> `원천(sources...)`
- `상하관계(superiority...)` -> `우위와 종속의 관계(superiority...)`
- `근원(source of law)` -> `원천(source of law)`

## 검산 메모

- 반영 후 13개 대상 파일은 `source-library`의 대응 파일과 byte-for-byte로 일치함을 확인했다.
- `git diff --check`에서 공백 오류는 발견되지 않았다.
- 이 문서는 전체 원문 diff를 대체하지 않는다. 실제 문장 단위 검토가 필요하면 `git diff` 또는 각 파일의 commit diff를 함께 확인한다.
