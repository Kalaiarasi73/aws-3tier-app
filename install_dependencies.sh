#!/bin/bash
echo "Installing Python dependencies..."
cd /home/ec2-user/myapp
sudo pip3 install -r requirements.txt
echo "Dependencies installed!"