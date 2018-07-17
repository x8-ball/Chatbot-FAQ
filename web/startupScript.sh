#!/bin/bash
#sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get autoremove && sudo apt-get autoclean;
#sudo apt-get install -y python-pip python-flask python-flask-sockets;
#sudo pip install flask, flask-socketio python-aiml;
cd ~/Chatbot-FAQ/web
export FLASK_APP=webserver.py;
python -m flask run --host=0.0.0.0;