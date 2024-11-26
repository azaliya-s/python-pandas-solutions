# Find Total Time Spent by Each Employee
# Write a solution to calculate the total time in minutes spent by each employee on each day at the office. Note that within one day, an employee can enter and leave more than once. The time spent in the office for a single entry is out_time - in_time.
# Solution for the 'Find Total Time Spent by Each Employee' problem.
import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    return (
        employees
        .rename(columns={'event_day':'day'})
        .assign(total_time=employees['out_time'] - employees['in_time'])
        .groupby(['day', 'emp_id'])['total_time'].sum()
        .reset_index()
        )