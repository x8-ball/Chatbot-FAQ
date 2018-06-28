#backward compatibility
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import (
         bytes, dict, int, list, object, range, str,
         ascii, chr, hex, input, next, oct, open,
         pow, round, super,
         filter, map, zip)
######

import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, 
    QPushButton, QAction, QLineEdit, QMessageBox, 
    QLabel, QDesktopWidget,QScrollArea)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot,Qt
from socketIO_client import SocketIO, LoggingNamespace


class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'Chatbot FAQ'
        self.left = 200
        self.top = 200
        self.width = 500
        self.height = 500
        self.initSockets()
        self.initUI()
 
    def initSockets(self):
        self.socketIO = SocketIO('127.0.0.1', 5000)
        self.socketIO.on('message', self.on_response)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.setWindowModality(Qt.NonModal)

        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()

        widget = self.geometry()
        x = ag.width() - widget.width()
        y = 2 * ag.height() - sg.height() - widget.height()
        self.move(x, y)


        #self.statusBar().showMessage('Message in statusbar.')
        # Create widget
        self.label = QLabel(self)
        pixmap = QPixmap('robi_bunt.png')
        self.label.setPixmap(pixmap.scaled(256,256, Qt.KeepAspectRatio))
        
        

        self.output = QLabel(self)
        #self.output.setText("lorem ipsum dolor sita mia iasdjasiodjaojsdoijajisdodajsji")

        # Create a button in the window
        self.button = QPushButton('Ask Robi', self)
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        # Create textbox
        self.textbox = QLineEdit(self)

        self.pinboard = QLabel(self)
        self.pinboard.setAlignment(Qt.AlignCenter)
        self.pinboard.setStyleSheet("color: white; ")
        self.history = ""
        self.pinboard.setText(self.history)
        #self.pinboard.setAttribute(Qt.WA_TranslucentBackground)
        self.pinboard.resize(self.width,300)
        ySize = 100
        self.textbox.resize(200,ySize)
        self.button.resize(100,ySize)
        self.output.resize(200,100)

        yAxis = 300 - self.label.height() - self.button.height()

        xAntiPattern = self.textbox.width() + self.button.width()
        """
        self.textbox.move(0,yAxis)
        self.button.move(200,yAxis)
        self.output.move(0,0)
        """
        self.pinboard.move(0,0)
        self.textbox.move(1,self.height-self.textbox.height()-1)
        self.button.move(1+self.textbox.width(),self.height-self.button.height()-1)
        self.output.move(0,0)
        self.label.move(self.width/2,self.height/2)
        self.show()
    def on_response(self,*args):
    #print('on_response', args)
        try:
            self.history += 'Answered: '+ args[0]['answer'] + '\n'
            self.pinboard.setText(self.history)
            print(args[0]['answer'])
            #QMessageBox.question(self, 'Nachricht', "Antwort: " + args[0]['answer'], QMessageBox.Ok, QMessageBox.Ok)
            self.textbox.setText("")
        except:
            pass


    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        self.history += 'Asked: '+ textboxValue + '\n'
        self.pinboard.setText(self.history)
        self.output.hide()
        self.socketIO.send({
            "text" : textboxValue,
            "type" : "question"
            })
        self.socketIO.wait(seconds=1) 

 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())