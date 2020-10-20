import unittest

from scrapy.http import Request, TextResponse
from scrapy.utils.test import get_crawler

from cyclops.resources.crawler.spiders.cyclone_spider import CycloneSpider


class TestCycloneSpider(unittest.TestCase):
    """Test CycloneSpider. """

    def setUp(self):
        settings = {}
        crawler = get_crawler(CycloneSpider, settings_dict=settings)
        self.spider = crawler._create_spider(
            custom_settings={'ROBOTSTXT_OBEY': False})

    @unittest.skip("skip until deferred testcase is implemented")
    def test_parse_method(self):
        headers = {'User-Agent': 'cyclone-project (+http://www.twitter.com)'}

        request = Request(
            url='https://rammb-data.cira.colostate.edu/tc_realtime/index.asp',
            headers=headers)

        response = TextResponse(url=request.url, request=request)
        data = yield self.spider.parse(response)

        item = dict(list(data).pop())
        self.assertEqual(item['basin'], 'test')
