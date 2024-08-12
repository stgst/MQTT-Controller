import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("tschool/car/control")

def on_message(client, userdata, msg):
    command = json.loads(msg.payload.decode())
    print("Command received: " + str(command))
    FL, FR, BL, BR = command['FL'], command['FR'], command['BL'], command['BR']

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("124.218.226.248", 1883, 60)

client.loop_forever()
