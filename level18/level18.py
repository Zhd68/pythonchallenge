import gzip
from difflib import Differ

with gzip.open('deltas.gz', 'rb') as f:
    left_data = []
    right_data = []
    #print(f.read())
    for line in f:
        left_data.append(line[:53].decode() + '\n')
        right_data.append(line[56:].decode())

compare = Differ().compare(left_data, right_data)
#print(list(compare))

space_data, plus_data, minus_data = [], [], []

for line in list(compare):
    if line[0] == ' ':
        space_data.extend(line[2:].split())
    elif line[0] == '+':
        plus_data.extend(line[2:].split())
    else:
        minus_data.extend(line[2:].split())

space_bytes = bytes([int(i, 16) for i in space_data])
plus_bytes = bytes([int(i, 16) for i in plus_data])
minus_bytes = bytes([int(i, 16) for i in minus_data])

with open('space.png', 'wb') as space:
    space.write(space_bytes)
with open('plus.png', 'wb') as plus:
    plus.write(plus_bytes)
with open('minus.png', 'wb') as minus:
    minus.write(minus_bytes)