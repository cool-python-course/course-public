import sys
import logging
from flask import Blueprint, request, Response

tachometer_api = Blueprint('tachometer', __name__, url_prefix='/tachometer')

LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(
    filename='tachometer.log',
    filemode='w',
    format=LOG_FORMAT,
    level=logging.DEBUG
)
LOG = logging.getLogger()
LOG.addHandler(logging.StreamHandler(stream=sys.stdout))

@tachometer_api.route('/', methods=['POST'])
def create_route_record():
    LOG.debug(f'{__name__} Request Received: {request.get_json()}')
    data = request.get_json()
    if 'driver' not in data or 'vehicle' not in data or 'start' not in data or 'speed' not in data:
        LOG.error(f'Bad Request: {data}')
        return Response('Problem', status=400)

    return f'Hello {data["driver"]}'
