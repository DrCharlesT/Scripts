import urllib2
import re
import hashlib

v5i32 = ""
v5i63 = ""
unix = ""

def main():	
	#Opens the website
	website = urllib2.urlopen("http://www.symantec.com/security_response/definitions/download/detail.jsp?gid=sep")

	#Gets the html of the website
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

	#Creates a list to be appended to
	file_names = []

	#Get the file name
	for x in xrange(0, len(downloads)):
		file_names.append(downloads[x].split('/')[-1])
		print file_names[x]

	#Calls the function to get the MD5s
	MD5_hashes = get_MD5(file_names)

	#Calls the function to download the files and get their filenames
	saved_file_names = download_files(downloads)

	#Gets the file's hashes
	file_MD5_hashes = get_file_MD5(saved_file_names)

	#Compares the MD5 hashes
	if compare_MD5(MD5_hashes,file_MD5_hashes):
		for x in xrange(0, len(file_MD5_hashes)):
			print MD5_hashes[x] + "   " + file_MD5_hashes[x]
	else:
		print "MD5 hashes failed"



def get_MD5(file_names):
	#Opens the website to the MD5-hash list
	website = urllib2.urlopen("http://www.symantec.com/avcenter/download/md5-hash.txt")

	#Runs through the website looking for the correct filename
	for line in website:
		#print line
		if file_names[0] in line:
			print line
			v5i32_hash = line[:32]
			print v5i32_hash
		if file_names[1] in line:
			print line
			v5i64_hash = line[:32]
			print v5i64_hash
		if file_names[2] in line:
			print line
			unix_hash = line[:32]
			print unix_hash
	#Creates a list the hold the hashes
	MD5_hashes = [v5i32_hash,v5i64_hash,unix_hash]

	#Returns a list of hashes
	return MD5_hashes	

def get_file_MD5(saved_file_names):
	file_MD5_hashes = []
	for x in xrange(0,len(saved_file_names)):
		#Opens the file and reads the data
		with open(saved_file_names[x], 'rb') as fh:
			m = hashlib.md5()
			while True:
				#Only reads a portion of the data at a time
				data = fh.read(8192)
				if not data:
					break
				m.update(data)
			#Adds the MD5 to a list of MD5s
			file_MD5_hashes.append(m.hexdigest())
			print m.hexdigest()
	#Returns the list of MD5 hashes
	return file_MD5_hashes

def compare_MD5(MD5_hashes,file_MD5_hashes):
	#Compares the MD5 hashes, They will be in the same order
	if MD5_hashes == file_MD5_hashes:
		return True
	else:
		return False
	print MD5_hashes
	print file_MD5_hashes	


def download_files(downloads):		
	saved_file_names = []
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

		#Closes the file
		f.close()

		#Saves all of the file names, this is mainly used if the filename is changed
		saved_file_names.append(file_name)
	
	#Returns the filenames so they can be verified
	return saved_file_names

#Starts the Program
main()