#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @Date:   2016-03-31
# @Last Modified by:   Tasdik Rahman
# @Last Modified time: 2016-04-02 21:42:24
# @GPLv3 License
# @http://tasdikrahman.me
# @https://github.com/prodicus

"""
gets the list of top 70 restaurants in and around bangalore by scraping the
data off http://burrp.com
"""

import json
import copy
import os

from bs4 import BeautifulSoup

from utils import request_page

BASE_URL = "http://burrp.com"
BASE_BANGALORE = "{0}/{1}".format(BASE_URL, "bangalore")
SEED_URL = "http://www.burrp.com/bangalore/best/restaurants/{0}"
HOTEL_LISTING_PAGES = [SEED_URL.format(i) for i in range(1, 70)]
HOTEL_LISTING_PAGES.insert(0,
                           "http://www.burrp.com/bangalore/best/restaurants")
"""
>>> pprint.pprint(HOTEL_LISTING_PAGES)
['http://www.burrp.com/bangalore/best/restaurants',
 'http://www.burrp.com/bangalore/best/restaurants/1',
 'http://www.burrp.com/bangalore/best/restaurants/2',
  ....
 'http://www.burrp.com/bangalore/best/restaurants/40']
"""

FILE = os.path.join("data","hotel_info_list.json")

# each page in "HOTEL_LISTING_PAGES" has about 10 hotels listed in it


def get_hotel_links_from_listing(soup):
    """
    writes json info retrieved from a page lets say
    'http://www.burrp.com/bangalore/best/restaurants/1'
    """
    listing_content = soup.find("ul", {"id": "listing_content"})
    li_list = listing_content.find_all("li")

    hotels_info_dict = {}

    for li in li_list:
        # the first hotel in the page
        hotel_link = li.find("div", {"class": "list_lft_1"}).a['href']

        hotel_link = "{0}{1}".format(BASE_URL, hotel_link)

        hotel_url_title = hotel_link.split("/")[-2]

        hotel_id = int(hotel_link.split("/")[-1])

        hotel_menu_link = "{base}/{name}/menu/{id}".format(
            base=BASE_BANGALORE,
            name=hotel_url_title,
            id=hotel_id
        )

        hotel_reviews_link = "{base}/{name}/reviews/{id}".format(
            base=BASE_BANGALORE,
            name=hotel_url_title,
            id=hotel_id
        )

        hotel_title = \
            li.find("div", {"class": "list_lft_1"}).a['title'].lower()
        try:
            cuisines = [
                x.strip() for x in li.find("div", {"class": "list_top_txt"}).get_text().split(",")
            ]
        except AttributeError:
            cuisines = None

        try:
            address = \
                li.find("div", {"class": "btn_lft_cont"}).p.get_text().lower()
        except AttributeError:
            address = None

        try:
            total_rating = \
                float(li.find("div", {"class": "list_star"}).get_text())
        except AttributeError:
            total_rating = None

        try:
            total_ratings_given = \
                int(li.find(
                    "div", {"class": "list_rat"}).get_text().split()[0])
        except AttributeError:
            total_ratings_given = None

        try:
            meal_for_2 = float(
                li.find("div", {"class": "meal2"}).span.get_text())
        except AttributeError:
            meal_for_2 = None

        # building up the dict file
        hotels_info_dict = {
            "hotel_id": hotel_id,
            "hotel_url_title": hotel_url_title,
            "hotel_menu_link": hotel_menu_link,
            "hotel_reviews_link": hotel_reviews_link,
            "hotel_info": [
                {
                    "meal_for_2": meal_for_2,
                    "hotel_link": hotel_link,
                    "hotel_title": hotel_title,
                    "hotel_address": address,
                    "cuisines": cuisines
                }
            ],
            "rating": [
                {
                    "total_rating": total_rating,
                    "total_ratings_given": total_ratings_given
                }
            ]
        }

        # print(json.dumps(hotels_info_dict))
        return hotels_info_dict


def scrape():
    json_list = []
    for listing_page in HOTEL_LISTING_PAGES:
        html = request_page(listing_page)
        if html:
            # if any html was returned by the method request_page()
            soup = BeautifulSoup(html, 'lxml')
            json_list.append(
                copy.copy(get_hotel_links_from_listing(soup))
            )

    with open(FILE, 'w') as f:
        f.write(json.dumps(json_list))


def main():
    scrape()

if __name__ == "__main__":
    main()
