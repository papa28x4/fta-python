'''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                           String
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''

# A sequence of characters enclosed within a single or double quote is referred to as a string

# a string using single quotes
word1 = 'learn'

# a string using double quotes
word2 = "python"

# Get the length of a string
print(word2, 'is', len(word2), 'characters long')

# Access string characters
intro = "hello world"

print(intro[4]) # prints o

# Python allows negative indexing
print(intro[-7]) # prints o

''' Slicing Operator colon : '''
# Using the Slice Operator, we can access range of characters
# [start_index:end_index] 
print(intro[1:5]) # prints ello (start from index 1 and stops at 4 (excludes 5))

# slice operator does not mutate the origin. It creates a copy


''' Strings are immutable '''
# Like in Javascript, strings in python cannot be modified. Any attempt to modify a character in a string
# will throw an error

b = 'unchangeable'
# b[5] = 'x' # throws error => TypeError: 'str' object does not support item assignment


''' Multiline String '''
 
# if you want to write a string that spans multiple lines, then you need use either """ or '''. E.g.

quote = """
Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. 
And the only way to do great work is to love what you do. If you haven’t found it yet, keep looking. Don’t settle. 
As with all matters of the heart, you’ll know when you find it.
                                        ------ Steve Jobs ------------
"""

print(quote)


''' IN keyword '''

# To check if a substring exists in a string, use IN keyword. If found returns True, otherwise False

lang = 'Javascript'

print('c' in lang) # prints True
print('Java' in lang) # prints True
print('z' in lang) # prints False