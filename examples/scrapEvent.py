#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 22:02:09 2020

@author: alexander
"""
import time
# importing webdriver from selenium
from selenium import webdriver
 
# Here Chrome  will be used
driver = webdriver.Chrome()
 
# URL of website
url = "https://www.geeksforgeeks.org/"
 
# Opening the website
driver.get(url)
 
# getting the button by class name
button = driver.find_element_by_class_name("read-more")
print(button)
# clicking on the button
button.click()
driver.close();