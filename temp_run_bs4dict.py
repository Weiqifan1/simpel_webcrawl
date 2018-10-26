import bs4
import os
import sys
import requests
import re
import time
import pickle
import bs4dictionary as bs
import dictlist as dl

def run():
    #mulige hjemmesider (men mange links:)
    #'https://en.wikipedia.org/wiki/Python_(programming_language)'
    #2018-10-25: chr: jeg har forsoegt at lave en wordpress side med få links:
    # 'https://progtest591184608.wordpress.com/page-1-first-generation-link/'

    number_of_generations = 2
    url = 'https://progtest591184608.wordpress.com/page-1-first-generation-link/'

    start_time = time.time()

    # lav et objekt (scrape_result) der holder en dictionary med de scrapede links:
    start_list = []
    start_list.append(url)
    scrape_result = bs.create_dictlist(start_list, number_of_generations)
    
    #tag vores dictionary (scrape_result.pub_dict), og serilizer til filen 'links_serialized':
    filename = 'links_serialized'
    outfile = open(filename, 'wb')
    pickle.dump(scrape_result.pub_dict, outfile)
    outfile.close()
    
    #læs den serialiserede fil ind igen som en dictionary 
    # (vi serialiserede bare fordi vi kan (og skal lære det))
    infile = open(filename,'rb')
    deserial_dict = pickle.load(infile)
    infile.close()
    print(deserial_dict == scrape_result.pub_dict) # skal gerne være true

    

    elapsed_time = time.time() - start_time
    pretty_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
    print(pretty_time)




'''
# 2018-10-26 Koden laver den oenskede dictionary, men er grim, serialisere ikke og tegner ikke en graf
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
'''