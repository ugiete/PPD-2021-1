from xmlrpc.server import SimpleXMLRPCServer

hashTable = dict()

def get(k):
    try:
        return hashTable[k]
    except:
        return None

def put(v):
    aux = v + 0.5
    k = hash(aux)
    hashTable[k] = v
    
    return str(k)

# A simple server with get and put functions
server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
print("Listening on port 8000...")
server.register_function(get, 'get')
server.register_function(put, 'put')
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("Server Interrupted")
    exit(0)
