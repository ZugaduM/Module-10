import queue
from threading import Thread
from time import sleep


class Table:

    def __init__(self, number):
        self._number = number
        self.is_busy = False


class Cafe:

    def __init__(self, tables):
        self.__queue = queue.Queue()
        self.__tables = tables
        self.__min_customers = 1
        self.__max_customers = 21

    def customer_arrival(self):
        for i in range(self.__min_customers, self.__max_customers):
            print(f'Посетитель номер {i} прибыл.')
            self.serve_customer(i)
            sleep(1)

    def serve_customer(self, customer_number):
        for value in self.__tables:
            if not value.is_busy:
                value.is_busy = True
                customer = Customer(customer_number, value, self)
                customer.start()
                return
        self.__queue.put(customer_number)
        print(f'Посетитель номер {customer_number} ожидает свободный стол')

    def table_ready(self, table):
        if not self.__queue.empty():
            next_customer = self.__queue.get()
            customer = Customer(next_customer, table, self)
            customer.start()
        else:
            table.is_busy = False


class Customer(Thread):

    def __init__(self, cust_id, cust_table, cafe_link):
        Thread.__init__(self)
        self.__name = cust_id
        self.__table = cust_table
        self.__cafe = cafe_link

    def run(self):
        print(f"Посетитель номер {self.__name} сел за стол {self.__table._number}")
        sleep(5)
        print(f"Посетитель номер {self.__name} покушал и ушёл")
        self.__cafe.table_ready(self.__table)


# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()
