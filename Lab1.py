# 10. Знайти найменше спільне кратне (НСК) двох цілих чисел за
# допомогою рекурсії.

def gcd(num1, num2):
    if num2 == 0:
        return abs(num1)
    return gcd(num2, num1%num2)


def lcm(num1, num2):
    return abs(num1*num2)/gcd(num1, num2)


print(lcm(3, 7))
print(lcm(-3, -7))

# 14. Реалізувати алгоритм для розв’язання задачі «Ханойські вежі».
# Виписати послідовність ходів для перекладання n дисків вежі (n = 2;
# 3; 4; 5 дисків, використати онлайн гру).

class towers:
    def __init__(self, disk_count):
        self._disk_count = disk_count
        self._first_stick = ['='*i for i in range(1, disk_count+1)]
        self._first_stick.reverse()
        self._needed_form = self._first_stick.copy()
        self._second_stick = []
        self._third_stick = []
        self.dict = {0:self._disk_count, 1:self._first_stick, 2:self._second_stick, 3:self._third_stick}
        self._turn = 1
        
    def visualise(self, stick1, stick2):
        print(f"""Current turn is: {self._turn}
From {stick1}({list(self.dict.keys())[list(self.dict.values()).index(stick1)]})
To {stick2}({[list(self.dict.keys())[list(self.dict.values()).index(stick2)], "2|3"][self._turn == 1]})
""")
        stick2 += [stick1.pop(-1)]
        self._turn += 1
        print("Result: \n", self._first_stick, ' ', self._second_stick, ' ', self._third_stick, '\n', sep="")
        
 

def hanoi_tower(game_info, n, source, destination, auxiliary):
    if n==1:
        # print("Move disk 1 from source",source,"to destination",destination)
        game_info.visualise(source, destination)
        return
    hanoi_tower(game_info, n-1, source, auxiliary, destination)
    # print ("Move disk",n,"from source",source,"to destination",destination)
    game_info.visualise(source, destination)
    hanoi_tower(game_info, n-1, auxiliary, destination, source)

n = int(input("Enter n for HannoiTower: "))
game_info = towers(n)#.hanoi_tower()
hanoi_tower(game_info, game_info._disk_count, game_info._first_stick, game_info._third_stick, game_info._second_stick)