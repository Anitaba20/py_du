# du z 10.03.2026_Vytvorte program v Pythone, ktorý simuluje bankový účet a
# viacerých klientov pristupujúcich k nemu súčasne pomocou threadov.

# verzia_1: Spustite program bez synchronizácie a sledujte, či je výsledný zostatok správny.
# pridala som verziu, kde je time.slee(0.1) - väčšia šanca, že narazím na race condition

import threading
import time
import random

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            new_balance = self.balance - amount
            time.sleep(0.001)
            self.balance = new_balance

account = BankAccount(5000)

def client():
    for _ in range(100):
        amount = random.randint(1, 10)
        account.withdraw(amount)

threads = []

for i in range(10):
    thread = threading.Thread(target=client)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Final balance:", account.balance)





# verzia2: time.sleep(0,1)
import threading
import time
import random

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            new_balance = self.balance - amount
            time.sleep(0.1)
            self.balance = new_balance

account = BankAccount(5000)

def client():
    for _ in range(100):
        amount = random.randint(1, 10)
        account.withdraw(amount)

threads = []

for i in range(10):
    thread = threading.Thread(target=client)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Final balance:", account.balance)