import time

# 단방향 메신저
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
    else:
        print("Connect returned result code: " + str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Received message: " + msg.topic + " -> " + msg.payload.decode("utf-8"))

def on_disconnect(client, userdata, mid):
    print("In on_pub callback mid= ", mid)

def on_log(client, userdata, level, buf):
    print("log : ", buf)


# create the client
client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.on_log = on_log

# enable TLS
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

# set username and password
client.username_pw_set("JSPark", "Qlwutdma56")

# connect to HiveMQ Cloud on port 8883
client.connect("38eb288b38d446669aae84b29d57b8c6.s1.eu.hivemq.cloud", 8883)

contents = ''

time.sleep(5)

while contents != "exit":
    client.loop_start()

    # Message contents
    contents = input("메시지를 입력하세요: ")

    # publish "Hello" to the topic "my/test/topic"
    client.publish("my/test/topic", contents)


client.loop_stop()
client.disconnect()