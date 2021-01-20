from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

#Search Bar Widget class to use for searching for request log ID's 
class SearchBarWidget(QtWidgets.QWidget):

    #Init 
    def __init__(self, *args, **kwargs):

        #Call super init method 
        super(SearchBarWidget, self).__init__(*args, **kwargs)

        #Setup UI 
        self.setup_ui()


    #Set up UI
    def setup_ui(self):

        #Create a main vertical layout 
        self.layout = QtWidgets.QVBoxLayout()

        #Create a horizontal layout for the search bar and button 
        self.search_layout = QtWidgets.QHBoxLayout()

        #Create a label 
        self.label = QtWidgets.QLabel(text="Enter a Request Log ID")

        #Create a button and a line edit (search bar)
        self.search_btn = QtWidgets.QPushButton(text="Search")
        self.search_bar = QtWidgets.QLineEdit()

        #Create an integer only validator for the search line 
        #This will only allow numbers greater than 0 to be typed into the search bar
        self.validator = QtGui.QIntValidator(bottom=0, parent=self)

        #Set the validator for the line edit 
        self.search_bar.setValidator(self.validator)

        #Add the button and search bar to the horizontal search layout 
        self.search_layout.addWidget(self.search_bar)
        self.search_layout.addWidget(self.search_btn)

        #Set the margins of the main layout
        self.layout.addStretch(1)
        self.layout.setSpacing(5)

        #Add the label and search widgets to the main layout
        self.layout.addWidget(self.label)
        self.layout.addLayout(self.search_layout)

        #Set the layout of the widget 
        self.setLayout(self.layout)