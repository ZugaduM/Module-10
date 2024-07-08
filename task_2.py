from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power
        self.__enemis = 100
        self.__days = 0

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.__enemis != 0:
            self.__enemis -= self.power
            self.__days += 1
            print(
                f'{self.name} сражается дней: {self.__days}, осталось {self.__enemis} врагов.'
            )
            sleep(1)
        print(f'{self.name} одержал победу спустя {self.__days} дней(дня)!')


list_of_threads = []

first_knight = Knight('Sir Lancelot', 10)
first_knight.start()
list_of_threads.append(first_knight)

second_knight = Knight("Sir Galahad", 20)
second_knight.start()
list_of_threads.append(second_knight)

for var in list_of_threads:
    var.join()

print('Все битвы закончились!')
