#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import xml.etree.ElementTree as Et

from bs4 import BeautifulSoup as Bs

try:
    import xbmcplugin
    VIDEOS_PER_PAGE = xbmcplugin.getSetting("videos_per_page")
    IMAGE_QUALITY = xbmcplugin.getSetting("image_quality")
except ImportError:
    VIDEOS_PER_PAGE = 200
    IMAGE_QUALITY = 400


def get_languages():
    """
    return: dict with all available languages and with urls to rss
    """
    page_url = 'http://www.ex.ua/rss/81708'
    items = dict()
    try:
        page = urllib2.urlopen(page_url)
        string = ''.join(page.readlines())
        root = Et.fromstring(string)
        all_items = root[0].findall('item')
        for item in all_items:
            # str like 'Відео [UA - українська]'
            title = item.find('title').text.encode('utf-8')
            index = title.index('[') + 1
            lang_code = title[index:index + 2]  # short repr like 'UA'
            url = 'http://www.ex.ua/rss/{0}'.format(item.find('guid').text)
            items[lang_code] = url
    except urllib2.URLError:
        print("Check you internet")
    except Exception, e:
        raise e
    return items


def list_languages():
    return get_languages().keys()


def get_categories(lang):
    """
    :param lang: language code
    return: dict like {'category': 'url_for_videos'}
    """
    langs = get_languages()
    page_url = langs[lang]
    items = dict()
    try:
        page = urllib2.urlopen(page_url)
        string = ''.join(page.readlines())
        root = Et.fromstring(string)
        all_items = root[0].findall('item')
        for item in all_items:
            # link w/o parameters
            text = '{0}'.format(item.find('link').text)
            items[item.find('title').text.encode('utf-8')] = text[0:text.index('?')]
    except urllib2.URLError:
        print("Check you internet")
    except Exception, e:
        raise e
    return items


def list_categories(lang):
    return get_categories(lang).keys()


def list_videos(url, videos_per_page=VIDEOS_PER_PAGE, page=0):
    """
    :param page: number of page for paginator
    :param videos_per_page: from Setting
    :param url: url from get_categories
    """
    video_detail = {"title": "",
                    "img": "",
                    "id": "",
                    "playlist": ""}
    path = '{0}?per={1}&p={2}'.format(url, videos_per_page, page)
    videos = []
    try:
        page = urllib2.urlopen(path)
        if page.code != 200:
            raise Exception
        soup = Bs(page.read(), 'html.parser')
        results = soup.findAll("td", {"valign": "center", "align": "center"})

        for video in results:
            if video.img:
                video_detail['title'] = video.img['alt']
                # url w/o quality factor
                video_detail['img'] = video.img['src'][0:len(video.img['src']) - 4]
                # strip for id
                video_detail['id'] = video.a['href'][1:video.a['href'].index('?')]
                video_detail['playlist'] = 'http://www.ex.ua/playlist/{0}.xspf'.format(video_detail['id'])
                videos.append(video_detail)
            else:
                continue
    except urllib2.URLError:
        print("Check you internet")
    except Exception, e:
        raise e
    return videos
