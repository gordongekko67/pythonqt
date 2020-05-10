import datetime
import sys
import time

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, \
    QCalendarWidget, QDateEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QDateTime, QDate
from PyQt5.uic.properties import QtCore, QtGui
from docutils.nodes import label
import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt


def grafica(textbox, data1r, data2r):
    #try:
        goog_data2 = data.DataReader(textbox, 'yahoo', data1r, data2r)

    #except FileNotFoundError:


        goog_data = goog_data2.tail(620)
        lows = goog_data['Low']
        highs = goog_data['High']

        fig = plt.figure()
        ax1 = fig.add_subplot(111, ylabel='Google price in $')
        highs.plot(ax=ax1, color='c', lw=2.)
        lows.plot(ax=ax1, color='y', lw=2.)
        plt.hlines(highs.head(200).max(), lows.index.values[0], lows.index.values[-1], linewidth=2, color='g')
        plt.hlines(lows.head(200).min(), lows.index.values[0], lows.index.values[-1], linewidth=2, color='r')
        plt.axvline(linewidth=2, color='b', x=lows.index.values[200], linestyle=':')
        plt.show()

        print("fine corsa")
        time.sleep(30)

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 textbox - pythonspot.com'
        self.left = 20
        self.top = 40
        self.width = 4000
        self.height = 3400
        self.initUI()
        data1r = 0
        data2r = 0

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox

        self.label = QLabel('Nome Azione',self)
        self.label.move(100, 160)
        self.label.show()

        self.nome = QLineEdit(self)
        self.nome.move(300, 160)
        self.nome.show()

        self.dat1 = QDateEdit(self)
        self.dat1.move(500, 160)
        self.dat1.show()

        self.dat2 = QDateEdit(self)
        self.dat2.move(800, 160)
        self.dat2.show()


        # Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(400, 260)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.nome.text()
        data1g = self.dat1.text()
        data1r = datetime.datetime.strptime(data1g, "%d/%m/%Y").strftime("%Y-%m-%d")

        data2g = self.dat2.text()
        data2r = datetime.datetime.strptime(data2g, "%d/%m/%Y").strftime("%Y-%m-%d")

        print(data1r)
        print(data2r)

        if (textboxValue == ""):

            QMessageBox.question(self, 'Message - pythonspot.com', "You typed  Blank: " + textboxValue, QMessageBox.Ok,
                                 QMessageBox.Ok)
            self.textbox.setText("")
        else:
            QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok,
                                 QMessageBox.Ok)
            grafica(textboxValue, data1r,data2r)
            #self.textbox.setText("")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
