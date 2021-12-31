from urllib.request import urlopen
import re

url = 'http://www.pythonchallenge.com/pc/def/equality.html'
contents = urlopen(url).read().decode()

pat = '[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]'

msg = re.findall(pat, contents)
for lit in msg:
    print(lit[4:-4], end='')