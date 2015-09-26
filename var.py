#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
mylist=[]
fw = open("viooz.txt","a")
html_text = requests.get("http://viooz.ac/genre/")
plain_text = html_text.text
soup = BeautifulSoup(plain_text,'lxml')
for i in soup.find_all('td'):
	info = i.find('a').get('href')
	mylist.append("www.viooz.ac"+info+"page/")
		
print mylist