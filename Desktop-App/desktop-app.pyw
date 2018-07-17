###############
#TextToSpeech Dependencies#
#from gtts import gTTS
#from playsound import playsound
###############

import sys
import socket

from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLineEdit, QLabel, QDesktopWidget, QScrollArea
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import pyqtSlot,Qt
from socketIO_client import SocketIO

HOST = '141.79.88.5'
IMAGES_DIRECTORY = './images/'
class App(QWidget):
    def __init__(self):
        super(App,self).__init__()
        # for Windows super().__init__()
        self.title = 'Chatbot FAQ'
        self.initSockets()
        self.setWindow()
        self.adjustWindow()
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
        self.setWindowFlags(Qt.FramelessWindowHint)
        #self.setWindowFlags( Qt.Widget | Qt.WindowStaysOnTopHint | Qt.TransparentMode)
        self.setWindowFlags(self.windowFlags() | Qt.TransparentMode)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowModality(Qt.NonModal)  

    def adjustWindow(self):
        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()
        self.usedGeometry = ag
        #self.usedGeometry.setTop(-10)
        self.setGeometry(self.usedGeometry)
        widget = self.geometry()
        x = ag.width() - widget.width()
        y = 2 * ag.height() - sg.height() - widget.height()
        self.move(x, y)

    def adjustWidgets(self):
        rightBorder = self.usedGeometry.width()
        bottomBorder = self.usedGeometry.height()

        self.avatar.move(rightBorder-256,bottomBorder-256)       
        self.button.move(self.avatar.pos().x() -self.button.width(),bottomBorder- self.button.height())
        self.inputArea.move(self.button.pos().x() -self.inputArea.width(),self.button.pos().y())
        self.pinboard.move(rightBorder-self.pinboard.width(),self.avatar.pos().y()-self.pinboard.height())

    def initSockets(self):
        print("checking if server is up")
        if self.checkIfHostUp():
            self.socketIO = SocketIO(HOST, 5000)
            self.socketIO.on('message', self.on_response)   
        else:
            raise Exception('Host is not up')

    def createPinboard(self):
        pinboard = QLabel(self)
        pinboard.setAlignment(Qt.AlignCenter)
        #pinboard.setStyleSheet("color: white; ")
        pinboard.setStyleSheet("image: url("+IMAGES_DIRECTORY+"sprechblase.png)")
        pinboard.setFont(QFont("Times",13,QFont.Bold))
        pinboard.setText("")
        pinboard.resize(800,300)
        return pinboard

    def createButton(self):
        button = QPushButton('Ask Robi', self)
        button.resize(100,100)
        button.clicked.connect(self.on_click)
        return button

    def createAvatar(self):
        avatar = QLabel(self)
        pixmap = QPixmap(IMAGES_DIRECTORY+ 'robi.png')
        avatar.setPixmap(pixmap.scaled(256,256, Qt.KeepAspectRatio))
        return avatar

    def createInputArea(self):
        inputArea = QLineEdit(self)
        inputArea.resize(200,100)
        return inputArea
        
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
            self.inputArea.setText("")
            """
            tts = gTTS(text=args[0]['answer'], lang='de')
            tts.save("..mp3")
            playsound("..mp3")
            """
        except:
            pass

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.inputArea.text()
        self.history = 'Asked: '+ textboxValue + '\n'
        self.pinboard.setText(self.history)
        self.socketIO.send({
            "text" : textboxValue,
            "type" : "question"
            })
        self.socketIO.wait(seconds=0.1) 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())