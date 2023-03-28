import pandas as pd
import numpy as np
from pydataset import data



fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", 
          "honeycrisp apple", "tomato", "watermelon", "honeydew", 
          "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", 
          "gooseberry", "papaya"]


type([fruits])

fruits[0]

pd.Series(fruits)
fruits_series = pd.Series(fruits)
# type(fruits_series)
# # # # # fruits_series

# # fruits_series.head()

# type(fruits_series)

# fruits_series

# # 1. Determine the number of elements in fruits.
print('\nQuestion 1')
print(fruits_series.size)
type(fruits_series)
fruits_series.size
fruits_series.count()
len(fruits_series)
fruits_series.index
fruits_series.shape
#         # 17


# # 2. Output only the index from fruits.
print('\nQuestion 2')
print(fruits_series.index)
fruits_series.index
    # RangeIndex(start=0, stop=17, step=1)
list(fruits_series.index)
print(list(fruits_series.index))

# # 3. Output only the values from fruits.
print('\nQuestion 3')
print(fruits_series.values)
fruits_series.values
#     # array(['kiwi', 'mango', 'strawberry', 'pineapple', 'gala apple',
#     #    'honeycrisp apple', 'tomato', 'watermelon', 'honeydew', 'kiwi',
#     #    'kiwi', 'kiwi', 'mango', 'blueberry', 'blackberry', 'gooseberry',
#     #    'papaya'], dtype=object)


# # 4. Confirm the data type of the values in fruits.
print('\nQuestion 4')
fruits_series.dtype
print(fruits_series.describe())
#     # dtype('O')

# # 5. Output only the first five values from fruits.
print('\nQuestion 5')
print(fruits_series.head())
#     # 0         kiwi
#     # 1         mango
#     # 2    strawberry
#     # 3     pineapple
#     # 4    gala apple


# # 5a. Output the last three values. 
print('\nQuestion 5a')
print(fruits_series.tail(3))
#     # 14    blackberry
#     # 15    gooseberry
#     # 16        papaya  
       
# # #5b. Output two random values from fruits.
print('\nQuestion 5b')
print(fruits_series.sample(2))
#     # 15    gooseberry 
#     # 8     honeydew


# # 6. Run the .describe() on fruits to see what information it 
# # returns when called on a Series with string values.
print('\nQuestion 6')
print(fruits_series.describe())
#     # count       17
#     # unique      13
#     # top       kiwi
#     # freq         4
#     # dtype: object

# # 7. Run the code necessary to produce only the unique string values from fruits.
print('\nQuestion 7')
for i in fruits_series.unique():
    print(i)
#     # kiwi
#     # mango
#     # strawberry
#     # pineapple
#     # gala apple
#     # honeycrisp apple
#     # tomato
#     # watermelon
#     # honeydew
#     # blueberry
#     # blackberry
#     # gooseberry
#     # papaya


# # 8. Determine how many times each unique string value occurs in fruits.
print('\nQuestion 8')
fruits_series.value_counts()
print(fruits_series.value_counts())
#     # kiwi                4
#     # mango               2
#     # strawberry          1
#     # pineapple           1
#     # gala apple          1
#     # honeycrisp apple    1
#     # tomato              1
#     # watermelon          1
#     # honeydew            1
#     # blueberry           1
#     # blackberry          1
#     # gooseberry          1
#     # papaya              1
#     # dtype: int64

# # Correct ans
fruits_series.nunique()
print('\n',fruits_series.nunique())

# # 9. Determine the string value that occurs "most" frequently in fruits.
print('\nQuestion 9')
fruits_series.mode()
print(fruits_series.mode())
# # 0    kiwi
# # dtype: object


# # You can also use this
fruits_series.describe()
print('\n',fruits_series.describe())

# # You can also use this
fruits_series.value_counts().nlargest()
print('\n',fruits_series.value_counts().nlargest())



# # 10. Determine the string value that occurs "least" frequently in fruits.
print('\nQuestion 10')
print(fruits_series.value_counts().nsmallest(keep='all'))


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercises Part II
# Explore more attributes and methods while you continue to work with the fruits Series.

# 1. Capitalize all the string values in fruits.
print("Original Array:")
print(fruits_series,'\n')
print('Part II, Question 1')
fruits_series.str.capitalize()
print(fruits_series.str.capitalize(),'\n')


# 2. Count the letter "a" in all the string values (use string vectorization).
print('Part II, Question 2')
fruits_series.str.count('a')
print(fruits_series.str.count('a'))

# 3. Output the number of vowels in each and every string value.
print('\nPart II, Question 3')

count = 0
dict = {}
for lines in fruits_series:
    for char in lines:
        if char in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            count += 1
            dict[lines] = count
    count = 0

for keys, values in dict.items():
    print (keys, values, 'vowels')



# 4. Write the code to get the longest string value from fruits.
print('\nPart II, Question 4')
max_length = fruits_series.str.len().max()
longest_fruit = fruits_series.loc[fruits_series.str.len().idxmax()]

print(f"Longest fruit is '{longest_fruit}' with length {max_length}.")



# 5. Write the code to get the string values with 5 or more letters in the name.
print('\nPart II, Question 5')

total_length = fruits_series.str.len()
fruits_series[total_length]
print(fruits_series[total_length >= 5])
print(total_length >= 5)


# 6. Find the fruit(s) containing the letter "o" two or more times.
print('\nPart II, Question 6')
print("Original Array:")
print(fruits_series,'\n')

fruits_series.str.contains('o')
print(fruits_series.str.contains('o'))
print(fruits_series[fruits_series.str.contains('o')])


# 7. Write the code to get only the string values containing the substring "berry".
print('\nPart II, Question 7')

fruits_series.str.contains('berry')
print(fruits_series[fruits_series.str.contains('berry','\n')],'\n')


# 8. Write the code to get only the string values containing the substring "apple".
print('\nPart II, Question 8')

fruits_series.str.contains('apple')
print(fruits_series[fruits_series.str.contains('apple')],'\n')


# 9. Which string value contains the most vowels?
print('\nPart II, Question 9')


max_count = 0
max_word = None

for word in fruits_series:
    vowel_count = 0
    for vowels in word:
        if vowels in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            vowel_count += 1
        
    if vowel_count > max_count:
        max_count = vowel_count
        max_word = word

print(f"The word with the most vowels is '{max_word}' with '{max_count}' vowels.")


print('\nPart II, Question 9 -Alternate solution')
def vowel_cnt(words):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in words:
            if char in vowels:
                count += 1
    return count

vowel_counts = fruits_series.apply(vowel_cnt)

max_index = vowel_counts.idxmax()
max_words = fruits_series[max_index]
print(max_index)
print(f"The word with the most vowels is '{max_words}' with '{max_index}' vowels.")
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercises Part III

#  Use pandas to create a Series named letters from the following string.
#  The easiest way to make this string into a Pandas series is to use list
#  to convert each individual letter into a single string on a basic Python list.

# 'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'
print('\nPart III, Setup')

def convert(string):
    list1 = []
    list1[:0] = string
    return list1

strl = "hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy"
str_slicing = convert(strl)

print(str_slicing)

pd.Series(str_slicing)
letters = pd.Series(str_slicing)
print(letters)

# 1. Which letter occurs the most frequently in the letters Series?
print('\nPart III, Question 1')
letters.mode()
print(f"This is the letter that occurs the most frequently '{letters.mode()}'.")

# # You can also use this
letters.describe()
print('\n',letters.describe())

# # You can also use this
letters.value_counts().nlargest()
print('\n',letters.value_counts().nlargest())


# 2. Which letter occurs the Least frequently?
print('\nPart III, Question 2')
print(letters.value_counts().nsmallest(1,keep='first'))
    # l is the letter that occurs the least frequantly

# 3. How many vowels are in the Series?
print('\nPart III, Question 3')
vowels = list('aeiou')
vowels_mask = letters.isin(vowels)
num_vowels = vowels_mask.sum()

# A one liner - 
num_vowels = letters.isin(vowels).sum()
print(num_vowels)
    # 34 vowels

# 4. How many consonants are in the Series?
print('\nPart III, Question 4')
vowels = list('aeiou')
consonants_mask = ~letters.isin(vowels)
num_consonants = consonants_mask.sum()
print(num_consonants)
    # 166 consonants

# 5. Create a Series that has all of the same letters but uppercased.
print('\nPart III, Question 5')
letters.str.upper()
print(letters.str.upper())

# 6. Create a bar plot of the frequencies of the 6 most commonly occuring letters.
print('\nPart III, Question 6')

letters.value_counts().nsmallest(6,keep='first').plot.bar(title='Frequency of the 6 most commonly occuring letters', 
                                rot=0,color='blue',
                                ec='black',width=.9).set(xlabel='Letters',ylabel='Frequency')
