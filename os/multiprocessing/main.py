import sys
import time
import logging
from multiprocessing import  Process, Queue


LOG_FORMAT = '%(asctime)s | %(process)d | %(levelname)s | %(message)s'
logging.basicConfig(
    filename='multiprocessing.log',
    filemode='w',
    format=LOG_FORMAT,
    level=logging.INFO
)
LOG = logging.getLogger()
LOG.addHandler(logging.StreamHandler(stream=sys.stdout))

def _producer(queue: Queue, interval: int, number_or_messages: int) -> None:
    for i in range(number_or_messages):
        LOG.info(f'Message #{i}')
        queue.put(f'Message #{i}')
        time.sleep(interval)


def _consumer(queue: Queue, sampling_rate: int) -> None:
    while True:
        if not queue.empty():
            LOG.info(queue.get())
        time.sleep(sampling_rate)


if __name__ == '__main__':
    queue = Queue()
    producer = Process(target=_producer, args=(queue, 2, 10))
    consumer = Process(target=_consumer, args=(queue, 5))
    producer.start()
    consumer.start()
    producer.join()
    consumer.kill()
