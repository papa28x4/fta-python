'''
Comments
'''


# Comments can be used to provide explanation for a line or block of code. This improves
# the readability for you and others. The python interpreter skips comments and does not
# attempt to execute them. Because of the above, comments can also be used to temporarily
# make certain parts of our code inactive. This is useful when debugging as it can help us
# narrow down where the bug is originating from.

# To comment a line of code in python, we use the hash symbol (#). E.g
# In Javascript, it is double forward slashes //

# To print out to the terminal, we use the print function
print('Hello World')


# To comment out multiple lines we use either triple single quotes or triple double quotes
'''
print('a')
print('b')
print('c')
'''

"""
print('a')
print('b')
print('c')
"""

# To do same in Javascript => /*  multilines */




'''
Print Function
'''

# Print is to Python what console.log is to Javascript
# With the Print function, you can output the result of variables, functions, classes etc

# When you have multiple print statements, it's a good idea to label them, so
# you'd easily identify which output belongs to a particular print statement.

a = 5
b = 4

# labelling it as shown below improves readability
print('5 times 4 =', a*b)
print('5 plus 4 =', a+b)
print('5 minus 4 =', a-b)
print('5 divided 4 =', a/b)



''' Print sep parameter '''

# sep is short for separator. By default, sep is set to a single space (sep=" "), so when you print the line below
print('Lagos', 'Ondo', 'Ogun', 'Oyo')  # it prints => Lagos Ondo Ogun Oyo

# If you want to separate the states in the print function with another separator other than the default
print('Lagos', 'Ondo', 'Ogun', 'Oyo', sep=" | ")  # prints => Lagos | Ondo | Ogun | Oyo

print('Lagos', 'Ondo', 'Ogun', 'Oyo', sep=" & ")  # prints => Lagos & Ondo & Ogun & Oyo


''' Print end parameter '''

# Print by default puts a line return or "\n" at the end of each print command. This makes each print statement output
# its content on a new line below that of the previous print statement. This happens because the end argument is set to
# new line by default (end="\n"). This behaviour can be changed by supplying a different value to the "end" argument

# Default behaviour (end="\n")
print('*')
print('*')
print('*')
# OUTPUT
'''
*
*
*
'''

# Make these multiple print statements print on one line
print('*', end="")
print('*', end="")
print('*')
# OUTPUT => ***

# Make these multiple print statements print on one line separated by a semicolon
print("Lagos", end="; ")
print("Ondo", end="; ")
print("Ogun", end="; ")
print("Oyo")

# OUTPUT => Lagos; Ondo; Ogun; Oyo


# Note: sep defines the behaviour of one print statement; end defines the behaviour of multiple print statements





''' 
help command
'''

# Help like its name implies is there to assist you. You just pass in a valid Python function to the help command, and
# it would show what that function is used for and the options (arguments) that available to you.

help(print)
