def clean_up(string):
    return_string = ' '
    for char in string:
        if char.isalpha():
            return_string += char
        elif return_string[-1] != ' ':
            return_string += ' '
            
    return return_string

print(clean_up("---what's my +*& line?") == " what s my line ")

list = [(2,3,2), (3,2,5), (3,1,0)]
for x, y, z in list:
    print(x, z)