from random import randint
from time import sleep
from src.utils import *
import paho.mqtt.client as mqtt

Client = mqtt.Client("Main")
Client.connect("localhost")
Client.subscribe("putok")
Client.subscribe("getok")
Client.message_callback_add("putok", put_confirmation)
Client.message_callback_add("getok", get_confirmation)
Client.loop_start()

DHT = init_dht(8)

for node in DHT:
    node.join()

for node in DHT:
    node.getNeighbors()

while True:
    key = randint(0, pow(2,32))
    put(Client, key, str(randint(0, 1000)))
    sleep(1)
    get(Client, key)
    sleep(1)

for node in DHT:
    node.disconnect()

Client.loop_stop(force=True)
Client.disconnect()