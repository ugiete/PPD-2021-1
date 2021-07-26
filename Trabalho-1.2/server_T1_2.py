from xmlrpc.server import SimpleXMLRPCServer

hashTable = dict()

def get(k):
    if(k in hashTable.keys()):
        return hashTable[k]
    
    return None

def put(v):
    aux = v + 0.5
    k = hash(aux)
    hashTable[k] = v
    
    return k

# A simple server with get and put functions
server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_multicall_functions()
server.register_function(get, 'get')
server.register_function(put, 'put')
server.serve_forever()
