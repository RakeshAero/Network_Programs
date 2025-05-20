import socket
import threading

def processThread(s):
    return True


def connection():
    host = '127.0.0.1'
    port = 4444
    while True:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((host,port))
        s.listen(4)

        conn,addr = s.accept()
        client_server = threading.Thread(target=processThread,args=(conn,))