def triangle(n):
    for round in (range(1,n + 1)):
        print('*' * round)
triangle(5)

def right_triangle(height):
    for num in range(1,height + 1):
        stars = num
        spaces = height - num
        print(F"{' ' * spaces}{'*' * stars}")

    

    

right_triangle(5)


