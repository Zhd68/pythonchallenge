import requests
import re

#step1
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
page = requests.get(url)

pat = r'(?<=info=).+(?= for)'

msg_info = re.findall(pat, str(page.cookies))
msg_info_str = str(msg_info[0]).replace('%20', ' ')
print(msg_info_str)

#step2
url_busynothing = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='
busynothing = '12345'
result = []
while True:
    page_busynothing = requests.get(url_busynothing + busynothing)
    content = page_busynothing.text
    cook = re.findall(pat, str(page_busynothing.cookies))
    busynothing = content.split(' ')[-1]
    result.append(cook[0])
    if not busynothing.isdigit():
        break

msg = ''    
for sym in result:
    msg += sym
print(msg)