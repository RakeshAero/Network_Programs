import socket

host = 'localhost'
port = 4444

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect((host,port))

try:
    while True:
        data = sock.recv(2048).decode()
        if not data:
            print('disconnected')
            break
        print('Server : {}',format(data).strip())
        input = input('You : ')
        if input.lower() == 'q':
            print('Disconnecting :')
            break
        sock.sendall(input.encode())
except KeyboardInterrupt:
    print('\nConnection Closed By the server')
finally:
    sock.close()
    print('\nDisconnected')

