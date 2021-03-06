import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from docutils.nodes import label


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 textbox - pythonspot.com'
        self.left = 20
        self.top = 40
        self.width = 400
        self.height = 340
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)



        # Create textbox

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Name:')
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)

        self.nameLabel2 = QLabel(self)
        self.nameLabel2.setText('Cognome:')
        self.line2 = QLineEdit(self)

        self.line2.move(80, 60)
        self.line2.resize(200, 32)
        self.nameLabel2.move(20, 60)


        # Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(20, 120)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.line.text()
        if (textboxValue == ""):

            QMessageBox.question(self, 'Message - pythonspot.com', "You typed  Blank: " + textboxValue, QMessageBox.Ok,
                                   QMessageBox.Ok)
            self.textbox.setText("")
        else:
            QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok,
                                 QMessageBox.Ok)
            self.textbox.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())