import os

DB_HOST = 'DB_HOST'
DB_PORT = 'DB_PORT'
DB_NAME = 'DB_NAME'
DB_USER = 'DB_USER'
DB_PASS = 'DB_PASS'


def _validate_environment_variable() -> None:
    if not all( key in os.environ.keys() for key in [DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS]):
        print('Missing Environment Variable!')
        exit(-1)
    try:
        int(os.environ[DB_PORT])
    except TypeError as err:
        print(f'{err}')
        exit(-1)

def get_database_name() -> str:
    _validate_environment_variable()
    return os.environ[DB_NAME]

def get_mongodb_connection_string():
    _validate_environment_variable()
    return f'mongodb://{os.environ[DB_USER]}:{os.environ[DB_PASS]}@{os.environ[DB_HOST]}:{os.environ[DB_PORT]}/{os.environ[DB_NAME]}?authSource=admin'

