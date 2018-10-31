#!/usr/bin/python3

import csv
import pandas as pd
from textblob import TextBlob

def find_sentiment(review):
    x = TextBlob(review).sentiment
    if x.polarity < 0:
        return 'Negative'
    else:
        return 'Positive'


def main():
    
    review_file_name = 'reviews_60601-60606.csv' # Input review file name
    restaurant_file_name = 'restaurants_60601-60606.csv' # Input restaurant file name
    output_file_name = 'rest_review.csv' # Output file name

    review_df = pd.read_csv(review_file_name, header=0)
    restaurant_df = pd.read_csv(restaurant_file_name, header=0)

    review_df = review_df[['restaurantID', 'reviewContent', 'rating']]
    restaurant_df = restaurant_df[['restaurantID', 'name']]
    
    headers = ['Restaurant Name', 'Sentiment labels', 'Review Rating']
    
    final_list = []

    for i in range(len(review_df)):
        res_name = restaurant_df.loc[restaurant_df['restaurantID'] == review_df.loc[i, 'restaurantID']].iloc[0][1]
        sentiment_label = find_sentiment(str(review_df.loc[i, 'reviewContent']))
        rating = review_df.loc[i, 'rating']
        temp_list = []
        temp_list.append(res_name)
        temp_list.append(sentiment_label)
        temp_list.append(rating)
        final_list.append(temp_list)

    with open(output_file_name, 'w') as o_file:
        writer = csv.writer(o_file, dialect = 'excel')
        writer.writerow(headers)
        writer.writerows(final_list)
    print('Done')

if __name__ == '__main__':
    main()