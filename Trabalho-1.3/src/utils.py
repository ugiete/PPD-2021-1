from time import sleep
from src.nodes import Node
from numpy import array
from random import sample

def init_dht(size: int) -> array:
    return array([Node(id, serial) for serial, id in enumerate(sample(range(pow(2, 32)), size))], dtype=Node)

def put(Client, k: int, v: str) -> None:
    Client.publish("put", f"{k}:{v}")
    sleep(0.5)

def put_confirmation(_client, user_data, message):
    print(message.payload.decode('utf-8'))

def get(Client, k: int) -> None:
    Client.publish("get", k)
    sleep(0.5)

def get_confirmation(_client, user_data, message):
    print(message.payload.decode('utf-8'))