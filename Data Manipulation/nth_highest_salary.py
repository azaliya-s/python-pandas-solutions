# Nth Highest Salary
# Solution for the 'Nth Highest Salary' problem.
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salary_sorted = employee['salary'].sort_values(ascending=False).drop_duplicates()
    
    # Check if N is within the valid range
    if N > len(salary_sorted) or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    # Get the nth highest salary
    nth_highest = salary_sorted.iloc[N-1]
    
    # Return the result as a DataFrame
    return pd.DataFrame({f'getNthHighestSalary({N})': [nth_highest]})
