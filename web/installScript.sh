#!/bin/bash
#sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get autoremove && sudo apt-get autoclean;
#sudo apt-get install -y python-pip python-flask python-flask-sockets;
#sudo pip install flask, flask-socketio python-aiml;
sudo pip --no-cache-dir install -r requirements.txt;

line="bash ~/Chatbot-FAQ/web/startupScript.sh"
grep -q -F line ~/.bashrc || echo line >> ~/.bashrc