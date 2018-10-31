#!/usr/bin/python3
    
from math import radians, cos, sin, sqrt, asin
import csv
import pandas as pd

# Considering 1 block in Chicago is 200m
# Considering radius of each business place as 50m for on premises crimes

def main():
    
    three_block_threshold = 600
    on_premises_threshold = 50

    crime_list = []
    grocery_store_list = []
    restaurant_list = []
    school_list = []
    
    final_list = []
    final_list.append(['Year', 'Business Type', 'Business Name', 'Address', 'Has Tobacco License', 'Has Liquor License', 'Crime Type', '#Crimes', '#Arrests', '#OnPremises'])
    
    with open('Crimes.csv') as crime_file:
        r = csv.reader(crime_file)
        for row in r:
            crime_list.append(row)
    del(crime_list[0])
    #lat = row[19] long = row[20] 

    with open('Grocery_Stores.csv') as grocery_store_file:
        r = csv.reader(grocery_store_file)
        for row in r:
            grocery_store_list.append(row)
    del(grocery_store_list[0])
    #lat = row[14] long = row[15] 

    with open('Restaurants.csv') as restaurant_file:
        r = csv.reader(restaurant_file)
        for row in r:
            restaurant_list.append(row)
    del(restaurant_list[0])
    #lat = row[7] long = row[8]

    with open('Schools.csv') as school_file:
        r = csv.reader(school_file)
        for row in r:
            school_list.append(row)
    del(school_list[0])
    #lat = row[91] long = row[92] 
    
    for i in range(len(grocery_store_list)):
        for j in range(len(crime_list)):
            g_lat = float(grocery_store_list[i][14])
            g_long = float(grocery_store_list[i][15])
            c_lat = float(crime_list[j][19])
            c_long = float(crime_list[j][20])
            dist = get_distance(g_lat, g_long, c_lat, c_long)
            if dist <= three_block_threshold:
                row = []
                row.append(crime_list[j][17])
                row.append('Grocery Store')
                row.append(grocery_store_list[i][0])
                row.append(grocery_store_list[i][5] + ', CHICAGO, IL ' + grocery_store_list[i][6])
                row.append('Yes')
                row.append('Yes')
                row.append(crime_list[j][5])
                row.append(1)
                if crime_list[j][8] == 'true':
                    row.append(1)
                else:
                    row.append(0)
                if dist <= on_premises_threshold:
                    row.append(1)
                else:
                    row.append(0)
                final_list.append(row)

    for i in range(len(restaurant_list)):
        for j in range(len(crime_list)):
            r_lat = float(restaurant_list[i][7])
            r_long = float(restaurant_list[i][8])
            c_lat = float(crime_list[j][19])
            c_long = float(crime_list[j][20])
            dist = get_distance(r_lat, r_long, c_lat, c_long)
            if dist <= three_block_threshold:
                row = []
                row.append(crime_list[j][17])
                row.append('Restaurant')
                row.append(restaurant_list[i][1])
                row.append(restaurant_list[i][6])
                row.append('No')
                if restaurant_list[i][23] == 'Full Bar' or restaurant_list[i][23] == 'Beer & Wine Only':
                    row.append('Yes')
                else:
                    row.append('No')
                row.append(crime_list[j][5])
                row.append(1)
                if crime_list[j][8] == 'true':
                    row.append(1)
                else:
                    row.append(0)
                if dist <= on_premises_threshold:
                    row.append(1)
                else:
                    row.append(0)
                final_list.append(row)

    for i in range(len(school_list)):
        for j in range(len(crime_list)):
            s_lat = float(school_list[i][91])
            s_long = float(school_list[i][92])
            c_lat = float(crime_list[j][19])
            c_long = float(crime_list[j][20])
            dist = get_distance(s_lat, s_long, c_lat, c_long)
            if dist <= three_block_threshold:
                row = []
                row.append(crime_list[j][17])
                row.append('School')
                row.append(school_list[i][4])
                row.append(school_list[i][90])
                row.append('No')
                row.append('No')
                row.append(crime_list[j][5])
                row.append(1)
                if crime_list[j][8] == 'true':
                    row.append(1)
                else:
                    row.append(0)
                if dist <= on_premises_threshold:
                    row.append(1)
                else:
                    row.append(0)
                final_list.append(row)

            #dis = haversine(g_lat, g_long, c_lat, c_long)
            #print(c, grocery_store_list[i][0], g_lat, g_long, crime_list[j][0], c_lat, c_long, dist, dis)

    df = pd.DataFrame(final_list[1:], columns=final_list[0])
    df = df.groupby(['Year', 'Business Type', 'Business Name', 'Address', 'Has Tobacco License', 'Has Liquor License', 'Crime Type'])[['#Crimes', '#Arrests', '#OnPremises']].sum()
    df.to_csv('Crime_Report.csv', encoding='utf-8')

    print('Done')


    

def get_distance(lat1, long1, lat2, long2):
    R = 6371
    long1, lat1, long2, lat2 = map(radians, [long1, lat1, long2, lat2])
    x1 = R * cos(lat1) * cos(long1)
    y1 = R * cos(lat1) * sin(long1)
    x2 = R * cos(lat2) * cos(long2)
    y2 = R * cos(lat2) * sin(long2)
    d = sqrt((x2 - x1)**2 + (y2 - y1)**2) * 1000
    return d

# def haversine(lat1, lon1, lat2, lon2):
#     lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
#     dlon = lon2 - lon1 
#     dlat = lat2 - lat1 
#     a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
#     c = 2 * asin(sqrt(a)) 
#     m = 6371 * c * 1000
#     return m

if __name__ == '__main__': main()