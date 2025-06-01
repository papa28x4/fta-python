''' (1) '''
# Given the below url, use the strip method to get "example"
url = 'www.example.com'
result = url.strip('w.com')
print(result)  # Output: 'example'
# Expected result => 'example'

''' (2) '''
# Given the following string:
sentence = 'Aunty Aunika is the Author'
result = sentence.strip('Aunty')
print(result)
# Expected result => 'Aunika is the Author'


''' (3) '''
# Replace 's' with '$'. Only replace the first 2
sample = 'Recessions'
result = sample.replace('s', '$', 2)
print(result)
# Expected result => Rece$$ions


''' (4) '''
# Write a program to transform a word to its continuous tense
word = 'drive'
result = word.replace('e', '') + 'ing'
print(result)
# Expected result => driving


''' (5) '''
price = 2000
txt = f'The price is {price:,} dollars'
print(txt)

# Use Modifiers to get the result below
# Expected result => The price is 2,000 dollars
