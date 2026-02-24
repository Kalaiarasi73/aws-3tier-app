#!/bin/bash
pkill -f "python3 app.py" || true
cd /home/ec2-user/myapp
sudo pip3 install flask
sudo python3 app.py > /tmp/flask.log 2>&1 &