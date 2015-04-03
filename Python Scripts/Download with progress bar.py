import urllib2

#URL of the file to download
url = "http://download.microsoft.com/download/D/A/B/DABCD424-C549-4B0A-ADCC-F080C4537A50/Windows-KB913086-201503.iso"

#Nameing convention
file_name = url.split('/')[-1]
#Opens the link
u = urllib2.urlopen(url)
#Creates the file
f = open(file_name, 'wb')
#Gets info on the file
meta = u.info()
#Gets the filesize from the metadata
file_size = int(meta.getheaders("Content-Length")[0])
#Prints information for user
print "Downloading: %s Bytes: %s" % (file_name, file_size)

file_size_dl = 0
block_sz = 8192
#Writes to the file 
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    #Updates information for user
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print status,

f.close()