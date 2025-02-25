def center_of(string):

    even_one = (len(string) // 2) - 1
    even_two_odd = (len(string) // 2)
    two_char = [string[even_one], string[even_two_odd]] 

    if len(string) < 2:
        return string
    elif len(string) % 2 == 0:
        return ''.join(two_char)
    else:
        return string[even_two_odd]
    


print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True