import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, 
    QPushButton, QAction, QLineEdit, QMessageBox, 
    QLabel, QDesktopWidget)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot,Qt
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 image - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        #self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(self.left, self.top, self.width, self.height)


        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()

        widget = self.geometry()
        x = ag.width() - widget.width()
        y = 2 * ag.height() - sg.height() - widget.height()
        self.move(x, y)


        #self.statusBar().showMessage('Message in statusbar.')
        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('robi_bunt.jpg')
        label.setPixmap(pixmap.scaled(256,256, Qt.KeepAspectRatio))
        self.resize(pixmap.width(),pixmap.height())
 
        # Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(0,widget.height()+self.button.height())
 
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(0,widget.height()+self.button.height() + self.textbox.height())
        self.textbox.resize(300,100)

        self.show()
 
    @pyqtSlot()
    def on_click(self):
        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()
        textboxValue = self.textbox.text()
        print(str(ag) + ' ' + str(sg))
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")

 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())