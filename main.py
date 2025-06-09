from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Paul!'

@app.route('/joshua')
def joshua():
    return 'Hello from joshua2!'

@app.route('/Byron')
def Byron():
        return 'Hello from Byron!'
  
@app.route('/Amelia')
def Peeps():
    return 'Hello from Amelia!'
  
@app.route('/William')
def William():
    return 'Hello from William now'

@app.route('/Paul')
def Paul():
    return 'Hello from Paul 2!'


@app.route('/kingston')
def kingston():
    return 'Hello from Kingston'
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
