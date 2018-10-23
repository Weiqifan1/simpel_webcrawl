import re
import bs4
import pprint
import requests
from tqdm import tqdm

print("hello")

def scrape_links(from_url, for_depth, all_links={}):
    # This is what the exercise below asks you to implement!
    pass


start_url = 'https://www.version2.dk/artikel/google-deepmind-vi-oeger-sikkerheden-mod-misbrug-sundhedsdata-1074452'

link_dict = scrape_links(from_url=start_url, for_depth=2)

def dump(a_dict):
    with open('./internet.py', 'w') as out_file:
        out_file.write('LINKS_DICT =' + pprint.pformat(a_dict))


def flatten(lst):
    import itertools
    return list(itertools.chain.from_iterable(lst))


def scrape_links(from_url, for_depth, all_links={}):

    if for_depth >= 1:
        print('Scraping level {}'.format(for_depth))
        
        if isinstance(from_url, list):
            if all_links:
                already_seen = list(all_links.keys())
                still_to_scrape = [l for l in from_url if not l in already_seen]
            else:
                still_to_scrape = from_url

        elif isinstance(from_url, str):
            if all_links:
                already_seen = list(all_links.keys())
                still_to_scrape = [l for l in [from_url] if not l in all_links.keys()]
            else:
                still_to_scrape = [from_url]

        edges_dict = scrape_links_of_pages(still_to_scrape)
        
        for_depth -= 1
        
        all_links.update(edges_dict)

        values = flatten(edges_dict.values())
        #dump(all_links)
        scrape_links(values, for_depth, all_links=all_links)
    else:
        print('Done')
        
    return all_links

start_url = 'https://www.version2.dk/artikel/google-deepmind-vi-oeger-sikkerheden-mod-misbrug-sundhedsdata-1074452'

link_dict = scrape_links(from_url=start_url, for_depth=2)

print('{} pages link to {} other pages'.format(len(list(link_dict.keys())), 
                                               len(flatten(link_dict.values()))))


