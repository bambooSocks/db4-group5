import network
import time
from umqtt.robust import MQTTClient
import os
import sys
import _thread
from key import Key

class MQTT:

    def __init__(self, ssid, pswd):
        self.WIFI_SSID = ssid
        self.WIFI_PSWD = pswd

        self.subLoopRunning = False

        # create a random MQTT clientID 
        random_num = int.from_bytes(os.urandom(3), 'little')
        self.mqtt_client_id = bytes('client_'+str(random_num), 'utf-8')
        #email = db4g5@hotmail.com password db4password
        self.ADAFRUIT_IO_URL = b'io.adafruit.com' 
        self.ADAFRUIT_USERNAME = b'db4g5'
        self.ADAFRUIT_IO_KEY = Key()

        self.connect()
    
    def __del__(self):
        self.subLoopRunning = False

    def connect(self):
        # turn off the WiFi Access Point
        ap_if = network.WLAN(network.AP_IF)
        ap_if.active(False)

        # connect the device to the WiFi network
        wifi = network.WLAN(network.STA_IF)
        wifi.active(True)
        wifi.connect(self.WIFI_SSID, self.WIFI_PSWD)

        attempt_count = 0
        while not wifi.isconnected() and attempt_count < 20:
            attempt_count += 1
            time.sleep(1)

        if attempt_count == 20:
            print('could not connect to the WiFi network')
            sys.exit()

        self.client = MQTTClient(client_id=self.mqtt_client_id, 
                    server=self.ADAFRUIT_IO_URL, 
                    user=self.ADAFRUIT_USERNAME, 
                    password=self.ADAFRUIT_IO_KEY,
                    ssl=False)

        try:            
            self.client.connect()
        except Exception as e:
            print('could not connect to MQTT server {}{}'.format(type(e).__name__, e))
            sys.exit()

    # used to publish new data to a certain topic
    def publish(self, topic, value):
        mqtt_feedname = bytes('{:s}/feeds/{:s}'.format(self.ADAFRUIT_USERNAME, topic), 'utf-8')
        try:
            self.client.publish(mqtt_feedname, bytes(str(value), 'utf-8'), qos=0)
        except Exception:
                self.connect()

    # used to poll client subscriptions
    def __sub_loop(self):
        while self.subLoopRunning:
            try:
                self.client.check_msg()
                time.sleep(2)
            except Exception:
                self.connect()



    # run only once with custom function func(topic, msg)
    def setCallback(self, cb):
        self.client.set_callback(cb)

    # add a subscription
    def subscribe(self, topic):
        mqtt_feedname = bytes('{:s}/feeds/{:s}'.format(self.ADAFRUIT_USERNAME, topic), 'utf-8')
        self.client.subscribe(mqtt_feedname)
        if self.subLoopRunning == False:
            self.subLoopRunning = True
            _thread.start_new_thread(self.__sub_loop, ())
