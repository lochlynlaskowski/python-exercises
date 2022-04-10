# 1. Conditional Basics
# a. prompt the user for a day of the week, print out whether the day is Monday or not
# b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend
# c. create variables and make up values for
#   the number of hours worked in one week
#   the hourly rate
#   how much the week's paycheck will be
#   write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

if 'Monday' == input("Please enter the day of the week: "):
    print('Today is Monday.')
else:
    print('Today is not Monday.')
    
day_of_the_week = input('Please enter the day of the week: ')
if day_of_the_week in ('Saturday', 'Sunday'):
    print('Today is a weekend.')
else:
    print('Today is a weekday.')


hourly_rate = 22
hours_worked = int(input("Please enter the number of hours worked: "))
weekly_paycheck = (hourly_rate * hours_worked)
overtime_check = ((hourly_rate * 1.5) * (hours_worked - 40))

if hours_worked > 40:
    print(overtime_check + weekly_paycheck)
else: 
    print(weekly_paycheck)


# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.

i = 5
while i <= 15:
    print(i)
    i += 1

# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

i = 0
while i <= 100:
    print(i)
    i += 2

# Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i >= -10:
    print(i)
    i -= 5

# Create a while loop that starts at 2, and displays the number 
# squared on each line while the number is less than 1,000,000. 

i = 2
while i <= 1000000:
    print(i)
    i = i ** 2

# Write a loop that uses print to create the output shown below. 100 95 90 85 80 75 70 
# 65 60 55 50 45 40 35 30 25 20 15 10 5

i = 100
while i >= 5:
    print(i)
    i -= 5
# For Loops
# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

number = int(input('Please enter a number: '))
for i in range(1,11):
    print('{} * {} = {}'.format(number, i, (number * i)))