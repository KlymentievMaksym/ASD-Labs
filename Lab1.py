# 10. Знайти найменше спільне кратне (НСК) двох цілих чисел за
# допомогою рекурсії.

def gcd(num1, num2):
    if num2 == 0:
        return num1
    return gcd(num2, num1%num2)


def lcm(num1, num2):
    return num1*num2/gcd(num1, num2)


print(lcm(3, 7))

# 14. Реалізувати алгоритм для розв’язання задачі «Ханойські вежі».
# Виписати послідовність ходів для перекладання n дисків вежі (n = 2;
# 3; 4; 5 дисків, використати онлайн гру).

def visualise(stick1, stick2, miniturn):
    print(f"This is miniturn with name: {miniturn}")
    stick1 += [stick2.pop(-1)]


def start_towers(disk_count):
    first_stick = ['='*i for i in range(1, disk_count+1)]
    first_stick.reverse()
    towers(disk_count, first_stick)
    
    
def towers(disk_count, first_stick, second_stick=[], third_stick=[], turn=1, miniturn=1):
    if turn == 1:
        print(first_stick, second_stick, third_stick)
    if turn % 2 != 0:
        second_stick += [first_stick.pop(-1)]
        # visualise(stick1, stick2, miniturn)
        third_stick += [first_stick.pop(-1)]
        # visualise(stick1, stick2, miniturn)
        third_stick += [second_stick.pop(-1)]
        # visualise(stick1, stick2, miniturn)
        turn += 1
    else:
        second_stick += [first_stick.pop(-1)]
        second_stick += [third_stick.pop(-1)]
        first_stick += [third_stick.pop(-1)]
        first_stick += [second_stick.pop(-1)]
        third_stick += [second_stick.pop(-1)]
        turn += 1
    if len(third_stick) != disk_count:
        towers(disk_count, first_stick, second_stick, third_stick, turn)
    else:
        print(first_stick, second_stick, third_stick)
    
start_towers(4)