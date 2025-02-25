def multiply(num1, num2):
    return int(num1) * int(num2)

print(multiply(5, 3) == 15)  # True

def square(number, power):
    value = 1
    for _ in range(1, int(power) + 1):
        value = multiply(value, number)
    return value



def product(num4, power_of):
    return abs(num4) ** abs(power_of)

print(product(5, 5))
print(square(5, 5))