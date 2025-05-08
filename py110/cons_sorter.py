def cons_string_counter(string):
    CON = (['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                    'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'])
    return_value = 0
    
    string = string.replace(' ', '')
    for char in range(1, len(string)):
        if string[char] in CON and string[char - 1] in CON:
            return_value += 1 
    
    return return_value



def sort_by_consonant_count(list):
    return_dict = {}
    return_list = []
    final_list = []

    for string in list:
        str_count = cons_string_counter(string)
        return_dict[string] = str_count

    index = 0
    for item in return_dict:
        return_list.append(return_dict.get(item))
        return_list.sort(reverse=True)
    
    index = 0
    while index != len(return_list):
        for key in return_dict:
            if return_list[index] == return_dict[key]:
                final_list.append(key)
                del return_dict[key]
                break           
        index += 1         
    
    return final_list
            
        


my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']

