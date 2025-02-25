# question 2
strone  = "Come over here!"  # True
strtwo = "What's up, Doc?"  # False

def is_end(str,char):
    if str[-1] == char:
        return True
    else: return False
    
print(is_end(strone, '!'))
print(is_end(strtwo, '!'))

# questions 3 
famous_words = "seven years ago..."
old_string = "Four score and"
# way 1
new_string = old_string + ' ' + famous_words
# way 2
def prepend(new,old):
    return str(new) + ' ' + str(old)
double_new_string = prepend(old_string, famous_words)

print(double_new_string, new_string)

# question 4
munsters_description = "the Munsters are CREEPY and Spooky."
print(munsters_description[0].upper() + munsters_description[1:].lower())

# question 5 
print(munsters_description.swapcase())

# question 6
str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

if 'Dino' in str1:
    print('str1 = True')
else: print('str2 = False') 

if 'Dino' in str2:
    print('str2 = True')
else: print('str2 = False') 

# question 7
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]

flintstones.append('Dino')
print(flintstones)

# question 8
flintstones += ['Dino', 'Hoppy']
print(flintstones)

# question 9
advice = "Few things in life are as important as house training your pet dinosaur."

new_advice = advice.split()
keepers = []
for keep in new_advice:
    if keep == 'house':
        break
    keepers.append(keep)
print(' '.join(keepers))


print(advice.split('house')[0]) # cool

# question 10
advice = "Few things in life are as important as house training your pet dinosaur."

advice_list = advice.split()
find_word = advice_list.index('important')
advice_list.insert(find_word,'urgent')
advice_list.remove('important')
advice = ' '.join(advice_list)

# advice.replace('important', 'urgent')
print(advice)