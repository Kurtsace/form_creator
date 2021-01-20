from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

#Tab widgets 
from .custom_tabs.SATabWidget import SATabWidget
from .custom_tabs.SRTabWidget import SRTabWidget
from .custom_tabs.FVTabWidget import FVTabWidget

#Main tab widget that will house all of the other tabs and their respective widgets 
class MainTabWidget(QtWidgets.QWidget):

    #Init 
    def __init__(self, *args, **kwargs):

        #Call super method 
        super(MainTabWidget, self).__init__(*args, **kwargs)

        #Setup UI
        self.setup_ui()

    #Setup UI 
    def setup_ui(self):

        #Set vertical layout 
        self.layout = QtWidgets.QVBoxLayout()

        #Initialize main tab 
        self.main_tab = QtWidgets.QTabWidget()

        #Set the size policy
        self.size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.main_tab.setSizePolicy(self.size_policy)

        #Initialize tab widgets 
        self.sa_tab = SATabWidget()
        self.sr_tab = SRTabWidget()
        self.fv_tab = FVTabWidget()

        #Add the tab widgets as tabs 
        self.main_tab.addTab(self.sa_tab, self.sa_tab.tab_name)
        self.main_tab.addTab(self.sr_tab, self.sr_tab.tab_name)
        self.main_tab.addTab(self.fv_tab, self.fv_tab.tab_name)

        #Add the main tab to the layout 
        self.layout.addWidget(self.main_tab)

        #Set the widget layout 
        self.setLayout(self.layout)