import requests
from PIL import Image, ImageDraw
from io import BytesIO

url_image = 'http://www.pythonchallenge.com/pc/return/wire.png'
page_image = requests.get(url_image, auth=('huge', 'file'))
img = Image.open(BytesIO(page_image.content))
data = list(img.getdata())

img_result = Image.new('RGB', (100, 100))
draw = ImageDraw.Draw(img_result)

motion = ((1, 0), (0, 1), (-1, 0), (0, -1))
x, y = (-1, 0)
first_draw = [99, 99, 0, 1]
delta = 0
motion_word = 'top'

for pix in data:
    from operator import add
    if motion_word == 'top':
        x, y = map(add, (x, y), motion[0])
        draw.point((x, y), pix)
        if x == first_draw[0] - delta:
            motion_word = 'right'
            continue
        
    if motion_word == 'right':
        x, y = map(add, (x, y), motion[1])
        draw.point((x, y), pix)
        if y == first_draw[1] - delta:
            motion_word = 'bottom'
            continue
        
    if motion_word == 'bottom':
        x, y = map(add, (x, y), motion[2])
        draw.point((x, y), pix)
        if x == first_draw[2] + delta:
            motion_word = 'left'
            continue
        
    if motion_word == 'left':
        x, y = map(add, (x, y), motion[3])
        draw.point((x, y), pix)
        if y == first_draw[3] + delta:
            motion_word = 'top'
            delta += 1
            continue
            
img_result.show()




