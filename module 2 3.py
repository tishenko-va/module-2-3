my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
first_main = 0
while first_main < len(my_list):

    if my_list[first_main] >= 0:
        if my_list[first_main] != 0:
            print(my_list[first_main])
        first_main = first_main +1
        continue
    else:
        break

