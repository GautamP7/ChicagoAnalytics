#!/usr/bin/python3

import urllib
import requests
from bs4 import BeautifulSoup
import csv
import re
import time
import random

def get_census_block(lat, lon):
    main_url = "https://geocoding.geo.census.gov/geocoder/geographies/coordinates?x=%s&y=%s&benchmark=4&vintage=4"%(lon,lat)
    time.sleep(0.1)
    page = requests.get(main_url)
    time.sleep(0.1)
    soup = BeautifulSoup(page.content, 'html.parser')
    block_num = soup.findAll(text = re.compile('GEOID'))
    for each in block_num:
        if(len(each.strip()) == 22):
            block_num = each
            break
    block_num = "".join(block_num)
    num_array = block_num.split(':')
    if len(num_array) == 1:
        num = num_array[0]
    else:
        num = num_array[1]
    num = num.strip()
    num = num[5:]
    return num
    
            

def main():
    i = 0
    business_lic_file = 'LB.csv'
    business_list = []
    headings = ['Census Block', '#Businesses with liquor licenses']
    with open(business_lic_file) as i_file:
        with open('Out.csv', 'w') as o_file:
            writer = csv.writer(o_file)
            writer.writerow(headings)
            reader = csv.reader(i_file)
            for row in reader:
                cb = get_census_block(row[0], row[1])
                temp_list = []
                temp_list.append(cb)
                temp_list.append(1)
                writer.writerow(temp_list)
                print(i, temp_list)
                i = i + 1

if __name__ == '__main__':
    main()