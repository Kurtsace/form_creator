from PyQt5 import QtCore, QtGui, QtWidgets
from view.MainWindow import MainWindow

app = QtWidgets.QApplication([])

window = MainWindow()
window.show()

app.exec_()