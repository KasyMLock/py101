def countup(stop):
    if stop > 0:
        if stop == 1:
            print('Blastoff!')
        countup(stop - 1)
        print(stop)


countup(5)