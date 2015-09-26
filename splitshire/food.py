#!/usr/bin/env python

__author__ = 'tasdik'

import requests
import pprint                   ### for printing the dictionary in a readable form 
from bs4 import BeautifulSoup
import urllib2                  ### to check whether the link exits or not

dic = {}

url = "http://www.splitshire.com/category/food/page/"
i = 0  
while i <= 10: 
    new_url = url + str(i) + "/"
    plain_text = requests.get(new_url).text
    soup = BeautifulSoup(plain_text)

    for link in soup.findAll('div', {"class": "featured_img"}):
        img_link = link.find('a').find('img').get('src')
        img_description = link.find('a').find('img').get('alt')
        dic[img_description] = img_link

    i += 1
    
pprint.pprint(dic)