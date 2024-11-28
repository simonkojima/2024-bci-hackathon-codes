import time
import pythonosc.udp_client

ip = "127.0.0.1"
port = 7400

client = pythonosc.udp_client.SimpleUDPClient(ip, port)

data = 1
client.send_message("/osc/test", data)
time.sleep(1)

data = 0.23
client.send_message("/osc/test", data)
time.sleep(1)

data = "hello"
client.send_message("/osc/test", data)
time.sleep(1)

data = 1
client.send_message("/filter", data)
