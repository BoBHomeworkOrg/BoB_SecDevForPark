from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return 'hello BoB From Jung Kyoung Jae(user154)'

@app.route("/add")
def add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = a + b
    return str(result)

@app.route("/sub")
def sub():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = a - b
    return str(result)

if __name__ =="__main__":
    app.run(host='0.0.0.0',port=8154)
