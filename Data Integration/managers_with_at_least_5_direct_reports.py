# Managers with at Least 5 Direct Reports
# Solution for the 'Managers with at Least 5 Direct Reports' problem.
import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
     report_df = employee.groupby('managerId', as_index = False).agg(reportee_count = ('managerId', 'count'))
     return employee[employee['id'].isin(report_df[report_df['reportee_count']>=5]['managerId'])][['name']]
