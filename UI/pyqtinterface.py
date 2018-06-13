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
    QLabel, QDesktopWidget)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot,Qt
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'Chatbot FAQ'
        self.left = 200
        self.top = 200
        self.width = 300
        self.height = 300
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
       

        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()

        widget = self.geometry()
        x = ag.width() - widget.width()
        y = 2 * ag.height() - sg.height() - widget.height()
        self.move(x, y)


        #self.statusBar().showMessage('Message in statusbar.')
        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('robi_bunt.png')
        label.setPixmap(pixmap.scaled(256,256, Qt.KeepAspectRatio))
        #self.resize(pixmap.width(),pixmap.height())
 
        self.output = QLabel(self)
        self.output.setText("lorem ipsum dolor sita mia iasdjasiodjaojsdoijajisdodajsji")

        # Create a button in the window
        self.button = QPushButton('Show text', self)
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        # Create textbox
        self.textbox = QLineEdit(self)
        
 
        ySize = 50
        self.textbox.resize(200,ySize)
        self.button.resize(100,ySize)
        self.output.resize(200,100)

        yAxis = 300 - label.height() - self.button.height()
        self.textbox.move(0,yAxis)
        self.button.move(200,yAxis)
        self.output.move(0,0)
        
        self.show()
 
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        print("lalal")
        self.output.hide()
        QMessageBox.question(self, 'Nachricht', "Eingabe: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")

 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())