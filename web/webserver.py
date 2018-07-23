#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask,render_template,request
from flask_socketio import SocketIO, send

import sys
import os
sys.path.append('.')
sys.path.append('modell')
import brain

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('message')
def handleMessage(msg):
	#print request.remote_addr
	if(msg['type']):
		if(msg['type'] == "question"):
			print('User fragte: ' + msg['text'])
			answer = brain.calcResponse(msg['text'],request.remote_addr)
			send({"answer" : answer})
			print('Antwort: ' + str(answer))

@socketio.on('connect')
def on_connect():
    if(not brain.loadBrain(request.remote_addr)):
    	send({"answer" : "Robi ist gerade sehr beschäftigt und hat keine Zeit"})

@socketio.on('disconnect')
def on_disconnect():
	brain.deleteBrain(request.remote_addr)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
	adress =  '192.168.0.116'
	_gifFiles = []
	for file in os.listdir("./static"):
	    if file.endswith(".gif"):
	        _gifFiles.append(file)
	return render_template('index.html',adress = adress,gifFiles = _gifFiles)

if __name__ == '__main__':
	app.host = '0.0.0.0'
	socketio.run(app)
