# Practice Problems: Easy 3 in py101

# question 1 solution 1
numbers = [1, 2, 3, 4]

del_nums = list(numbers)

del del_nums[0:]
print(del_nums)

# solustion 2 
for num in range(len(numbers)):
    numbers.pop()

print(numbers)

# question 5

#def is_color_valid(color):
#    if color == "blue" or color == "green":
#        return True
#   else:
#        return False

# solution 1 
def is_color_valid(color):
    valid_color = ["blue", "green"]
    return color in valid_color

print(is_color_valid("pink"))
print(is_color_valid("orange"))
print(is_color_valid("green"))

# solution 2 
def is_color_valid(color):
    return color == "blue" or color == "green"

print(is_color_valid("pink"))
print(is_color_valid("blue"))
print(is_color_valid("green"))