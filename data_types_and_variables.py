# 1. You have rented some movies for your kids: 
# The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), 
# and Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?

rental_lengths = [3,5,1]
rental_cost = 0
for n in rental_lengths:
    rental_cost += (n * 3)
print(rental_cost)


# 2. Suppose you're working as a contractor for 3 companies: 
# Google, Amazon and Facebook, they pay you a different rate per hour. 
# Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

g = 400
a = 380
f = 350
print((g * 6) + (a * 4) + (f * 10))

# 3 A student can be enrolled to a class only if the class is not full 
# and the class schedule does not conflict with her current schedule.

class_is_not_full = True
no_schedule_conflict = True
enrollment = class_is_not_full and no_schedule_conflict
print(enrollment)

# 4 A product offer can be applied only if people buys more than 2 items, and the offer has not expired. 
# Premium members do not need to buy a specific amount of products.

items_bought = 4
offer_not_expired = True
premium_member = False

offer_applied = premium_member or ((items_bought > 2) and offer_not_expired)

print(offer_applied)

# 5 Continue working in your data_types_and_variables.py file. Use the following code to follow the instructions below:
# username = 'codeup'
# password = 'notastrongpassword'
# Create a variable that holds a boolean value for each of the following conditions:
# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace

username = 'codeup'
password = 'notastrongpassword'
pw_min_5 = len(password) >= 5
un_max_20 = len(password) < 20
cannot_match = (password != username)

print(pw_min_5)
print(un_max_20)
print(cannot_match)



