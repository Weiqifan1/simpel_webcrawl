import bs4
import os
import sys
import requests
import re
#import urllib2


def find_links():
    URL = 'https://en.wikipedia.org/wiki/Python_(programming_language)'

    response = requests.get(URL)
    # print(response.text)
# Exception hvis 404 eller brug if html_page.ok
# html_page.raise_for_status()

#links = []

    soup = bs4.BeautifulSoup(response.text, 'html5lib')
    # print(soup)

# <a href="(.*)".'?

    links = soup.select("a[href]")
    print(links)
    for a in links:
        text = a["href"]
        #regex = re.compile(r'<a href="(.*)".*?').findall(text)
        print(text)


find_links()
