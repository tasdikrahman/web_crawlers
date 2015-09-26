#!/usr/bin/env python

__author__ = "Tasdik"

from bs4 import BeautifulSoup
import requests
import pprint


dic = {}
categories = []

url = "http://www.splitshire.com/"
plain_text = requests.get(url).text
soup = BeautifulSoup(plain_text, 'lxml')

## to find all the categories first 

###########################################################################
## found all the categories
for full in soup.findAll("div", {"class": "widget widget_categories"}):
	# print full.prettify()
	for li in full.find_all('li'):
		# print li.prettify()
		for a in li.find_all('a'):
			# print a.get("href")
			var = a.get("href")
			# print type(var)
			categories.append(var)
			# categories.append[a.get("href")]
###########################################################################


print 'printing the categories : \n'
## prints all the categories

for i in categories:
	print i

print '\n\nGetting all the links'

###########################################################################
## scraping all the categories by taking all the category links from the list "categories"

for category in categories:
	print 'Inside category : ' + category 
	print '\n\n'
	i = 0 
	while i <= 30:
		url = category + "/page/" + str(i) + "/"
		plain_text = requests.get(url).text

		soup = BeautifulSoup(plain_text)

		for link in soup.findAll('div', {"class": "featured_img"}):
			img_link = link.find('a').find('img').get('src')
			img_description = link.find('a').find('img').get('alt')
			dic[img_description] = img_link
			print img_description, dic[img_description]

		i += 1

	print '\n\n'
###########################################################################

print '\n\nPrinting the whole dictionary : \n\n'
print '###########################################################################'

pprint.pprint(dic)