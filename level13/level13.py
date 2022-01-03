import xmlrpc.client
proxy = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')

print(proxy.system.listMethods())
print(proxy.system.methodHelp('phone'))
print(proxy.system.methodSignature('phone'))

print(proxy.phone('Bert'))