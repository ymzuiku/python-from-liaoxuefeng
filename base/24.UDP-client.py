import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 4007))

for v in [b'Michael', b'Tracy', b'Sarah']:
    s.sendto(v, ('127.0.0.1', 4006))
    print(s.recv(1024).decode('utf-8'))
# s.close()


while True:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s, i am udp!' % data, addr)