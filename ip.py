from scapy.all import IP,send


packet=IP(dst="10.0.0.2",proto=0xFF)
send(packet)
