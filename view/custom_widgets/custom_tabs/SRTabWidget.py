from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

#Custom widgets 
from .common_widgets.widgets import *
from .sr_tab_widgets.SRDependentsWidget import SRDependentsWidget

#Pop up dialog 
from ..popup_dialog.popups import warning_popup

#Son Rise Village tab widget class
class SRTabWidget(QtWidgets.QWidget):

    #Init
    def __init__(self, *args, **kwargs):

        #Super method 
        super(SRTabWidget, self).__init__(*args, **kwargs)

        #Set the tab name 
        self.tab_name = "Son Rise Village"

        #Setup UI
        self.setup_ui()

    #Setup UI 
    def setup_ui(self):

        #Create main vertical layo ut 
        layout = QtWidgets.QVBoxLayout()

        #Instantiate the client info widget 
        self.client_info_widget = ClientInfoWidget()

        #Instantiate a night spin box widget 
        self.night_spinbox_widget = NightSpinboxWidget()

        #Instantiate a dependents widget 
        self.dependents_widget = SRDependentsWidget()

        #Create the create btn widget 
        self.create_btn = QtWidgets.QPushButton(text="Create")

        #Create a vertical spacer
        spacer = QtWidgets.QSpacerItem(0,2)

        #Add the widgets to the layout 
        layout.addSpacerItem(spacer)
        layout.addWidget(self.client_info_widget)
        layout.addWidget(self.night_spinbox_widget)
        layout.addWidget(self.dependents_widget)
        layout.addWidget(self.create_btn)

        #Set the layout 
        self.setLayout(layout)

