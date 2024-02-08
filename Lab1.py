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

class towers:
    def __init__(self, disk_count):
        self._disk_count = disk_count
        self._first_stick = ['='*i for i in range(1, disk_count+1)]
        self._first_stick.reverse()
        self._second_stick = []
        self._third_stick = []
        self._turn = 1
        self._mini_turn = 1
        
    def visualise(self, stick1, stick2):
        print(f"Current miniturn is: {self._mini_turn}") #\nFrom {stick2} to {stick1}S
        stick1 += [stick2.pop(-1)]
        self._mini_turn += 1
        print(self._first_stick, self._second_stick, self._third_stick, '\n')
    
    def start_turn(self):
        print(f"Current turn is: {self._turn}")
        if self._turn == 1:
            print(self._first_stick, self._second_stick, self._third_stick, '\n')
        if self._turn % 2 != 0:
            # if "=" not in self._second_stick:
            #     self.visualise(self._second_stick, self._first_stick)
            #     self.visualise(self._third_stick, self._first_stick)
            #     self.visualise(self._third_stick, self._second_stick)
            # else:
            #     self.visualise(self._first_stick, self._second_stick)
            #     self.visualise(self._third_stick, self._second_stick)
            #     self.visualise(self._third_stick, self._first_stick)
            if self._disk_count == 1:
                self.visualise(self._third_stick, self._first_stick)
            elif self._turn == self._disk_count-2:#self._disk_count != 2:
                self.visualise(self._third_stick, self._first_stick)
                self.visualise(self._second_stick, self._first_stick)
                self.visualise(self._second_stick, self._third_stick)
            else:
                self.visualise(self._second_stick, self._first_stick)
                self.visualise(self._third_stick, self._first_stick)
                self.visualise(self._third_stick, self._second_stick)
        else:
            # self.visualise(self._, self._)
            self.visualise(self._third_stick, self._first_stick)
            self.visualise(self._first_stick, self._second_stick)
            self.visualise(self._third_stick, self._second_stick)
            self.visualise(self._third_stick, self._first_stick)
        self._turn += 1
        if len(self._third_stick) != self._disk_count:
            self.start_turn()
            
# start_towers(4)

towers(3).start_turn()