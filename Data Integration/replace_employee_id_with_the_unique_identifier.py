# Replace Employee ID With The Unique Identifier
# Solution for the 'Replace Employee ID With The Unique Identifier' problem.
import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(employees, employee_uni, on = 'id', how = 'left')[['unique_id', 'name']]
