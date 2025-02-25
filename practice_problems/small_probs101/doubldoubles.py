def twice(number):
    number_string = str(number)
    index_half_length = len(str(number)) // 2
    if str(number_string[:index_half_length]) == str(number_string[index_half_length:]):
        return number
    else:
        return number * 2
    

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True