def cathat(string):
    if string.count(' cat') == string.count(' hat'):
        return True
    else: return False 

print(cathat('hello there cat in the hat'))
print(cathat('hey there you are a cat'))
print(cathat('umm... is that a cat wearing a hat?'))
print(cathat('that is certainly not a hat'))
print(cathat('that is'))