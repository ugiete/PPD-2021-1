from subprocess import Popen
from sys import argv, executable
from time import time, sleep
from random import randint
from multiprocessing.pool import ThreadPool
from src.client import Client
from src.utils import generate_list

def putThread(client: Client, n: int, M: int) -> list:
    return [client.put(randint(0, M)) for _ in range(n)]

def toStr(v: int) -> str:
    return str(v)

if __name__ == "__main__":
    params = argv[1:]
    port = 8000 if params == [] or params[0].lower() != '--port' else int(params[1])

    serverProcess = Popen([executable, 'connectServer.py', str(port)])
    sleep(2)

    client = Client(port=port)

    M = 1000000
    m = 20

    nThreads = 2

    jobs = []

    start = time()

    pool = ThreadPool(processes = nThreads)
    keys = pool.map(client.put, generate_list(M), chunksize = 1)

    #for i in range(nThreads):
    #    elements_per_thread = m // nThreads
#
    #    thread = Thread(target=putThread(client, elements_per_thread, M))
    #    jobs.append(thread)
#
#
    #for j in jobs:
    #    j.start()
#
    #for j in jobs:
    #    j.join()
    
    #for k in keys:
    #    client.get(k)

    pool.close()

    print(time() - start)

    #print(keys)

    serverProcess.kill()