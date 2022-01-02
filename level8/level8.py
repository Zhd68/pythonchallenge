import bz2
from urllib.request import urlopen
from PIL import Image, ImageDraw
import re

un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
print(bz2.decompress(un).decode('utf-8'))
print(bz2.decompress(pw).decode('utf-8'))

url = 'http://www.pythonchallenge.com/pc/def/integrity.html'
content = urlopen(url).read().decode()
content_lines = content.splitlines()
pat = '\d+'
coords = re.findall(pat, content_lines[11])

url_image = 'http://www.pythonchallenge.com/pc/def/integrity.jpg'
img = Image.open(urlopen(url_image))
draw = ImageDraw.Draw(img)

width = []
height = []
for i in range(len(coords)):
    if i % 2 == 0:
        width.append(coords[i])
    else:
        height.append(coords[i])

for i in range(len(width)-1):
    draw.line((int(width[i]), int(height[i]), int(width[i+1]), int(height[i+1])))
img.show()