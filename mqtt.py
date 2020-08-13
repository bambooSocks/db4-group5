import network
import time
from umqtt.robust import MQTTClient
import os
import sys
from key import Key

class MQTT:

    def __init__(self, ssid, pswd):
        self.WIFI_SSID = ssid
        self.WIFI_PSWD = pswd

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

        # create a random MQTT clientID 
        random_num = int.from_bytes(os.urandom(3), 'little')
        mqtt_client_id = bytes('client_'+str(random_num), 'utf-8')
        #email = db4g5@hotmail.com password db4password
        self.ADAFRUIT_IO_URL = b'io.adafruit.com' 
        self.ADAFRUIT_USERNAME = b'db4g5'
        self.ADAFRUIT_IO_KEY = Key()

        self.client = MQTTClient(client_id=mqtt_client_id, 
                            server=self.ADAFRUIT_IO_URL, 
                            user=self.ADAFRUIT_USERNAME, 
                            password=self.ADAFRUIT_IO_KEY,
                            ssl=False)
        try:            
            self.client.connect()
        except Exception as e:
            print('could not connect to MQTT server {}{}'.format(type(e).__name__, e))
            sys.exit()
    
    def publish(self, measurement, value):
        mqtt_feedname = bytes('{:s}/feeds/{:s}'.format(self.ADAFRUIT_USERNAME, measurement), 'utf-8')
        self.client.publish(mqtt_feedname, bytes(str(value), 'utf-8'), qos=0)
