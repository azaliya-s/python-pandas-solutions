# Customers Who Never Order
# Solution for the 'Customers Who Never Order' problem.
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    filtered_customers = customers[~customers['id'].isin(orders['customerId'])]
    result = filtered_customers[['name']].rename(columns={'name': 'Customers'})
    
    return result
