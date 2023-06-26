#!/usr/bin/python3
# 2-safe_print_list_integers.py

def safe_print_list_integers(my_list=[], x=0):
    count = 0;
    try:
        for i in range(x):
            if (isinstance(my_list[i], int)):
                print("{:d}".format(my_list[i]), end='')
                count +=1  # Number of elemnt printed
    except ValueError:  # In order to skip non int items quietly
        pass
    except IndexError:  # Raise default error
        raise
    print()  # Print new line
    return count
