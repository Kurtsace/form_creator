from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from services.pdf import create_auth_form_sa
from model.client import client_info
from view.custom_widgets.popup_dialog.popups import warning_popup

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

        #Connect signals 
        self.connect_signals()

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
        spacer = QtWidgets.QSpacerItem(0,1)
        spacer2 = QtWidgets.QSpacerItem(0, 35)

        #Add widgets to the layout
        layout.addSpacerItem(spacer) 
        layout.addWidget(self.client_info_widget)
        layout.addWidget(self.night_spinbox_widget)
        layout.addSpacerItem(spacer2)
        layout.addWidget(self.create_btn)
        layout.addSpacerItem(spacer) 

        #Set the layout 
        self.setLayout(layout)

    #Connect signals 
    def connect_signals(self):
        self.create_btn.clicked.connect(self.create_form)

    # Create auth form
    def create_form(self):

        #Make sure fields are populated 
        if self.client_info_widget.is_populated():

            #Make sure gender is selected
            gender = self.client_info_widget.get_selected_gender()
            if ( gender != ''):

                #Set gender
                client_info['gender'] = gender

                #Create form 
                create_auth_form_sa(self.night_spinbox_widget.value())
            else:
                # Show warning message
                warning_popup("Gender needs to be selected!")
        else:
            #Show warning 
            warning_popup("No client selected! Make sure to search for a request log first.")
