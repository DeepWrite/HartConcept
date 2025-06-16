## 영문섹션

### 진입
cd /Users/jeyounson/HartConcept/TEX/chapters
폰트 파일과 템플릿 파일이 있는 폴더임.

### Md 파일을 tex 파일로 변환 (mybook-template.tex 템플릿 이용)

pandoc /Users/jeyounson/HartConcept/OriginalText/CHAPTERS/chapter_1.md -o /Users/jeyounson/HartConcept/TEX/chapters/chapter_1.tex --template=mybook-template.tex

## 한글 섹션

### 진입
cd /Users/jeyounson/HartConcept/TEX/trans-chapters/sections
폰트 파일과 템플릿 파일이 있는 폴더임.

### Md 파일을 tex 파일로 변환 (hartbook-template.tex 템플릿 이용)

pandoc /Users/jeyounson/HartConcept/TRANSLATIONS/CHAPTERS/chapter_1-translation.md -o /Users/jeyounson/HartConcept/TEX/trans-chapters/sections/chapter_1-translation.tex --template=hartbook-template.tex