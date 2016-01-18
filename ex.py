import urllib2
import xml.etree.ElementTree as ET

def get_languages():
    '''
    return a dict with all awailable languages and with urls to rss
    '''
    page_url = 'http://www.ex.ua/rss/81708'
    items = dict()
    try:
        page = urllib2.urlopen(page_url)
        string = ''.join(page.readlines())
        root = ET.fromstring(string)
        all_items = root[0].findall('item')
        for x in all_items:
            items[x[0].text] = 'http://www.ex.ua/rss/{0}'.format(x[4].text)
    except Exception, e:
        pass
    return items