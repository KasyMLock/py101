
# encrypt function; use -shift_amount value to decrypt 
def encrypt(string, shift_amount):
    shift_amount = int(shift_amount)
    string = string.upper()
    finished_string = ''

    for char in string:
        if ord(char) >= 65 and ord(char) <= 90:
            shift_ord = ord(char) + shift_amount
            if shift_ord > 90:
                shift_ord -= 26
            elif shift_ord < 65:
                shift_ord += 26
            finished_string += chr(shift_ord)
        else: finished_string += char

    return finished_string

def goodness_finder(string):
    string_goodness = 0.0
    string = string.upper()
    for char in string:
        match char:
            case 'A':
                string_goodness += .0817
            case 'B':
                string_goodness += .0149
            case 'C':
                string_goodness += .0278
            case 'D':
                string_goodness += .0425
            case 'E':
                string_goodness += .1270
            case 'F':
                string_goodness += .0223
            case 'G':
                string_goodness += .0202
            case 'H':
                string_goodness += .0609
            case 'I':
                string_goodness += .0697
            case 'J':
                string_goodness += .0015
            case 'K':
                string_goodness += .0077
            case 'L':
                string_goodness += .0402
            case 'M':
                string_goodness += .0241
            case 'N':
                string_goodness += .0675
            case 'O':
                string_goodness += .0751
            case 'P':
                string_goodness += .0193
            case 'Q':
                string_goodness += .0009
            case 'R':
                string_goodness += .0599
            case 'S':
                string_goodness += .0633
            case 'T':
                string_goodness += .0906
            case 'U':
                string_goodness += .0276
            case 'V':
                string_goodness += .0098
            case 'W':
                string_goodness += .0236
            case 'X':
                string_goodness += .0015
            case 'Y':
                string_goodness += .0197
            case 'Z':
                string_goodness += .0007
            case _:
                string_goodness += 0

    return string_goodness

def encrypted_goodness_finder(string):
    most_guess_value = 0.0
    most_valuable_string = ''
    most_shift = 0
    for guess in range(0,26):
        guess_string = encrypt(string, guess)
        goodness_value = goodness_finder(guess_string)
        if goodness_value > most_guess_value:
            most_guess_value = goodness_value
            most_valuable_string = guess_string
            most_shift = guess

    return F'{most_valuable_string} Value:{most_guess_value:.4F} Shift:{most_shift}'


print(encrypted_goodness_finder('LQKP OG CV GKIJV DA VJG BQQ'))










