import RPi.GPIO as GPIO
import json
import paho.mqtt.client as mqtt
import time


thread = None

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ir = 15

mqttc = mqtt.Client()
mqttc.connect("192.168.195.7") #<--- Please change IP to match the location of your MQTT broker
# 192.168.195.7
mqttc.loop_start()

GPIO.setup(ir, GPIO.IN, GPIO.PUD_DOWN)


def data_collect():
    GPIO.add_event_detect(ir, GPIO.FALLING, callback=post_score, bouncetime=200)
    while True:
        time.sleep(0)

    """while True:

        time.sleep(0)
        t1 = time.time()
        try:
            channel = GPIO.wait_for_edge(ir,
                                         GPIO.RISING,
                                         timeout=5000)
            if channel != None:
                rpm = 0
                brokerMessage = {'Status': 'scored', 'Player': '1', 'Score': 1, 'Data': '0'}
                print("message sent")
                mqttc.publish("lights/player1", json.dumps(brokerMessage))
            else:
                brokerMessage = {"rpm": 1}
        except KeyboardInterrupt:
            connection.close()
            GPIO.cleanup()
            sys.exit(0)"""


def post_score(channel):
    brokerMessage = {'Status': 'scored', 'Player': '1', 'Score': 1, 'Data': '0'}
    print("message sent")
    mqttc.publish("lights/player2", json.dumps(brokerMessage))


if __name__ == '__main__':
    data_collect()
    print("started")
