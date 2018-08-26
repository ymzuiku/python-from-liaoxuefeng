import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1', 4005))

s.listen(5)
print('watiing...')


def tcplink(sock, addr):
    # print('accept new connection from %s' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('hello, %s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s colsed.' % addr)


while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
