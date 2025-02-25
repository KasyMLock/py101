# question 4 
def is_an_ip_number(str):
    if str.isdigit():
        number = int(str)
        return 0 <= number <= 255
    else: return False



def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    while len(dot_separated_words) == 4:
        for word in dot_separated_words:
            if is_an_ip_number(word) is False:
                return False 
                      
        return True
    return False 
        
   

print(is_dot_separated_ip_address('10.4.5.11'))
print(is_dot_separated_ip_address('0'))
print(is_dot_separated_ip_address('14.85.foo.89'))
print(is_dot_separated_ip_address('14.56.85.89.80'))
print(is_dot_separated_ip_address('14.56.865.89'))
print("_")

# question 5