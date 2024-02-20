import numpy as np


# Бульбашки
def sort_bubble(lst):
    is_not_changed = False
    was_changed = False
    while not is_not_changed:
        for index in range(len(lst)-1):
            if lst[index] > lst[index+1]:
                lst[index], lst[index+1] = lst[index+1], lst[index]
                was_changed = True
        if not was_changed :
            is_not_changed = True
        was_changed = False


lst = [12, 13, 414, -13, 0, 3232, 32.4, 0.4]
sort_bubble(lst)
print(lst)


# метод Шелла
def find_h_by_k(k, ki=1):
    if ki == k:
        return 1
    return 2*find_h_by_k(k, ki+1) + 1

def sort(lst, index, addition):
    try:
        if lst[index] > lst[index+addition]:
            lst[index], lst[index+addition] = lst[index+addition], lst[index]
    except IndexError:
        pass


def sort_shell(lst):
    n = len(lst)
    k_max = round(np.log2(n)) - 1

    k = 1
    index = 0

    while k != k_max:
        hk = find_h_by_k(k)
        while index <= n:
            last_index = index + hk
            sort(lst, index, hk)
            new_index = index
            while last_index > new_index:
                new_index += 1
                sort(lst, new_index, hk)
            index += hk
        k += 1
    hk = 1

lst = [12, 13, 414, -13, 0, 3232, 32.4, 0.4]
sort_shell(lst)
print(lst)