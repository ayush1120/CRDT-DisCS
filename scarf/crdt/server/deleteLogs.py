import sys
sys.path.append('../../')

import os

from crdt.server.config import NUM_SERVERS


if __name__ == "__main__":
    for index in range(1, NUM_SERVERS+1):
        log_name = 'node'+str(index)+'.log'
        if os.path.exists(log_name):
            os.remove(log_name)

    