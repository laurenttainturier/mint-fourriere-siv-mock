from flask import Flask

app = Flask(__name__)


@app.route('/hello_world')
def hello_world():
    return 'hello world'


@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def error():
    return 'Unknown error', 500


if __name__ == '__main__':
    app.run()
