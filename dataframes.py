from pydataset import data
import pandas as pd
import numpy as np

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

type(df)

# data('mpg', show_doc=True) # view the documentation for the dataset
mpg = data('mpg') # load the dataset and store it in a variable


# 1. Copy the code from the lesson to create 
# a dataframe full of student grades.
print(f'Part I, Question 1')
print(type(df))
print(df)

# a. Create a column named passing_english that 
# indicates whether each student has a passing 
# grade in english.
print(f'\nPart I, question a')
passing_english = df.loc[df['english'] >= 70, 'passing_english'] = 'Passing'
failing_english = df.loc[df['english'] < 70, 'passing_english'] = 'Failing'
print(df)


# b. Sort the english grades by the passing_english column. 
# How are duplicates handled?
    # duplicates are not ignore
print(f'\nPart I, Question b')
df_sort = df.sort_values(by='passing_english')
print(df_sort)


# c. Sort the english grades first by passing_english and then by student name. 
# All the students that are failing english should be first,
#  and within the students that are failing english they should be 
# ordered alphabetically. The same should be true for the students passing english. 
# (Hint: you can pass a list to the .sort_values method)
print(f'\nPart I, Question c')
df_sort2 = df.sort_values(by=['passing_english','name'])
print(df_sort2)


# d. Sort the english grades first by passing_english, 
# and then by the actual english grade, similar to how we did in the last step.
print(f'\nPart I, Question d')
df_sort3 = df.sort_values(by=['passing_english','english'], ascending=(True, False))
print(df_sort3)

# e. Calculate each students overall grade and add it as a column on the dataframe.
#  The overall grade is the average of the math, english, and reading grades.
print(f'\nPart I, Question d')
df['overall_grade'] = df.mean(axis=1)
print(df)

df['overall'] = round((df.math + df.english + df.reading)/3, 2)
 
# 2. Load the mpg dataset. Read the documentation for the dataset and use it for 
# the following questions:

# Load the dataset and store it in the variable mpg.
print(f'\nPart II, Question 1')
from pydataset import data
mpg = data('mpg')
mpg.head()


# a. How many rows and columns are there?
print(f'\nPart II, Question a')
data('mpg', show_doc=True) 


# b. What are the data types of each column?
print(f'\nPart II, Question b')
mpg.head()
print(mpg.head())


# c. Summarize the dataframe with .info and .describe
print(f'\nPart II, Question c')
mpg = data('mpg')
print('\nInfo')
print(mpg.info())
print('\nDescribe')
print(mpg.describe())


# d. Rename the cty column to city.
print(f'\nPart II, Question d')
mpg.rename(columns={'cty': 'city'}, inplace=True)
print(mpg)


# e. Rename the hwy column to highway.
print(f'\nPart II, Question e')
mpg.rename(columns={'hwy': 'highway'}, inplace=True) # if you put inplace it saves automatically
print(mpg)

# f. Do any cars have better city mileage than highway mileage?
print(f'\nPart II, Question f')
mpg['better_gas'] = mpg['city'] > mpg['highway'] # create a new column indicating whether city gas mileage is better than highway gas mileage
cars_with_better_city_mileage = mpg[mpg['better_gas']] # subset the data to get only the rows where city gas mileage is better than highway gas mileage

if cars_with_better_city_mileage.empty:
    print('No cars have better city mileage than highway mileage.')
else:
    print('The following cars have better city mileage than highway mileage:\n')
    print(cars_with_better_city_mileage[['manufacturer', 'model']])

print(mpg)

# g. Create a column named mileage_difference this column should 
# contain the difference between highway and city mileage for each car.
print(f'\nPart II, Question g')
mpg['mileage_difference'] = mpg['highway'] - mpg['city']
print(mpg.head())

# h. Which car (or cars) has the highest mileage difference?
print(f'\nPart II, Question h')
# mpg[mpg.mileage_difference == mpg.mileage_difference.max()].value_count()
mpg[mpg.mileage_difference == mpg.mileage_difference.max()]

print(mpg)

# i. Which compact class car has the lowest highway mileage? The best?
print(f'\nPart II, Question i')
mpg['class'] == 'compact'

mpg[mpg['class'] == 'compact']

mpg_compact = mpg[mpg['class'] == 'compact']

# mpg_compact.hightway.min()
mpg_compact[mpg_compact.highway == mpg_compact.highway.min()]
mpg_compact[mpg_compact.highway == mpg_compact.highway.max()]

# j. Create a column named average_mileage that is the mean of the city 
# and highway mileage.
print(f'\nPart II, Question j')
mpg['avg_milage'] = (mpg.city + mpg.highway)/2
print(mpg.head())


# k. Which dodge car has the best average mileage? The worst?
print(f'\nPart II, Question k')
mpg_dodge = mpg[mpg.manufacturer == 'dodge']

mpg_dodge.head()

mpg_dodge[mpg_dodge.avg_milage == mpg_dodge.avg_milage.min()]


# 4. Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:
print(f'\nPart III, Load the Mamals dataframe')

data('Mammals', show_doc=True)

mams = data('Mammals')


# a. How many rows and columns are there?
print(f'\nPart III, Question a')
mams.shape

# b. What are the data types?
print(f'\nPart III, Question b')
mams.head()

# c. Summarize the dataframe with .info and .describe
print(f'\nPart III, Question c')
mams.info()
mams.describe()
# d. What is the the weight of the fastest animal?
print(f'\nPart III, Question d')
mams.speed.max()
mams[mams.speed == mams.speed.max()]


# e. What is the overal percentage of specials?
print(f'\nPart III, Question e')
mams.specials.sum()
len(mams)
(mams.specials.sum()/len(mams))*100
    # 9.345794392523365

mams.specials.value_counts(True)


# f. How many animals are hoppers that are above the median speed? 
print(f'\nPart III, Question f')
mams_columns = mams.columns
print(mams_columns)

mams[mams.hoppers]
print('\n',mams[mams.hoppers])

mams_hop = [mams.speed > mams.speed.median()]
print('\n',mams_hop)

mams_hop_median = mams[(mams.hoppers == True) & (mams.speed > mams.speed.median())]

round(len(mams[(mams.hoppers == True) & (mams.speed > mams.speed.median())])/len(mams) * 100, 2)

hoppers = mams[(mams.hoppers == True)]
hoppers.head()
print('\n',hoppers.head())

# What percentage is this?
print(f'\nPart III, Question f(a)')
percentage = round(len(hoppers[(hoppers.speed > mams.speed.median())]) /len(mams) *100, 2)

print(f'The percentage is', percentage)
