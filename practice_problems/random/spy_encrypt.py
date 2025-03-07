def spy_encript(string):
    finished_list = []
    string = string.upper()
    for char in string:
        real = ord(char)
        if real == 32:
            finished_list.append(chr(real))
        elif real < 60:
            real += 26
            finished_list.append(chr(real + 5))
        elif real > 85:
            real -= 26
            finished_list.append(chr(real + 5))
        else:    
            finished_list.append(chr(real + 5))
    return ''.join(finished_list)

print(spy_encript('SPY CODER'))