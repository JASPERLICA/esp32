# **************************************#
#  MQTT in MicroPython with Thingspeak  #
# **************************************#
# Author: George Bantique               #
#         TechToTinker Youtube Channel  #
#         TechToTinker.blogspot.com     #
#         tech.to.tinker@gmail.com      #
# Date: Dec.5, 2020                    #
# Please feel free to modify the code   #
# according to your needs.              #
# **************************************#

# **************************************#
# Load necessary libraries
import machine
import network
import wifi_credentials
from umqtt.simple import MQTTClient
import dht
import time

# **************************************#
# Objects:
led = machine.Pin(2,machine.Pin.OUT)
#d = dht.DHT22(machine.Pin(23))


# **************************************#
# Configure the ESP32 wifi as STAtion.
sta = network.WLAN(network.STA_IF)
if not sta.isconnected():
  print('connecting to network...')
  sta.active(True)
  #sta.connect('wifi ssid', 'wifi password')
  sta.connect(wifi_credentials.ssid, wifi_credentials.password)
  while not sta.isconnected():
    pass
print('network config:', sta.ifconfig())

# **************************************#
# Global variables and constants:
mqtt_server = "broker.emqx.io"
client_id = 'esp32_Jasper'
user = "emqx"
password = "public"

#SERVER = "mqtt.thingspeak.com"
#client = MQTTClient("umqtt_client", SERVER)
#CHANNEL_ID = "1249898"
#WRITE_API_KEY = "PJX6E1D8XLV18Z87"

#SERVER = "broker.emqx.io"
client = MQTTClient(client_id, mqtt_server,1883, user, password,keepalive=60)
CHANNEL_ID = "JasperLica"
WRITE_API_KEY = "hhhPJX6E1D8XLV18Z87"

# topic = "channels/1249898/publish/PJX6E1D8XLV18Z87"
#topic = "channels/" + CHANNEL_ID + "/publish/" + WRITE_API_KEY
topic ="Jasperesp32"
UPDATE_TIME_INTERVAL = 5000 # in ms unit
last_update = time.ticks_ms()

# **************************************#
# Main loop:
while True:
    if time.ticks_ms() - last_update >= UPDATE_TIME_INTERVAL:
        #d.measure()
        #t = d.temperature()
        #h = d.humidity()
        t = "65c"
        h= "448"
        #payload = "field1=" + str(t) + "&field2=" + str(h)
        payload = "field1={}&field2={}" .format(str(t), str(h))

        client.connect()
        client.publish(topic, payload)
        client.disconnect()

        print(payload)
        led.value(not led.value())
        last_update = time.ticks_ms()