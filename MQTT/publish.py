import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connection OK")
    else:
        print("Bad connection Returned code= ", rc)

def on_disconnect(client, userdata, mid):
    print("In on_pub callback mid= ", mid)

def on_publish(client, userdata, mid):
    print("In on_pub callback mid= ", mid)


# 새로운 클라이언트 생성
client = mqtt.Client("JSPARK")
# 콜백 함수 설정 
# on_connect(브로커에 접속)
# on_disconnect(브로커에 접속종료)
# on_publsih(메세지 발행)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish
# address : localhost, port: 1883 에 연결
client.connect("38eb288b38d446669aae84b29d57b8c6.s1.eu.hivemq.cloud", 8883)
client.loop_start()
# common topic으로 메시지 발행
client.publish('common', json.dumps({"succcess": "ok"}), 1)
client.loop_stop()
# 연결 종료
client.disconnect()