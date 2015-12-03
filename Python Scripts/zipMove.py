#Created by Charles Dardaman
#12/03/2015
#This program will take the existing log file and rename it with the date.
#It will then zip the file using 7zip and move it onto a server on the network.

import os
import time
import shutil

print "Start"

#Variables
oldFileName = "SyslogCatchAll.txt"
newFileName = time.strftime("%Y%m%d") + "_" + oldFileName
zippedName = time.strftime("%Y%m%d") + "_" + SyslogCatchAll.7z
serverPath = "//server/"
filePath = "//file/"

print oldFileName
print newFileName
print zippedName
print serverPath
print filePath


#Renames the file
os.rename(filePath + oldFileName, filePath + newFileName)

#Zips the folder


#Moves the folder onto the server
shutil.move(filePath + zippedName, serverPath + zippedName)

print "End"