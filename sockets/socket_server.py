import socket

def server_prorgam():
    host='127.0.0.1'
    port=4444
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #IPv4,TCP
    s.bind((host,port)) #use bind() to make a way 
    s.listen(2) #listening on port 4444
    print('Listening on port 4444 ...!')
    conn,addr = s.accept() #accept the message sent by client
    print('Connected to {}'.format(addr))

    while True :
        message = conn.recv(1024).decode()  #received message
        if not message:
            break
        print('Message => {}'.format(message))
        
        message = input('-->')  #send message 

        conn.send(message.encode())

    conn.close()


if __name__ == '__main__':
    server_prorgam()