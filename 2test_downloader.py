#!/usr/bin/env python

import urllib2
from BeautifulSoup import BeautifulSoup

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
    soup = BeautifulSoup(html_page)
    for div in soup.findAll('div', attrs={'class="_6ks"'}):
        print div

if __name__ == "__main__":
    main()
