import requests
import re
from PIL import Image, ImageDraw, ImageColor
from io import BytesIO

def cut_the_list(some_list):
    '''Returns two lists. The first list consists of the even elements of the original list, the second one of the odd elements.'''
    width = []
    height = []
    for i in range(len(some_list)):
        if i % 2 == 0:
            width.append(some_list[i])
        else:
            height.append(some_list[i])
    return width, height

url = 'http://www.pythonchallenge.com/pc/return/good.html'
content = requests.get(url, auth=('huge', 'file')).text
comment = content.split('first+second=?')[1]
pat = r'\d+'

#отделяем списки точек из комментариев
first = re.findall(pat, comment.split('second:')[0])
second = re.findall(pat, comment.split('second:')[1])

width_first, height_first = cut_the_list(first)
width_second, height_second = cut_the_list(second)

url_image = 'http://www.pythonchallenge.com/pc/return/good.jpg'
page_image = requests.get(url_image, auth=('huge', 'file'))
img = Image.open(BytesIO(page_image.content))
draw = ImageDraw.Draw(img)

for i in range(len(width_first)-1):
    draw.line((int(width_first[i]), int(height_first[i]), int(width_first[i+1]), int(height_first[i+1])), fill=ImageColor.getrgb("red"))

for i in range(len(width_second)-1):
    draw.line((int(width_second[i]), int(height_second[i]), int(width_second[i+1]), int(height_second[i+1])), fill=ImageColor.getrgb("red"))

img.show()