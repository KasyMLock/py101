def repeat(string, times):
    for _ in range(times):
        print(string)



def crunch(input_string):
    last_letter = ''
    finished = ''
    for letter in input_string:
        if last_letter == letter:
            continue
        else:
            last_letter = letter 
            finished += letter
    return finished

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')