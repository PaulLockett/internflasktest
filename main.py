from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Paul!'

@app.route('/Amelia')
def Peeps():
    return 'Hello from Amelia!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
