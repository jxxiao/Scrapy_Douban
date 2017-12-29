# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    _id = scrapy.Field()
    name = scrapy.Field()
    director = scrapy.Field()
    screenwriter = scrapy.Field()
    actor = scrapy.Field()
    type = scrapy.Field()

    average = scrapy.Field()
    rating_people = scrapy.Field()
    rating_five = scrapy.Field()
    rating_four = scrapy.Field()
    rating_three = scrapy.Field()
    rating_two = scrapy.Field()
    rating_one = scrapy.Field()

    country = scrapy.Field()
    language = scrapy.Field()
    release_date = scrapy.Field()
    runtime = scrapy.Field()
    other_name = scrapy.Field()
    info_describle = scrapy.Field()
    imdb_url = scrapy.Field()


class MovieCommentItem(scrapy.Item):
    pass

