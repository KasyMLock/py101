def xor(value1, value2):
    if value1 and value2:
        return False 
    else: return True


print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)