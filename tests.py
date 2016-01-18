#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import ex

LANGUAGE = 'EN'
LANGUAGE_URL = 'http://www.ex.ua/rss/80925'
CATEGORY = 'Movies'
CATEGORY_URL = 'http://www.ex.ua/rss/82316'

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


if __name__ == '__main__':
    unittest.main()