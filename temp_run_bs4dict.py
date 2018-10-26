import bs4
import os
import sys
import requests
import re
import time
import bs4dictionary as bs
import dictlist as dl

def run():
    #mulige hjemmesider (men mange links:)
    #'https://en.wikipedia.org/wiki/Python_(programming_language)'
    # 'https://progtest591184608.wordpress.com/page-1-first-generation-link/'

    number_of_generations = 2

    #2018-10-25: chr: jeg har forsoegt at lave en wordpress side med få links:
    url = 'https://progtest591184608.wordpress.com/page-1-first-generation-link/'

    start_time = time.time()

    start_list = []
    start_list.append(url)
    scrape_result = bs.create_dictlist(start_list, number_of_generations)
    #print(scrape_result.pub_dict)

    
    print("total number of links: " + str(len(scrape_result.pub_list)))
    print("number of unique links: " + str(len(list(set(scrape_result.pub_list)))))
    key_list = []
    value_list = []
    item_list = []
    for key, value in scrape_result.pub_dict.items():
        key_list.append(key)
        item_list.append(key)
        for thing in value:
            item_list.append(thing)
            value_list.append(thing)
    print("number of unique dict keys: " + str(len(list(set(key_list)))))
    print("number of unique dict values: " + str(len(list(set(value_list)))))
    print("number of unique items in dict: " + str(len(list(set(item_list)))))
    

    elapsed_time = time.time() - start_time
    pretty_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
    print(pretty_time)

    print(scrape_result.pub_dict)

    #generations resultater med siden: # 'https://progtest591184608.wordpress.com/page-1-first-generation-link/'
    #gammel version (kun lister, ingen dictionary)
    #1 8 68 1392
    # ny version med dictionary: (muligvis forkert):
    # 1 9 71 1412/1413