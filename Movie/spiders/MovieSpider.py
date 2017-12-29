# -*- coding: utf-8 -*-

import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from Movie.items import MovieInfoItem
from scrapy.shell import inspect_response
from scrapy import shell

class MovieSpider(CrawlSpider):

    name = "douban_movie"
    allowed_domains = ["douban.com"]
    start_urls = ["https://movie.douban.com/tag/?icn=index-nav"]
    rules = {

        Rule(LinkExtractor(allow='/tag/', restrict_xpaths="//div[@class='article']"), follow=True),
        Rule(LinkExtractor(allow="\?start=\d+\&type=", restrict_xpaths="//div[@class='paginator']"), follow=True),
        Rule(LinkExtractor(allow="/subject/\d+/$", restrict_xpaths="//div[@class='article']"),callback='parse_item')
        #Rule(LinkExtractor(allow="/subject/\d+/$"))
    }


    def parse_item(self, response):


        print response.url

        item = MovieInfoItem()
        text = response.body
        sel = Selector(text=text)

        if response.status == 200:

            # inspect_response(response,self)
            try:

                item['_id'] = response.url[-9:-1]
                item['name'] = sel.xpath("//div[@id='wrapper']/div/h1/span[1]/text()").extract()
                item['director'] = sel.xpath("//div[@id='info']/span[1]/span[2]/a/text()").extract()
                item['screenwriter'] = sel.xpath("//div[@id='info']/span[2]/span[2]/a/text()").extract()
                item['actor'] = sel.xpath("//div[@id='info']/span[3]/span/a/text()").extract()
                item['type'] = sel.xpath("//span[@property='v:genre']/text()").extract()

                item['average'] = sel.xpath('//strong[@class="ll rating_num"]/text()').extract()
                item['rating_people'] = sel.xpath('//a[@class="rating_people"]/span/text()').extract()
                item['rating_five'] = sel.xpath('//div[@class="ratings-on-weight"]/div[1]/span[2]/text()').extract()
                item['rating_four'] = sel.xpath('//div[@class="ratings-on-weight"]/div[2]/span[2]/text()').extract()
                item['rating_three'] = sel.xpath('//div[@class="ratings-on-weight"]/div[3]/span[2]/text()').extract()
                item['rating_two'] = sel.xpath('//div[@class="ratings-on-weight"]/div[4]/span[2]/text()').extract()
                item['rating_one'] = sel.xpath('//div[@class="ratings-on-weight"]/div[5]/span[2]/text()').extract()

                # 取得国家信息xpath无法使用改用正则表达式
                # 先将位置匹配成pattern对象
                pattern = re.compile(r'<span class="pl">制片国家/地区:</span>(.*?)<br/>', re.S)
                info_region = re.findall(pattern=pattern, string=text)
                if len(info_region) > 0:
                    info_region = info_region[0]
                else:
                    info_region = None
                item['country'] = info_region

                # 取得语言信息同上
                pattern = re.compile(r'<span class="pl">语言:</span>(.*?)<br/>', re.S)
                info_language = re.findall(pattern=pattern, string=text)
                if len(info_language) > 0:
                    info_language = info_language[0]
                else:
                    info_language = None

                item['language'] = info_language

                item['release_date'] = sel.xpath("//span[@property='v:initialReleaseDate']/text()").extract()
                item['runtime'] = sel.xpath("//span[@property='v:runtime']/text()").extract()

                pattern = re.compile(r'<span class="pl">又名:</span>(.*?)<br/>', re.S)
                info_other_name = re.findall(pattern=pattern, string=text)
                if len(info_other_name) > 0:
                    info_other_name = info_other_name[0]
                else:
                    info_other_name = None

                item['other_name'] = info_other_name

                info_describle = sel.xpath('//span[@class="all hidden"]/text()').extract()
                # info_describe_str = "".join(info_describe).replace('\n','').replace(' ','').replace('\u3000','')

                info_describle = [myl.replace('\n', '').replace(' ', '').replace('\u3000', '') for myl in info_describle]
                item['info_describle'] = info_describle

                imdb_id = sel.xpath("//div[@id='info']/a[1]/text()").extract()
                imdb_url = ['http://www.imdb.com/' + myl for myl in imdb_id]
                item['imdb_url'] = imdb_url

                print item

                yield item
            except:
                print
                "------------------------------------------error-----------------------------------------"
        else:
            print
            '**********************************************************************************************'