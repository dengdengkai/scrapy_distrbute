# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from datetime import datetime
class YouyuanPipeline(object):
    def __init__(self):
        self.lists = []
        self.filename = open("youyuan.json", "w")

    def process_item(self, item, spider):
        # ensure_ascii=False禁用Ascii码，采用unicode码
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        #self.lists.append(content.encode("utf-8"))
        #self.filename.write(self.lists)
        self.filename.write(content.encode("utf-8"))

        # 格林威治时间，距离中国 +8 时区
        item['time'] = datetime.utcnow()
        # 爬虫名
        item['spidername'] = spider.name

        return item
    def close_spider(self,spider):
        self.filename.close()
