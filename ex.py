#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import xml.etree.ElementTree as ET

def get_languages():
    '''
    return: dict with all awailable languages and with urls to rss
    '''
    page_url = 'http://www.ex.ua/rss/81708'
    items = dict()
    try:
        page = urllib2.urlopen(page_url)
        string = ''.join(page.readlines())
        root = ET.fromstring(string)
        all_items = root[0].findall('item')
        for item in all_items:
            # str like 'Відео [UA - українська]'
            title = item.find('title').text.encode('utf-8')
            index = title.index('[')+1
            lang_code = title[index:index+2] # short repr like 'UA'
            url = 'http://www.ex.ua/rss/{0}'.format(item.find('guid').text)
            items[lang_code] = url
    except Exception, e:
        pass
    return items

def list_languages():
    return get_languages().keys()

def get_categories(lang):
    '''
    input: language code
    return: dict like {'category': 'url_for_videos'}

    '''
    langs = get_languages()
    page_url = langs[lang]
    items = dict()
    try:
        page = urllib2.urlopen(page_url)
        string = ''.join(page.readlines())
        root = ET.fromstring(string)
        all_items = root[0].findall('item')
        for item in all_items:
            items[item.find('title').text.encode('utf-8')] = 'http://www.ex.ua/rss/{0}'.format(item.find('guid').text)
    except Exception, e:
        pass
    return items

def list_categories(lang):
    return get_categories(lang).keys()