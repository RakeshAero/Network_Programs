import socket

host = ""
port=4444


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen()
print("Echo Server Started Listening on PORT 4444")

conn,addr = s.accept()
print("Connected with IP : {} , PORT : {}".format(addr[0],addr[1]))
conn.sendall("Welcome to the Simple Echo chat Server\r\n".encode())


string = ""
while True:
    data = conn.recv(2048)
    data = data.decode()
    # data = data.strip()
    if not data:
        break
   
    string += data

    if "\n" in string:
        fullmessage = string.strip()
        print("Echo > {}".format(fullmessage))
        if fullmessage == "q":
            break
        else:
            conn.sendall((fullmessage + "\r\n").encode())
        string = ""

s.close()


