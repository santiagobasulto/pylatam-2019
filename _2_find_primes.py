import time
import itertools
from concurrent.futures import ThreadPoolExecutor
import speaker_buddy as buddy

def split_list(a_list, chunks):
    # return (itertools.islice(a_list, i,len(a_list), chunks) for i in range(chunks))
    return (a_list[i::chunks] for i in range(chunks))


def is_prime(n):
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    for divisor in range(3, n, 2):
        if n % divisor == 0:
            return False
    return True


def find_next_prime(n):
    for val in itertools.count(n + 1):
        if is_prime(val):
            return val


with open('data/prime_mixture.txt') as fp:
    numbers = [int(n.strip()) for n in fp.read().split() if n]


def search_primes_single_thread(numbers):
    return [n for n in numbers if is_prime(n)]


def search_primes_multi_thread(numbers, chunks=4):
    with ThreadPoolExecutor(max_workers=chunks) as pool:
        results = pool.map(is_prime, numbers)

    return results

# Single thread
print('Single thread:')
with buddy.measure_time() as tm:
    results = search_primes_single_thread(numbers)

tm.print()
print(f"Found {len(results)} primes out of {len(numbers)} total numbers.")
print('\n')
print('-' * 80)
print('\n')
print('Multithreaded thread:')
with buddy.measure_time() as tm:
    results = search_primes_multi_thread(numbers)

tm.print()
print(f"Found {sum(results)} primes out of {len(numbers)} total numbers.")
