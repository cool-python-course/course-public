from flask import Flask

from tachometer_controller import tachometer_api

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    print('Hello')
    print(tachometer_api)
    app.register_blueprint(tachometer_api)

    app.run(host='0.0.0.0', port=5000, debug=True)
