#!/bin/bash
#sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get autoremove && sudo apt-get autoclean;
#sudo apt-get install -y python-pip python-flask python-flask-sockets;
#sudo pip install flask, flask-socketio python-aiml;
cd ~/Chatbot-FAQ/web
sudo apt-get -y install python-pip libevent-dev python-all-dev;
sudo pip install -r requirements.txt;

LINE='bash ~/Chatbot-FAQ/web/startupScript.sh'
FILE=~/.bashrc
crontab -l | grep -q 'search string'  && echo 'crontab schon vorhanden' || grep -qF "$LINE" "$FILE"  || echo "$LINE" | sudo tee --append "$FILE"
reboot