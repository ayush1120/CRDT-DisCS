import concurrent.futures
import time
import os


start = time.perf_counter()

def run_command(index, ip_list_file):
    command = 'python server.py ' + str(index) + ' ' + str(ip_list_file)
    os.system(command)


ip_list_file = 'ip_list.txt'


with concurrent.futures.ProcessPoolExecutor() as executor:
    indices = [i for i in range(0, 3)]
    results = [executor.submit(run_command, index, ip_list_file) for index in indices]
    
    for f in concurrent.futures.as_completed(results):
        print(f.result())
    

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 3)} seconds')
