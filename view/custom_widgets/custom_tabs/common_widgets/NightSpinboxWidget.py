from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtCore import Qt

#Night spin box widget 
class NightSpinboxWidget(QtWidgets.QWidget):

    #Init 
    def __init__(self, *args, **kwargs):

        #Call super 
        super(NightSpinboxWidget, self).__init__(*args, **kwargs)

        #Setup UI 
        self.setup_ui()

    #Setup UI
    def setup_ui(self):

        #Create the main layout 
        layout = QtWidgets.QFormLayout()
        
        #Create the label
        self.night_label = QtWidgets.QLabel("Nights:")

        #Create the spinbox 
        self.nights_spinbox = QtWidgets.QSpinBox()

        #Set min/max value for spin box 
        self.nights_spinbox.setMaximum(7)
        self.nights_spinbox.setMinimum(1)

        #Add the widgets to the layout 
        layout.addRow(self.night_label, self.nights_spinbox)

        #Set the main layout 
        self.setLayout(layout)

    #Get value of the spin box
    def value(self):
        return self.nights_spinbox.value()