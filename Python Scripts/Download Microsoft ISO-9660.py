import urllib2
import re
import time

#Open first url
website = urllib2.urlopen("http://support.microsoft.com/en-us/kb/913086")

html = website.read()

#Gets all the links on the first page
links = re.findall('"((http)s?://.*?)"',html)

#Turns the links into a proper list
links = [x[0] for x in links]

smaller_list = []

#Sorts the links to get the correct ones
for x in xrange(0, len(links)):
	if "FamilyId=" in links[x]:
		smaller_list.append(links[x])
 
 #The first sorted link is the most recent
download_url = smaller_list[0]

#Microsoft blocks bots so this is needed to pretend to be a browser
request = urllib2.Request(download_url, headers={'User-Agent' : "Magic Browser"})

download_page = urllib2.urlopen(request)

html_download = download_page.read()

#Gets all of the links on the second page
download_links = re.findall('"((http)s?://.*?)"',html_download)

#Turns the links into a proper list
download_links = [x[0] for x in download_links]

#Sorts the links, the first link is once again the one we are looking for
for x in xrange(0,len(download_links)):
	if "details" in download_links[x]:
		print download_links[x]
		download_link = download_links[x]
		break
	
#Since I am unable to scrape the correct link I will scrape a link with the correct variables
#and then add in the word used in Microsoft's naming scheme		
download_link = download_link.replace("details", "confirmation")

#Loads up the 3 webpage
request_month_download = urllib2.Request(download_link, headers={'User-Agent' : "Magic Browser"})

month_download_page = urllib2.urlopen(request_month_download)

html_month_download = month_download_page.read()

#Gets all of the links of the third page
month_links = re.findall('"((http)s?://.*?)"',html_month_download)

#Turns the links into a proper list
month_links = [x[0] for x in month_links]

#Finds the ISO download link
for x in xrange(0,len(month_links)):
	if ".iso" in month_links[x]:
		print month_links[x]
		exact_link = month_links[x]
		break


#Downloads the link with a progress bar
url = exact_link

file_name = time.strftime("%m%Y") + " Security Release ISO Image.iso"
u = urllib2.urlopen(url)
f = open(file_name, 'wb')
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])
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