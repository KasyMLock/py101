def running_total(list):
    run_total = 0
    ret_list = []

    for num in list:
        run_total += int(num)
        ret_list.append(run_total)
        
    return ret_list



print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True