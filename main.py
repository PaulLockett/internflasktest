from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Paul!'

@app.route('/William')
def William():
    return 'Hello from William now'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
