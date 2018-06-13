from flask import Flask,render_template
from flask_socketio import SocketIO, send
import sys
# Add the ptdraft folder path to the sys.path list
sys.path.append('.')
sys.path.append('../../modell')

import brain

app = Flask(__name__)
app.debug = True
app.host = '0.0.0.0'
socketio = SocketIO(app)
#bei localhost: '127.0.0.1'
adress = 'chatbot.local'

@socketio.on('message')
def handleMessage(msg):
	print("handleMessage")
	print(msg)
	if(msg['type']):
		if(msg['type'] == "question"):
			#calculate answer and send to user
			print('user asked : ' + msg['text'])
			answer = brain.calcResponse(msg['text'])
			send({"answer" : answer})
			print('Antwort: ' + str(answer))
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
	return render_template('index.html',adress = adress)


if __name__ == '__main__':
	if len(sys.argv) > 1:
		adress = sys.argv[1]
	socketio.run(app)