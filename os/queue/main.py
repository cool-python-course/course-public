import os
import signal
import sys
import time
import random
import logging
import multiprocessing


LOG_FORMAT = '%(asctime)s | %(process)d | %(levelname)s | %(message)s'
logging.basicConfig(
    filename='queue.log',
    filemode='w',
    level=logging.DEBUG,
    format=LOG_FORMAT
)
LOG = logging.getLogger()
LOG.addHandler(logging.StreamHandler(stream=sys.stdout))

GENERATED_VALUE_BOUNDS = (0, 100)

def producer(task_queue: multiprocessing.Queue, n_of_tasks: int, delay: int ) -> None:
    for _ in range(n_of_tasks):
        task = {
            'x': random.randint(GENERATED_VALUE_BOUNDS[0], GENERATED_VALUE_BOUNDS[1])
        }
        LOG.info(f'Generates Task {task}')
        task_queue.put(task)
        LOG.info(f'Producer sleeps {delay} secs')
        time.sleep(delay)
    LOG.info(f'Producer has generated all the Tasks')

def consumer(task_queue: multiprocessing.Queue, rate: int) -> None:
    LOG.info('Consumer Starts')
    while True:
        LOG.info('Consumer Samples Task Queue')
        while task_queue.empty() == False:
            task = task_queue.get()
            LOG.info(f'Consumer Reads Task {task}')
            task['solution'] = task['x'] ** 2 if 'x' in task else '0'
            LOG.info(f'Solution {task}')
        LOG.info('Consumer sleeps due to Empty Task Queue')
        time.sleep(rate)



if __name__ == '__main__':
    LOG.info('Hello World')
    task_queue = multiprocessing.Queue()

    LOG.info(f'Main Fork Producer Process')
    producer_pid = os.fork()
    if producer_pid == 0:
        producer(task_queue, 10, 2)
        exit(0)

    LOG.info(f'Main forks Consumer Process')
    consumer_pid = os.fork()
    if consumer_pid == 0:
        consumer(task_queue, 3)
        exit(0)

    LOG.info(f'Main waits for Producer')
    os.waitpid(producer_pid, 0)
    LOG.info(f'Main Waited for Producer')
    while task_queue.empty() == False:
        time.sleep(1)
    LOG.info(f'Main Kills the Consumer')
    os.kill(consumer_pid, signal.SIGTERM.value)

