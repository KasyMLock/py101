import array


def create_dict(names, ages):
    return_dict = dict(zip(names, ages))
    return return_dict


name_list = ['Kasy', 'Molly', 'Pepper', 'jake', 'john', 'maria']
age_list = [33, 34, 2, 7, 9]


print(dict(zip(name_list, age_list,)))

