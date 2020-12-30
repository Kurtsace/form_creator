#Form Creator 
#Created by: Kurt Palo 
#For: HCC (MHRC)

#UI class
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from FormCreatorTab import Ui_MainWindow
import resource

#Main window 
class Ui(QtWidgets.QMainWindow):

    #Initialize 
    def __init__(self):

        #Super class
        super(Ui, self).__init__()

        #Load the UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Show the UI
        self.show()