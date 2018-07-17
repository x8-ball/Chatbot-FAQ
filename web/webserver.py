from flask import Flask,render_template
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
	if(msg['type']):
		if(msg['type'] == "question"):
			print('User fragte: ' + msg['text'])
			answer = brain.calcResponse(msg['text'])
			send({"answer" : answer})
			print('Antwort: ' + str(answer))

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
	_gifFiles = []
	for file in os.listdir("./static"):
	    if file.endswith(".gif"):
	        _gifFiles.append(file)
	return render_template('index.html',adress = adress,gifFiles = _gifFiles)

if __name__ == '__main__':
	app.host = '0.0.0.0'
	adress =  'localhost'
	#adress = '141.79.88.5'
	socketio.run(app)