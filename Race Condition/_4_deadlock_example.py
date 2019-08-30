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
        lock_1.acquire()
        lock_2.acquire()

        print(f"1 > 2: ${amount}")
        account_1 -= amount
        account_2 += amount

        check_balance()

        lock_2.release()
        lock_1.release()

def move_funds_from_2_to_1():
    global account_1, account_2

    while True:
        amount = random.randint(0, 10)
        lock_2.acquire()
        lock_1.acquire()

        print(f"2 > 1: ${amount}")
        account_2 -= amount
        account_1 += amount
        check_balance()

        lock_1.release()
        lock_2.release()


# def execute_forever(function, lock):
#     while True:
#         lock.acquire()
#         function()
#         lock.release()
#         # time.sleep(.1)

print("Initiating funds transfer. Will halt when a deadlock is produced.")
lock_1 = threading.Lock()
lock_2 = threading.Lock()

t1 = threading.Thread(target=move_funds_from_1_to_2)
t2 = threading.Thread(target=move_funds_from_2_to_1)
# t1 = threading.Thread(target=execute_forever, args=(move_funds_from_1_to_2, lock))
# t2 = threading.Thread(target=execute_forever, args=(move_funds_from_2_to_1, lock))

t1.start()
t2.start()
