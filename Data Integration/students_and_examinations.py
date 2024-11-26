# Students and Examinations
# Write a solution to find the number of times each student attended each exam. Return the result table ordered by student_id and subject_name.
# Solution for the 'Students and Examinations' problem.
import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
     examination_count = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name = 'attended_exams')

     student_subject = pd.merge(students, subjects, how = 'cross')

     result_df = pd.merge(student_subject, examination_count, on = ['student_id', 'subject_name'], how = 'left')

     result_df = result_df[['student_id', 'student_name','subject_name', 'attended_exams']].sort_values(by = ['student_id', 'subject_name'])

     result_df['attended_exams'] = result_df['attended_exams'].fillna(0)

     return result_df   
