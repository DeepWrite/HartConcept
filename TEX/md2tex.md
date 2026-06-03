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

### 마지막 FOOTNOTE 헤더 삭제

### 따옴표 앞부분 변환
`  

### 주석부분 \newpage


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
