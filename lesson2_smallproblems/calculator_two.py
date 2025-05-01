import time

loop_control = True

print('____________________________________________________________')
print("hello user, this is a calculator app!")
time.sleep(1)
print("we will start by asking for 2 seperate numbers followed by "
    "the operation you want to perform on them.")
time.sleep(1)


while loop_control == True:
    print('____________________________________________________________')
    num1 = str(input("first number?: "))
    num1 = num1.strip()
    while not num1.isdigit():
        num1 = str(input("i'm sorry that will not work for the first number. Try again?: "))

    num2 = str(input("and second number?: "))
    num2 = num2.strip()
    while not num2.isdigit():
        num2 = str(input("i'm sorry that will not work for the second number. Try again?: "))

    op = input("what is the operation you would like to use?: ")



    num1 = float(num1)
    num2 = float(num2)
    return_number = 0

    op = str(op.lower().strip())
    matchcase_control = False
    while matchcase_control == False:
        match op:
            case '+'|'plus'|'add'|'addition'|'ad':
                return_value = num1 + num2
                matchcase_control = True
            case '-'|'minus'|'takeaway'|'negative':
                return_value = num1 - num2
                matchcase_control = True
            case 'x'|'times'|'multiply'|'*':
                return_value = num1 * num2
                matchcase_control = True
            case '/'|'divide'|'division'|'in':
                return_value = num1 / num2
                matchcase_control = True
            case 'power'|'to the power of'|'exp'|'exponent':
                return_value = num1 ** num2
                matchcase_control = True
            case _:
                op = input("that does not work for an operator, try again?: ")
                matchcase_control = False
        
    print("calculating...")
    time.sleep(2)
    print(F"{num1} {op} {num2} = {return_value}")
    
    agloop = input("would you like to do another? Y/N: ")
    agloop = agloop.upper()
    if agloop.startswith('Y'):
        loop_control = True
    else:
        loop_control = False
        print("fine then, goodbye!")
        time.sleep(1)