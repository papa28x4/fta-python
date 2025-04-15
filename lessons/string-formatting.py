'''
Python String Formatting
'''

# This is the preferred way to format a string. This feature is available in python 3.6 and above
# To use f-string, put an f in front of the string like this:

name = "John Doe"
age = 46
sex = "male"

bio = f"I am {name}, {sex}, {age} years old."

print(bio)  # prints => I am John Doe, male, 46 years old.

price = 865

market_report = f"Fuel price is now N{price}"

print(market_report)  # prints => Fuel price is now N865

################ Using Modifiers ##################################
# A modifier is included by adding a colon : followed by a legal formatting type, like .2f
# which means fixed point number with 2 decimals:

# if we want to display price with 2 decimal places

market_report = f"Fuel price is now N{price:.2f}"

print(market_report)  # prints => Fuel price is now N865.00