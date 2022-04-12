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

# Create a for loop that uses print to create the output shown below.
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

for i in range(1,10):
    print(str(i) * i)
    i += 1

# break and continue

# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue 
# prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). 
# Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

# Your output should look like this:
# Number to skip is: 27

# Here is an odd number: 1
# Here is an odd number: 3
# Here is an odd number: 5
# Here is an odd number: 7
# Here is an odd number: 9
# Here is an odd number: 11
# Here is an odd number: 13
# Here is an odd number: 15
# Here is an odd number: 17
# Here is an odd number: 19
# Here is an odd number: 21
# Here is an odd number: 23
# Here is an odd number: 25
# Yikes! Skipping number: 27
# Here is an odd number: 29
# Here is an odd number: 31
# Here is an odd number: 33
# Here is an odd number: 35
# Here is an odd number: 37
# Here is an odd number: 39
# Here is an odd number: 41
# Here is an odd number: 43
# Here is an odd number: 45
# Here is an odd number: 47
# Here is an odd number: 49

number = input('Please enter an odd number between 1 and 50: ')
while True:

    if not number.isdigit():
        print('That is not a number! Try again.')
        number = input('Please enter an odd number between 1 and 50: ')
        continue
        
    else:
        break
        
for i in range(1, 50, 2):
    if i == number:
        print(f'Yikes! Skipping number: {i}')
        continue
    print(f'Here is an odd number: {i}')

