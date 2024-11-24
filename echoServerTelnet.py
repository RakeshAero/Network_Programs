import socket

host = ""
port=4444


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #AF_NET = IPv4 , SOCK_STREAM = TCP
s.bind((host,port))
s.listen()
print("Echo Server Started Listening on PORT 4444")

conn,addr = s.accept()
print("Connected with IP : {} , PORT : {}".format(addr[0],addr[1]))
conn.sendall("Welcome to the Simple Echo chat Server: Type='q' to Exit\r\n".encode())


string = ""
while True:
    data = conn.recv(2048)
    data = data.decode()
    if not data:
        break
   
    else:
        for char in data:
            if char == "\b":  #checking for backspace
                if(len(string) > 0):
                    string = string[:-1] #remove 1 char 
                    conn.sendall(" \b".encode()) #replace or overwirte that character with space
            else:
                string += char
        

        if "\n" in string:
            fullmessage = string.strip()
            print("Echo > {}".format(fullmessage))
            if fullmessage == "q":
                break
            else:
                conn.sendall((fullmessage + "\r\n").encode())
                #TODO: To Build a Chat server between telnet 
            string = ""

s.close()


