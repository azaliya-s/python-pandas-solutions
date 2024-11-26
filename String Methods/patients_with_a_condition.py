# Patients With a Condition
# Solution for the 'Patients With a Condition' problem.
import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients['conditions'].str.contains(r'\bDIAB1')]
