#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, unittest
sys.path.append(os.path.join(os.path.dirname(__file__), "resources/lib"))
import ex

LANGUAGE = 'EN'
LANGUAGE_URL = 'http://www.ex.ua/rss/80925'
CATEGORY = 'Movies'
CATEGORY_URL = 'http://www.ex.ua/82316'
URL='http://www.ex.ua/ru/video/foreign_series?r=23775'

class ExParsingTest(unittest.TestCase):
    def test_list_languages(self):
        langs = ex.list_languages()
        self.assertTrue(len(langs)>0)
    
    def test_get_languages(self):
        langs = ex.get_languages()
        self.assertTrue(LANGUAGE in langs)

    def test_get_categories(self):
        categories = ex.get_categories(LANGUAGE)
        self.assertEqual(categories[CATEGORY], CATEGORY_URL)
    
    def test_list_categories(self):
        categories = ex.list_categories(LANGUAGE)
        self.assertTrue(len(categories) > 0)

    def test_list_video(self):
        videos = ex.list_videos(URL, ex.VIDEOS_PER_PAGE)
        self.assertTrue(len(videos) > 0)

if __name__ == '__main__':
    unittest.main()