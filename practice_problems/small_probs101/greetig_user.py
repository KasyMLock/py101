# start
# (input) request user to give name
#

def is_letters(string):
    if string.isalpha() or '!' in string:
        return True
    else: return False

name = input("What is your first name? ").strip(' ').capitalize()

while is_letters(name) is False:
    name = input(F"i'm sorry {name} is either not letters or has a "
                 F"space try again: ").strip(' ').capitalize()


if name[-1] == '!':
    print(F"HELLO {name.upper()}! WHY ARE WE YELLING?")
else:
    print(F"Hello {name}.")