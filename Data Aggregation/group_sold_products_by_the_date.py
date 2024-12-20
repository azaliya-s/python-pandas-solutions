# Group Sold Products By The Date
# Write a solution to find for each date the number of different products sold and their names. The sold products names for each date should be sorted lexicographically. Return the result table ordered by sell_date
# Solution for the 'Group Sold Products By The Date' problem.
import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
     return activities.groupby('sell_date')['product'].agg([
        ('num_sold', 'nunique'),
        ('products', lambda x: ',' .join(sorted(x.unique())))]).reset_index()
