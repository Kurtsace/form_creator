#Main test file 

from PyQt5 import QtCore, QtGui, QtWidgets
from view.MainWindow import MainWindow

if __name__ == '__main__':

    app = QtWidgets.QApplication([])

    window = MainWindow()
    window.show()

    app.exec_()