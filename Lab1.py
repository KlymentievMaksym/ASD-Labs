# 10. Знайти найменше спільне кратне (НСК) двох цілих чисел за
# допомогою рекурсії.
# 14. Реалізувати алгоритм для розв’язання задачі «Ханойські вежі».
# Виписати послідовність ходів для перекладання n дисків вежі (n = 2;
# 3; 4; 5 дисків, використати онлайн гру).

import numpy as np




def lcd(num1, num2, dict_for_prime_num1={}, dict_for_prime_num2={}):
    def find_one_prime_number(num, dict_for_prime_num={}):
        if num != 1:
            for i in range(np.inf):
                if num%i == 0:
                    return i
    prime_num1 = find_one_prime_number(num1, dict_for_prime_num1={})
    

# if num1 == 1 and num2 == 1:
#     return 1
# for prime in dict_for_prime_num1:
#     num1 = num1/prime
# for prime in dict_for_prime_num2:
#     num2 = num2/prime
# return 