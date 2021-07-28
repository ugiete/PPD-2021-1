from os import system
from subprocess import Popen
from sys import argv, executable
from time import time, sleep
from random import randint, seed
from src.client import Client
from threading import Thread


def putThread(client: Client, M: int, keylist: list, initial: int, end: int) -> None:
    try:
        seed(time())
        for i in range(initial, end):
            keylist[i] = client.put(randint(1, M+1))
    except:
        print("Algum erro aconteceu no put")
        exit(0)

def getThread(client: Client, keylist: list, valuelist: list, initial: int, end: int) -> None:
    try:
        for i in range(initial, end):
            valuelist[i] = client.get(keylist[i])
    except:
        print("Algum erro aconteceu no get")
        exit(0)


if __name__ == "__main__":
    try:
        params = argv[1:]
        try:
            port = 8000 if params == [] or params[0].lower() != '--port' else int(params[1])
        except IndexError:
            print("Digite a porta a utilizar, ou utilize a porta padrao atraves do comando python main.py")
            exit(0)

        serverProcess = Popen([executable, 'connectServer.py', str(port)])
        sleep(1)

        M = 1000000
        m = 1000000
        keylist = list(range(M))
        valuelist = list(range(M))
        for i in range(M):
            keylist[i] = 0
            valuelist[i] = 0
        nThreads = [1,2,4,8]

        timestamps = {}

        jobs = list()

        for idx in nThreads:
            elements_per_thread = m // idx
            start = time()

            for i in range(idx):
                initial = elements_per_thread*i
                end = elements_per_thread*(i+1)

                thread = Thread(target=putThread(
                    Client(port=port), M, keylist, initial, end))
                jobs.append(thread)

            for j in jobs:
                j.start()

            for j in jobs:
                j.join()
            
            jobs.clear()
            
            for i in range(idx):
                initial = elements_per_thread*i
                end = elements_per_thread*(i+1)

                thread = Thread(target=getThread(
                    Client(port=port), keylist, valuelist, initial, end))
                jobs.append(thread)

            for j in jobs:
                j.start()

            for j in jobs:
                j.join()
            
            end = time() - start

            timestamps[idx] = end
            
            for i in range(m):
                keylist[i] = 0
                valuelist[i] = 0

            jobs.clear()

        serverProcess.kill()
        print(timestamps)
    except KeyboardInterrupt:
        serverProcess.kill()
        print(timestamps)
        exit(0)
