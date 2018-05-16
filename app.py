from flask import Flask

app = Flask(__name__)

#是是
@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
