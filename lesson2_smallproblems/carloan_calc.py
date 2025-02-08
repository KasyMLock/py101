# car/mortgage calculator


# while control is True:
    # How much is the loan for?:
    #   sub-routine for prompt and loop to insure proper answer.
    # How much interest?:
    #   sub-routine for prompt and loop to insure proper answer.
    # How long is the term?:
    #   sub-routine for prompt and loop to insure proper answer.
    # Math block
    # Finish with formatted "string answer"
# ask if another calculation?: return to top if yes.

print("""
    """)

# greeting block
print("Hello user! This program is designed to calculate a loan")
print("Please use numbers to answer the following three questions:")
print("||")

# function to validate numbers
def invalid_number(num_str):
    if float(num_str) < 1:
        return True
    try:
        int(num_str)
    except ValueError:
        return True
    return False

# loop wrap for overall program
againcontrol = True
while againcontrol is True:

    # prompt loan amount
    AMOUNT = input("What is the total amount of the loan?: ")
    while invalid_number(AMOUNT):
        AMOUNT = input(F"There is a mistake: {AMOUNT} is not a valid number,"
                     " please try again: ")

    # prompt interest amount
    INTEREST = input("What is the interest rate for the loan?: %")
    while invalid_number(INTEREST):
        INTEREST = input(F"There is a mistake: {INTEREST} is not a valid number,"
                       " please try again: ")

    # prompt duration in years amount
    TERM = input("How many years will the loan term be?: ")
    while invalid_number(TERM):
        TERM = input(F"There is a mistake: {TERM} is not a valid number, "
                    "please try again: ")

    #math block
    term_months = float(TERM) * 12
    interest_bymonth = (float(INTEREST) / 100) / 12
    total_monthly = float(AMOUNT) * (interest_bymonth /
    (1 - (1 + interest_bymonth) ** (-term_months)))

    # return block
    print("||")
    print(F"If this loan were ammortized your monthly payment would be "
          F"${total_monthly:.2F}")
    print(F"After {term_months} payments in {TERM} years(the term), "
          F"you will have paid ${total_monthly * term_months:.2F}")

    # again?
    print("||")
    again = input("would you like to do another loan calculation? ")
    good_again = again.lower()
    if good_again[0] == 'y':
        againcontrol = True
    else: againcontrol = False
