def decending_order(number):
    print(number, end=' ')
    while True:
        if number == 0: 
            break
        else:
            number -= 1
            print(number, end=' ')

decending_order(10)
