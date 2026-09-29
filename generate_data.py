

# create 1000 datasets for train and test model 
import random
import pandas as pd

students = []  # create a empty list

for i in range(1000):
    # adding features(inputs)
   study_hours = round(random.uniform(0, 16), 1)     #Generate a random study time between 1 and 10, then keep one digit after the decimal.
   attendance = round(random.uniform(0,100), 1)
   previous_marks = round(random.uniform(0,100), 1)
   assignments = random.randint(0, 10)                #randint → whole number , uniform → decimal number
   internal_marks = round(random.uniform(0, 20), 1)
    # formula for output using linear regression
   final_marks = study_hours * 2.5 + attendance * 0.20 + previous_marks * 0.30 + assignments * 1.0 + internal_marks* 0.35 + random.uniform(-5, 5)
   final_marks = max(0, min(100, final_marks))

   students.append([ study_hours, attendance, previous_marks,assignments, internal_marks, round(final_marks, 1)]) 
# when loop run 1000 times, every time diff data append due to randomness in student list
#   So student list gradually becomes:
#  [6, 80, 70, 8, 65, 75],
#  [4, 75, 60, 7, 55, 68],
#  ....44

data = pd.DataFrame( students,
    columns=[
       "study_hours",
       "attendance",
       "previous_marks",
       "assignments",     
       "internal_marks",
       "final_marks"
    ]  
)
# students → our raw list of records
# pd.DataFrame() → converts it into a table
# columns=[...] → gives names to each column

data.to_csv("data.csv", index=False)        # save data as CSV,  index=False means Pandas won't add an unnecessary row-number column.
print("1000 students records created succesfully")
print(data.head())    #shows the first 5 rows so we can check whether our dataset looks correct
