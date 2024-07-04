from threading import Thread
from time import sleep


def some_func(args):
    if args == 'word':
        for i in range(ord('a'), ord('j') + 1):
            print(chr(i))
            sleep(1)
    if args == 'numb':
        for i in range(1, 11):
            print(i)
            sleep(1)

my_thread_one = Thread(target=some_func, args=('numb',))
my_thread_two = Thread(target=some_func, args=('word',))

my_thread_one.start()
my_thread_two.start()

my_thread_one.join()
my_thread_two.join()
