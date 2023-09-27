import socket

BYTES_TO_READ = 4096

def get(host, port):
    request = b"GET / HTTP/1.1\nHost: " + host.encode('utf-8') + b"\n\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #this line initializes a socket
    s.connect((host,port)) #this connects to google
    s.send(request) #this requessts google homepage
    s.shutdown(socket.SHUT_WR) #this states that I'm done sending the request
    result = s.recv(BYTES_TO_READ) #continuously receiving the responce
    while(len(result)>0):
        print(result)
        result = s.recv(BYTES_TO_READ)

    s.close() #this is to close the socket
    

get("www.google.com", 80)
