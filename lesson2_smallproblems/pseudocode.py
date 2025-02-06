#a function that returns the sum of two numbers

#start

# define a function(first,second):
#   return first + second 


def sumoftwon(first,second):
    return first + second 

print(sumoftwon(2,2))


# a function that takes a list of strings and returns them added
# togeather

# start
# define a function listto_string(list):
#   return list using ' '.join(list) funciton 
# another way would be to use a loop to do it more manually

def listto_string(list):
    return ' '.join(list)


that = ['this is a string', 'that is a string', 'as well as this']
print(listto_string(that))

# a function that takes a list of integers, and returns 
# a new list with every other element from the original list, 
# starting with the first element. 

# start
# set counter = 0
# set new_list = []
# define function every_other(list):
#   for items in list:
#       add to new_list every other item on list  
#       return new_list 



def every_other(list):
    counter = 0
    new_list = []
    
    while counter < len(list):
        new_list.append(list[counter])
        counter += 2
    return new_list

this = [1, 4, 7, 8, 9, 5, 3, 4, 6, 8, 34, 52, 6, 2, 135, 32, 4, 6, 9]
print(every_other(this))


# a function that determines the index of the 3rd occurrence of a
# given character in a string.
# 
# start
# 
# define function third_pays_forall(char, string):
#   set counter = 0
#   for loop in string:
#       if char == char at index location in string:
#           add 1 to counter 
#       elif if counter == 3 return print 'the third occurance of {char}..etc'
#       else: continue    


def third_pays_forall(char,string):
    counter = 0
    location = -1 
    for ch in string:
        location += 1
        if ch == char:
            counter += 1
            if counter == 3:
                return print(F"The third occurance of {char} is in index location[{location}] in '{string}'")
            
        else: continue

    if counter < 3: return print(F"There are less than three instances of '{char}' in '{string}'")

third_pays_forall('x', 'axbxcdxex')


# a function that takes two lists of numbers and returns the result of merging the lists in
# in such a way that they co-mingle every other item in the list. [b,a,b,a,b,a,b,a] a_list in 
# even positions and b_list in odd positions.

# start
# define a function eo_list_merge(list_even, list_odd)
#    set final_list = list_odd
#    set location = 0
#    for loop to cycle through list_even:
#       location += 2
#       add each item to final_list in location index
#   return final_list

def eo_list_merge(list_even, list_odd):
    final_list = list_odd
    location = 1
    for item in list_even:
        final_list.insert(location,item)
        location += 2
    return final_list

this_list = [2, 4, 6, 8]
that_list = [1, 3, 5, 7]

print(eo_list_merge(this_list, that_list))

#first try!!!