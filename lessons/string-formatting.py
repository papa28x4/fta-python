'''
Python String Formatting
'''

# It is a common routine to concatenate strings with variables. Python offers several ways to achieve this

''' Method 1 '''
### The + operator ###
first_name = "Jamie"
last_name = "Foxx"
full_greeting = "Hello, " + first_name + " " + last_name + "!"

print('full greeting from + operator:', full_greeting)  # Hello, Jamie Foxx!

# If you attempt to use the + operator on a string and an integer, you will get an error
# print("8" + 8)  # TypeError: can only concatenate str (not "int") to str

# The above behaviour is different from what Javascript would do. It won't throw an error. Rather Javascript will do a
# type coercion converting the integer to a string and concatenate them.
# console.log("8" + 8)  # 88


''' Method 2'''
### Using the % operator ###
# % is the modulus operator when applied on integers but when applied on a string, % becomes the format operator.
# The format operator uses symbols like %d, %f, %s etc as placeholders that would be eventually  replaced with
# the data stored in variables. Although it's the old way of doing string formatting, it's still
# important to understand it because you might come across it in legacy code.

# If there is just one replacement variable, you don't need brackets
count = 36
fact = "Nigeria has %d states" % count
print("Naija fact:", fact)  # Nigeria has 36 states

# If there is more than one replacement variable, they should be enclosed in brackets separated by commas.
# The replacement is dependent on the order of the variables. The first variable (first_name) will replace the first %s,
# while the second variable will replace the second %s.

full_greeting = "Hello, %s %s!" % (first_name, last_name)
print('full greeting from % operator:', full_greeting)  # Hello, Jamie Foxx!


# name='TutorialsPoint'
# print ('Welcome To %.5s The largest Tutorials Library' % (name, ))


''' Method 3'''
# The format method
# The format method uses curly bracket {} as placeholders. There are 3 ways to apply the format method:

# Using empty placeholders
biodata = "My name is {}, I'm {}".format("John", 36)
print('biodata1:', biodata)  # prints => My name is John, I'm 36

# Using numbered indexes
# string.format(0, 1, 2 ... )
biodata = "My name is {0}, I'm {1}".format("John", 36)
print('biodata2:', biodata)  # prints => My name is John, I'm 36

choice = "I prefer {1} to {0}".format("apples", "grapes")
print("My choice: ", choice)  # prints => I prefer grapes to apples

# Using named indexes
biodata = "My name is {fname}, I'm {age}".format(fname="John", age=36)
print('biodata3:', biodata)  # prints => My name is John, I'm 36



''' Method 4'''
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