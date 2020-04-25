import multiprocessing
from server import run_server
import time
import os


start = time.perf_counter()


ip_list_file = 'ip_list.txt'

processes = []


def run_command(index, ip_list_file):
    command = 'python server.py ' + str(index) + ' ' + str(ip_list_file)
    os.system(command)

for i in range(0, 3):
    index = i
    p = multiprocessing.Process(target=run_command, args=[index, ip_list_file])
    p.start()
    processes.append(p)
    time.sleep(1)


for process in processes:
    process.join()


finish = time.perf_counter()
print(f'Finished in {round(finish-start, 3)} seconds')
