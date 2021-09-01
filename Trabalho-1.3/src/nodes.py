from operator import itemgetter
from time import sleep
import paho.mqtt.client as mqtt

class Node():
    """Node class
    """

    def __init__(self, id: int, serial: int) -> None:
        self.id = id
        self.serial = serial
        self.client = mqtt.Client(f"Node_{serial}")
        self.siblings = {}
        self.table = {}

        self.connect()
        
    
    def connect(self, host: str = "127.0.0.1") -> None:
        self.client.message_callback_add("join", on_joined_sibling)
        self.client.user_data_set(self)
        self.client.connect(host) 
        self.client.subscribe("join")
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
        
        self.before = (keys[before_index], self.siblings[keys[before_index]]),
        self.after = (keys[after_index], self.siblings[keys[after_index]])
    
    

def on_joined_sibling(_client: mqtt.MQTT_CLIENT, node: Node, message: mqtt.MQTTMessage):
    sibling_id = message.payload.decode('ascii')
    node.addSibling(sibling_id)