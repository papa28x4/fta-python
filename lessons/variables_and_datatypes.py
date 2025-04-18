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

''' Swap Variables'''

pos_one = 1
pos_two = 2

pos_one, pos_two = pos_two, pos_one

print('pos_one after swap:', pos_one)  # prints 2
print('pos_two after swap:', pos_two)  # prints 1


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
print(number1, 'is of type', type(number1))  # prints <class 'int'>

number2 = 8.0
print(number2, 'is of type', type(number2))  # prints <class 'float'>

number3 = 1+4j
print(number3, 'is of type', type(number3))  # prints <class 'complex'>


################################## String ################################################################

# String holds sequence of characters. It is enclosed with single quote or double quotes

sentence = 'I am string'

print(sentence, 'is of type', type(sentence))  # prints => <class 'str'>


#################################### Boolean #############################################################

# This represents one of the two values: True or False
# Notice the boolean values start with uppercase whereas in Javascript it is true or false

a = True
print('True is of type:', type(a))  # prints => <class 'bool'>

b = False
print('False is of type:', type(b))  # prints => <class 'bool'>

# Each time you compare two values, Python returns a boolean
score1 = 40
score2 = 30
print('Is score1 less than score2?', score1 < score2)  # False
print('Is score1 equal to score2?', score1 == score2)  # False
print('Is score1 more than score2?', score1 > score2)  # True

######### Truthy and Falsy ###########
# Truthy and Falsy refer to values of other data types that evaluate to True and False respectively when evaluated in
# a boolean context. The bool function is used to coerce other data types into a boolean.

# Most Values are True (Truthy)
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.

print("empty string =>", bool(''))  # Falsy
print("zero =>", bool(0))  # Falsy
print("empty list =>", bool([]))  # Falsy
print("empty tuple => ", bool(()))  # Falsy
print("empty set => ", bool(set()))  # Falsy
print("empty dict => ", bool({}))  # Falsy


##################################### List ################################################################
# A list is an ORDERED collection of items. A list has items separated by comma wrapped in square brackets. It shares a
# lot of similarities with the array in Javascript

list_example = ["BMW", "Benz", "Volvo", "Toyota", "Audi"]

print(list_example, 'is of type', type(list_example))  # prints => <class 'list'>

# Because they are ordered, they can be accessed with the index number starting from zero
print('first item in list_example', list_example[0])
print('second item in list_example', list_example[1])
print('third item in list_example', list_example[2])


# We delve deeper into lists in a future lesson


##################################### Tuple ################################################################
# Like a list, a tuple is an ordered collection of items. The difference between them is that a tuple is immutable.
# This makes tuples a good choice when you want the data in your collection to be read-only and constant.
# A Tuple is denoted by comma separated values enclosed in parentheses.

# Create an empty tuple
tuple1 = ()

# A tuple with content
tuple2 = ("hello", "world")

print(tuple2, 'is of type', type(tuple2))  # prints => <class 'tuple'>

# A tuple with one element
# To create a tuple with one item, you must include a comma after the item, otherwise Python will see it as a string

data1 = ("home alone",)
data2 = ("home alone")
print("data1 is of type:", type(data1))  # <class 'tuple'>
print("data2 is of type:", type(data2))  # <class 'str'>


# Let's see an example of the immutability of tuples
my_list = ["One", "Three", "Five", "Seven"]
my_tuple = ("One", "Three", "Five", "Seven")

my_list[1] = "Eight"
print('updated my_list', my_list)  # ['One', 'Eight', 'Five', 'Seven']

# If you try to do the same with a tuple, you get a type error
# my_tuple[1] = "Eight"  # TypeError: 'tuple' object does not support item assignment (Uncomment and run to see error)

# Like lists, tuples can be accessed using the index number
print('To get the first item from left to right:', my_tuple[0])  # One
print('To get the last item or the first from the right to left:', my_tuple[-1])  # Seven


##################################### Set ################################################################

# A set holds a collection of unique items. Duplicates are not allowed.
# Unlike tuples and lists, sets are unordered. This means you can't use index numbers because the order is not
# guaranteed i.e. random order
# A set is enclosed in curly brackets

my_set = {"Lagos", "Kano", "Enugu"}

# The set() function creates a set object
new_set = set()
print(new_set)  # set()

scores = [65, 56, 54, 65, 70, 45, 70, 90]
# pass the scores list to the set function to convert it to set
unique_scores = set(scores)
print('unique scores =>', unique_scores)  # {65, 70, 45, 54, 56, 90} #it dropped duplicates

##################################### Dictionary ################################################################
# Just like your normal english dictionary has a words and meanings, python dictionary in similar fashion has keys
# and values {key:value}. It's similar to object data type in Javascript.

# In Python 3.6 and earlier, dictionaries were unordered but from Python version 3.7, dictionaries are ordered.
# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will
# not change.

# To create an empty dictionary
new_dict = {}
new_dict2 = dict()

# The dictionary can contain values of any data type:
my_dict = {
  "customer": "Shola",
  "years": 2,
  "paid": True,
  "package": ["diamond", "gold", "silver"]
}

####### Accessing a dictionary ###########
# We use the key to access a dictionary
print("customer name:", my_dict["customer"])

# Dictionaries are very important data type. We talk about dictionaries in greater detail in a future lesson
