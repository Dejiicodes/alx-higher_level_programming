#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
        except IndexError:
            break
        else:
            count += 1

    print()
    return count

if __name__ == "__main__":
    # Example usage:
    my_list = [1, 2, 3, 4, 5]
    x = 3
    print(safe_print_list(my_list, x))
