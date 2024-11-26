# Daily Leads and Partners
# For each date_id and make_name, find the number of distinct lead_id's and distinct partner_id's.
# Solution for the 'Daily Leads and Partners' problem.
import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    return daily_sales.groupby(['date_id', 'make_name']).agg({'lead_id' : 'nunique', 'partner_id' : 'nunique'}).reset_index().rename(columns = {'lead_id': 'unique_leads', 'partner_id': 'unique_partners'})
