import time
import queue
import random

import threading

THREAD_POOL_COUNT = 4  # How many threads will we create?
AVAILABLE_SITES = ['Google', 'Microsoft', 'Facebook', 'Amazon', 'Yahoo', 'Twitter']

ready_queue = queue.Queue()
results_queue = queue.Queue()

for _ in range(20):
    random_site = random.choice(AVAILABLE_SITES)
    ready_queue.put(random_site)

def process_website(ready_q, results_q):
    while True: # Interesting!
        site = ready_q.get()
        res = random.randint(0, 100)
        results_q.put((site, res))
        ready_q.task_done()  # Interesting!

for _ in range(THREAD_POOL_COUNT):
    worker = threading.Thread(target=process_website, args=(ready_queue, results_queue))
    worker.daemon = True  # Interesting!
    worker.start()

ready_queue.join()

print(results_queue.qsize())

while not results_queue.empty():
    site, result = results_queue.get()
    print(f"Result of {site}: {result}")

print("All done!")