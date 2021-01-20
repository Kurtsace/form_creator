from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

#Custom widgets 
from .common_widgets.SearchBarWidget import SearchBarWidget
from .common_widgets.ClientInfoWidget import ClientInfoWidget

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

        #Add a SearchBarWidget 
        self.search_bar = SearchBarWidget()
        
        #Add the SA client info widget
        self.client_info_widget = ClientInfoWidget()

        #Add the create button 
        self.create_btn = QtWidgets.QPushButton(text="Create")

        #Add widgets to the layout 
        layout.addWidget(self.search_bar)
        layout.addWidget(self.client_info_widget)
        layout.addWidget(self.create_btn)

        #Set the layout 
        self.setLayout(layout)
