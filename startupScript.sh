#!/bin/bash
#sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get autoremove && sudo apt-get autoclean;
sudo apt-get install -y python-pip python-flask python-flask-sockets;
#sudo pip --no-cache-dir install -r requirementsServer.txt;
sudo pip install flask, flask-socketio python-aiml;
cd web/app;
export FLASK_APP=frontend.py;
python -m flask run --host=0.0.0.0;