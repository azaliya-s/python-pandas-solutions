# Customer Placing the Largest Number of Orders
# Solution for the 'Customer Placing the Largest Number of Orders' problem.
import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
     order_counts =  orders.groupby('customer_number')['order_number'].count().reset_index()
     max_orders_customer = order_counts[order_counts['order_number'] == order_counts['order_number'].max()][['customer_number']]
    
     return max_orders_customer
