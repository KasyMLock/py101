#print(explanation and request of user to give 6 numbers)
# request first number
# request second number
# request third number
# request fourth number
# request fifth number
# request sixth number
# compile first 5 numbers into a list 
# save last number to last_number variable
# if statement:
    #if last number in list:
        #return designated confimation
    #else : return designated non-confimation

def int_check(int):
    int = int.strip()
    if int.isdigit():
        return True
    else: return False


print()

print("Hello User, please enter a series of 6 numbers, digits only please.(1, 3, 4, etc.)")
series = []



tmp = input("Enter the 1st number: ")
while int_check(tmp) == False:
    tmp = input(F"{tmp} is not a digit, try again: ")
tmp = tmp.strip()
series.append(tmp)

tmp = input("Enter the 2nd number: ")
while int_check(tmp) == False:
    tmp = input(F"{tmp} is not a digit, try again: ")
tmp = tmp.strip()
series.append(tmp)

tmp = input("Enter the 3rd number: ")
while int_check(tmp) == False:
    tmp = input(F"{tmp} is not a digit, try again: ")
tmp = tmp.strip()
series.append(tmp)

tmp = input("Enter the 4th number: ")
while int_check(tmp) == False:
    tmp = input(F"{tmp} is not a digit, try again: ")
tmp = tmp.strip()
series.append(tmp)

tmp = input("Enter the 5th number: ")
while int_check(tmp) == False:
    tmp = input(F"{tmp} is not a digit, try again: ")
tmp = tmp.strip()
series.append(tmp)




last_number = input("Enter the last number: ")
while int_check(last_number) == False:
    last_number = input(F"{last_number} is not a digit, try again: ")
last_number = last_number.strip()




if last_number in series:
    print(F"{last_number} is in {' '.join(series)}.")
else:
    print(F"{last_number} is not in {' ' .join(series)}.")






