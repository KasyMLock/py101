def zero_converter(number):
    if number == 0:
        print('Absolute zero')
    elif number < 0:
        final_string = ''
        return_num = number
        while return_num != 0:
            return_num += 1
            final_string += ' ' + str(return_num)
        print(final_string)  

    else:
        final_string = ''
        return_num = number
        while return_num != 0:
            return_num -= 1
            final_string += ' ' + str(return_num)
        print(final_string)  

zero_converter(5)
zero_converter(-5)
zero_converter(0)