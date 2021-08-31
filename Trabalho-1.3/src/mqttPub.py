import paho.mqtt.client as mqtt

mqttBroker = "127.0.0.1" 

client = mqtt.Client("Node_1")
client.connect(mqttBroker)