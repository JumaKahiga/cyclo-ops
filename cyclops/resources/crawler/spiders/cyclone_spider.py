"""
Cyclone spider
"""

import logging

from scrapy.spiders import Spider

logger = logging.getLogger(__name__)


class CycloneSpider(Spider):
    """Scrap cyclone data from NOAA Satelites and Information
    """

    name = 'cyclone_data'
    start_urls = [
        'https://rammb-data.cira.colostate.edu/tc_realtime/index.asp'
    ]
    custom_settings = {'ROBOTSTXT_OBEY': False}
    max_retries = 5

    def parse(self, response):
        base_url = 'https://rammb-data.cira.colostate.edu/tc_realtime/'
        storms = response.css('div.basin_storms')

        for storm in storms:
            basin = storm.css('h3::text').get()

            _storm_url = storm.css('li a::attr(href)').get()
            storm_url = base_url + _storm_url if _storm_url else None

            _img_url = storm.css('li a img::attr(src)').get()
            img_url = base_url + _img_url if _img_url else None

            _storm_identifier = storm.css('li a::text').get()
            _storm_identifier_ = _storm_identifier.rstrip(
            ) if _storm_identifier else None
            storm_identifier = ' '.join(
                _storm_identifier_.split()) if _storm_identifier_ else None

            basin_data = {
                'basin': basin,
                'storm_url': storm_url,
                'storm_identifier': storm_identifier,
                'img_url': img_url
            }

            yield basin_data
