from time import sleep
import paho.mqtt.client as mqtt

class Client():
    """External client
    """

    def __init__(self, serial: int, host: str = "localhost") -> None:
        self.serial = serial
        self.client = mqtt.Client(f"Client_{serial}")

        self.connect(host = host)
        
    
    def connect(self, host: str) -> None:
        self.client.message_callback_add("putok", put_confirmation)
        self.client.message_callback_add("getok", get_confirmation)
        self.client.user_data_set(self)
        self.client.connect(host)
        self.client.subscribe("putok")
        self.client.subscribe("getok")
        self.client.loop_start()

    def put(self, k: int, v: str) -> None:
        self.client.publish("put", f"{k}:{v}")
        sleep(0.5)
    
    def get(self, k: int) -> None:
        self.client.publish("get", k)
        sleep(0.5)
    
    def disconnect(self) -> None:
        self.client.loop_stop(force = True)
        self.client.disconnect()

def put_confirmation(client: mqtt.MQTT_CLIENT, _user_data: None, message: mqtt.MQTTMessage) -> None:
    print(message.payload.decode('utf-8'))

def get_confirmation(client: mqtt.MQTT_CLIENT, _user_data: None, message: mqtt.MQTTMessage) -> None:
    print(message.payload.decode('utf-8'))