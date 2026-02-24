from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! My AWS 3-Tier App is Running!"

@app.route('/users')
def users():
    return "Users page is working!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)