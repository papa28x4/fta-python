# We had earlier touched on Dictionaries but we want to delve deeper


# Dictionaries do not allow duplicate. The latter key will override the former key with the same name

animal = {
    'name': 'quincy',
    'type': 'dog',
    'breed': 'American Bulldog',
    'breed': 'German Shepherd'
}

print(animal)  # {'name': 'quincy', 'type': 'dog', 'breed': 'German Shepherd'}

# To get the number of items in a dictionary we use len() function

print('The number of items is:', len(animal))  # The number of items is: 3

''' Using the get() method'''
# Previously we mentioned that to access items in dictionary, we can reference it by its key within square brackets e.g.

print('animal type:', animal['type'])  # animal type: dog

# However, if we try to use a key that doesn't exist, we get a KeyError

# print('animal max speed:', animal['max-speed'])  # KeyError: 'max-speed' (Uncomment line to see error)

# Alternatively, we can use the get method to retrieve items from a dictionary
print('animal name:', animal.get('name'))  # animal name: quincy

# And if we try to access a non-existent key, get() method doesn't return an error. It returns None
print('animal max speed:', animal.get('max-speed'))  # animal max speed: None

''' Get all keys '''
# To get all the keys in a dictionary we use the keys() method.
print(animal.keys())  # dict_keys(['name', 'type', 'breed'])

# It returns the keys as a dict_keys object. If we want it as a list, we can typecast to a list
# by using the list constructor method. To Typecast means to convert from one datatype to another
print('keys lists:', list(animal.keys()))  # key lists: ['name', 'type', 'breed']

''' Get all values'''
# To get all the keys in a dictionary we use the values() method.
print(animal.values())  # dict_values(['quincy', 'dog', 'German Shepherd'])
# Typecast to a list
print('values list:', (list(animal.values())))


''' Get both the keys and values'''
# Use the items() method to get all keys and values in a dictionary

print(animal.items())  # dict_items([('name', 'quincy'), ('type', 'dog'), ('breed', 'German Shepherd')])
# Typecast to a list
print('items list:', (list(animal.items())))
# items list: [('name', 'quincy'), ('type', 'dog'), ('breed', 'German Shepherd')]

# You get a list of tuples with each tuple containing a key-value pair

''' Modifying a dictionary '''
# To change the animal's name
animal['name'] = 'Rocky'

print('updated animal:', animal)  # updated animal: {'name': 'Rocky', 'type': 'dog', 'breed': 'German Shepherd'}

# To add a new key
animal['legs'] = 4

print('updated2 animal:', animal)
# updated2 animal: {'name': 'Rocky', 'type': 'dog', 'breed': 'German Shepherd', 'legs': 4}

# We can also use the update method to achieve the same thing. The update() method will update the dictionary with the
# items from a given argument. If the item does not exist, the item will be added.
animal.update({'name': 'buddy'})

print('updated3 animal:', animal)
# updated3 animal: {'name': 'buddy', 'type': 'dog', 'breed': 'German Shepherd', 'legs': 4}

animal.update({'can_fly': False})

print('updated4 animal:', animal)
# updated4 animal: {'name': 'buddy', 'type': 'dog', 'breed': 'German Shepherd', 'legs': 4, 'can_fly': False}


''' Removing Items '''

# Using popitem() method
# Since dictionaries are now ordered, the popitem() method now removes the last inserted item. In Previous versions
# (i.e. version 3.6 and earlier), a random item is removed instead:

animal.popitem()
print('After popitem:', animal)
# After popitem: {'name': 'buddy', 'type': 'dog', 'breed': 'German Shepherd', 'legs': 4}
# As can be seen above, the can_fly key no longer exists because it was the last inserted item

# Using pop() method
# This gives you more control as you can specify the exact item you want to delete. Passing the key name to the pop()
# method removes that item.
# Let's remove the breed key
animal.pop('breed')
print('After breed key deletion:', animal)  # After breed key deletion: {'name': 'buddy', 'type': 'dog', 'legs': 4}

# To clear the all the items of a dictionary
animal.clear()
print('empty dictionary:', animal)  # empty dictionary: {}

# With clear(), the dictionary exists, but it's empty. If you want to remove the dictionary itself use the del statement

del animal

# If you attempt to print animal, it will return a not defined error because variable no longer exists
# print(animal) # NameError: name 'animal' is not defined (Uncomment line to see error)

''' Check if a key exists in Dictionary'''
# Use 'in' keyword to check if a key is present
# syntax: <key_name> in <dictionary_name>

student = {
    'name': 'David Jones',
    'sex': 'male',
    'age': 46,
    'level': 500,
    'paid': True
}

print('is age present?', 'age' in student)  # is age present? True
print('is department present?', 'department' in student)  # is department present? False

''' Loop over a Dictionary'''
# Method 1:
for key in student:
    print(key, student[key])

# Method 2:
for key, value in student.items():
    print(key, value)

# With both methods you get the output below
'''
name David Jones
sex male
age 46
level 500
paid True
'''

# If for any reason you need to retrieve the index number, you can wrap the dictionary within the enumerate function
for index, key in enumerate(student):
    print(index, key, student[key])

'''
0 name David Jones
1 sex male
2 age 46
3 level 500
4 paid True
'''

''' Copying a Dictionary'''
student2 = student

print('student2:', student2)  # student2: {'name': 'David Jones', 'sex': 'male', 'age': 46, 'level': 500, 'paid': True}

# This is student2 is a shallow copy of student. This means no new dictionary was created. Only a reference to the
# original dictionary is copied. In other words, student and student2 point to the same object. That is why if you
# modify student2, student will be affected and vice versa.

student2['age'] = 35

print('student:', student)  # student: {'name': 'David Jones', 'sex': 'male', 'age': 35, 'level': 500, 'paid': True}
print('student2:', student2)  # student2: {'name': 'David Jones', 'sex': 'male', 'age': 35, 'level': 500, 'paid': True}

# To really create independent copies
student3 = student.copy()
print('student3:', student3)  # student3: {'name': 'David Jones', 'sex': 'male', 'age': 35, 'level': 500, 'paid': True}

student3['name'] = 'Fredrick Forysth'

print('student:', student)  # student: {'name': 'David Jones', 'sex': 'male', 'age': 35, 'level': 500, 'paid': True}
print('std3:', student3)  # std3: {'name': 'Fredrick Forysth', 'sex': 'male', 'age': 35, 'level': 500, 'paid': True}