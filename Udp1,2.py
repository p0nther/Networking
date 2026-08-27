import socket

ip='10.0.0.2'
port=31337
message=b"Hello, World!\n"
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto(message,(ip,port))
data, addr=s.recvfrom(1024)
s.close()

print(f"data: {data.decode()}\naddr: {addr}")

#

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip='10.0.0.2'
dport=31337
sport=31338
message= b"Hello, World!\n"
s.bind(('0.0.0.0',sport))
s.sendto(message,(ip,dport))
data, addr=s.recvfrom(1024)
s.close()
print(f'data: {data.decode()}\naddr: {addr}')
