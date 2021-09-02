from random import randint
from time import sleep
from src.utils import init_clients, init_dht
from sys import argv

if __name__ == '__main__':
    try:        
        try:
            flag_idx = argv.index("--clients")
            clients = int(argv[flag_idx + 1])
        except:
            clients = 1

        try:
            flag_idx = argv.index("--iterMax")
            iterMax = int(argv[flag_idx + 1])
            print(f"{iterMax} iterações (max)")
        except:
            iterMax = float('inf')
        
        print('Ctrl+C para sair')

        print('\nCarregando nós ...')

        DHT = init_dht(8)
        Clients = init_clients(clients)

        for node in DHT:
            node.join()

        for node in DHT:
            node.getNeighbors()
        
        print("Publicando")

        it = 0
        while it < iterMax:
            for c in Clients:
                key = randint(0, pow(2,32))
                c.put(key, str(randint(0, 1000)))
                c.get(key)
                sleep(0.5)

            it = it + 1
        
        print("Aguarde desconexão")

        for node in DHT:
            node.disconnect()

        for c in Clients:
            c.disconnect()

        print("Programa finalizado!")  

    except KeyboardInterrupt:
        print("Aguarde desconexão")

        for node in DHT:
            node.disconnect()

        for c in Clients:
            c.disconnect()

        print("Programa finalizado!")    
