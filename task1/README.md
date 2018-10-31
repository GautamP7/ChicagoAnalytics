# Task 1: Crime Report based on the Type of Business

#### Problem statement
----
Report the types of crime (Assault, Battery, etc) within 3 blocks of (a) Grocery Stores (b) Schools, and (c) Restaurants.

#### Tools used
----
- Python3
- Pandas
- Plotly

#### Technical Approach
----
1. Extracted Grocery stores data, Schools data and Crimes data from the City of Chicago’s data portal.
2. Used the Restaurants data from Yelp.
3. Calculated the Euclidean distance between the location of each crime and the location of each business using their respective latitudes and longitudes.
4. Considered 600m as the threshold for determining if the crimes were within 3 blocks of a said business and considered 50m as the threshold for determining if the crimes occurred on the premises of a said business.
5. Grouped the crimes by [year, business type, business name, address, crime type] and summed the no. of crimes, no. of arrests and the no. of crimes on premises of a business, for each.
6. Plotted the no. of crimes on premises of each business on a map using plotly.

#### Analysis
----
1. The crimes considered for obtaining the result are from the years 2001 to 2017.
2. From the resulting dataset, it is observed that the highest no. of crimes are of type theft, followed by deceptive practice and battery.
3. Among the zip codes 60601 - 60607, the highest no. of crimes occurred in the zip code 60601.

#### Files
----
Data files - `Crimes.csv`, `Grocery_Stores.csv`, `Restaurants.csv`, `Schools.csv`
Code - `report_crime.py`
Output file - `Crime_Report.csv`