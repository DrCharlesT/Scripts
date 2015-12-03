#Created by Charles Dardaman
#12/03/2015
#This program will take the existing log file and rename it with the date.
#It will then zip the file using 7zip and move it onto a server on the network.

import os
import time

print "Start"

#Variables
oldFileName = "SyslogCatchAll.txt"
newFileName = time.strftime("%Y%m%d") + "_" + oldFileName
serverPath = "//server/"
filePath = "//file/"

print newFileName
print serverPath
print filePath

#Renames the file
os.rename(filePath + oldFileName, filePath + newFileName)


print "End"