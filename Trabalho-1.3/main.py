from src.utils import init_dht

DHT = init_dht(8)

for node in DHT:
    node.join()
