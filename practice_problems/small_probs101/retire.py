from datetime import datetime

current_year = datetime.now().year



age = input("what is your age? ").strip(' ')
while age.isdigit() is False:
    age = input(F"{age} is not a viable answer, please make "
                F"sure there are no spaces and only numbers. Try again: ").strip(' ')

retire_age = input("At what age would you like to retire? ").strip(' ')
while retire_age.isdigit() == False:
    retire_age = input(F"{retire_age} is not a viable answer, please make "
                F"sure there are no spaces and only numbers. Try again: ").strip(' ')

years_togo = int(retire_age) - int(age)
retirement_year = int(current_year) + int(years_togo)


print(F"It's {current_year}. You will retire in the year {retirement_year}.")
print(F"You only have {years_togo} years of work to go!")