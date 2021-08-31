from threading import Thread
import paho.mqtt.client as mqtt

def on_message(_client, _user_data, message):
    print(message)

class Node():
    """Node class
    """

    def __init__(self, id: int, serial: int) -> None:
        self.id = id
        self.siblings = []

        self.client = mqtt.Client(f"Node_{serial}")
        self.client.connect("127.0.0.1") 
        self.client.subscribe("join")
        self.client.on_message = on_message
        
    
    def join(self) -> None:
        self.client.publish("join", self.id)


