import sys
import requests
import re
import time
import bs4
from tqdm import tqdm
import dictlist as dl


def create_dictlist(list_ofNums, repeat, old_links = None):
    if old_links == None:
        old_links = dl.Dictlist()
        list_ofNums = dl.Dictlist(list_ofNums)
        print("****Scraping started..." + str(repeat) + " generations****")
    if repeat > 0:
        new_list = dl.Dictlist()
        new_list.pub_dict = list_ofNums.pub_dict
        for item in tqdm(list_ofNums.pub_list):
            if item not in old_links.pub_list:
                new_list.append_item(item)

                list_of_all_children = remove_startswith(_get_html_page(item))

                temp_child = []
                for thing in list_of_all_children:
                    if thing not in old_links.pub_list:
                          temp_child.append(thing)                       
                new_list.append_list(item, temp_child)
                #end of forsoeg:
                old_links.append_item(item)
        new_list.pub_list = list(set(new_list.pub_list))
        return create_dictlist(new_list, repeat-1, old_links)
    else:
        print("****Scraping finished****")
        return list_ofNums


def remove_startswith(listOfLinks):
    unwant = "https://progtest591184608.wordpress.com/page"
    new_list = []
    for item in listOfLinks:
        if item.startswith(unwant):
            new_list.append(item)
    return new_list


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
