__author__ = 'Charles'

import socket

#This is an echo server, it sends us back anything that we send to it
ip = "54.201.246.241"
port = 1338

s = socket.socket()

s.connect((ip,port))

#set time out for trial and error
s.settimeout(2)

#used to get past timeout exception
#after setting timeout it attempts to receive data, if it doesn't receive date then just continue anyways
try:
    print s.recv(1)
except socket.timeout:
    pass

#s.send("I wonder if this is all logged...\n")
s.send("\x08\x48\x61\x63\x6B\x0A")
#s.send("\x183981320912098312038123-01\x0a")

#Recieve data that was sent
received = s.recv(16)
print received.encode("hex")

input()

#close the socket when done
s.close()