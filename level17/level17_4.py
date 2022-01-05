import requests

url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
page = requests.get(url)

msg = {'info': 'the flowers are on their way'}

page = requests.post(url, cookies = msg)

print(page.text)