def welcome(list,dict):
    return(F"Hello, {' '.join(list)}! Nice to have "
            F"a {dict['title']} {dict['occupation']} around.")


list1 = ["John", "Q", "Doe"]
dict1 = {"title": "Master", "occupation": "Plumber"}

print(welcome(list1, dict1))

