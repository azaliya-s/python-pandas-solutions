# Second Highest Salary
# Solution for the 'Second Highest Salary' problem.
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates()
    second_highest = unique_salaries.nlargest(2).iloc[-1] if len(unique_salaries) >= 2 else None
    if second_highest is None:
        return pd.DataFrame({'SecondHighestSalary': [None]})

    # Create a DataFrame with the second highest salary
    result_df = pd.DataFrame({'SecondHighestSalary': [second_highest]})

    return result_df

