#Created by Charles Dardaman
#12/03/2015
#This program will take the existing log file and rename it with the date.
#It will then zip the file using 7zip and move it onto a server on the network.

import os
import time
import shutil
import subprocess


#Variables
oldFileName = "SyslogCatchAll.txt"
newFileName = time.strftime("%Y%m%d") + "_" + oldFileName
zippedName = time.strftime("%Y%m%d") + "_" + "SyslogCatchAll.7z"
serverPath = "//server/"
filePath = "//file/"


#Renames the file
os.rename(filePath + oldFileName, filePath + newFileName)

#Zips the folder
subprocess.call(["C:/7za.exe", 'a', '-t7z', '-m0=lzma', '-mx=9', '-mfb=64', '-md=32m', '-ms=on', filePath + zippedName, filePath + newFileName])

#Moves the folder onto the server
shutil.move(filePath + zippedName, serverPath + zippedName)
