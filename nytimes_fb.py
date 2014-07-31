#!/usr/bin/env python

import urllib, urllib2
import re
import HTMLParser

def http_download(url):
    try:
        request = urllib2.Request(url)
        return urllib2.urlopen(request).read()
    except urllib2.HTTPError, e:
        exit()
    except urllib2.URLError, e:
        exit()

def unescape_url(url_str):
    return re.sub(r"\\\\/", "/", url_str)

def decode_unicode_url(url_str):
    return decode_quoted_url(re.sub(r"\\\\(u[0-9A-F]{6})", r"\\\1", url_str).decode('unicode-escape'))

def decode_quoted_url(url_str):
    return urllib.unquote(url_str)

def extract_shortened_urls(url):
    html_page = http_download(url)
    escaped_seq = re.compile(r"^https?:(\\{2}/){2}nyti\.ms\\{2}/[a-zA-Z0-9]+$")
    unicode_seq = re.compile(r"^https?\\{2}u00253A(\\{2}u00252F){2}nyti\.ms\\{2}u00252F[a-zA-Z0-9]+$")
    url_encoded_seq = re.compile(r"^https?%3A%2F%2Fnyti.ms%2F[a-zA-Z0-9]+$")
    clean_url_seq = re.compile(r"^https?://nyti.ms/[a-zA-Z0-9]+$")
    parser = HTMLParser.HTMLParser()
    url_list = {}

    for element in re.findall("https?.{,30}nyti\.ms[/a-zA-Z0-9\\%]+", html_page):
        if escaped_seq.match(element):
            target_url = unescape_url(element)
        elif unicode_seq.match(element):
            target_url = decode_unicode_url(element)
        elif url_encoded_seq.match(element):
            target_url = decode_quoted_url(element)
        elif clean_url_seq.match(element):
            target_url = element
        else:
            print element + "$"
            raise Exception("Invalid match")

        if target_url not in url_list:
            url_list[target_url] = True
    return url_list

def apply_transform(url_list):
    for target_url in url_list:
        print target_url

def main():
    url_list = extract_shortened_urls("http://facebook.com/nytimes/")
    apply_transform(url_list)

if __name__ == "__main__":
    main()
