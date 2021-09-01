from src.utils import init_dht

DHT = init_dht(8)

for node in DHT:
    node.join()

for i, node in enumerate(DHT):
    print(f"Nó {i}")
    node.showSiblings()