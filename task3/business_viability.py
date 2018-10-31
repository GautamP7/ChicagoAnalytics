#!/usr/bin/python3

import csv
import pandas as pd
from datetime import datetime

def main():
    food_inspection_file = 'Food_Inspections_Sorted.csv' # Name of the input file
    output_file = 'Business_Viability_Final.csv' # Name of the output file

    food_insp_df = pd.read_csv(food_inspection_file, header=0)
    food_insp_df = food_insp_df[['AKA Name', 'Address', 'Inspection Date', 'Results']]
    
    temp_result = food_insp_df.loc[0, 'Results']
    final_list = []
    headings = ['Restaurant Name', 'Address', 'Failed inspection on', 'Alive for x years']

    i = 0

    while i < len(food_insp_df) - 1:
        while food_insp_df.loc[i, 'Results'] != 'Fail' and i < len(food_insp_df) - 1:
            i = i + 1

        if food_insp_df.loc[i, 'Results'] == 'Fail':
            temp_res_name = food_insp_df.loc[i, 'AKA Name']
            temp_res_addr = food_insp_df.loc[i, 'Address']
            st_date = food_insp_df.loc[i, 'Inspection Date']
            i = i + 1
            while temp_res_name == food_insp_df.loc[i, 'AKA Name'] and temp_res_addr == food_insp_df.loc[i, 'Address']:
                if food_insp_df.loc[i, 'Results'] == 'Out of Business':
                    end_date = food_insp_df.loc[i, 'Inspection Date']
                    yrs = get_years(st_date, end_date)
                    y = st_date[:4]
                    m = st_date[4:6]
                    d = st_date[6:]
                    temp_list = []
                    temp_list.append(temp_res_name)
                    temp_list.append(food_insp_df.loc[i, 'Address'])
                    temp_list.append(st_date)
                    temp_list.append(yrs)
                    final_list.append(temp_list)
                    break
                i = i + 1

    with open(output_file, 'w') as o_file:
        writer = csv.writer(o_file)
        writer.writerow(headings)
        writer.writerows(final_list)
    print('Done')

def get_years(st_date, end_date): # Returns the duration between the start date and end date in years
    date_format = "%m/%d/%Y"
    d0 = datetime.strptime(st_date, date_format)
    d1 = datetime.strptime(end_date, date_format)
    delta = d1 - d0
    return delta.days / 365.0


if __name__ == '__main__':
    main()