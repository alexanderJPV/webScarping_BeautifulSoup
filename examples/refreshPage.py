#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 11:28:24 2020

@author: alexander
"""

url="http://www.flashscore.com/tennis/wta-singles/australian-open-2016/results/"
try:
    from urllib.request import Request, urlopen
    from selenium import webdriver
    req = Request(url)
    s = urlopen(req,timeout=20).read()
    driver = webdriver.Chrome()
    driver.get(url)
    try:
         driver.find_element_by_xpath("""//*[@id="tournament-page-results-more"]/tbody/tr/td/a""").click()
         time.sleep(5)
    except:
         print("No more results to show...")
         
    body = driver.find_element_by_id("fs-results")
    soup = BeautifulSoup(body.get_attribute("innerHTML"), "lxml")
    matches = []
    rrows = soup.find_all("tr")
    for rrow in rrows:
         if rrow.attrs['class']!=['event_round']:
             matches.append(rrow)
            
    print(matches)
except:
    print("Webpage doesn't exist")
