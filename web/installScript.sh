#!/bin/bash
#sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get autoremove && sudo apt-get autoclean;
#sudo apt-get install -y python-pip python-flask python-flask-sockets;
#sudo pip install flask, flask-socketio python-aiml;
sudo pip --no-cache-dir install -r requirements.txt;

LINE='bash ~/Chatbot-FAQ/web/startupScript.sh'
FILE=~/.bashrc
grep -qF "$LINE" "$FILE"  || echo "$LINE" | sudo tee --append "$FILE"