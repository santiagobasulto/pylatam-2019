import time
import threading
import random

account_1 = 1000
account_2 = 1000

def check_balance(expected_total=2000):
    total = account_1 + account_2
    if total != expected_total:
        print(f"\t====== INVALID AMOUNT: ${total} ======")

check_balance()

def move_funds_from_1_to_2():
    global account_1, account_2

    amount = random.randint(0, 10)
    account_1 -= amount
    account_2 += amount
    check_balance()

def move_funds_from_2_to_1():
    global account_1, account_2

    amount = random.randint(0, 10)
    account_2 -= amount
    account_1 += amount
    check_balance()


def execute_forever(function):
    while True:
        function()
        # time.sleep(.1)

t1 = threading.Thread(target=execute_forever, args=(move_funds_from_1_to_2,))
t2 = threading.Thread(target=execute_forever, args=(move_funds_from_2_to_1,))

t1.start()
t2.start()
