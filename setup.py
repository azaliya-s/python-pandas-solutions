import os
import subprocess

# Problem categories and their respective problems
problems = {
    "Data Filtering": [
        "Big Countries",
        "Recyclable and Low Fat Products",
        "Customers Who Never Order",
        "Article Views I",
    ],
    "String Methods": [
        "Invalid Tweets",
        "Calculate Special Bonus",
        "Fix Names in a Table",
        "Find Users With Valid E-Mails",
        "Patients With a Condition",
        "Count Occurrences in Text",
    ],
    "Data Manipulation": [
        "Nth Highest Salary",
        "Second Highest Salary",
        "Department Highest Salary",
        "Rank Scores",
        "Delete Duplicate Emails",
        "Rearrange Products Table",
    ],
    "Statistics": [
        "The Number of Rich Customers",
        "Immediate Food Delivery I",
        "Count Salary Categories",
        "Ads Performance",
    ],
    "Data Aggregation": [
        "Find Total Time Spent by Each Employee",
        "Game Play Analysis I",
        "Number of Unique Subjects Taught by Each Teacher",
        "Classes More Than 5 Students",
        "Customer Placing the Largest Number of Orders",
        "Group Sold Products By The Date",
        "Daily Leads and Partners",
    ],
    "Data Integration": [
        "Actors and Directors Who Cooperated At Least Three Times",
        "Replace Employee ID With The Unique Identifier",
        "Students and Examinations",
        "Managers with at Least 5 Direct Reports",
        "Sales Person",
        "Accepted Candidates From the Interviews",
    ],
}

# Initialize Git repository if not already initialized
if not os.path.exists(".git"):
    subprocess.run(["git", "init"])

# Process each category (branch)
for branch, problem_list in problems.items():
    # Create a branch for the category
    subprocess.run(["git", "checkout", "-b", branch])
    
    # Create a subfolder for the branch
    os.makedirs(branch, exist_ok=True)
    
    # Create problem files
    for problem in problem_list:
        # Create a file with a formatted name
        file_name = problem.lower().replace(" ", "_") + ".py"
        file_path = os.path.join(branch, file_name)
        
        # Write an initial template
        with open(file_path, "w") as file:
            file.write(f"# {problem}\n# Solution for the '{problem}' problem.\n\n")
    
    # Add files to Git
    subprocess.run(["git", "add", "."])
    
    # Commit changes
    subprocess.run(["git", "commit", "-m", f"Add problems for {branch}"])
    
# Return to the main branch
subprocess.run(["git", "checkout", "main"])
