from xmlrpc.client import ServerProxy, MultiCall
#from time import time
#from random import randint

class Client():
    """RPC Client
    """

    def __init__(self, host: str = "localhost", port: int = 8000) -> None:
        self._proxy = ServerProxy(f"http://{host}:{port}", allow_none = True)
    
    def get(self, k: str) -> int:
        return self._proxy.get(k)
    
    def put(self, v: int) -> int:
        return self._proxy.put(v)
    
    def show(self) -> str:
        return self._proxy.show()



#def run(value):
#    keylist = list(range(value))
#    start = time()
#
#    proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
#    multicall = xmlrpc.client.MultiCall(proxy)
#    for v in value:
#        keylist[v] = multicall.put(v)
#    
#    end = time() - start