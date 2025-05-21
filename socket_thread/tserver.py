import socket
import threading

def thread_program(conn,addr):

    print("Connected to : ",addr)
    message = "Request in Progress please wait"
    conn.send(message.encode())

    # while message.lower().strip() != "exit":
    for i in range(4):
        conn.send(message.encode())
        data = conn.recv(1024).decode()
        if not data:
            print("No messages Received")
    
        print("Client => ",data)
        # message = input("Server => ")
    conn.close()



def server_program():
    host = '127.0.0.1'
    port = 4444
   
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(4)

    print("Server Listening on Port => {}".format(port))

    while True:
        conn,addr = s.accept()
        client_server = threading.Thread(target=thread_program,args=(conn,addr,))
        client_server.start()


if __name__ == "__main__":
    server_program()