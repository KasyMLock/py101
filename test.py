dictionary = {'xx': 1, 'xxx': 2, 'xxhh': 2, 'xxjj': 2, 'xxyy': 2, 'xxxx': 3,}
values_list = []
return_list = []

for item in dictionary:
    values_list.append(dictionary.get(item, 'nothing'))
values_list.sort(reverse=True)



index = 0
while index != len(values_list):
    for key in dictionary:
        if values_list[index] == dictionary[key]:
            return_list.append(key)
            del dictionary[key]
            break
    index += 1





