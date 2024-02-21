import numpy as np
import random
import timeit


# Бульбашки
def sort_bubble(lst, killer=1, moves=0, compares=0):
    was_changed = False
    for index in range(len(lst)-killer):
        compares += 1
        if lst[index] > lst[index+1]:
            lst[index], lst[index+1] = lst[index+1], lst[index]
            moves += 1
            was_changed = True
    if not was_changed :
        return moves, compares
    else:
        return sort_bubble(lst, killer+1, moves, compares)


lst = [12, 13, 414, -13, 0, 3232, 32.4, 0.4]
time = timeit.timeit(lambda: sort_bubble(lst.copy()), number=1000)
moves, compares = sort_bubble(lst)
n = len(lst)
print(f"List: {lst} \nLen is: {n} \nTheoretical average Moves: {n*(n-1)/4}, Theoretical Compares: {n*(n-1)/2} \nMoves used: {moves}, Compares used: {compares} \ntime used: {time}\n")


## For Shell sort
def insertion_sort(lst):
    n = len(lst)
      
    if n <= 1:
        return
 
    for i in range(1, n):
        key = lst[i]
        j = i-1
        while j >= 0 and lst[j] > key:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key 


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