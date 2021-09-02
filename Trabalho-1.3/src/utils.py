from time import sleep

from src.client import Client
from src.nodes import Node
from numpy import array
from random import sample

def init_dht(size: int) -> array:
    return array([Node(id, serial) for serial, id in enumerate(sample(range(pow(2, 32)), size))], dtype=Node)

def init_clients(size: int) -> array:
    return array([Client(serial) for serial in range(size)], dtype=Node)