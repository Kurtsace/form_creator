from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

# Custom widget class that contains the client info fields as follows:
#
# Calculate Approved Amount  | QLabel
# Col 1                                  | Col 2                           | Col 3
# Days: [  ] | QLabel : QSpinBox           [] Food | QCheckBox QLabel
# Adults: [  ] | QLabel : QSpinBox         [] Diapers | QCheckBox QLabel     $Calculated amount | QLabel
# Children: [  ] | QLabel : QSpinBox       [] Fuel | QCheckBox QLabel
#
# Safeway Location : [        ] | QLabel : QComboBox

class FVCalcAmountWidget(QtWidgets.QWidget):

    #Init 
    def __init__(self, *args, **kwargs):

        #Super method 
        super(FVCalcAmountWidget, self).__init__(*args, **kwargs)

        #Setup UI
        self.setup_ui()

    #Setup UI
    def setup_ui(self):

        #Create label 
        self.calc_label = QtWidgets.QLabel(text="Calculate Approved Amount")

        #Create the first column form group
        column1_formgroup = self.create_c1_formgroup()

        #Create the second column form group 
        column2_formgroup = self.create_c2_formgroup()

        #Create the third column (standalone widget as it only has 1 element)
        self.column3_total_amount = QtWidgets.QLabel(text="$0.00")
        self.column3_total_amount.setAlignment(Qt.AlignCenter)

        #Create the safeway location combo box widget 
        self.safeway_label = QtWidgets.QLabel(text="Safeway Location:")
        self.safeway_combobox = QtWidgets.QComboBox()

        #Add the safeway label and combo box into its own form layout
        safeway_layout = QtWidgets.QFormLayout()
        safeway_layout.addRow(self.safeway_label, self.safeway_combobox)

        #Create the vertical spacers for each column
        self.vertical_spacer1 = QtWidgets.QFrame()
        self.vertical_spacer1.setFrameShape(QtWidgets.QFrame.VLine)
        self.vertical_spacer1.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        self.vertical_spacer2 = QtWidgets.QFrame()
        self.vertical_spacer2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vertical_spacer2.setFrameShape(QtWidgets.QFrame.VLine)

        #Create a horizontal layout to house all the column elements 
        calc_h_layout = QtWidgets.QHBoxLayout()

        #Add the horizontal layouts/widgets into its own horizontal layout
        calc_h_layout.addLayout(column1_formgroup)
        calc_h_layout.addWidget(self.vertical_spacer1)
        calc_h_layout.addLayout(column2_formgroup)
        calc_h_layout.addWidget(self.vertical_spacer2)
        calc_h_layout.addWidget(self.column3_total_amount)

        #Create a vertical layout to house all widgets/layouts
        calc_main_layout = QtWidgets.QVBoxLayout()

        #Add the layouts and widgets 
        calc_main_layout.addWidget(self.calc_label)
        calc_main_layout.addLayout(calc_h_layout)
        calc_main_layout.addLayout(safeway_layout)

        #Set the main layout 
        self.setLayout(calc_main_layout)

     #Creates the first column of the calculated amount widgets
    def create_c1_formgroup(self):

        # Create widget labels for column 1 of the calculated section
        self.days_label = QtWidgets.QLabel(text="Days:")
        self.adults_label = QtWidgets.QLabel(text="Adults:")
        self.children_label = QtWidgets.QLabel(text="Children")

        # Create spin box widgets for each label
        self.days_spinbox = QtWidgets.QSpinBox()
        self.adults_spinbox = QtWidgets.QSpinBox()
        self.children_spinbox = QtWidgets.QSpinBox()

        #Set min/max for each spinbox as per MHRC specs
        self.days_spinbox.setMaximum(4)
        self.days_spinbox.setMinimum(1)
        self.adults_spinbox.setMaximum(2)
        self.adults_spinbox.setMinimum(1)
        self.children_spinbox.setMaximum(7)
        self.children_spinbox.setMinimum(0)

        # Create a form layout to house widgets in a form-like fashion
        c1_formgroup = QtWidgets.QFormLayout()

        # Add the individual rows to the form group
        c1_formgroup.addRow(self.days_label, self.days_spinbox,)
        c1_formgroup.addRow(self.adults_label, self.adults_spinbox)
        c1_formgroup.addRow(self.children_label, self.children_spinbox)

        #Return the form group
        return c1_formgroup

    #Creates the second column widgets of the calculated section 
    def create_c2_formgroup(self):

        #Create the widget labels for column 2 of the calculated section 
        self.food_label = QtWidgets.QLabel(text="Food")
        self.diapers_label = QtWidgets.QLabel(text="Diapers")
        self.fuel_label = QtWidgets.QLabel(text="Fuel")

        #Create the checkboxes for each label 
        self.food_checkbox = QtWidgets.QCheckBox()
        self.diapers_checkbox = QtWidgets.QCheckBox()
        self.fuel_checkbox = QtWidgets.QCheckBox()

        #Create a form layout to house the widgets in form-like fashion
        c2_formgroup = QtWidgets.QFormLayout()

        #Add the rows to the form group 
        c2_formgroup.addRow(self.food_checkbox, self.food_label)
        c2_formgroup.addRow(self.diapers_checkbox, self.diapers_label)
        c2_formgroup.addRow(self.fuel_checkbox, self.fuel_label)

        c2_formgroup.setSpacing(15)

        #Return the form layout 
        return c2_formgroup

