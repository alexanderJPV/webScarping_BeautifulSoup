 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 12:09:02 2021

@author: alexander
"""
import requests
#from bs4 import BeautifulSoup
import os

def downLoadImg(urlp,nompost, x, fileDownland):
    Image = fileDownland
    img = nompost
    filePath = Image # file path for the directory
    originPath = os.getcwd()
    # create directory for required images poster
    if not os.path.exists(filePath): # if the dir doesn't exist
        os.makedirs(filePath) # create the dir
        
    # move to new directory
    os.chdir(filePath)
    pathFinish = os.getcwd()
    try:
        url = urlp
        response = requests.get(url) # go to the url and store it in the response var
        if response.status_code == 200:
            nameFilepath = img + '-' + str(x) + '.jpg' 
            with open(nameFilepath, 'wb') as f: # open the image as the mentioned file format, (w for writing, and b for binary)
                print(response)
                f.write(requests.get(url).content) # get the content of the url and write/save in the created dir
                f.close() # stop writing/saving the image
                pathFinish += "/" + nameFilepath
    except:
        print('Image not found')
        pass # repeat the loop again 
    os.chdir(originPath)
    print(pathFinish)
    return pathFinish
#-----------------------------------------------------------------

# url = "https://pelisplus.me/pelicula/life-in-a-year/"
# page = requests.get(url)
# soup = BeautifulSoup(page.content,'html.parser')

# poster = soup.find('img',{'id':'cover'})['src']
# print(downLoadImg(poster, 'life-in-a-year',1,'poster'))
