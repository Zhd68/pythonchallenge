import xmlrpc.client
proxy = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')

print(proxy.phone('Leopold'))