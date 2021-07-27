import xmlrpc.client
from time import time
from random import randint

def run(value):
    keylist = list(range(value))
    start = time()

    proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
    multicall = xmlrpc.client.MultiCall(proxy)
    for v in value:
        keylist[v] = multicall.put(v)
    
    end = time() - start