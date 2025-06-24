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