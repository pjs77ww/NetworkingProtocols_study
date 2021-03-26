import paho.mqtt.client as mqtt

f = open("log.txt", 'w')

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)

def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))
    f.close()

def on_subscribe(client, userdata, mid, granted_qos):
    print("subscribed: " + str(mid) + " " + str(granted_qos))


def on_message(client, userdata, msg):
    print(str(msg.payload.decode("utf-8")))
    f.write(str(msg.payload.decode("utf-8")))
    f.write("\n")

def on_log(client, userdata, level, buf):
    print("log : ", buf)
    f.write(buf)
    f.write("\n")

# 새로운 클라이언트 생성
client = mqtt.Client("SHJeon")
# 콜백 함수 설정 on_connect(브로커에 접속)
# on_disconnect(브로커에 접속중료)
# on_subscribe(topic 구독),
# on_message(발행된 메세지가 들어왔을 때)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_log = on_log

# enable TLS
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

# set username and password
client.username_pw_set("JSPark", "Qlwutdma56")

# connect to HiveMQ Cloud on port 8883
client.connect("38eb288b38d446669aae84b29d57b8c6.s1.eu.hivemq.cloud", 8883)

# common topic 으로 메세지 발행
client.subscribe('my/test/topic', 1)

# # 발표용 broker
# client.connect("broker.mqttdashboard.com", 1883)

# # 발표용 topic
# client.subscribe('hello', 1)
client.loop_forever()