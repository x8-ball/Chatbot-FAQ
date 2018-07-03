#backward compatibility
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import (
         bytes, dict, int, list, object, range, str,
         ascii, chr, hex, input, next, oct, open,
         pow, round, super,
         filter, map, zip)
###############
#TextToSpeech Dependencies#
from gtts import gTTS
from playsound import playsound
###############

import sys
import socket

from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, 
    QPushButton, QAction, QLineEdit, QMessageBox, 
    QLabel, QDesktopWidget,QScrollArea)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot,Qt
from socketIO_client import SocketIO, LoggingNamespace

HOST = '127.0.0.1'
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'Chatbot FAQ'
        self.history = ''

        self.left = 200
        self.top = 200
        self.width = 500
        self.height = 500

        self.inputWidgetHeight = 100

        self.initSockets()
        self.setWindow()
        self.initUI()

    def checkIfHostUp(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((HOST, 5000))
        if result == 0:
           return True
        else:
           return False

    def setWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #self.setWindowFlags(Qt.FramelessWindowHint)
        #self.statusBar().showMessage('Message in statusbar.')
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowModality(Qt.NonModal)  
        self.adjustWindow()

    def adjustWindow(self):
        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()

        widget = self.geometry()
        x = ag.width() - widget.width()
        y = 2 * ag.height() - sg.height() - widget.height()
        self.move(x, y)

    def initSockets(self):
        if self.checkIfHostUp():
            self.socketIO = SocketIO('127.0.0.1', 5000)
            self.socketIO.on('message', self.on_response)   
        else:
            raise Exception('Host is not up')

    def createPinboard(self):
        pinboard = QLabel(self)
        pinboard.setAlignment(Qt.AlignCenter)
        pinboard.setStyleSheet("color: white; ")
        pinboard.setText("")
        #pinboard.setAttribute(Qt.WA_TranslucentBackground)
        pinboard.resize(self.width,300)
        return pinboard

    def createButton(self):
        # Create a button in the window
        button = QPushButton('Ask Robi', self)
        button.resize(100,self.inputWidgetHeight)
        # connect button to function on_click
        button.clicked.connect(self.on_click)
        return button

    def createAvatar(self):
        avatar = QLabel(self)
        pixmap = QPixmap('robi_bunt.png')
        avatar.setPixmap(pixmap.scaled(256,256, Qt.KeepAspectRatio))
        return avatar

    def createInputArea(self):
        inputArea = QLineEdit(self)
        inputArea.resize(200,self.inputWidgetHeight)
        return inputArea

    def adjustWidgets(self):
        yAxis = 300 - self.avatar.height() - self.button.height()
        xAntiPattern = self.inputArea.width() + self.button.width()
        self.pinboard.move(0,0)
        self.inputArea.move(1,self.height-self.inputArea.height()-1)
        self.button.move(1+self.inputArea.width(),self.height-self.button.height()-1)
        self.avatar.move(self.width/2,self.height/2)        

    def initUI(self):
        # Create widgets
        self.avatar = self.createAvatar()
        self.button = self.createButton()
        self.inputArea = self.createInputArea()
        self.pinboard = self.createPinboard()
        self.adjustWidgets()
        self.show()


    def on_response(self,*args):
        try:
            self.history += 'Answered: '+ args[0]['answer'].replace(".",".\n") + '\n'
            self.pinboard.setText(self.history)
            #   print(args[0]['answer'])
            #QMessageBox.question(self, 'Nachricht', "Antwort: " + args[0]['answer'], QMessageBox.Ok, QMessageBox.Ok)
            self.inputArea.setText("")
            tts = gTTS(text=args[0]['answer'], lang='en')
            tts.save("tmp.mp3")
            playsound("tmp.mp3")
        except:
            pass


    @pyqtSlot()
    def on_click(self):
        textboxValue = self.inputArea.text()
        self.history += 'Asked: '+ textboxValue + '\n'
        self.pinboard.setText(self.history)
        #self.output.hide()
        self.socketIO.send({
            "text" : textboxValue,
            "type" : "question"
            })
        self.socketIO.wait(seconds=0.1) 

 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())