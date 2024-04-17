import numpy as np
import random
import timeit

numbers = [100, 1000, 10000]


# Бульбашки
def sort_bubble(lst):
    killer = 1
    moves = 0
    compares = 0
    was_changed = True
    while was_changed:
        was_changed = False
        for index in range(len(lst)-killer):
            compares += 1
            if lst[index] > lst[index+1]:
                lst[index], lst[index+1] = lst[index+1], lst[index]
                moves += 1
                was_changed = True
        killer += 1
        if not was_changed:
            return moves, compares


# lst = [12, 13, 414, -13, 0, 3232, 32.4, 0.4]
for number in numbers:
    lst = random.sample(range(-10*number, 10*number), number)

    time = timeit.timeit(lambda: sort_bubble(lst.copy()), number=5)
    moves, compares = sort_bubble(lst)
    n = len(lst)
    print(f"Sorted by bubble random List: {lst} \nLen is: {n} \nTheoretical average Moves: {n*(n-1)/4}, Theoretical Compares: {n*(n-1)/2} \nMoves used: {moves}, Compares used: {compares} \ntime used: {time}\n")


# For Shell sort
def find_all_ds(m, d):
    k = m
    i = 0
    while k != 1:
        if k == m:
            d += [1]
        else:
            d += [2*d[i] + 1]
            i += 1
        k -= 1


# # метод Шелла
# def sort_shell(lst, N):
#     m = round(np.log2(N)-1)
#     d = []
#     find_all_ds(m, d)
#     not_finished = True
#     index = -1
#     gap = d[index]

#     moves = 0
#     compares = 0

#     while not_finished:
#         j = gap
#         while j < n:
#             i = j-gap
#             while i >= 0:
#                 compares += 1
#                 if lst[i+gap] > lst[i]:
#                     break
#                 else:
#                     moves += 1
#                     lst[i+gap], lst[i] = lst[i], lst[i+gap]

#                 i = i-gap
#             j += 1
#         if gap == 1:
#             not_finished = False
#         else:
#             index -= 1
#             gap = d[index]
#     return moves, compares


def sort_shell(lst, N):
    m = round(np.log2(N)-1)
    d = []
    find_all_ds(m, d)

    moves = 0
    compares = 0

    for k in range(len(d)-1, -1, -1):
        for i in range(d[k]+1, N):
            a = lst[i]
            j = i

            while j - d[k] >= 1 and lst[j-d[k]] > a:
                compares += 1
                lst[j] = lst[j - d[k]]
                moves += 1
                j -= d[k]
            compares += 1

            lst[j] = a
            moves += 1
    return moves, compares


for number in numbers:
    # lst = [12, 13, 414, -13, 0, 3232, 32.4, 0.4]

    lst = random.sample(range(-10*number, 10*number), number)
    n = len(lst)

    time = timeit.timeit(lambda: sort_shell(lst.copy(), n), number=10)
    moves, compares = sort_shell(lst, n)

    print(f"List: {lst} \nLen is: {n} \nTheoretical average Moves: {n**(6/5)}, Theoretical Compares: {n**(6/5)} \nMoves used: {moves}, Compares used: {compares} \ntime used: {time}\n")
