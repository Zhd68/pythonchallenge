from urllib.request import urlopen
from PIL import Image
import re

url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
content = urlopen(url)
img = Image.open(content)
width, height = img.size
data = list(img.getdata())

cut_data = []
decode_data_item = []
decode_data_all = []
for i in range(height):
    cut_data.append(data[width * i: width * (i + 1)])
    for tuples in cut_data[i]:
        decode_data_item.append(chr(tuples[0]))
    decode_data_all.append(decode_data_item)
    decode_data_item = []

data_msg = ''
for i in range(0, width, 7):
    data_msg += decode_data_all[43][i]
print(data_msg)

pat = '\d+'
msg = re.findall(pat, data_msg)
print(msg)

result = ''
for lit in msg:
    result += chr(int(lit))
print(result)