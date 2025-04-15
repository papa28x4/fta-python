# laugh = "ha"
# full_laugh = laugh * 3
# print(full_laugh)

words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print("Sentence:", sentence)


''' (1) Strip() '''
# This removes all leading and trailing spaces

greeting = 'hello'
word = '  world  '
exclamation = '!'
print('before strip:', greeting+word+exclamation)  #  hello  world  !
print('after strip:', greeting+word.strip()+exclamation)  # helloworld!

# You can also specify the leading and trailing character it should remove

print('###testing###'.strip('#')) # prints => testing

# Note: it will only remove the character if it's in-front or at the back not in the middle. e.g.
print('###te#st#ing###'.strip('#')) # prints => te#st#ing

# if you want to remove space on the left side (leading space)
print(' remove-leading-space'.lstrip())  # remove-leading-space
# if you want to remove space on the right side (trailing space)
print('remove-trailing-space  '.rstrip()) # remove-trailing-space


''' (2) Replace() '''
# This will replace all the occurences of a given string with another
# syntax: string.replace(oldvalue, newvalue, count)

chain = "Mountains-can-be-surmounted"
print('replace-all:', chain.replace('-', '&'))  # prints => Mountains&can&be&surmounted

# If you don't want all occurrences to be replaced, then you can specify a value for the third argument(count)
# Because we gave count a value of 1, only one of dashes was replaced
print('replace-just-one:', chain.replace('-', '&', 1))  # prints => Mountains&can-be-surmounted


''' (3) Split() '''
# This splits a string into a list (list is to python what array is to Javascript). By default, the split will use the
# space character to break up a string

sentence = "I heard Python is easy"
print(sentence.split())  # prints => ['I', 'heard', 'Python', 'is', 'easy']

# You can also specify your delimiter. Let's use a dot in our next example
sentence = "333.666.999"
print(sentence.split('.'))  # prints => ['333', '666', '999']
# if we want to control the amounts of split, we specify a value for the maxsplit argument
print(sentence.split('.', maxsplit=1))  # prints => ['333', '666.999']

# if we want the split to start from right to left, we use rsplit() method
print(sentence.rsplit('.', maxsplit=1))  # prints => ['333.666', '999']

''' (4) Join() '''
# This is reverse of split. You can get string back from a list of strings.

list_of_strings = ['I', 'heard', 'Python', 'is', 'easy']

# use space to join a list of string
print(' '.join(list_of_strings))  # I heard Python is easy

# use - to join a list of string
print('-'.join(list_of_strings))  # I-heard-Python-is-easy

# use | to join a list of string
print('|'.join(list_of_strings))  # I|heard|Python|is|easy


''' (5, 6, 7, 8) lower(), upper(), capitalize(), title()'''

print('lower-version:', 'I AM GETTING BETTER EVERYDAY'.lower())  # i am getting better everyday

print('upper-version:', 'i am getting better everyday'.upper())  # I AM GETTING BETTER EVERYDAY

print('capitalized-version:', 'i am getting better everyday'.capitalize())  # I am getting better everyday

print('title-version:', 'i am getting better everyday'.title())  # I Am Getting Better Everyday


''' (9) islower() '''
# This returns true only when every alphabet character of the string is in lower case, otherwise it returns False
print('is-lower-test1:', 'I AM GETTING BETTER EVERYDAY'.islower())  # False
print('is-lower-test2:', 'I Am Getting Better Everyday'.islower())  # False
print('is-lower-test3:', 'i am getting better everyday'.islower())  # True


''' (10) isupper()'''
# This returns true only when every alphabet character of the string is in upper case, otherwise it returns False
print('is-upper-test1:', 'I AM GETTING BETTER EVERYDAY'.isupper())  # True
print('is-upper-test2:', 'I Am Getting Better Everyday'.isupper())  # False
print('is-upper-test3:', 'i am getting better everyday'.isupper())  # False


''' (11, 12, 13) isalpha(), isnumeric(), isalnum()'''

# isalpha() returns true if all characters are alphabets
print('is-alpha-test:', '0903456789'.isalpha())  # False
print('is-alpha-test::', 'LA771BDG'.isalpha())  # False
print('is-alpha-test::', 'Johnbull'.isalpha())  # True

# isnumeric() returns true if all characters are numbers
print('is-numeric-test:', '0903456789'.isnumeric())  # True
print('is-numeric-test::', 'LA771BDG'.isnumeric())  # False
print('is-numeric-test::', 'Johnbull'.isnumeric())  # False

# isalnum() returns true if all characters are either numbers or alphabets.
print('is-alphanumeric-test:', '0903456789'.isalnum())  # True
print('is-alphanumeric-test::', 'LA771BDG'.isalnum())  # True
print('is-alphanumeric-test::', 'Johnbull'.isalnum())  # True
# isalnum() returns false because of the presence of a special character, hyphen.
print('is-alphanumeric-test::', 'LA-771-BDG'.isalnum())  # False

''' (14) Count() '''
# Not to be confused with len().
# len() gets the length of the string while count() gets the frequency of occurrence

# syntax => string.count(value, start, end)
# value	Required. The value to search for
# start	Optional. Where to start the search. Default is 0
# end	Optional. Where to end the search. Default is to the end of the string


animal = "hippopotamus"

# let's find how many times 'o' appears in 'hippopotamus'
print('o occurs', animal.count('o'), 'times')  # 2
# let's find how many times 'p' appears in 'hippopotamus'
print('p occurs', animal.count('p'), 'times')  # 3


''' (15, 16) find(), rfind()  '''
# Find returns the index of the first occurrence of the search value. If it doesn't find it, returns -1.

# syntax => string.find(value, start, end). The arguments have the same definitions with count()

print(animal.find('p'))  # prints => 2
# if want it to search for next 'p', we can start our search from 3, by giving our start argument a value of 3
print(animal.find('p', 3))  # prints => 3
print(animal.find('x'))  # prints => -1  (because x is not present)

# find() searches from left to right. To start our search from right to left, we can use rfind
print(animal.rfind('p'))  # prints => 5


''' (17, 18) startsWith(), endsWith() '''

print('Python'.startswith('Py'))  # True
print('Python'.startswith('Pt'))  # False
print('Python'.endswith('o'))  # False
print('Python'.endswith('hon'))  # True

# Note: Javascript has similar methods but they are spelt slightly different - startsWith() & endsWith() [camel case].


''' (19) Partition '''

# This divides a string into a tuple of 3 items. A tuple is another python datatype for storing multiple items.

# The first element contains the part before the delimiter used to divide the string.
# The second element contains the delimiter.
# The third element contains the part after the delimiter.

url = "http://example.com/page"
divisions = url.partition("://")
print('divisions:', divisions)  # ('http', '://', 'example.com/page')

# You access a tuple like you access a Javascript array or Python list
protocol = divisions[0]
path = divisions[2]

print('protocol:', protocol, 'path:', path)  # protocol: http path: example.com/page

# Let's compare partition() to split()
s = "Obi is a good man"

print(s.partition("is"))  # ('Obi ', 'is', ' a good man')
print(s.split("is"))  # ['Obi ', ' a good man']

# From the above we can notice the following differences:
# 1. Partition preserves the delimiter, split doesn't. A delimiter is the substring used to split the main string
# 2. Partition returns a tuple; split returns a list
# 3. Partition will always return 3 items. Split can return less or more.


# When to use partition instead of split?
# When you want 3 and only 3 items. This makes partition's result predictable which can be a good thing

# Consider this scenario. Credentials are supplied in the format => credentials = "email:password"
# And we want to extract the email and password

credentials = "john.doe@example.com:MyP@ssw:rd!"

email, delimiter, password = credentials.partition(":")
# first item (i.e. index 0) in tuple is saved in the variable email, second in delimiter & third in password

print('email is:', email)  # john.doe@example.com
print('password is:', password)  # MyP@ssw:rd!

email, delimiter, password = credentials.split(":")

print('email is:', email)  # john.doe@example.com
print('password is:', password)  # rd! (password is split because password makes use of a colon which is the delimiter)


''' (20) swapcase() '''

# This turns lowercase to uppercase and vice versa

print('Precious Stones'.swapcase()) # pRECIOUS sTONES
