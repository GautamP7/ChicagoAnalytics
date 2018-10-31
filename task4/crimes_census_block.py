
import urllib
import requests
from bs4 import BeautifulSoup
import csv
import re
import time

def get_lant_long(fileName):
	file = csv.reader(open(fileName, 'r'))
	all_lat_long = []
	while True:
		try:
			lat_long = []
			line = next(file)
			x = line[1]
			y = line[0]
			lat_long.append(x.strip())
			lat_long.append(y.strip())
			all_lat_long.append(lat_long)
		except:
			break
	return all_lat_long
def make_url_connection(fileName):
	all_lat_long = get_lant_long(fileName)
	index = 1
	result = []
	dict = {}
	use_cache = 1
	for lat_long in all_lat_long:
		num = "no census block number"
		lat_long = tuple(lat_long)
		if lat_long in dict:
			print("use_cache: {} ".format(use_cache))
			num = dict[lat_long]
			use_cache = use_cache + 1
		else:	
			time.sleep(0.1) #wait for the result
			main_url = "https://geocoding.geo.census.gov/geocoder/geographies/coordinates?x=%s&y=%s&benchmark=4&vintage=4"%(lat_long[0],lat_long[1])
			time.sleep(0.1)
			page = requests.get(main_url)
			soup = BeautifulSoup(page.content, 'html.parser')
			block_num = soup.findAll(text = re.compile('GEOID'))
			for each in block_num:
				if(len(each.strip()) == 22):
					block_num = each
					break
			block_num = "".join(block_num) #convert list to string
			print(block_num)
			num_array = block_num.split(':')
			if len(num_array) == 1:
				num = num_array[0]
			else:
				num = num_array[1]
			dict[lat_long] = num
		num = num.strip()
		num = num[5:]
		temp = [num]
		result.append(temp)
		print(index)
		print(num)
		index = index + 1
	return result
def make_csv_file(fileName):		
	result = make_url_connection(fileName)
	with open('Crimes_Census_Block.csv', "w", newline = "") as outFile:
		writer = csv.writer(outFile)
		writer.writerows(result)
make_csv_file('Crimes.csv')

	