# Sales Person
# Write a solution to find the names of all the salespersons who did not have any orders related to the company with the name "RED".
# Solution for the 'Sales Person' problem.
import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    return sales_person[~sales_person['sales_id'].isin(pd.merge(left = orders, right= company[company['name']== 'RED'], on = 'com_id', how = 'inner')['sales_id'].unique())][['name']]


