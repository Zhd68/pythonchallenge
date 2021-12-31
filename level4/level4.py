from urllib.request import urlopen

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
nothing = '12345'
result = []

for i in range(400):
    content = urlopen(url + nothing).read().decode()
    nothing = content.split(' ')[-1]
    result.append(nothing)

new_lesson = [i for i in result if not i.isdigit()]
print(new_lesson)