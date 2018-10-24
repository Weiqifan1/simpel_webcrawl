import sys
import requests
import re
import time
import bs4
from tqdm import tqdm
# bs4 cheatsheet. http://akul.me/blog/2016/beautifulsoup-cheatsheet/


def my_chr2(list_ofNums, repeat, old_links = None):
    if old_links == None:
        old_links = []
        print("****Scraping started..." + str(repeat) + " generations****")
    if repeat > 0:
        new_list = []
        for item in tqdm(list_ofNums):
            if item not in old_links:
               new_list = new_list + _get_html_page(item) 
               old_links.append(item)
        new_list = list(set(new_list)) #removes duplicates
        return my_chr2(new_list, repeat-1, old_links)
    else:
        print("****Scraping finished****")
        return list_ofNums

def _get_html_page(url):
    try:
        response = requests.get(url)
        raw_list = _soup_link_list(response)
        return _remove_malformed_links(raw_list)
    except:
        return []

# Make a soup object with all links.
def _soup_link_list(response):
    soup = bs4.BeautifulSoup(response.text, 'html5lib') # html5lib er den parser vi bruger.
    links = soup.select("a[href]")
    list = []
    for a in links:
        text = a["href"]
        #print(text)
        list.append(text)
    return list


def _remove_malformed_links(all_links):
    velformed = []
    for item in all_links:
        validation_result = re.match(_url_regex, item) is not None
        if validation_result:
            velformed.append(item)
    return velformed


# url validation regex:
# https://stackoverflow.com/questions/7160737/python-how-to-validate-a-url-in-python-malformed-or-not
_url_regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

