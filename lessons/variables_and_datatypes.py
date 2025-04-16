'''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                            Variables
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''


# A variable is a container that holds data. Unlike Javascript, in Python there is no keyword like var, let or const
# before the variable name.
word = "Hello World"

# word is a variable storing the value "Hello World"
# We can use the print function to see the content of a variable
print(word)  # prints => word

# In Javascript, we can declare a variable without assigning it a value. We cannot do that in Python. When we declare
# a variable, we must assign it a value.

# If for some reason we want the variable to be empty, then we can assign it None (This is like Null in Javascript) e.g.

count = None

'''
Assigning multiple values to multiple variables
'''

# You can do it like this
name = 'John Doe'
age = 48
sex = 'male'

# OR you can do all on one line

name, age, sex = 'John Doe', 48, 'male'

print(name)  # prints John Doe
print(age)   # 48
print(sex)   # male

'''To assign the same value to multiple variables'''

score1 = score2 = score3 = 80

print(score1)  # prints 80
print(score2)  # prints 80
print(score3)  # prints 80

''' Swapping Variables'''

pos_one = 1
pos_two = 2

pos_one, pos_two = pos_two, pos_one

print('pos_one after swap:', pos_one)
print('pos_two after swap:', pos_two)


'''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                            Data Types
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''

# Variables can store different datatypes. To get the datatype, use the type() function

############################## Numeric ###############################################################

# Numeric data type is used to hold numeric values
# Integers, floating-point numbers and complex numbers are classified under the number data type


number1 = 40
print(number1, 'is of type', type(number1)) # prints <class 'int'>

number2 = 8.0
print(number2, 'is of type', type(number2)) # prints <class 'float'>

number3 = 1+4j
print(number3, 'is of type', type(number3)) # prints <class 'complex'>


################################## String ################################################################

# String holds sequence of characters. It is enclosed with single quote or double quotes


sentence = 'I am string'

print(sentence, 'is of type', type(sentence))  # prints => <class 'str'>


#################################### Boolean #############################################################

# This represents one of the two values: True or False
# Notice the boolean values start with uppercase unlike Javascript where it is true or false

a = True
print('True is of type:',type(a))  # prints => <class 'bool'>

b = False
print('False is of type:', type(b))  # prints => <class 'bool'>

# Each time you compare two values, Python returns a boolean
score1 = 40
score2 = 30
print('Is score1 less than score2?', score1 < score2)
print('Is score1 equal to score2?', score1 == score2)
print('Is score1 more than score2?', score1 > score2)

######### Truthy and Falsy ###########
# Truthy and Falsy refer to values of other data types that evaluate to true and false respectively when evaluated in
# a boolean context. The bool function is used to coerce other data types into a boolean

# Most Values are True (Truthy)
#
# Any string is True, except empty strings.
#
# Any number is True, except 0.
#
# Any list, tuple, set, and dictionary are True, except empty ones.

print("empty string =>", bool(''))  # Falsy
print("zero =>", bool(0))  # Falsy
print("empty list =>", bool([]))  # Falsy
print("empty tuple => ", bool(()))  # Falsy
print("empty set => ", bool(set()))  # Falsy
print("empty dict => ", bool({}))  # Falsy

##################################### List ################################################################



# Sequence => list, tuple, range (holds collection of items)
# Boolean => bool (holds either True or False)
# Set => set (holds collection of unique items)