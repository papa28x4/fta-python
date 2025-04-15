'''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                            List
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''

# When we want to store a collection of data(i.e. multiple objects), we can use either a list, tuple, set or dictionary.

# Lists are denoted by square brackets and the items in a list are separated by commas.

# The list in python is similar in many ways to the array in Javascript

countries = []  # This creates an empty list

continents = list()  # This is the alternative way to create an empty list

# a list of five countries

countries = ['Nigeria', 'Ghana', 'Egypt', 'Benin', 'South Africa']

# A list can contain items of different datatypes.

student = ['Kunle', 19, 'Engineering', True, None]


'''
List Characteristics
'''

# They maintain the order of elements
# A list can be modified after creation
# They can contain duplicate values


'''
Getting the length of list
'''
# To get the number of items contained in a list, we can use the len() function
print('number of countries:', len(countries))


'''
Accessing a list
'''

# List like array in Javascript are zero-based indexed. This means the index of the first item in a list
# is zero.

languages = ['HTML', 'CSS', 'SQL', 'PHP']

print(languages[0])  # prints HTML
print(languages[3])  # prints PHP

############################### Negative Indexing #############################################################

# Unlike Javascript Arrays, Python Lists support negative indexing

print(languages[-1])  # prints PHP (which is the last item in the array or the first counting from the right)
print(languages[-2])  # prints SQL (which is the second item counting from the right)


# Let see what happens when you try to get an index that does not exist
# print(languages[5]) # this throws up an "IndexError: list index out of range" error


'''
Change a specific List Item
'''
# We can change the items of a list by assigning new values using the = operator.
# Assuming we no longer want to learn PHP. So we want to replace PHP with Python

languages[-1] = "Python"

print("Updated Languages:", languages)


'''
Slicing a List
'''

# In javascript, to slice an array you would do use slice() method e.g. array.slice(start_index, end_index)
# In python to slice a list, you would use the slicing operator :
# syntax => List_variable_name[start_index : end_index]. The end_index will not be included in the slice.

# Example:
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# get a list of items from index 2 to index 5 (index 6 will not be included)
print("alphabets[2:6]=", alphabets[2:6])  # prints ['c', 'd', 'e', 'f']

# get a list with items from index 2 to index -3 (index -2 will not be included)
print("alphabets[2:-2]=", alphabets[2:-2])  # prints ['c', 'd', 'e', 'f']


########################### Omitting Start and End Indices in Slicing ##########################################

# If you omit the start index, slicing will start from the first element
# If you omit the end index, slicing will go all the way to include last element

# get a list with items from index 3 to last
print("alphabets[5: ] =", alphabets[3:])

# get a list from the first item to index 4
print("alphabets[: 5] =", alphabets[:5])

# omitting both start and end index will get a list from start to end items.
# This is one way to make a copy of a list because every item on original list is sliced.
print("alphabets[:] =", alphabets[:])

# Note: The slice operator creates a new list. It does not mutate the original list


'''
Add an item to a Python List
'''

##
# In Javascript, you would use push() method to add an item to end of an array
# In Python, you would use the append() method

states = ["Ekiti", "Plateau", "Imo", "Borno"]

states.append("Kano")

print("Updated States:", states)


'''
Add Elements to a Python List
'''
# The append() method adds just one element to the end of a list. If you want to add multiple elements to
# the end of a list, the extend() method should be used

states.extend(["Katsina", "Benue"])

print("Extended State list:", states)


'''
Add Elements at the Specified Index
'''

# Sometimes we want to add an element but not to end. The insert() method gives us the flexibility to insert
# an element at any index in a list

# To add Delta between Ekiti and Plateau

states.insert(1, "Delta")  # 1 represents the specific index where the insertion should occur

print("Updated State list after insertion:", states)


# Note: The append(), extend() and insert() methods mutate the original array

'''
Remove an Item From a List
'''

# We can remove the specified item from a list using the remove() method.

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# remove "Tuesday" from days
days.remove("Tuesday")

print('days:', days)

'''
Remove One or More Elements of a List
'''

# remove() can only remove one item. To remove one or more items, we can use del statement.
fruits = ["apple", "banana", "grapes", "carrot", "dates", "coconut", "soursop", "pineapple"]

# delete the item at index 1
del fruits[1]  # This deletes banana from fruits
print('updated fruits:', fruits)  # prints => ['apple', 'grapes', 'carrot', 'dates', 'coconut', 'soursop', 'pineapple']

# delete items from index 1 to index 3
del fruits[1:4]  # This deletes banana from fruits
print('updated fruits after deleting index 1 to 3:', fruits)  # prints => ['apple', 'coconut', 'soursop', 'pineapple']

# The del state can also be used to delete the entire list
del fruits

print(fruits)  # This will now throw a "NameError: name 'fruits' is not defined" indicating the fruits list is gone












