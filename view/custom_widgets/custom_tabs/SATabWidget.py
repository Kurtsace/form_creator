from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

#Custom widgets 
from .common_widgets.widgets import *

#Salvation Army tab class
class SATabWidget(QtWidgets.QWidget):

    #Init 
    def __init__(self, *args, **kwargs):

        #Call super method 
        super(SATabWidget, self).__init__(*args, **kwargs)

        #Set tab name 
        self.tab_name = "Salvation Army"

        #Setup UI
        self.setup_ui()

    #Setup UI 
    def setup_ui(self):

        #Set vertical layout 
        layout = QtWidgets.QVBoxLayout()
        
        #Add the SA client info widget
        self.client_info_widget = ClientInfoWidget()

        #Instantiate a night spin box widget 
        self.night_spinbox_widget = NightSpinboxWidget()

        #Add the create button 
        self.create_btn = QtWidgets.QPushButton(text="Create")

        #Create a vertical spacer
        spacer = QtWidgets.QSpacerItem(0,2)

        #Add widgets to the layout
        layout.addSpacerItem(spacer) 
        layout.addWidget(self.client_info_widget)
        layout.addWidget(self.night_spinbox_widget)
        layout.addWidget(self.create_btn)

        #Set the layout 
        self.setLayout(layout)

    #Set client info fields
    def set_client_info_fields(self):
        
        #Set the client info widget fields
        self.client_info_widget.set_fields()