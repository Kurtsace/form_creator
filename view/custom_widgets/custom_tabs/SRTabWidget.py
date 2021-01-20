from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

#Custom widgets 
from .common_widgets.SearchBarWidget import SearchBarWidget
from .common_widgets.ClientInfoWidget import ClientInfoWidget
from .sr_tab_widgets.SRDependentsWidget import SRDependentsWidget

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

        #Connect all signals 

    #Setup UI 
    def setup_ui(self):

        #Create main vertical layo ut 
        layout = QtWidgets.QVBoxLayout()

        #Instantiate the search bar widget
        self.search_bar = SearchBarWidget()

        #Instantiate the client info widget 
        self.client_info_widget = ClientInfoWidget()

        #Instantiate a dependents widget 
        self.dependents_widget = SRDependentsWidget()

        #Create the create btn widget 
        self.create_btn = QtWidgets.QPushButton(text="Create")

        #Add the widgets to the layout 
        layout.addWidget(self.search_bar)
        layout.addWidget(self.client_info_widget)
        layout.addWidget(self.dependents_widget)
        layout.addWidget(self.create_btn)

        #Set the layout 
        self.setLayout(layout)

    #Connect signals 
    def connect_signals(self):

        #Connect search btn signal from search bar widget 
        self.search_bar.search_btn.clicked.connect(self.search_btn_clicked)

    #Search btn clicked 
    def search_btn_clicked(self):
        pass
