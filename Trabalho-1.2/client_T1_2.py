import xmlrpc.client
from time import time
from random import randint

def run(m):
    keylist = list(range(m))
    start = time()

    proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
    multicall = xmlrpc.client.MultiCall(proxy)
    for v in m:
        value = randint(0, m)
        keylist[v] = multicall.put(value)
    
    end = time() - start