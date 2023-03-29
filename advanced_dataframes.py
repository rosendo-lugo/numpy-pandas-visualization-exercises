import pandas as pd
import numpy as np

np.random.seed(123)

# Create list of values for names column.

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# Randomly generate arrays of scores for each student for each subject.
# Note that all the values need to have the same length here.

math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))


# Construct the DataFrame using the above lists and arrays.

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades,
                   'classroom': np.random.choice(['A', 'B'], len(students))})

# There are several ways to create dataframes, we've already 
# seen how we can create a dataframe from a dictionary:
pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})


# We can also create dataframes from a 2d data structure, 
# either a numpy array or a list of lists:
pd.DataFrame([[1, 2, 3], [4, 5, 6]])

# The array designates the numbers inside the table
# and the next line with the columns in it lables the 
# columns as 'a', 'b', 'c'.
array = np.array([[1, 2, 3], [4, 5, 6]])
pd.DataFrame(array, columns=['a', 'b', 'c'])

# Once those are installed, we can create the connection string. 
# In general, database connection urls will have this format:
from env import host, user, password

url = f'mysql+pymysql://{user}:{password}@{host}/employees'

# Once this url is defined, we can use it with the read_sql function 
# to have pandas treat the results of a SQL query as a dataframe.
pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url)

# It is common to have longer SQL queries that we want to read
#  into python, and an example of how we might break a query 
# into several lines is below:

sql = '''
SELECT
    emp_no,
    first_name,
    last_name
FROM employees
WHERE gender = 'F'
LIMIT 100
'''

employees = pd.read_sql(sql, url)
employees.head()


# ******************Passwords and Sensitive Information******************

# Don't add and commit files with passwords or other sensitive 
# information in them to a git repository!

query = '''
SELECT
    t.title as title,
    d.dept_name as dept_name
FROM titles t
JOIN dept_emp USING (emp_no)
JOIN departments d USING (dept_no)
LIMIT 100
'''

title_dept = pd.read_sql(query, url)
title_dept.head()



# Exercises I
# Run python -m pip install pymysql from your terminal to install pymysql.

# Create a notebook or python script named advanced_dataframes to do 
# your work in for these exercises.


# 1. Run python -m pip install pymysql from your terminal to 
# install the mysql client (any folder is fine)
print('Exercises I, Question 1')
print(f'This part was download and installed')

# 2. cd into your exercises folder for this module and 
# run echo env.py >> .gitignore
print('\nExercises I, Question 2')
print(f'The echo env.py >> .gitignore was run')


# 3. Create a function named get_db_url. 
# It should accept a username, hostname, password, and 
# database name and return a url connection string 
# formatted like in the example at the start of this lesson.
print('\nExercises I, Question 3')
# from env import username, password, hostname

from env import user, host, password

def get_db_url(database_name):
    return f"mysql+pymysql://{user}:{password}@{host}/{database_name}"

print(f'this is the function that was created:\n'
   '"def get_db_url(database_name):\n'
        'return f"mysql+pymysql://[user]:[password]@[host]/[database_name]"')

# # 4. Use your function to obtain a connection to the employees database.
print('\nExercises I, Question 4')

employees_table = pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url) 
print('\n',employees_table)

# # 5. Once you have successfully run a query:
# # 5a. Intentionally make a typo in the database url. 
print('\nExercises I, Question 5a')
def get_db_url(database_name):
    return f"mysql+pymysql:{user}:{password}@{host}/{database_name}" #the // were removed after mysql+pymysql

url = get_db_url('employees')
test_employees_table = pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url) 
print('\n',test_employees_table)

# #   What kind of error message do you see?
print(f'This is what I saw:\n'
      'Could not parse rfc1738 URL from string')

# # 5b. Intentionally make an error in your SQL query.
print('\nExercises I, Question 5b')
query = '''
SELECT
    t.title as title,
    d.dept_name as dept_name
FROM titles t
JOIN dept_emp USING (emp_) # On emp_no the 'no' was removed
JOIN departments d USING (dept_no)
LIMIT 100
'''

title_dept = pd.read_sql(query, url)
title_dept.head()
print(title_dept.head())

# #   What does the error message look like?
print(f'This is what I saw:\n'
      'OperationalError: (pymysql.err.OperationalError) (1054, "Unknown column emp_ in ''from' 'clause")')


# # 6. Read the employees and titles tables into two separate DataFrames.
print('\nExercises I, Question 6')

limit_employees_table = pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url) 
print('\n',f'Employees table\n',limit_employees_table)


limit_titles_table = pd.read_sql('SELECT * FROM titles LIMIT 5 OFFSET 50', url) 
print('\n',f'Titles table\n',limit_titles_table)

# # 7. How many rows and columns do you have in each DataFrame? 
# #I'm assuming that is talking about the employees and title tables.
print('\nExercises I, Question 7')
employees_table = pd.read_sql('SELECT * FROM employees', url) 
print('\n',f'Employees table\n',employees_table)


titles_table = pd.read_sql('SELECT * FROM titles', url) 
print('\n',f'Titles table\n',titles_table)

print(f'Employees table',employees_table.shape)
print(f'Titles table',titles_table.shape)
# #   Is that what you expected?
        # Yes


# # 8. Display the summary statistics for each DataFrame.
print('\nExercises I, Question 8')
print(f'Employees table',employees_table.describe())
print(f'Titles table',titles_table.describe())

# # 9. How many unique titles are in the titles DataFrame?
print('\nExercises I, Question 9')
print(f'Titles table',limit_titles_table.title.nunique())
print(f'Titles table',len(limit_titles_table.nunique()))

# # 10. What is the oldest date in the to_date column?
print('\nExercises I, Question 10')
print(f'Titles table',titles_table.to_date.min())

# datetime.date(1985, 3, 1)

# # 11. What is the most recent date in the to_date column?
print('\nExercises I, Question 11')
# datetime.date(1999, 01, 01)

print(f'Titles table',titles_table.to_date.max())

print(f'Titles table',titles_table[titles_table.to_date != titles_table.to_date.max()])

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercises II
# 1. Copy the users and roles DataFrames from the examples above.
print('\nExercises II, Question 1')
print('Both DataFrames were copy')
# Create the users DataFrame.
import pandas as pd
import numpy as np

users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
print(f'\nUsers Table\n',users)

# Create the roles DataFrame
roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
print(f'\nRoles Table\n',roles)


# 2. What is the result of using a right join on the DataFrames?
print('\nExercises II, Question 2')

right_join = pd.merge(roles,users, how='right', right_on='id', left_on='id', indicator=True)
print(f'Right join\n',right_join)

# 3. What is the result of using an outer join on the DataFrames?
print('\nExercises II, Question 3')
outer_join = pd.merge(roles,users, how='outer', right_on='id', left_on='id', indicator=True)
print(f'Outer join\n',outer_join)

# 4. What happens if you drop the foreign keys from 
# the DataFrames and try to merge them?
print('\nExercises II, Question 4')
empty_users = users.drop(columns=['name','role_id'])
print(f'\nEmpty users table',empty_users)

empty_roles = roles.drop(columns=['name'])
print(f'\nEmpty roles table',empty_roles)


# 5. Load the mpg dataset from PyDataset.
print('\nExercises II, Question 5')

# 6. Output and read the documentation for the mpg dataset.
print('\nExercises II, Question 6')

# 7. How many rows and columns are in the dataset?
print('\nExercises II, Question 7')

# 8. Check out your column names and perform any cleanup 
# you may want on them.
print('\nExercises II, Question 8')

# 9. Display the summary statistics for the dataset.
print('\nExercises II, Question 9')

# 10. How many different manufacturers are there?
print('\nExercises II, Question 10')

# 11. How many different models are there?
print('\nExercises II, Question 11')

# 12. Create a column named mileage_difference 
# like you did in the DataFrames exercises; 
# this column should contain the difference between
#  highway and city mileage for each car.
print('\nExercises II, Question 12')

# 13. Create a column named average_mileage like 
# you did in the DataFrames exercises; this is the 
# mean of the city and highway mileage.
print('\nExercises II, Question 13')

# 14. Create a new column on the mpg dataset named
#  is_automatic that holds boolean values denoting
#  whether the car has an automatic transmission.
print('\nExercises II, Question 14')

# 15. Using the mpg dataset, find out which which
#  manufacturer has the best miles per gallon on average?
print('\nExercises II, Question 15')

# 16. Do automatic or manual cars have better miles per gallon?
print('\nExercises II, Question 16')





