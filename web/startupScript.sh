#!/bin/bash
#Updatet den Raspberry Pi
#sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get autoremove && sudo apt-get autoclean;
#Wechsel in Chatbot-Verzeichnis und zieht neueste Dateien von Repository, insofern 
#cd ~/Chatbot-FAQ
#git pull
cd ~/Chatbot-FAQ/web
export FLASK_APP=webserver.py;
python -m flask run --host=0.0.0.0;