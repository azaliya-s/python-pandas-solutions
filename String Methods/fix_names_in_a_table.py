# Fix Names in a Table
# Solution for the 'Fix Names in a Table' problem.
import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    return users.assign(name = users['name'].str.capitalize()).sort_values(by = 'user_id')
