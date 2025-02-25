def print_in_box(string):
    print('+', ('-' * (len(string))),'+')
    print('|', (' ' * (len(string))),'|')
    print('|', string, '|')
    print('|', (' ' * (len(string))),'|')
    print('+', ('-' * (len(string))),'+')


print_in_box('To boldly go where no one has gone , way to far, '
             'for this box to work am I right? how about we wrap this up a bit before.')
