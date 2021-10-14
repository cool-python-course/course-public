"""
Bonus Task:
 - Add evaluate end point which evaluate an Expression if it is well formatted
    For Example:
        - 5 + 3 => 8
        - (2*10)-3 => 17
 - The evaluate end point should return 4XX Status Code if the expression is not well formatted.
    For Exmaple:
        - (5+3 => Missing Bracket
        - 4 x 2 => Unknown operation (x is not equal to *)
"""
from flask import Flask
from calculator_router import calculator_api

app = Flask(__name__)

@app.route('/')
def hello():
    """
    curl 'http://localhost:5001/' --verbose
    :return:
    """
    return 'Hello World'

if __name__ == '__main__':
    print(f'Hello World')
    app.register_blueprint(calculator_api)
    app.run(host='0.0.0.0',port=5001, debug=True)