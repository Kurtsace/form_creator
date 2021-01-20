from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtCore import Qt

#Tab widgets 
from .common_widgets.SearchBarWidget import SearchBarWidget
from .fv_tab_widgets.FVClientInfoWidget import FVClientInfoWidget
from .fv_tab_widgets.FVCalcAmountWidget import FVCalcAmountWidget

#Food voucher tab class
class FVTabWidget(QtWidgets.QWidget):

    #Init 
    def __init__(self, *args, **kwargs):

        #Super method 
        super(FVTabWidget, self).__init__(*args, **kwargs)

        #Set the tab name 
        self.tab_name = "Food Voucher"

        #Setup UI 
        self.setup_ui()

    #Setup UI method 
    def setup_ui(self):

        #Create the main vertical layout 
        layout = QtWidgets.QVBoxLayout()

        #Instantiate the search widget 
        self.search_bar = SearchBarWidget()

        #Instantiate the FV Client Info Widget
        self.client_info_widget = FVClientInfoWidget()

        #Instantiate the FV Calc Amount Widget 
        self.calc_amount_widget = FVCalcAmountWidget()

        #Create the create btn widget
        self.create_btn = QtWidgets.QPushButton(text="Create")

        #Create a vertical spacer
        spacer = QtWidgets.QSpacerItem(0,23)

        #Add widgets to the main layout 
        layout.addWidget(self.search_bar)
        layout.addWidget(self.client_info_widget)
        layout.addWidget(self.calc_amount_widget)
        layout.addSpacerItem(spacer)
        layout.addWidget(self.create_btn)

        #Set the main layout 
        self.setLayout(layout)