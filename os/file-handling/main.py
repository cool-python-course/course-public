import sys
import logging
from typing import List, Tuple

LOG_FORMAT = '%(asctime)s | %(process)d | %(levelname)s | %(message)s'
logging.basicConfig(
    filename='files.log',
    filemode='w',
    level=logging.DEBUG,
    format=LOG_FORMAT
)
LOG = logging.getLogger()
LOG.addHandler(logging.StreamHandler(stream=sys.stdout))

def read_usernames_from_passwd() -> List[str]:
    result = []
    with open('/etc/passwd','r') as passwd:
        LOG.info(f'File {passwd} has been opened for reading')
        line = passwd.readline()
        LOG.info(line)
        while line:
            LOG.info(line)
            username, comment, home_dir, shell = parse_passwd_record(line)
            LOG.info(f'Username: {username}, Comment: {comment}, Home: {home_dir}, Shell: {shell}')
            line = passwd.readline()
    return result

def parse_passwd_record(record : str) -> Tuple[str, str, str, str]:
    fields = record.split(':')
    return (
        fields[0],
        fields[4],
        fields[5],
        fields[6]
    )

if __name__ == '__main__':
    print('Hello World')
    read_usernames_from_passwd()