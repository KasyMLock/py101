
def increasing_power(number):
    power = 1
    return_string = ''
    while True:
        total = power ** 2
        if total >= number:
            break
        else: 
            return_string = return_string + ' ' + str(total) 
            power += 1 
    print(return_string)

increasing_power(100)
increasing_power(1000)


