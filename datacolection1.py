#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 15:06:44 2018

@author: fanyang
"""

import os, requests
import bs4
from bs4 import BeautifulSoup
import numpy
import re
import csv

'''
img_url = "https://images.media-allrecipes.com/userphotos/250x250/1448794.jpg"

img_name = os.path.basename(img_url)

img = requests.get(img_url)

file = open('/Users/fanyang/python/finalproject/recipeimage/'+img_name,'wb')

file.write(img.content)

file.close
'''
'''
root_url = 'https://www.allrecipes.com'

index_url = root_url + '/recipes/17562/dinner/'
'''

'''
def get_recipe_page_urls():
    response = requests.get(index_url)
    soup = bs4.BeautifulSoup(response.text,"lxml")
    return [a.attrs.get('href') for a in soup.select('div.grid-card-image-container a[href^=https://www.allrecipes.com/recipe]')]
'''
'''print(get_recipe_page_urls())'''


'''
response = requests.get(index_url)
soup = bs4.BeautifulSoup(response.text,"lxml")
links = [a.attrs.get('href') for a in soup.select('div.grid-card-image-container a[href^=https://www.allrecipes.com/recipe]')]
print(links)
'''
'''
def get_recipe_data(recipe_page_url):
    recipe_data= {}
    response = requests.get(recipe_page_url)
    soup = bs4.BeautifulSoup(response.text,"lxml")
    recipe_data['title'] = soup.select('div#recipe-summary h1')[0].get_text()
    return recipe_data

a=get_recipe_page_urls()
print(get_recipe_data(a[0]))
'''

root_url = 'http://www.myrecipes.com/'
page1_url = 'search/ingredient-chef?qt='
pagen_url ='search?q=&page='
urls=[]

def get_recipe_urls():
    index_url = root_url + page1_url
    response = requests.get(index_url)
    soup = bs4.BeautifulSoup(response.text,"lxml")
    for a in soup.select('div.search-results-container a[href^=/recipe]'):
        urls.append(a.attrs.get('href'))
    for i in range(2,100):
            index_url = root_url + pagen_url + str(i)
            response = requests.get(index_url)
            soup = bs4.BeautifulSoup(response.text,"lxml")
            for a in soup.select('div.search-results-container a[href^=/recipe]'):
                urls.append(a.attrs.get('href'))
    return urls

def get_recipe_data(recipe_page_url):
    recipe_data={}
    response = requests.get(root_url + recipe_page_url)
    responset = requests.get(root_url + recipe_page_url).text
    soup = bs4.BeautifulSoup(response.text,"lxml")
    recipe_data['title'] = soup.find('h1').get_text()
    try:
        recipe_data['preptime'] = int(re.sub('[^0-9]','0',soup.select('div.recipe-meta-item-body')[0].get_text().split()[0]))
        recipe_data['cooktime'] = int(re.sub('[^0-9]','0',soup.select('div.recipe-meta-item-body')[0].get_text().split()[0]))
        recipe_data['totaltime'] = recipe_data['preptime'] + recipe_data['cooktime']
        
    except IndexError:
        recipe_data['preptime'] = 0
        recipe_data['cooktime'] = 0
        recipe_data['totaltime'] = recipe_data['preptime'] + recipe_data['cooktime']   
        
    try:
        recipe_data['ingredients'] = soup.select('div.ingredients')[0].get_text().split('\n')
    except IndexError:
        recipe_data['ingredients'] = 'None'
        
    try:
        recipe_data['steps'] = soup.select('div.recipe-instructions')[0].get_text().split('\n')
    except IndexError:
        recipe_data['steps'] = 'None'   
        
    return recipe_data    

def save_recipe_data_dict2csv1(dict,file):
    with open(file,'a') as f:
        w = csv.writer(f)
        w.writerow(dict.keys())
        w.writerow(dict.values())
        
def save_recipe_data_dict2csv2(dict,file):
    with open(file,'a') as f:
        w = csv.writer(f)
        w.writerow(dict.values())
        
        
save_pwd = "/Users/fanyang/python/finalproject/"
save_name = "recipe_data.csv"
file = save_pwd + save_name 
a=[]

recipe_page_url = get_recipe_urls()
'''for url in recipe_page_url:
    a.append(get_recipe_data(url)) 

for i in range(0,len(recipe_page_url)+1,2):
    a.append(get_recipe_data(recipe_page_url[i]))
for i in range(1,len(a)):
    save_recipe_data_dict2csv2(a[i],file)
'''
for i in range(0,len(recipe_page_url),2):
    if i == 0:
        save_recipe_data_dict2csv1(get_recipe_data(recipe_page_url[i]),file)
    else:
        save_recipe_data_dict2csv2(get_recipe_data(recipe_page_url[i]),file)

if __name__ == '__main__':
    main()
