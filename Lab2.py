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


# lst = [12, 13, 414, -13, 0, 3232, 32.4, 0.4]
lst = [random.randint(-1000, 1000) for i in range(100)]

time = timeit.timeit(lambda: sort_bubble(lst.copy()), number=1000)
moves, compares = sort_bubble(lst)
n = len(lst)
print(f"List: {lst} \nLen is: {n} \nTheoretical average Moves: {n*(n-1)/4}, Theoretical Compares: {n*(n-1)/2} \nMoves used: {moves}, Compares used: {compares} \ntime used: {time}\n")


## For Shell sort
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

# метод Шелла
def sort_shell(lst, N, showP=False):
    m = round(np.log2(N)-1)
    d = []
    find_all_ds(m, d)
    not_finished = True
    index = -1
    gap=d[index]
    
    moves = 0
    compares = 0
      
    while not_finished:
        j=gap 
        if showP:
            print(j)
        while j<n: 
            i=j-gap
            while i>=0: 
                compares += 1
                if lst[i+gap]>lst[i]: 
                    break
                else: 
                    moves += 1
                    lst[i+gap],lst[i]=lst[i],lst[i+gap] 
  
                i=i-gap
            j+=1
        if gap == 1:
            not_finished = False
        else:
            index -= 1
            gap=d[index]
    return moves, compares


# lst = [12, 13, 414, -13, 0, 3232, 32.4, 0.4]
lst = [random.randint(-1000, 1000) for i in range(100)]
n = len(lst)

time = timeit.timeit(lambda: sort_shell(lst.copy(), n), number=1000)
moves, compares = sort_shell(lst, n)

print(f"List: {lst} \nLen is: {n} \nTheoretical average Moves: {n**(6/5)}, Theoretical Compares: {n*np.log2(n)} \nMoves used: {moves}, Compares used: {compares} \ntime used: {time}\n")
