#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 20:33:23 2020

@author: alexander
"""
import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re

from time import sleep
from random import randint
from selenium import webdriver

#initiate data storage
year = 2020
titles = []
years = []
time = []
imdb_ratings = []
metascores = []
votes = []
us_gross = []
# Here Chrome  will be used
driver = webdriver.Chrome()

def scrapPage(url, nropestana):
    url_movie = "https://pelisplus.me"+url
    driver.execute_script("window.open('"+url_movie+"','new_window"+str(nropestana)+"')")
    # Hacemos click en el primer enlace y lo abrimos en una pestaña nueva
    # tab=browser.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div/div/div[1]/a[1]')
    # tab.send_keys(Keys.COMMAND + Keys.RETURN)
    print(url_movie)

try:
    # URL of website
    url = "https://pelisplus.me/peliculas-"+str(year)+"/"
    # Opening the website
    driver.get(url)
except:
    print("...................url not found!!!")
    
try:
     for i in range(0):
         button = driver.find_element_by_class_name("butmore")
         button.click()
         sleep(5)
         #print(soup.find('div', class_='butmore'))
         print(i)
except:
     print("...................No more pages!!!")

body = driver.find_element_by_class_name("main-peliculas")
soup = BeautifulSoup(body.get_attribute("innerHTML"), "html.parser")
movies = soup.find_all('div', class_='item-pelicula pull-left')
#for movie in movies:
#    scrapPage(movie.a['href'])
scrapPage("/pelicula/inmune/",1)
scrapPage("/pelicula/life-in-a-year/",2)
#browser.refresh() 
#driver.close();
