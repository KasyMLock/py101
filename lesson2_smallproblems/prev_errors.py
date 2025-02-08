def invalid_number(num_str):
    try: 
        int(num_str)      
    except ValueError:
        return True
    return False
        

s = ('hello '
     'world')
print(s) 
      