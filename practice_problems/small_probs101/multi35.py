def multisum(num):
    summed = 0
    for n in range(int(num) + 1):
        if n % 3 == 0 or n % 5 == 0:
            summed += n
    return summed

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)