
import os
import sys
import logging
import time

LOG_FORMAT = '%(asctime)s | %(process)d | %(levelname)s | %(message)s'
logging.basicConfig(filename='signals.log',
                    filemode='w',
                    format=LOG_FORMAT,
                    level=logging.DEBUG)
LOG = logging.getLogger()

def sleep_and_count(max_count: int = 1, sleep_inerval: int = 1) -> None:
    for i in range(max_count):
        LOG.info(f'Iteration: {i}')
        time.sleep(sleep_inerval)



if __name__ == '__main__':
    
    print('Hello World')
    print(f'Operating System: {os.name}')
    print(f'Uname: {os.uname()}')
    print(f'Platform: {sys.platform}')

    LOG.error('Hello')
    sleep_and_count(10)
