from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Paul!'

@app.route('/Paul')
def Paul():
    return 'Hello from Paul 2!'


@app.route('/kingston')
def kingston():
    return 'Hello from Kingston'
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
