# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @Date:   2016-04-02 21:34:01
# @Last Modified by:   Tasdik Rahman
# @Last Modified time: 2016-04-02 21:42:18

import urllib.request
from urllib.error import URLError, HTTPError

def request_page(url):
    """
    returns the scraped HTML content
    """
    try:
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
        return None
    except URLError as e:
        print('Failed to reach the server.')
        print('Reason: ', e.reason)
        return None
    else:
        # if eveything is good till here, return the HTML
        return response.read().decode('utf-8')
