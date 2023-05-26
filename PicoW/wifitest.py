# basic wifi test

import os
import ipaddress
import wifi
import socketpool

print()
print("Connecting to WiFi")

#  connect to your SSID
wifi.radio.connect(os.getenv('WIFI_SSID'), os.getenv('WIFI_PASS'))

print("Connected to WiFi")

pool = socketpool.SocketPool(wifi.radio)

#  prints MAC address to REPL
print("MAC address: ", [hex(i) for i in wifi.radio.mac_address])

#  prints IP address to REPL
print("IP address: ", wifi.radio.ipv4_address)

#  pings Google
ipv4 = ipaddress.ip_address("8.8.4.4")
print("Ping google.com: %f ms" % (wifi.radio.ping(ipv4)*1000))
