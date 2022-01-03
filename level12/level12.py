with open('evil2.gfx', 'rb') as f:
    data = f.read()
    #print(data)
    for i in range(5):
        open('{}.jpg'.format(i), 'wb').write(data[i::5])