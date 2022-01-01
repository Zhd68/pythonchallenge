from zipfile import ZipFile

myzip = ZipFile('channel.zip', 'r')

name_file = '90052'
extension = '.txt'
comments = []
while True:
    content = myzip.open(name_file + extension).read().decode()
    name_file = content.split(' ')[-1]
    if not name_file.isdigit():
        break
    comments.append(myzip.getinfo(name_file + extension).comment.decode())
print(name_file)

for comm in comments:
    print(comm, end='')