from scapy.all import IP, TCP, sr1, send 

network_layer=IP(dst="10.0.0.2")
trans_layer=TCP(sport=31337, dport=31337, seq=31337,flags='S')
packet= sr1(network_layer / trans_layer)

if packet and packet.haslayer(TCP):
        server_seq=packet.seq
        server_ack=packet.ack
# seq mean:  "This is where I am starting."
# ack mean: 

# Seq: "My current ID."
# Ack: "Your ID + 1."
        final_ack=TCP(sport=31337, dport=31337, seq= server_ack, ack=server_seq+1 , flags='A')

        send(network_layer/final_ack)
