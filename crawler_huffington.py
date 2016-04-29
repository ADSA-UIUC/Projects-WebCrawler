import urllib2
from bs4 import BeautifulSoup
for i in range(2016, 2017):
	for j in range(3, 4):
		for x in range(1, 30):
			req_url = urllib2.urlopen("http://www.huffingtonpost.com/archive/" + str(i) + "-" + str(j) + "-" + str(x))
			html_data = None
			#with urllib2.urlopen(req_url) as html:
			#	html_data = html.read()
			soup = BeautifulSoup(req_url)
			links = []
			for link in soup.find_all('a'):
					links.append(link.get('href'))
					#print(link.get("href"))
			file = open("link_file_huffington",'a')
			huff_link = "http://www.huffingtonpost.com/"
			archive = "/article"
			for i in links:
				if huff_link in i and archive not in i:
					file.write(i + '\n')
			file.close()
#file.close()
print("done")