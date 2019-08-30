import time
import threading
import random

DEBUG = False

account_1 = 1000
account_2 = 1000

def check_balance(expected_total=2000):
    total = account_1 + account_2
    if total != expected_total:
        print(f"\t====== INVALID AMOUNT: ${total} ======")
        exit()

check_balance()

def move_funds_from_1_to_2():
    global account_1, account_2
    while True:

        amount = random.randint(0, 10)
        lock.acquire()

        print(f"1 > 2: ${amount}")
        account_1 -= amount
        account_2 += amount

        check_balance()

        lock.release()

def move_funds_from_2_to_1():
    global account_1, account_2

    while True:
        amount = random.randint(0, 10)
        lock.acquire()

        print(f"2 > 1: ${amount}")
        account_2 -= amount
        account_1 += amount
        check_balance()

        lock.release()


# def execute_forever(function, lock):
#     while True:
#         lock.acquire()
#         function()
#         lock.release()
#         # time.sleep(.1)

print("Initiating funds transfer. Will report when a Race Condition is found.")
lock = threading.Lock()

t1 = threading.Thread(target=move_funds_from_1_to_2)
t2 = threading.Thread(target=move_funds_from_2_to_1)
# t1 = threading.Thread(target=execute_forever, args=(move_funds_from_1_to_2, lock))
# t2 = threading.Thread(target=execute_forever, args=(move_funds_from_2_to_1, lock))

t1.start()
t2.start()
