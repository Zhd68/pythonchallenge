import requests
from PIL import Image
from io import BytesIO
import numpy as np
from itertools import groupby

def cut_it(image_list ,width, height):
    '''Returns a list. It is obtained by dividing the original list into <height> lists of length <width>'''
    cut_image = []
    for i in range(height):
        cut_image.append(image_list[width * i: width * (i + 1)])
    return cut_image

url_image = 'http://www.pythonchallenge.com/pc/return/mozart.gif'
page_image = requests.get(url_image, auth=('huge', 'file'))
img = Image.open(BytesIO(page_image.content))
width, height = img.size
data = list(img.getdata())

cut_data = cut_it(data ,width, height)

#search pink line
term_list = []
for color, num in groupby(cut_data[1]):
    term_list.append(str(color))
    term_list.append(len((list(num))))
print(term_list)
#pink color 195, 5 pixels in a row

for i in range(height):
    start = cut_data[i].index(195)
    cut_data[i] = cut_data[i][start:] + cut_data[i][start::-1]

data_imege_result = np.array(cut_data)
img_result = Image.fromarray(data_imege_result.astype(np.uint8))
img_result.show()


