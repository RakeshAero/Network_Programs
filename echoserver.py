import socket

host=""
port=4444

serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serv.bind((host,port))
serv.listen()
print('Echo Client Server Started :')
conn,addr = serv.accept()
print('\nConnected with IP => ',addr[0])
print('\nPort => ',addr[1])

try:
    while True:
        data = serv.recv(2048).decode()
        
        if not data:
            print('Disconnected')

        client_message = data.strip()
        if client_message.lower() == 'q':
            print('Disconnected')
            break

        print('\nClient : ',data.strip()) 
        message = input('\nServer : ')
        serv.sendall((message + '\r\n').encode())
except KeyboardInterrupt:
    print('Keyboard Interrupt')

finally:
    serv.close()
    print('Disconnected')