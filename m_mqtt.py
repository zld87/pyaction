import paho.mqtt.client as mqtt_client
from paho import mqtt
import time
import json
import random

broker = '127.0.0.1'  # mqtt代理服务器地址
port = 1883
keepalive = 60     # 与代理通信之间允许的最长时间段（以秒为单位）
topic = "/python/mqtt"  # 消息主题
client_id = f'python-mqtt-pub-{random.randint(0, 1000)}'  # 客户端id不能重复

def connect_mqtt():
    # '''连接mqtt代理服务器'''
    def on_connect(client, userdata, flags, rc):
        # '''连接回调函数'''
        # 响应状态码为0表示连接成功
        if rc == 0:
            print("Connected to MQTT OK!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # 连接mqtt代理服务器，并获取连接引用
    client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION2, client_id)
    client.on_connect = on_connect
    client.connect(broker, port, keepalive)
    return client


client = connect_mqtt()
client.loop_start()
