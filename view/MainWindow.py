from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets

#Custom widgets 
from .custom_widgets.MainTabWidget import MainTabWidget
from .custom_widgets.custom_tabs.common_widgets.SearchBarWidget import SearchBarWidget

#Main Window class 
class MainWindow(QMainWindow):

    #Init
    def __init__(self, *args, **kwargs):

        #Call super method 
        super(MainWindow, self).__init__(*args, **kwargs)

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

        #Instantiate a main tab widget 
        self.main_tab = MainTabWidget()

        #Add it to the main vertical layout
        self.vertical_layout.addWidget(self.main_tab)

        #Add the main tab as the central widget 
        self.setCentralWidget(self.central_widget)
