from socketIO_client import SocketIO, LoggingNamespace

def on_response(*args):
	#print('on_response', args)
	try:
		print(args[0]['answer'])
	except:
		pass

socketIO = SocketIO('127.0.0.1', 5000)
socketIO.on('message', on_response)
socketIO.send({
			"text" : 'hi',
			"type" : "question"
			})
socketIO.wait(seconds=0.3)