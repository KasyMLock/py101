def stringy(number):
    return_string = ''
    index = 1
    for _ in range(number):
        if index % 2 == 1 or index == 1:
            return_string += '1'
            index += 1 
        else:
            return_string += '0'
            index += 1
    return return_string   

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True

def stringish(numb):
    return_stringish = ''
    for index in range(numb):
        return_stringish += '1' if index % 2 == 0 else '0'
    return return_stringish

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True