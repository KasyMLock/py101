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

print(encrypt('LQKP OG CV GKIJV DA VJG BQQ', -2))