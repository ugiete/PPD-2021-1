import xmlrpc.client
from time import time
from random import randint

def run(m):
    keylist = list(range(m))
    valuelist = list(range(m))
    start = time()

    proxy = xmlrpc.client.ServerProxy("http://localhost:8000/", allow_none=True)
    for i in range(m):
        value = randint(0, 2*m)
        keylist[i] = proxy.put(value)
    
    for i in range(m):
        valuelist[i] = proxy.get(keylist[i])

    
    end = time() - start

    print('\nTempo total: ' + str(end))