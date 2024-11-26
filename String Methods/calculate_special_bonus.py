# Calculate Special Bonus
# Write a solution to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee's name does not start with the character 'M'. The bonus of an employee is 0 otherwise. Return the result table ordered by employee_id.
# Solution for the 'Calculate Special Bonus' problem.
import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
     employees['bonus'] = 0
     employees.loc[(employees['employee_id'] % 2 != 0) & (~employees['name'].str.startswith('M')), 'bonus'] = employees['salary']
     result_df = employees[['employee_id', 'bonus']].sort_values(by='employee_id', ascending=True)
    
     return result_df
