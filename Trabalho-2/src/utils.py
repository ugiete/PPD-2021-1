from time import sleep

from src.client import Client
from src.nodes import Node
from numpy import array, delete, append
from numpy.random import choice 
from random import randint

def init_dht(taboo: list) -> array:
    id = randint(0, pow(2, 32) - 1)
    taboo.append(id)
    new_node = Node(id, 1)
    new_node.join()
    return array([new_node], dtype=Node)

def node_operation() -> bool:
    x = randint(1, 3)

    if x == 1:
        print('-----------------------------------------------PASS')
        return None
    elif x == 3:
       print('-----------------------------------------------RMV')
       return False
    
    print('-----------------------------------------------ADD')
    return True

def update_dht(taboo: list, dht: array, cur_node: int) -> None:
    op = node_operation()

    if op == True:
        id = randint(0, pow(2, 32) - 1)
        while id in taboo:
            id = randint(0, pow(2, 32) - 1)

        new_node = Node(id, cur_node + 1)
        print(f'Nó {cur_node+1} adicionado, com id {id}')
        dht = append(dht, new_node)

        new_node.join()
        sleep(1)

        for node in dht:
            node.getNeighbors()

        return cur_node + 1, dht
    elif op == False and len(dht) > 1:
        left_node = choice(dht)
        print(f'Nó {left_node.serial} removido')
        node_index = list(dht).index(left_node)
        left_node.leave()
        sleep(1)
        left_node.disconnect()
        del left_node
        dht = delete(dht, node_index)

        for node in dht:
            node.getNeighbors()

    return cur_node, dht

def init_clients(size: int) -> array:
    return array([Client(serial) for serial in range(size)], dtype=Node)
