import numpy as np
from src import gdpr

if __name__ == '__main__':
    print('Hello World')
    print(gdpr.generate_users())

    log_entries = gdpr.generate_logs_entries(10,2)
    for log_entry in log_entries:
        print(f'{log_entry}')
