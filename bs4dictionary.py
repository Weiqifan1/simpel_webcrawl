import sys
import requests
import re
import time
import bs4
from tqdm import tqdm
import dictlist as dl
# bs4 cheatsheet. http://akul.me/blog/2016/beautifulsoup-cheatsheet/


def create_dictlist(list_ofNums, repeat, old_links = None):
    if old_links == None:
        old_links = dl.Dictlist()#[]
        list_ofNums = dl.Dictlist(list_ofNums)
        print("****Scraping started..." + str(repeat) + " generations****")
    if repeat > 0:
        new_list = dl.Dictlist()#[]
        new_list.pub_dict = list_ofNums.pub_dict
        for item in tqdm(list_ofNums.pub_list):
            if item not in old_links.pub_list:
                new_list.append_item(item)
                #nyt forsoeg:
                                    #funktion der fjerne non-wordpress
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


########################################################## remove non wordpress -- start
#2018-10-26 - fjerner vlaues der ikke starter med https://progtest591184608.wordpress.com/page
#replace:   new_list.append_list(item, remove_startswith(_get_html_page(item)))
#with:      new_list.append_list(item, _get_html_page(item))

def remove_startswithDict(mydict):
    newdict = {}
    unwant = "https://progtest591184608.wordpress.com/page"
    key_list = []
    for key, value in mydict.items():
        key_list.append(key)
        #print(key_list)
    for key in key_list:
        value_set = mydict[key]
        new_set = []
        for mylink in value_set:
            if mylink.startswith(unwant):
                new_set.append(mylink)
        newdict[key] = new_set
    return newdict

def remove_startswith(listOfLinks):
    unwant = "https://progtest591184608.wordpress.com/page"
    new_list = []
    for item in listOfLinks:
        if item.startswith(unwant):
            new_list.append(item)
    return new_list

######################################################remove non wordpress -- end

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



number_of_generations = 2

url = 'http://www.begravelseholbaek.dk/links.php'

#start_list = []
#start_list.append(url)
#print(len(my_chr2(start_list, number_of_generations)))

#print(_get_html_page(url))

#response = requests.get(url)
#print(response)