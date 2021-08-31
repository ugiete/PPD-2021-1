from src.nodes import Node
from numpy import array
from random import sample

def init_dht(size: int) -> array:
    return array([Node(id, serial) for serial, id in enumerate(sample(range(pow(2, 32)), size))], dtype=Node)