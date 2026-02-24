#!/bin/bash
echo "Starting Flask application..."
cd /home/ec2-user/myapp

# Kill any existing Flask process
sudo pkill -f "python3 app.py" || true

# Start Flask app in background
sudo nohup python3 app.py > /tmp/flask.log 2>&1 &

echo "Flask app started!"
