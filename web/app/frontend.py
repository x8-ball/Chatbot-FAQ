from flask import Flask,render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

@socketio.on('message')
def handleMessage(msg):
	print("handleMessage")
	print(msg.keys())
	if(msg['type']):
		if(msg['type'] == "rating"):
			print("rating answer " + str(msg))
		if(msg['type'] == "question"):
			#calculate answer and send to user
			send({"answer" : "generatedAnswer", "id" : "user_id"})
			print('Antwort: ' + str(msg))

@socketio.on('connect')
def on_connect():
    send({"session_id" : "currentUser123187391"})
    print("user connected")

@socketio.on('disconnect')
def on_disconnect():
    print('Client disconnected')

@app.route('/index')
def index():
	return render_template('index.html')


if __name__ == '__main__':
	socketio.run(app)