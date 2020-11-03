import os

from redis import Redis
from rq import Queue

from cyclops.resources.crawler.spiders.cyclone_spider import CycloneSpider

queue = Queue(connection=Redis(host=os.getenv('REDIS_HOST', '127.0.0.1')))

job = queue.enqueue(CycloneSpider.parse)
