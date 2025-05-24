import socket

def client_program():
    host = "127.0.0.1"
    port = 4444
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #IPv4,TCP
    s.connect((host,port))  #Connect to Host through Port
    print('Connected to Server : \n')

    message = input('--->') #send Message

    while message.lower().strip() != 'exit': 

        s.send(message.encode()) #--> Message sent

        data = s.recv(1024).decode() #--> Recieved Message

        if not data:
            print('No data received')
            break

        print('Received Message => {}'.format(data)) #--> Display Recieved Message

        message = input('--->') #-->Again send Message
    s.send(message.encode())
    s.close()

if __name__ == '__main__':
    client_program()
        