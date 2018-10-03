# -*- coding: utf-8 -*-
import scrapy
import pandas as pd

class BballrefSpider(scrapy.Spider):
    name = 'bballref'
    start_urls = ['https://www.basketball-reference.com/players/a',
                  'https://www.basketball-reference.com/players/b',
                  'https://www.basketball-reference.com/players/c',
                  'https://www.basketball-reference.com/players/d',
                  'https://www.basketball-reference.com/players/e',
                  'https://www.basketball-reference.com/players/f',
                  'https://www.basketball-reference.com/players/g',
                  'https://www.basketball-reference.com/players/h',
                  'https://www.basketball-reference.com/players/i',
                  'https://www.basketball-reference.com/players/j',
                  'https://www.basketball-reference.com/players/k',
                  'https://www.basketball-reference.com/players/l',
                  'https://www.basketball-reference.com/players/m',
                  'https://www.basketball-reference.com/players/n',
                  'https://www.basketball-reference.com/players/o',
                  'https://www.basketball-reference.com/players/p',
                  'https://www.basketball-reference.com/players/q',
                  'https://www.basketball-reference.com/players/r',
                  'https://www.basketball-reference.com/players/s',
                  'https://www.basketball-reference.com/players/t',
                  'https://www.basketball-reference.com/players/u',
                  'https://www.basketball-reference.com/players/v',
                  'https://www.basketball-reference.com/players/w',
                  'https://www.basketball-reference.com/players/y',
                  'https://www.basketball-reference.com/players/z',
                  ]
    df = pd.DataFrame(columns=['realname','team'])

    def parse(self, response):
        links = response.xpath('//*[@id="players"]/tbody/tr/th/a/@href').extract()
        for link in links:
            yield response.follow(link, callback=self.addplayer)
        self.df.drop_duplicates(inplace=True)
        self.df.to_csv('players.csv')

    def addplayer(self, response):
        player_name = response.xpath('//*[@id="meta"]/div/h1/text()').extract()
        teams = response.xpath("//table[1]/tbody/tr/td[2]/a/text()").extract()
        for team in teams:
           self.df = self.df.append({'realname':player_name, 'team':team},ignore_index=True)
           print({'realname':player_name, 'team':team})
