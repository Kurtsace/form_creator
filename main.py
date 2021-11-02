#Main test file 

from PyQt5 import QtCore, QtGui, QtWidgets
from view.MainWindow import MainWindow
from settings import settings

if __name__ == '__main__':

    # init settings 
    #settings.init()

    app = QtWidgets.QApplication([])

    window = MainWindow()
    window.show()

    app.exec_()

