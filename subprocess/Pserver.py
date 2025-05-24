import socket
import threading
from subprocess import Popen, STDOUT, PIPE


def client_thread(conn,addr):
    
    print("Connected to : ",addr)
    message = "Welcome {}".format(addr)
    conn.send(message.encode())
    

    received_message = conn.recv(1024).decode()

    if received_message == 'exit':
        conn.close()
        return
    
    # p = Popen(['dir'],stdin=PIPE,stdout=PIPE,stderr=STDOUT,shell=True)
    # while p.poll() is None:
    #     conn.sendall(p.stdout.readline())


def start_server():
    host = ''
    port = 4444
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(4)
    print("Server Listening on Port 4444")
    
    while True:
        conn,addr = s.accept()
        assign_thread = threading.Thread(target=client_thread,args=(conn,addr,))
        assign_thread.start()


if __name__ == "__main__":
    start_server() 