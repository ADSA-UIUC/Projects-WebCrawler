import urllib.request
import urllib.response

from bs4 import BeautifulSoup

# Collect all the links of the articles in the year of 2016 till 3/10/2016 on Wired.com

for i in range(1,185):

    req_url = urllib.request.Request("http://www.wired.com/2016/page/"+str(i))
    html_data = None

    print("Page: ",i)

    with urllib.request.urlopen(req_url) as html:
        html_data = html.read()

    soup = BeautifulSoup(html_data, 'html.parser')

    links = []

    for link in soup.find_all("div", class_="article-group"):
        for l in link.find_all('a'):
            links.append(l.get('href'))

    file = open("link_file_wired", 'a')

    page = "/page"
    for i in links:
        if page not in str(i):
            file.write(i+ "\n")


file.close()