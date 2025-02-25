# Practice Problems: Easy 2 in Lesson 3 of py101

# question 1 method 1
numbers_one = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

reversed_easy = list(numbers_one) # Found that (reversed_easy = numbers_one) would only
                              # create a second variable that would point to the 
                              # same location in memory. Needed to compile a 
                              # new list in order to create a true copy.

reversed_easy.reverse()
print(F"reversed_easy: {reversed_easy}")

# method 2 
reversed_hard = []
for num in numbers_one:
    reversed_hard.insert(0, num)
print(F"reversed_hard: {reversed_hard}")
print(F"numbers_one: {numbers_one}")

# question 2 
numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)

print(number1 in numbers)
print(number2 in numbers)

# question 3 
if 42 >= 10 and 42 <= 100:
    print('True')
else: print('False')

if 42 >= 100 and 42 <= 101:
    print('True')
else: print('False')

# after hint
print(42 in range(10,100))
print(42 in range(100,101))

# question 5
numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

print(type(numbers))
print(type(table))

# question 6

title = "Flintstone Family Members"

print(title.center(40))
# question 7
statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."

print(statement1.count('t'))
print(statement2.count('t'))

# question 8
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}
print('spot' in ages)

# question 9
ages['Marilyn'] = 22
ages['Spot'] = 237
print(ages)