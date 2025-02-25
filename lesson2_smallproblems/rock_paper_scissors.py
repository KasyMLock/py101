# Rock Paper Scissors game

# loop_control = True
# while loop_control == True
   # print(Start by explaining the game)
    # make a function promt_choose()
        # print 'choose' greeting
    # intput(Ask the user) "rock paper or scissors" using promt_choose()
    # make function computer_choose:
        # include a print out explaining what the computer chose.
        # // utilize random function in python
    # print results
    # "want to play again?"
        # loop_control = False if anserwered yes.
# choose function for user

import random

# function to help user choose
def user_choose(selection):
    selection = selection.lower()
    match selection:
        case 'paper'|'pa'|'pap'|'pape'|'p'|'1':
            return 'paper'
        case 'rock'|'ro'|'roc'|'r'|'2':
            return 'rock'
        case 'scissors'|'sc'|'sci'|'scis'|'scissor'|'s'|'3':
            return 'scissors'
        case 'lizard'|'l'|'liz'|'4':
            return 'lizard'
        case 'spock'|'sp'|'spo'|'spoc'|'5':
            return 'spock'
        case 'quit'|'q'|'exit'|'x'|'e':
            quit()
        case _:
            return 'error'

# dicionary for winning combos
WINNING_COMBOS = {
    'rock': ['scissors', 'lizard'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'spock': ['scissors', 'rock'],
    'lizard': ['spock', 'paper'],
}

# function to manage the dict and execute the game.
def game_mechanic(user,computer):
    if computer in WINNING_COMBOS[user]:
        return True
    else: return False

# function to enable a random choice for computer
VALID_SELECTION = ['paper', 'rock', 'scissors','lizard', 'spock']
def computer_choose():
    return random.choice(VALID_SELECTION)


# play again loop
overall_loop_control = True
while overall_loop_control is True:
    print("Welcome to Paper Rock Scissors!")

    # individual game loop
    user_wins = 0
    computer_wins = 0
    game_loop_control = True
    while game_loop_control is True:

        # user selection prompt
        user_selecion = user_choose(input(F"Please choose: "
                                        F"{', '.join(VALID_SELECTION)}: "))

        if user_selecion == 'error':
            print('|')
            user_selecion = user_choose(input(F"Computer doesn't recognise that "
                        F"selection, try: {', '.join(VALID_SELECTION)}. If the "
                        F"computer is too intimidating you can quit:'q' "))

        #mechanics block
        computer_selection = computer_choose()
        winner = ''
        if user_selecion == computer_selection: # Tie
            winner = 'it\'s a tie'

        elif game_mechanic(user_selecion, computer_selection):
            winner = 'YOU WIN'
            user_wins += 1

        else:
            winner = 'YOU LOSE'
            computer_wins += 1

        print("|")

        print(F"User chose ({user_selecion}) and the computer chose "
            F"({computer_selection}).")
        print(F"[{winner}] this round.")

        print(F"user wins: {user_wins}/3")
        print(F"computer wins: {computer_wins}/3")

        # score limit block
        if user_wins == 3:
            game_loop_control = False
            print('')
            print("****--congratulations! you have won best of 5!--****")
        elif computer_wins == 3:
            game_loop_control = False
            print('')
            print("***-I'm so sorry, you have failed to beat the computer-*** :(")

        print("_________")

        # close 'play again' loop
    overall_loop_control = input("would you like to play again? No one "
                                "has ever beaten the computer... y/n?  ")
    overall_loop_control = overall_loop_control.lower()

    if overall_loop_control.startswith('n'):
        overall_loop_control = False
    elif overall_loop_control[0].lower() == 'q':
        overall_loop_control = False
    else: overall_loop_control = True
