import pickle
from urllib.request import urlopen

url = 'http://www.pythonchallenge.com/pc/def/banner.p'

content = urlopen(url).read()
something_coded = pickle.loads(content)

for something_coded_list in something_coded:
    for symbol, number in something_coded_list:
        print(symbol * number, sep='', end='')
    print('')
