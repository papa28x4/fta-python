# range() is built-in function use for creating a sequence of numbers
# range() function takes 3 arguments - start, stop and step. Only stop is required, the other two are optional

# SYNTAX: range(start, stop, step)
# start	Optional. An integer number that specifies the number to start from. Default is 0
# stop	Required. An integer number that specifies the number to stop (not included). e.g. if the stop is 5, the sequence
# will stop at 4, if the stop is set at 10 the sequence will stop at 9 and so on
# step	Optional. An integer number specifying the amount to increment (+ve) or decrement(-ve) by. Default is 1

# Scenario 1:
# range(stop)
# When one argument is passed, it's taken as the stop. While start takes the default value of 0 and
# step the default value of 1
nums = range(5)  # sames as range(start=0, stop=5, step=1)

print(nums)  # It prints range(0, 5)

# To see the sequence of numbers embedded in a range we can do any of the following:
# a) Wrap it in a list()
print(list(nums))  # [0, 1, 2, 3, 4]

# b) Wrap in a tuple()
print(tuple(nums))  # (0, 1, 2, 3, 4)

# c) Wrap in a set()
print(set(nums))  # {0, 1, 2, 3, 4}

# d) Use a for loop
for num in nums:
    print(num)


# Scenario 2
# range(start, stop)
# When two arguments are passed, the first is the start and second is stop. The step takes the default of one
numbers = range(10, 20)

print(list(numbers))  # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# Scenario 3
# range(start, stop, step)
even_numbers = range(30, 50, 2)  #

print(list(even_numbers))  # [30, 32, 34, 36, 38, 40, 42, 44, 46, 48]

# As seen above, there is a common difference of 2. This is because a step of 2 was specified. Also observe that 50
# is not included even though it's an even number. This because your stop value will never be included in your sequence



# Task

# Use the aid of the range() function to generate the following sequence:

# i) (7, 14, 21, 28, 35, 42, 49, 56)
# ii) [52, 44, 36, 28, 20, 12, 4]
# iii) ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
# 'w', 'x', 'y', 'z']

