#!/usr/bin/env python

import urllib2
import re
import HTMLParser

url = "http://facebook.com/nytimes/posts/10150428621164999"

def http_download(url):
    try:
        request = urllib2.Request(url)
        return urllib2.urlopen(request).read()
    except urllib2.HTTPError, e:
        exit()
    except urllib2.URLError, e:
        exit()

def unescape_url(url_str):
    return re.sub(r"\\", "", url_str)

#def decode_unicode_url(url_str):
#    return 

def main():
    html_page = http_download(url)
    escaped_seq = re.compile(r"^https?:(\\{2}/){2}nyti\.ms\\{2}/[a-zA-Z0-9]+$")
    unicode_seq = re.compile(r"^https?\\{2}u00253A(\\{2}u00252F){2}nyti\.ms\\{2}u00252F[a-zA-Z0-9]+$")
    url_encoded_seq = re.compile(r"^https?%3A%2F%2Fnyti.ms%2F[a-zA-Z0-9]+$")
    parser = HTMLParser.HTMLParser()

    for element in re.findall("https?.{,30}nyti\.ms[^&]*(?=&)", html_page):
        if escaped_seq.match(element):
            print "ESCAPED: " + unescape_url(element)
        elif unicode_seq.match(element):
            print "UNICODE: " + element
        elif url_encoded_seq.match(element):
            print "URL ENCODED: " + parser.unescape(element)
        else:
            raise Exception("Invalid match")

if __name__ == "__main__":
    main()
