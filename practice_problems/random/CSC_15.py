# This is an excersice put on by the UW online free computer science website
# it is designed to take an input from a user of basic commands and process them.
# example: 10 GOTO 100, 50 GOTO 90, 100 GOTO 50, 90 END 

def get_basic():
    basic_list = []
    while True:
        x = input()
        basic_list.append(x)
        if x.endswith('END'):
            break
    return basic_list

def findLine(prog, target):
    i = 0
    for string in prog:    
        if string.startswith(target):
            return i
        else:
            i += 1

def execute(prog):
    location = 0
    visited = [False] * len(prog)
    while visited[location] == False:
        for string in prog:         
            visited[location] = True
            if prog[location].endswith('END'):
                return "success"
            T = prog[location].split()[2]
            location = findLine(prog, T)
    return "infinite loop"

print(execute(get_basic()))