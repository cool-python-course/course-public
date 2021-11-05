import pandas as pd
from util.logger import LOG
from persist.mongodb import get_collection


if __name__ == '__main__':
    LOG.info('Labor Market Analysis Process Started')
    jobs_collection = get_collection()
    dataset = pd.DataFrame(list(jobs_collection.find()))
    LOG.info('Labor Market Analysis Process Finished')
