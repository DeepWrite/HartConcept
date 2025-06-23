import re

with open("chapter_9-mymark.md", "r", encoding="utf-8") as f:
    content = f.read()

counter_start = 186  # 원하는 시작 번호
def replacer(match):
    global counter_start
    replacement = f"(p. {counter_start})"
    counter_start += 1
    return replacement

# \mymark를 찾아 대체
new_content = re.sub(r'\\mymark', replacer, content)

with open("chapter_9.md", "w", encoding="utf-8") as f:
    f.write(new_content)