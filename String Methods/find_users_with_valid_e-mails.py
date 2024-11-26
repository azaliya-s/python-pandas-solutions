# Find Users With Valid E-Mails
# Write a solution to find the users who have valid emails.
# A valid e-mail has a prefix name and a domain where: The prefix name is a string that may contain letters (upper or lower case), digits, underscore '_', period '.', and/or dash '-'. The prefix name must start with a letter. The domain is '@leetcode.com'.
# Solution for the 'Find Users With Valid E-Mails' problem.
import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
     valid_emails_df = users[users['mail'].str.match(r'^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode\.com$')]
    
     return valid_emails_df
