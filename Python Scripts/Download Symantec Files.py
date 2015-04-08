import urllib2
import re

v5i32 = ""
v5i63 = ""
unix = ""

def main():	
	#Opens the website
	website = urllib2.urlopen("http://www.symantec.com/security_response/definitions/download/detail.jsp?gid=sep")

	html = website.read()

	#Finds all of the HTTP links on the page
	all_links = re.findall('"((http)s?://.*?)"',html)

	#print all_links

	#print "------------------------------------------------------------"

	#Makes a list of just the information that is needed from the list of truples
	list_of_links = [x[0] for x in all_links]

	#Finds the 3 links that are wanted
	for x in xrange(0,len(list_of_links)):
		if "v5i32" in list_of_links[x]:
			v5i32 = list_of_links[x]
			print list_of_links[x]
		if "v5i64" in list_of_links[x]:
			v5i64 = list_of_links[x]
			print list_of_links[x]
		if "-unix" in list_of_links[x]:
			unix = list_of_links[x]
			print list_of_links[x]
		#print x
		
		x+=1	

	#Puts the 3 links into a list to be easily used in a loop
	downloads = [v5i32,v5i64,unix]

	#Calls the function to download the files
	#download_files(downloads)

def download_files(downloads):		
	for x in xrange(0,len(downloads)):	
		#Gets the correct download link
		url = downloads[x]

		#Makes a file name
		file_name = url.split('/')[-1]
		u = urllib2.urlopen(url)
		f = open(file_name, 'wb')
		meta = u.info()
		file_size = int(meta.getheaders("Content-Length")[0])

		#Shows downloading progress
		print "Downloading: %s Bytes: %s" % (file_name, file_size)

		file_size_dl = 0
		block_sz = 8192
		while True:
		    buffer = u.read(block_sz)
		    if not buffer:
		        break

		    file_size_dl += len(buffer)
		    f.write(buffer)
		    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
		    status = status + chr(8)*(len(status)+1)
		    print status,

		f.close()

main()