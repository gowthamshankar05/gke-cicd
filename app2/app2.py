from flask import Flask

app=Flask(__Name__)

@app.route('/')
def hello_world():
    return 'Hello, World app2!'

if __name__ == '__main__':
    app.run(debug=True, port=8081, host='0.0.0.0')