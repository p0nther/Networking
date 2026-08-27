from scapy.all import IP, TCP, send 

network_layer=IP(dst="10.0.0.2")
# why we need ack,seq : because TCP is a connection-oriented protocol. Unlike UDP, which just "fires and forgets," TCP needs these numbers to ensure data is reliable and organized.
trans_layer=TCP(sport=31337, dport=31337, seq=31337,ack=31337,flags="APRSF")

packet= network_layer / trans_layer
send(packet)
