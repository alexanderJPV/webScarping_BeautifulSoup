#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 20:33:23 2020

@author: alexander
"""
#import requests
from bs4 import BeautifulSoup
import pandas as pd
#import numpy as np
#import re

from time import sleep
#from random import randint
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import scrapMovie

# initiate data storage
year = 2020
trillers =[]
titles = []
years = []
time = []
genders = []
sinopsises = []
repartos = []
urlMovies = []
pathPosters = []
pathImgGallerys = []
# Here Chrome  will be used
driver = webdriver.Chrome()

def openOtherWindows(url_movie,nropestana):    
    try:
        driver.execute_script("window.open('"+url_movie+"','new_window"+str(nropestana)+"')")
        driver.switch_to_window(driver.window_handles[1]) 
        #driver.maximize_window()
    except:
        print("...................no se pudo abrir la pestaña!!!")
        
def clickMovie():
    try:
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "coverGallery")))
        ActionChains(driver).move_to_element(element).click().perform()
        #driver.find_element_by_xpath('//div[@class="video-backgroud"]/a').click()
        sleep(2)
    except:
        print(".....................no se pudo hacer click!!!")
    
def scrapAllData(url, nropestana):
    body = driver.find_element_by_class_name("pelicula-view")
    soup = BeautifulSoup(body.get_attribute("innerHTML"), "html.parser")
    triller = soup.find('div',{'class':'trailer modalshow'})['youtube']
    titulo_original = soup.find('div',{'class':'info-content'}).h1.text
    items_ifcont = soup.find('div',{'class':'info-content'}).find_all('p')
    fecha_anio = items_ifcont[1].find_all('span')[1].text
    x = str(items_ifcont[2].find_all('span')[1].text)
    duracion = x.replace(" mins.", "")
    genero = items_ifcont[3].find_all('span')[1].text
    sinopsis = items_ifcont[4].find_all('span')[1].text
    reparto_actores = items_ifcont[5].find_all('span')[1].text    
    poster = soup.find('img',{'id':'cover'})['src']
    imgGallery = soup.find('img',{'id':'coverGallery'})['src']
    z = url.replace("/", "")
    a = scrapMovie.downLoadImg(poster,z,nropestana,'poster/')
    b = scrapMovie.downLoadImg(imgGallery,z,nropestana,'gallery/')
    urlMovie = str(soup.find('iframe')['src'])
    finalUrl = urlMovie[32:len(urlMovie)]
    trillers.append(triller)
    titles.append(titulo_original)
    years.append(fecha_anio)
    time.append(duracion)
    genders.append(genero)
    sinopsises.append(sinopsis)
    repartos.append(reparto_actores)
    urlMovies.append(finalUrl)
    pathPosters.append(a)
    pathImgGallerys.append(b)
def closeWindows():
    # -----------> close windows
    try:
        driver.switch_to_window(driver.window_handles[2])
        sleep(1)
        driver.close()
    except:
        print("...not found windows number two")   
    try:
        driver.switch_to_window(driver.window_handles[1])
        sleep(2)
        driver.close()
    except:
        print("...not found windows number one")
        
    driver.switch_to_window(driver.window_handles[0])
    
def scrapPage(url, nropestana):
    url_movie = "https://pelisplus.me"+url
    # Hacemos click en el primer enlace y lo abrimos en una pestaña nueva
    openOtherWindows(url_movie,nropestana)
    clickMovie()  
    body = driver.find_element_by_class_name("pelicula-view")
    soup = BeautifulSoup(body.get_attribute("innerHTML"), "html.parser")
    try:
        soup.find('iframe')['src']
        scrapAllData(url,nropestana)
    except:
        driver.switch_to_window(driver.window_handles[1])
        sleep(1)
        clickMovie()
        scrapAllData(url,nropestana)
    closeWindows()

def toCvs():
    print(titles)
    print(trillers)
    print(years)
    print(time)
    print(genders)
    print(sinopsises)
    print(repartos)
    print(urlMovies)
    print(pathPosters)        
    print(pathImgGallerys)
    # panda dataFrame
    movies = pd.DataFrame({
        'title': titles,
        'triller': trillers,
        'year': years,
        'duracion': time,
        'gender': genders,
        'sinopsis':sinopsises,
        'reparto': repartos,
        'url':urlMovies,
        'pathposter': pathPosters,
        'pathGallery': pathImgGallerys
    })
    # cleaning and parsing some data
    movies['year'] = movies['year'].str.extract('(\d+)').astype(int)
    movies['duracion'] = movies['duracion'].str.extract('(\d+)').astype(int)
    # add dataframe to csv file named 'movies.csv'
    movies.to_csv('movies.csv')
    
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
          sleep(range(3,5))
          print(i)
except:
      print("...................No more pages!!!")

body = driver.find_element_by_class_name("main-peliculas")
soup = BeautifulSoup(body.get_attribute("innerHTML"), "html.parser")
movies = soup.find_all('div', class_='item-pelicula pull-left')
x = 1
for movie in movies:
    scrapPage(movie.a['href'],x)
    x+=1
    
#scrapPage("/pelicula/soul/",1)
#scrapPage("/pelicula/life-in-a-year/",2)
toCvs()

#browser.refresh() 
#driver.close();