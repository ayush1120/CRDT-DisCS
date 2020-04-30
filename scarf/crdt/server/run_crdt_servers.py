import concurrent.futures
import time
import os

import sys
sys.path.append('../../')

from crdt.server.server import startServer
from crdt.server.config import NUM_SERVERS

start = time.perf_counter()


with concurrent.futures.ProcessPoolExecutor() as executor:
    indices = [i for i in range(1, NUM_SERVERS+1)]
    results = [executor.submit(startServer, index) for index in indices]
    
    for f in concurrent.futures.as_completed(results):
        print(f.result())
    

finish = time.perf_counter()
print(f'Servers ran for {round(finish-start, 3)} seconds')
