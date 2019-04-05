# -*- coding: utf-8 -*-
import scrapy
import json

from ri_lab_01.items import RiLab01Item
from ri_lab_01.items import RiLab01CommentItem


class CartaCapitalSpider(scrapy.Spider):
    name = 'carta_capital'
    allowed_domains = ['cartacapital.com.br']
    start_urls = []

    def __init__(self, *a, **kw):
        super(CartaCapitalSpider, self).__init__(*a, **kw)
        with open('seeds/carta_capital.json') as json_file:
                data = json.load(json_file)
        self.start_urls = list(data.values())

    def parse(self, response):
        route = 'div.eltdf-container-inner a::attr(href)'
        for i in response.css(route):
            yield response.follow(i,self.postCss,meta= {'url': responde.url})

        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        
    def postCss(self, response){
        
    }

    yield{
         yield {
            'title': getCss('a.eltdf-pt-link::text'),
            'url': response.url,
            'subtitle': getCss('div.wpb_wrapper > h3::text'),
            'author': getCss('a.eltdf-post-info-author-link::text').get(),
            'date': getCss('div.eltdf-post-info-date > a::text'),
            'section': getCss('div.eltdf-post-info-category > a::text'),
            'text': getAllCss('div.eltdf-post-text-inner > a::text, div.eltdf-post-text-inner > p::text')
            }
    }