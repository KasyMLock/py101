def penultimate(string):
    lst = string.split()
    return lst[-2]

# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")

def middleword(string):
    word_list = string.split() 
    if len(word_list) % 2 == 1:
        index_odd = (len(word_list) // 2) + (len(word_list) % 2) - 1 # finds middle for odds
        return word_list[index_odd]
    else:
        index_even = (len(word_list) // 2) - 1
        even_plus = len(word_list) // 2
        list = [word_list[index_even], word_list[even_plus]]

        final_string = ' '.join(list)
        return final_string
        


print (middleword(' hey there love '))