## 2026 여름 작업 원칙

세 번째 번역본의 저자 수정 원문은
`source-library` packet 안의 Markdown이다.

`/Users/jeyounson/GithubRepo/source-library/sources/inbox/hart-concept-law-2026-06-02/source-surfaces/translation/CHAPTERS/`

`HartConcept/TRANSLATIONS/`는 수업 중 공개할 수 있는 release snapshot이지
B5 번역본의 working master text가 아니다.

아래 명령들은 기존 수작업 변환 기록으로 보존한다. 새 작업에서는 먼저
Markdown 원문을 고치고, 저장소 루트에서 다음 스크립트로 변환 대상을
확인한 뒤 TeX section을 재생성한다.

```bash
/Users/jeyounson/GithubRepo/source-library/exports/teaching/hart-concept-2026-summer/workflow/build_translation_tex_from_md.sh --dry-run
/Users/jeyounson/GithubRepo/source-library/exports/teaching/hart-concept-2026-summer/workflow/build_translation_tex_from_md.sh --write
```

TeX 파일은 인쇄 산출층이다. 번역 문장 수정은 TeX에 직접 넣지 말고
source-library Markdown 원문에 반영한 뒤 변환한다. 조판이나 빌드 문제로
TeX를 고쳤다면 같은 텍스트 변경을 source-library Markdown에도 되돌려
반영한다.

## 영문섹션

### 진입
cd /Users/jeyounson/HartConcept/TEX/chapters
폰트 파일과 템플릿 파일이 있는 폴더임.

### Md 파일을 tex 파일로 변환 (mybook-template.tex 템플릿 이용)

pandoc /Users/jeyounson/HartConcept/OriginalText/CHAPTERS/chapter_1.md -o /Users/jeyounson/HartConcept/TEX/chapters/chapter_1.tex --template=mybook-template.tex

## 한글 섹션

### 진입
cd /Users/jeyounson/HartConcept/TEX/trans-chapters

폰트 파일과 템플릿 파일이 있는 폴더임.

### Md 파일을 tex 파일로 변환 (hartbook-template.tex 템플릿 이용)

pandoc /Users/jeyounson/HartConcept/TRANSLATIONS/CHAPTERS/FRONTMATTER/01_1961_PREFACE-translation.md -o /Users/jeyounson/HartConcept/TEX/trans-chapters/sections/01_1961_PREFACE-translation.tex --template=hartbook-template.tex


pandoc /Users/jeyounson/HartConcept/TRANSLATIONS/CHAPTERS/FRONTMATTER/forTex.md -o /Users/jeyounson/HartConcept/TEX/trans-chapters/forTex.tex --template=hartbook-template.tex

pandoc /Users/jeyounson/HartConcept/TRANSLATIONS/CHAPTERS/chapter_1-translation.md -o /Users/jeyounson/HartConcept/TEX/trans-chapters/sections/chapter_1-translation.tex

pandoc /Users/jeyounson/HartConcept/TRANSLATIONS/CHAPTERS/chapter_2-translation.md -o /Users/jeyounson/HartConcept/TEX/trans-chapters/sections/chapter_2-translation.tex

pandoc /Users/jeyounson/HartConcept/TRANSLATIONS/CHAPTERS/chapter_3-translation.md -o /Users/jeyounson/HartConcept/TEX/trans-chapters/sections/chapter_3-translation.tex

pandoc /Users/jeyounson/HartConcept/TRANSLATIONS/CHAPTERS/chapter_4-translation.md -o /Users/jeyounson/HartConcept/TEX/trans-chapters/sections/chapter_4-translation.tex

pandoc /Users/jeyounson/HartConcept/TRANSLATIONS/CHAPTERS/chapter_5-translation.md -o /Users/jeyounson/HartConcept/TEX/trans-chapters/sections/chapter_5-translation.tex

pandoc /Users/jeyounson/HartConcept/TRANSLATIONS/CHAPTERS/chapter_6-translation.md -o /Users/jeyounson/HartConcept/TEX/trans-chapters/sections/chapter_6-translation.tex

pandoc /Users/jeyounson/HartConcept/TRANSLATIONS/CHAPTERS/chapter_7-translation.md -o /Users/jeyounson/HartConcept/TEX/trans-chapters/sections/chapter_7-translation.tex

pandoc /Users/jeyounson/HartConcept/TRANSLATIONS/CHAPTERS/chapter_8-translation.md -o /Users/jeyounson/HartConcept/TEX/trans-chapters/sections/chapter_8-translation.tex

pandoc /Users/jeyounson/HartConcept/TRANSLATIONS/CHAPTERS/chapter_9-translation.md -o /Users/jeyounson/HartConcept/TEX/trans-chapters/sections/chapter_9-translation.tex

pandoc /Users/jeyounson/HartConcept/TRANSLATIONS/CHAPTERS/chapter_10-translation.md -o /Users/jeyounson/HartConcept/TEX/trans-chapters/sections/chapter_10-translation.tex

pandoc /Users/jeyounson/HartConcept/TRANSLATIONS/CHAPTERS/chapter_11-POSTSCRIPT-translation.md -o /Users/jeyounson/HartConcept/TEX/trans-chapters/sections/chapter_11-POSTSCRIPT-translation.tex

pandoc /Users/jeyounson/HartConcept/TRANSLATIONS/CHAPTERS/FRONTMATTER/02_1994_Editors_Note.md -o /Users/jeyounson/HartConcept/TEX/trans-chapters/sections/02_1994_Editors_Note-translation.tex

pandoc /Users/jeyounson/HartConcept/TRANSLATIONS/CHAPTERS/FRONTMATTER/03_2012_Third_Preface.md -o /Users/jeyounson/HartConcept/TEX/trans-chapters/sections/03_2012_Third_Preface-translation.tex

pandoc /Users/jeyounson/HartConcept/TRANSLATIONS/CHAPTERS/FRONTMATTER/04_2012_INTRODUCTION.md -o /Users/jeyounson/HartConcept/TEX/trans-chapters/sections/04_2012_INTRODUCTION-translation.tex

### footnote 정의 블록 헤더 삭제

`## 제1장 각주`, `## Leslie Green 서론 각주`처럼 내용 없이 제목만 남는
표제는 원문의 `FOOTNOTES CHAPTER ...`에 해당한다. 이 표제들은 페이지 하단
footnote 정의 블록의 내부 헤더이므로 B5 PDF에는 출력하지 않는다.
`제n장 주석` 및 `제n장 제3판 주석`은 독자가 읽는 장말 주석 표제이므로
유지한다.

### 따옴표 앞부분 변환

한국어가 포함된 따옴표는 TeX 산출물에서도 유니코드 곡선 따옴표로 둔다.
홑따옴표는 `‘ ’`, 겹따옴표는 `“ ”`를 사용한다. 현재 XeLaTeX/KoPubWorld
조합에서는 TeX식 ASCII 홑따옴표(`...')가 실제 PDF에서 grave/apostrophe
모양으로 남을 수 있으므로, 한국어 용어와 문장은 TeX식 백틱/아포스트로피
관행에 맡기지 않는다. 영문 전용 quote와 영어 소유격/축약형 아포스트로피는
기계 변환하지 않는다.

예:

```tex
`법(law)이란 무엇인가?'
``입법자의 의도''
```

Pandoc 산출 뒤에도 한국어가 포함된 straight quote 쌍이나 TeX식 quote 쌍이
남으면 B5 후처리에서 유니코드 곡선 따옴표로 보정한다. 유니코드 따옴표
(`‘ ’`, `“ ”`, `「 」`)가 의도적으로 들어간 경우에는 그대로 둔다.

### 주석부분 \newpage

장별 주석 및 제3판 주석은 원본처럼 새 페이지에서 시작하고 본문보다 작은
폰트로 둔다. 각 주석 항목은 목록 들여쓰기 없이 보통 문단으로 놓으며,
페이지 표지는 강조하지 않고, 주석 제목 어절만 Markdown 강조로 표시한다.
제목은 마침표로 닫고 설명 본문은 보통체로 이어간다. Markdown 권장형은
`185쪽. *자연법(Natural Law).* 본문...`이다. 제목 없는 편집 메모는
`272쪽. [메모...]`처럼 쪽수로 시작하는 보통 문단으로 둔다.

B5 TeX 후처리는 쪽수 시작줄 앞에 미세한 줄간격을 넣고 들여쓰기를 제거한다.
제목 강조는 이탤릭이 아니라 `\notetitle{}` 고딕 처리로 바꾸며, 한국어와
영문 제목 모두 같은 방식으로 처리한다.


### 한국어 강조부분 고딕체로 전환


#### 또는 한국어만 애초에 변경(시도 안해 봤음)

\\emph\{(?=[\uAC00-\uD7AF])

를

\\emphksans{

로

#### 맨 먼저 숫자가 오는 경우 한국어인지 확인하여 변경

\\emph\{(?=\d)

를

\\emphksans{




xelatex dignity-bio.tex                                                                                                                 
