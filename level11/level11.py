import requests
from PIL import Image
from io import BytesIO
import numpy as np

def split_image(some_list):
    '''Returns two lists. The first list consists of the even elements of the original list, the second one of the odd elements.'''
    image1 = []
    image2 = []
    for i in range(len(some_list)):
        if i % 2 == 0:
            image1.append(some_list[i])
        else:
            image2.append(some_list[i])
    return image1, image2

def cut_it(image_list ,width, height):
    '''Returns a list. It is obtained by dividing the original list into <height> lists of length <width>'''
    cut_image = []
    for i in range(height):
        cut_image.append(image_list[width * i: width * (i + 1)])
    return cut_image


url_image = 'http://www.pythonchallenge.com/pc/return/cave.jpg'
page_image = requests.get(url_image, auth=('huge', 'file'))
img = Image.open(BytesIO(page_image.content))

width, height = img.size
data = list(img.getdata())

width_new_image, height_new_image = width, height // 2

image1, image2 = split_image(data)

# one image is enough to get the result
cut_image1 = np.array(cut_it(image1, width_new_image, height_new_image))
#cut_image2 = np.array(cut_it(image2, width_new_image, height_new_image))

img1 = Image.fromarray(cut_image1.astype(np.uint8))
#img2 = Image.fromarray(cut_image2.astype(np.uint8))

img1.show()
#img2.show()

