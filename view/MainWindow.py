from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt, QThreadPool
from PyQt5 import QtWidgets, QtGui

#Custom widgets 
from .custom_widgets.MainTabWidget import MainTabWidget
from .custom_widgets.custom_tabs.common_widgets.SearchBarWidget import SearchBarWidget

from resources import resource

#Main Window class 
class MainWindow(QMainWindow):
    #Init
    def __init__(self, *args, **kwargs):

        #Call super method 
        super(MainWindow, self).__init__(*args, **kwargs)

        # Begin a threadpool 
        self.threadpool = QThreadPool()

        #Setup UI
        self.setup_ui()

    #Setup UI
    def setup_ui(self):

        #Set fized window size 
        self.setFixedSize(400, 625)

        #Set the window title 
        self.setWindowTitle("Form Creator")

        #Create the central widget 
        self.central_widget = QtWidgets.QWidget()

        #Create main vertical layout 
        self.vertical_layout = QtWidgets.QVBoxLayout(self.central_widget)

        #Create the logo widget 
        self.logo_widget = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap(":Images/list.png")
        self.logo_widget.setPixmap(pixmap)
        self.logo_widget.setAlignment(Qt.AlignCenter)

        #Instantiate a main search bar widget
        self.search_bar_widget = SearchBarWidget(parent=self)

        #Instantiate a main tab widget 
        self.main_tab = MainTabWidget()

        #Add widgets to the main vertical layout
        self.vertical_layout.addWidget(self.logo_widget)
        self.vertical_layout.addWidget(self.search_bar_widget)
        self.vertical_layout.addWidget(self.main_tab)

        #Add the main tab as the central widget 
        self.setCentralWidget(self.central_widget)

    #Set methods 
    def set_client_info_fields(self):
        
        #Call the main tabs set client info fields method 
        self.main_tab.set_client_info_fields()
