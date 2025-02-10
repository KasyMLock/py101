# Rock Paper Scissors game

# loop_control = True
# while loop_control == True
   # print(Start by explaining the game)
    # make a function promt_choose()
        # print 'choose' greeting
    # intput(Ask the user) "rock paper or scissors" using promt_choose()
    # make function computer_chosose:
        # include a print out explaining what the computer chose.
        # // utilize random function in python
    # print results
    # "want to play again?"
        # loop_control = False if anserwered yes.
# choose function for user

import random

# function to help user choose
def user_choose(selection):
    match selection:
        case 'paper'|'Paper'|'PAPER'|'pape'|'p'|'P'|'1':
            return 'paper'
        case 'rock'|'Rock'|'ROCK'|'roc'|'R'|'r'|'2':
            return 'rock'
        case 'scissors'|'Scissors'|'scissor'|'Scissor'|'SCISSORS'|'s'|'S'|'3':
            return 'scissors'
        case 'quit'|'QUIT'|'q'|'exit'|'x':
            quit()
        case _:
            return 'error'

# function to enable a random choice for computer
selection_options = ['paper', 'rock', 'scissors']
def computer_choose():
    return random.choice(selection_options)


# play again loop
overall_loop_control = True
while overall_loop_control is True:
    print("Welcome to Paper Rock Scissors!")

    print("""
          """)
    # user selection prompt
    user_selecion = user_choose(input("Please choose: 'paper', 'rock', or "
                                      "'scissors'... "))
    if user_selecion == 'error':
        print('|')
        user_selecion = user_choose(input("Computer doesn't recognise that "
                        "selection, try: 'paper', 'rock' or 'scissors. If the "
                        "computer is too intimidating you can quit:'q' "))

    #mechanics block
    computer_selection = computer_choose()
    winner = ''


    if user_selecion == 'paper':
        if user_selecion == 'paper' and computer_selection == 'paper':
            winner = 'tie'
        elif user_selecion == 'paper' and computer_selection == 'rock':
            winner = 'user'
        elif user_selecion == 'paper' and computer_selection == 'scissors':
            winner = 'computer'

    if user_selecion == 'rock':
        if user_selecion == 'rock' and computer_selection == 'rock':
            winner = 'tie'
        elif user_selecion == 'rock' and computer_selection == 'scissors':
            winner = 'user'
        elif user_selecion == 'rock' and computer_selection == 'paper':
            winner = 'computer'

    if user_selecion == 'scissors':
        if user_selecion == 'scissors' and computer_selection == 'scissors':
            winner = 'tie'
        elif user_selecion == 'scissors' and computer_selection == 'paper':
            winner = 'user'
        elif user_selecion == 'scissors' and computer_selection == 'rock':
            winner = 'computer'

    print("|")

    print(F"User chose {user_selecion} and the computer chose "
          F"{computer_selection}. The winner is {winner}!")

    print("_________")

    # close play again loop
    overall_loop_control = input("would you like to play again? No one "
                                 "has ever beaten the computer... y/n?  ")
    if overall_loop_control[0].lower() == 'n':
        overall_loop_control = False
    else: overall_loop_control = True
