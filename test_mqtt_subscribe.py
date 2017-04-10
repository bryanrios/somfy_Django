import paho.mqtt.client as mqtt
from django_somfy.settings import SETTINGS

def on_connect(client, userdata, flags, rc):
    print("connected")
    client.subscribe("somfy/#")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.username_pw_set(SETTINGS['mqtt_user'], password=SETTINGS['mqtt_pass'])
mqttc.connect(SETTINGS['mqtt_host'], port=SETTINGS['mqtt_port'])

mqttc.loop_forever()
