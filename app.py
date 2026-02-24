from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! My AWS 3-Tier App is Running!"

@app.route('/users')
def users():
    conn = mysql.connector.connect(
        host="myprojectdb.cpwcqoq04ztq.ap-south-1.rds.amazonaws.com",
        user="admin",
        password="kalaiarasi123",
        database="myapp"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    return str(result)

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=80)
