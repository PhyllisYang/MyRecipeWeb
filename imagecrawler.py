#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 16:58:04 2018

@author: fanyang
"""

from icrawler.builtin import GoogleImageCrawler
import csv





# get certain column value of csv(for common csv file(','))
def get_origin_column_value(file, column_name):
    with open(file, 'r') as f:
        role_list = []
        reader = csv.reader(f, delimiter=',')
        fieldnames = next(reader)
        reader = csv.DictReader(f, fieldnames=fieldnames, delimiter=',')
        for row in reader:
            role_list.append(row[column_name])
        return role_list
'''
google_crawler = GoogleImageCrawler(feeder_threads=1,
                                    parser_threads=2,
                                    downloader_threads=4,
                                    storage={'root_dir':'/Users/fanyang/python/finalproject/recipeimage'})
 '''  
def craw_image(key,i):
    save_dir = '/Users/fanyang/python/finalproject/recipeimage' '''change to savin dir'''
    crawler = GoogleImageCrawler(feeder_threads=1,
                                    parser_threads=2,
                                    downloader_threads=4,
                                    storage={'root_dir':save_dir + '/' + str(i)})
    crawler.crawl(keyword = key, max_num=3)

 
'''
filters = dict(
    size='large',
    color='orange',
    license='commercial,modify',
    date=((2017, 1, 1), (2017, 11, 30)))'''
def main():
    file='/Users/fanyang/python/finalproject/recipe_data.csv' #change to recipe_data's dir
    column_name = 'title'
    search_list=get_origin_column_value(file,column_name)
    
    #google_crawler.crawl(keyword='cat', max_num=1)
    i=0
    
    for key in search_list:
        craw_image(key,i)
        i += 1
        
if __name__ == '__main__':
    main()
