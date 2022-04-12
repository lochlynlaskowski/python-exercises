# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number 
# or the string 2, False otherwise.

def is_two(number):
    if number == '2' or number == 2:
        return True
    else: 
        return False
    
print(is_two('4'))
    
    
# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(n):
    if n.lower() in 'a, e, i, o, u':
        return True
    else:
        return False
    
print(is_vowel('E'))

# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. 
# Use your is_vowel function to accomplish this.
def is_consonant(n):
    if only_letters == n.isalpha()
        return only_letters and not is_vowel
    else:
        return True
    
print(is_consonant('d'))

# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if
#  the word starts with a consonant.

def cap_word(word):
    if is_consonant(word[0].lower()):
        return (word[0].upper() + word[1:])
    else:
        return word  
    
print(cap_word('bapple'))


# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, 
# and return the amount to tip.

def calculate_tip(x,y):
    bill = x
    tip = y
    total_bill = (x * y) + x
    return(total_bill)
print(calculate_tip(100, .25))
    

# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the 
# price after the discount is applied.

def apply_discount(x,y):
    original_price = x
    discount = y
    new_price = x - (x * y)
    return(new_price)
print(apply_discount(50, .05))


# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input,
#  and return a number as output.

def handle_commas(str):
    return int(str.replace(',',''))

print(handle_commas('3,700,743'))

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
print(get_letter_grade(73)) 

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(str):

# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed
# Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]