from threading import Lock, Thread


class BankAccount():

  def __init__(self):
    self.__balance = 1000

  def deposit(self, amount):
    self.__balance += amount
    print(f'Deposited {amount}, new balance is {self.__balance}')

  def withdraw(self, amount):
    self.__balance -= amount
    print(f'Withdrew {amount}, new balance is {self.__balance}')

operation_lock = Lock()

def deposit_task(account, amount):
  with operation_lock:
    for _ in range(5):
      account.deposit(amount)


def withdraw_task(account, amount):
  with operation_lock:
    for _ in range(5):
      account.withdraw(amount)


account = BankAccount()

deposit_thread = Thread(target=deposit_task, args=(account, 100))
withdraw_thread = Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
