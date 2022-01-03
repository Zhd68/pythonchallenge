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

#link search
url = 'http://www.pythonchallenge.com/pc/return/bull.html'
content = requests.get(url, auth=('huge', 'file')).text
content_lines = content.splitlines()
pat = r'\d+'
coord = re.findall(pat, content_lines[10])
width_img, height_img = cut_the_list(coord)

url_image = 'http://www.pythonchallenge.com/pc/return/bull.jpg'
page_image = requests.get(url_image, auth=('huge', 'file'))
img = Image.open(BytesIO(page_image.content))

draw = ImageDraw.Draw(img)
for i in range(len(width_img)-1):
    draw.line((int(width_img[i]), int(height_img[i]), int(width_img[i+1]), int(height_img[i+1])), fill=ImageColor.getrgb("red"))
img.show()

#solution
def look_and_tell(num):
    '''generates the first n numbers of the sequence [1, 11, 21, 1211, 111221,'''
    from itertools import groupby
    #add the first member to the list     
    member = '1'
    yield member

    for i in range(num):
        member_list = []
        for value, quantity in groupby(member):
            member_list.append(str(len(list(quantity))))
            member_list.append(str(value))
        member = ''.join(member_list)
        yield member

a = list(look_and_tell(30))
print(len(a[30]))