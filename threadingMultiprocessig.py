from multiprocessing import Process
import os
import time

def square():
    for i in range(100):
        i*i
processes = []

num_proceses = os.cpu_count()

for i in range(num_proceses):
    p = Process(target=square)
    processes.append(p)


for p in processes:
    p.start()

for p in processes:
    p.join()

print('end main')