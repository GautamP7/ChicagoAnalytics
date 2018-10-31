# Task 4: Crimes influenced by Businesses with Liquor Licenses

#### Problem statement
----
Does having a liquor license influence crime incidents in the neighborhood?

#### Tools used
----
- Python3
- Pandas
- BeautifulSoup
- Plotly

#### Technical Approach
----
1. Used Crime dataset and Business Licenses dataset from the City of Chicago’s data portal.
2. Extracted the businesses with liquor license from the Business license dataset.
3. Used census.gov’s geocoding API and BeautifulSoup to get the census block for each crime and for each business with liquor license.
4. Grouped the businesses with liquor license by census block and summed the no. of businesses.
5. Grouped the crimes by census block and summed the no. of crimes and the no. of arrests.
6. Merged the results of the above 2 group by operations to get the no. of businesses with liquor license and the no. of crimes for each census block.
7. Used plotly to plot a stacked bar chart showing both, the no. of businesses with liquor license and the no. of crimes, for each census block.

#### Analysis
----
1. Some census blocks have more crimes with more businesses having liquor license whereas some census blocks have very less crimes even with more businesses having liquor license.
2. Similarly some census blocks have less crimes with lesser no. of businesses having liquor license whereas some census blocks have more crimes even though they have lesser no. of businesses having liquor license.
3. Therefore, it can be concluded that there is no correlation between the no. of businesses with liquor license and the no. of crimes, for a given region. Hence, having a liquor license does not influence crime incidents in the neighborhood.

#### Files
----
Data files - `Crimes_Census_Block.py`, `Business_Census_Block.py`, `LB.csv`  
Code - `crimes_influenced_by_liquor_report.py`, `crimes_census_block.py`, `business_census_block.py`  
Output file - `crimes_influenced_by_liquor_report.csv`