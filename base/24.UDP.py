import socket,time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('127.0.0.1', 4006))

print('bind 4006')

while True:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s, i am udp!' % data, addr)
    # time.sleep(1)
    s.sendto(b'hello i again send msg', addr)