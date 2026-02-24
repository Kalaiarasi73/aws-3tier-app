from flask import Flask
import boto3

app = Flask(__name__)

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
table = dynamodb.Table('users')

@app.route('/')
def home():
    return "Hello! My AWS 3-Tier App is Running!"

@app.route('/users')
def get_users():
    result = table.scan()
    return str(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)