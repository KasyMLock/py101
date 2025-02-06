# ask user for first number
# ask user for second number
# ask user for operator
# perform the math
# print results



# note I wanted to design a more robust calculator by providing
# multiple options for each operator; resulting in a variant of
# the lesson.

print('Welcome to Calculator')
def invalid_number(number_str): # provided by lesson
    try:
        int(number_str)
    except ValueError:
        return True
    return False

def prompt(message):
    print(F"==> {message}")

# block to start the program over if user wants to do another calculation at the end.
control = True
while control is True:

    # block to check if first number is valid
    first_number = input("==> first number to calculate?: ")
    while invalid_number(first_number):
        prompt("hmm.. that doesn't look like a valid number. Try again.")
        first_number = input("==>: ")

    # block to see if second number is valid
    second_number = input("==> second number to calculate?: ")
    while invalid_number(second_number):
        prompt("hmm.. that doesn't look like a valid number. Try again.")
        second_number = input("==>: ")

    # block to see if operator is valid
    operator = str(input("==> what is the operator you would like to use?: "))
    optrue = True
    while optrue is True:
        match operator:
            case '+' | 'plus' | 'addition' | 'Addition' | 'add' | 'Add':
                optrue = False
            case '-' | 'minus' | 'subtract' | 'Subtract':
                optrue = False
            case '*' | 'multiply' | 'x' | 'X' | 'Multiply' | 'time' | 'Times' | 'times':
                optrue = False
            case '/' | 'divide' | 'Divide':
                optrue = False
            case _:
                optrue = True
                operator = input("==> Not a recognized operator, try '+', '-', '/', or '*': ")

    # math block
    match operator:
        case '+' | 'plus' | 'addition' | 'Addition' | 'add' | 'Add':
            output = int(first_number) + int(second_number)
        case '-' | 'minus' | 'subtract' | 'Subtract':
            output = int(first_number) - int(second_number)
        case '*' | 'multiply' | 'x' | 'X' | 'Multiply' | 'time' | 'Times' | 'times':
            output = int(first_number) * int(second_number)
        case '/' | 'divide' | 'Divide':
            output = int(first_number) / int(second_number)
        case _:
            output = "operator doesn't exist or is beyond the bounderies of this simple calculator."

    # block to check for another calc.
    print(F"your answer is: {output}")
    another = str(input("would you like do do another?: "))
    match another:
        case 'y' | 'Y' | 'Yes' | 'YES' | 'yes':
            control = True
        case _:
            control = False
