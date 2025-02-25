# write a program that asks the user to enter an integer greater
# than 0, then asks whether the user 
# wants to determine the sum of the product of all the numbers between
# 1 and the entered integer, inclusive.
#  
# start
# open a while loop to eventually ask for another calc.
    # USER_INPUT = input( "ask user for a number: "))
    # remove spaces and test ifdiggit
    # range_list = list(range(USER_INPUT + 1)) 
    # list_sum = 0
    # for item in len(range_list):
        # add each item to value of list_sum
    # print(list_sum as well as remark)
    # ask for another calc? 
# close while loop to end program 
# end

# function checking for invalid numbers
def invalid_number(num):
    try: 
        int(num)
    except ValueError:
        return True
    return False

# beginning of program
print('-------------------------------------------------------------------------')
loop_control = True
while loop_control == True:
    print("Welcome, this program is designed to add or multiply all the numbers before " 
          "that of the user's input "
        "and return the result. for example: [sum of 7 is 28] or [product of 7 is 5040]")
    user_input = input("Please type a number: ").strip(' ')

    # check for valid number and spaces in integer
    while invalid_number(user_input):
        if ' ' in user_input.strip(' '):
            user_input = input("This string has a space in it get rid of the spaces: ")       
        else:
            user_input = input("That string did not math please try a number: ")

    # ask for either 'sum' or 'product'
    user_choice = input(("Enter 's' to compute sum, or 'p' to compute product: ")
                         .lower().strip(' '))
    while user_choice[0] not in ('s', 'p'):
        user_choice = input(F"{user_choice} is invalid try 's' for sum or 'p' for "
                            "product: ").lower().strip(' ')

 

    # math block
    if user_choice == 's':
        sum_of_all = 0
        for item in range(int(user_input) + 1):
            sum_of_all += item
            if not item == int(user_input):
                print(F"{sum_of_all} + {item + 1}")
        print(F"    ---your answer is: {sum_of_all}---")
    
    elif user_choice == 'p':
        product_of_all = 1
        for iter in range(int(user_input) + 1):
            if iter == 0: continue
            product_of_all *= iter
            if not iter == int(user_input):
                print(F"{product_of_all} x {iter + 1}")
        print(F"    ---your answer is: {product_of_all}---")

    else: print("Error, my cpu is on fire!")


    # again? block
    again = input(F"would you like to do another? y/n: ").lower().strip(' ')
    if again[0] == 'y':
        loop_control = True
    else:
        loop_control = False 
