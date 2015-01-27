__author__ = 'Charles'

#This imports a socket in order to connect to a remote host
#socket could be renamed using "import socket as test" this means you would use test.x instead of socket.x
import socket

#this is the location of the remote host and service
ip = "54.201.246.241"
port = 1337

#socket is related the the import, socket is an object
#From the library socket give us a socket
s = socket.socket()

#use socket to make the connecton
s.connect((ip,port))

#This prints out remote data, 1 stands for 1 byte of data
print s.recv(11)

input()

#close the socket when done
s.close()