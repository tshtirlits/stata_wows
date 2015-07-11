#!/usr/bin/python
# -*- coding: UTF-8 -*-
from grab import Grab
#from BeautifulSoup import BeautifulSoup
import html5lib

g = Grab('http://worldofwarships.ru/community/accounts/61510-T_Shtirlits/')
resp = g.go('http://worldofwarships.ru/community/accounts/61510-T_Shtirlits/')
#print(resp.body)
#print g.xpath_text(".//*[@id='general_pvp']/div[2]/div/div/div[1]/table/tbody/tr[2]/td[2]/span")
print g.doc.select(".//*[@id='general_pvp']/div[2]/div/div/div[1]/table/tbody/tr[2]/td[2]/span").text()
#print g.xpath('//div[@id="error"]').text_content()

#for elem in g.xpath_list('//h3'):
#    print elem.text

#print g.doc.tree.xpath_text(".//*[@id='general_pvp']/div[2]/div/div/div[1]/table/tbody/tr[2]/td[2]/span")
print ("Количество боев: ") + g.doc.select(".//*[@id='general_pvp']/div[2]/div/div/div[1]/table/tbody/tr[1]/td[2]/span").text()
