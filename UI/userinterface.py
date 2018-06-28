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