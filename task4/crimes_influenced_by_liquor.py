#!/usr/bin/python3

import pandas as pd

def main():
    crimes_file = 'Crimes_Census_Block.csv' # Input crimes file
    buisness_with_liquor_file = 'Business_Census_Block.csv' # Input businesses with liquor file
    output_file = 'crimes_influenced_by_liquor_report.csv' # Output file

    crime_df = pd.read_csv(crimes_file)
    business_df = pd.read_csv(buisness_with_liquor_file)

    crime_df = crime_df.groupby(['Census Block'], as_index=False)[['#Crimes', '#Arrests']].sum() # Grouping the crimes and arrests by census block
    business_df = business_df.groupby(['Census Block'], as_index=False)[['#Businesses with liquor licenses']].sum() # Grouping the businesses with liquor by census block

    #crime_df.to_csv('Crimes_agg.csv')
    #business_df.to_csv('Liquor_Businesses_agg.csv')

    df = pd.merge(business_df, crime_df, on='Census Block') # Merging the crimes and the no. of businesses with liquor by census block

    df.to_csv(output_file, index=False)

    print('Done')

if __name__ == '__main__':
    main()