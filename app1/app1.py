from flask import Flask


app=Flask(__Name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')