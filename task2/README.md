# Task 2: Sentiment Analysis of Yelp Reviews for a Restaurant

#### Problem statement
----
Perform sentiment analysis of Yelp reviews for each restaurant.

#### Tools used
----
- Python3
- Pandas
- TextBlob
- Plotly

#### Technical Approach
----
1. Used the Restaurants and Reviews data provided by the teaching team.
2. Used TextBlob to determine the polarity of each review text.
3. Reviews with polarity >= 0 were assigned positive sentiment whereas reviews with polarity < 0 were assigned negative sentiment.
4. Using plotly, plotted a scatter plot showing the review rating and sentiment labels of different reviews for each restaurant, depicting the points with positive sentiment labels in green and the points with negative sentiment labels in red.

#### Analysis
----
1. In general, the majority of reviews for each restaurant have a positive sentiment label.
2. Also, the majority of the ratings corresponding to each review for every restaurant are either 3 or 4, showing that either the customers are more generous in rating the restaurants or that the restaurants are indeed good enough.

#### Files
----
Data files - `restaurants.csv`, `reviews.csv`  
Code - `yelp_sentiment_analysis.py`  
Output file - `rest_review.csv`