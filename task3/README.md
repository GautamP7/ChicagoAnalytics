# Task 3: Viability of a Business after a Failed Food Inspection

#### Problem statement
----
What is the viability of a business, i.e., how long is a business active, after a failed food inspection?

#### Tools used
----
- Python3
- Pandas
- Plotly

#### Technical Approach
----
1. Extracted the Food Inspections dataset from the City of Chicago’s data portal.
2. Sorted the above dataset in ascending order of business name and inspection date.
3. Found the restaurants that had both failed a food inspection and gone out of business.
4. Calculated the duration in years between the latest failed food inspection date and the out of business date.
5. Used plotly to plot a scatter plot showing the number of years a business was alive after its most recent failed food inspection, for all businesses in zip codes 60601-60607.

#### Analysis
----
1. Most of the businesses that went out of business after failing a food inspection where only alive for around 3 years.
2. As it can be expected, majority of the businesses that failed a food inspection with very high risk violations went out of business within a year whereas the businesses that failed a food inspection with very low risk violations went out of business after 3-4 years.

#### Files
----
Data files - `Food_Inspections.csv`, `Food_Inspections_Sorted.csv`  
Code - `business_Viability.py`  
Output file - `Business_Viability.csv`
