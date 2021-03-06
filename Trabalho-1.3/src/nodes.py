from operator import itemgetter
from time import sleep
import paho.mqtt.client as mqtt

class Node():
    """Node class
    """

    def __init__(self, id: int, serial: int, host: str = "localhost") -> None:
        self.id = id
        self.serial = serial
        self.client = mqtt.Client(f"Node_{serial}")
        self.siblings = {}
        self.table = {}

        self.connect(host = host)
        
    
    def connect(self, host: str) -> None:
        self.client.message_callback_add("join", on_joined_sibling)
        self.client.message_callback_add("put", on_put)
        self.client.message_callback_add("get", on_get)
        self.client.user_data_set(self)
        self.client.connect(host) 
        self.client.subscribe("join")
        self.client.subscribe("put")
        self.client.subscribe("get")
        self.client.loop_start()
    
    def join(self) -> None:
        self.client.publish("join", f"{self.serial}@{self.id}")
        sleep(1)
    
    def addSibling(self, value: str) -> None:
        [serial, id] = value.split("@")

        self.siblings[int(serial)] = int(id)
        self.sortSiblings()
    
    def sortSiblings(self) -> None:
        self.siblings = {k: v for k,v in sorted(self.siblings.items(), key=itemgetter(1))}
    
    def getNeighbors(self) -> None:
        keys = list(self.siblings.keys())

        myIndex = keys.index(self.serial)
        before_index = myIndex - 1
        after_index = myIndex + 1 if myIndex < (len(keys) - 1) else 0
        
        self.before = (keys[before_index], self.siblings[keys[before_index]])
        self.after = (keys[after_index], self.siblings[keys[after_index]])
    
    def put(self, key: int, value: str) -> None:
        cond = key > self.before[1] and key <= self.id if self.before[1] < self.id else key > self.before[1] or key <= self.id
        if cond:
            self.table[key] = value
            self.client.publish("putok", f"Valor armazenado com sucesso no nó {self.serial}")
        
    def get(self, key:int) -> None:
        cond = key > self.before[1] and key <= self.id if self.before[1] < self.id else key > self.before[1] or key <= self.id
        if cond:
            value = self.table[key]
            self.client.publish("getok", f"Conteúdo armazenado \"{value}\", no nó {self.serial}")
        
    def disconnect(self) -> None:
        self.client.loop_stop(force=True)
        self.client.disconnect()

    
def on_joined_sibling(_client: mqtt.MQTT_CLIENT, node: Node, message: mqtt.MQTTMessage):
    sibling_id = message.payload.decode('utf-8')
    node.addSibling(sibling_id)

def on_put(_client: mqtt.MQTT_CLIENT, node: Node, message: mqtt.MQTTMessage):
    payload = message.payload.decode('utf-8')
    [key, value] = payload.split(":")

    node.put(int(key), value)

def on_get(_client: mqtt.MQTT_CLIENT, node: Node, message: mqtt.MQTTMessage):
    key = message.payload.decode('utf-8')

    node.get(int(key))