# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number 
# or the string 2, False otherwise.

def is_two(number):
    if number == '2' or number == 2:
        return True
    else: 
        return False
    

    
    
# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(string):
    if type(string) == str:
        result = string.lower() in 'a, e, i, o, u'
        return result
    else:
        return False
    


# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. 
# Use your is_vowel function to accomplish this.
def is_consonant(string):
    if type(string) == str:
        only_letters = string.isalpha()
        return only_letters and not is_vowel(string)
    else:
        return True
    


# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if
#  the word starts with a consonant.

def cap_word(word):
    if is_consonant(word[0].lower()):
        return (word[0].upper() + word[1:])
    else:
        return word  
    


# instructor answer
def capitalize_starting_consonant(string):
    if type(string) != str:
        return False
    first_letter = string[0]
    if is_consonant(first_letter):
        string = string.capitalize()
    return string


# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, 
# and return the amount to tip.

def calculate_tip(x,y):
    bill = x
    tip = y
    total_bill = (x * y) + x
    return(total_bill)



# instructor answer
def calculate_tip(bill, tip_percentage=0.2):
    if type(tip_percentage) != float:
        return False
    if tip_percentage < 0 or tip_percentage > 1:
        return 'the tip percentage must be between 0 and 1'
    return tip_percentage * bill
    

# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the 
# price after the discount is applied.

def apply_discount(x,y):
    original_price = x
    discount = y
    new_price = x - (x * y)
    return(new_price)



# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input,
#  and return a number as output.

def handle_commas(str):
    return int(str.replace(',',''))



# instructor answer
def handle_commas(somestring):
    if type(somestring) != str:
        return 'input must be a string'
    somestring = somestring.replace(',', '')
    if somestring.isdigit():
        return float(somestring)
    else:
        return 'input must be a string that is a number'

# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that 
# number (A-F).

def get_letter_grade(number):
    if number >= 90:
        letter = 'A'
    elif number >= 80:
        letter = 'B'
    elif number >= 70:
        letter = 'C'
    elif number >= 60:
        letter = 'D'
    else:
        letter = 'F'
        
    return(letter)


# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(string):
    if type(string) != str:
        return False
    output=''
    for letter in string:
        if is_consonant(letter):
            output += letter
    return output



# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed

def normalize_name(string):
    output = ''
    string = string.lower()
    for char in string:
        if char.isidentifier() or char == ' ':
            output += char
    output = output.strip()
    output = output.replace(' ', '_')
    return output


# Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of 
# the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(numbers):
    output = []
    for n, number in enumerate(numbers):
        sum_for_now = sum(numbers[:n +1])
        output.append(sum_for_now)
    return output



