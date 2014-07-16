#!/usr/bin/env python

import urllib2
import lxml.html
import re

url = "http://facebook.com/nytimes/posts/10150428621164999"

def http_download(url):
    try:
        request = urllib2.Request(url)
        return urllib2.urlopen(request).read()
    except urllib2.HTTPError, e:
        exit()
    except urllib2.URLError, e:
        exit()

def main():
    html_page = http_download(url)
    xpath_data = lxml.html.fromstring(html_page).xpath("//div[@class='_6ks']")
    print html_page
    print xpath_data, len(xpath_data)
    for i in xpath_data:
        print lxml.html.tostring(i)

if __name__ == "__main__":
    main()
