"""
from socketIO_client import SocketIO, LoggingNamespace
import logging


logging.getLogger('socketIO-client').setLevel(logging.DEBUG)
logging.basicConfig()

def on_connect():
    print('connect')

def on_disconnect():
    print('disconnect')

def on_response(*args):
    print('on_response', args)

socketIO = SocketIO('127.0.0.1', 5000)
print("ok")
socketIO.on('connect', on_connect)
socketIO.on('disconnect', on_disconnect)

# Listen
print("listen")
socketIO.on('response', on_response)
socketIO.send({
			"text" : 'testtext',
			"type" : "question"
			})
socketIO.wait(seconds=1)

# Stop listening
print("stop")
socketIO.off('aaa_response')
"""
from Tkinter import *
from PIL import ImageTk
import time
import sys
# Add the ptdraft folder path to the sys.path list
sys.path.append('../modell')
import brain

def send():
	answer = brain.calcResponse(e1.get())
	print(answer)
	w2.config(text = answer, )
	e1.delete(0,END)

root = Tk()
root.title("Chatbot")
image_file = "robi_bunt.jpg"
photo = ImageTk.PhotoImage(file=image_file)
#logo = PhotoImage(file="robi_bunt.jpg")

w1 = Label(root, image=photo,compound = CENTER)
#w1.configure(height=300, width=200)
w1.grid(row=0)

w2 = Label(root, text="antworten")
w2.grid(row=0,column=1)

e1 = Entry(root)
e1.grid(row=1,column=1)

b1 = Button(root, text='Senden', command=send)
b1.grid(row=1, column=2, sticky=W, pady=4)
#w2 = Label(root,justify=RIGHT,padx = 10,text='Input feld').pack(side="right")

root.mainloop()


"""
try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

root = tk.Tk()

# pick an image file you have in your working directory
# or specify full path

root.title(image_file)

# put the image on a canvas
cv = tk.Canvas()
cv.pack(side='top', fill='both', expand='yes')
img = cv.create_image(0, 0, image=photo, anchor='nw')
cv.update()

# optionally delete image after 5000 ms
cv.after(5000, cv.delete(img))
cv.update()

root.mainloop()
"""