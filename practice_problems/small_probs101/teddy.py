import random
name = input("Hello user, how should I address you? ")
random_number = random.randrange(20, 100)

if name == '':
    print(F"Teddy is {random_number} years old!")
    quit()

while name.isalpha() == False:
    name = input(F"i'm sorry {name} either has spaces or has "
                 F"non-alphabetical characters. Try again ").strip(' ')



print(F"{name} is {random_number} years old!")
