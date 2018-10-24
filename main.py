import bs4
import os
import sys
import requests
import re
import time
import bs4simple as bs

# godt link: https://www.digitalocean.com/community/tutorials/how-to-crawl-a-web-page-with-scrapy-and-python-3

# 'http://www.begravelseholbaek.dk/links.php'
#'https://en.wikipedia.org/wiki/Python_(programming_language)'


number_of_generations = 2

url = 'http://www.begravelseholbaek.dk/links.php'


start_time = time.time()

start_list = []
start_list.append(url)
print(len(bs.my_chr2(start_list, number_of_generations)))

elapsed_time = time.time() - start_time
pretty_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
print(pretty_time)