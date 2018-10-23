import bs4
import os
import sys
import requests
import re

# bs4 cheatsheet. http://akul.me/blog/2016/beautifulsoup-cheatsheet/


def get_html_page(url):

    try:
        if url.startswith('https://'):
            response = requests.get(url)
        else:
            new_url = 'https:' + url
            response = requests.get(new_url)
    
        # Exception hvis 404 eller brug if response.ok
        response.raise_for_status()

        # If no error make soup object with links.
        soup_link_list(response)
    except:
        # Handle bad links.
        print('fsfsf')


# Make a soup object with all links.
def soup_link_list(response):
    soup = bs4.BeautifulSoup(response.text, 'html5lib') # html5lib er den parser vi bruger.

    all_a_tags = soup.select("a[href]")
    #print(all_a_tags)
    for a in all_a_tags:
        links = a["href"]
        #regex = re.compile(r'<a href="(.*)".*?').findall(text)
        print(links)
        
    print('END')
    for url in links:
        get_html_page(url)




url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
get_html_page(url)
