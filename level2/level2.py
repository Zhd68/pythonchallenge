from urllib.request import urlopen
from collections import Counter

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
content = urlopen(url).read().decode()
comment = content.split('<!--')[-1]
comment_set = set(comment[:-3])
for symbol, count in Counter(comment).most_common(len(comment_set)):
    if count == 1:
        print(symbol, end='')
    