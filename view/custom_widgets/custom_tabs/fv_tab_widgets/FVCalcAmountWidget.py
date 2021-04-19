from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

# Import services
from services.calculations import calculate_food_amount

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

    # Init
    def __init__(self, *args, **kwargs):

        # Super method
        super(FVCalcAmountWidget, self).__init__(*args, **kwargs)

        # Setup UI
        self.setup_ui()

        # Connect signals 
        self.connect_signals()

    # Setup UI
    def setup_ui(self):

        # Create label
        self.calc_label = QtWidgets.QLabel(text="Calculate Approved Amount")

        # Create the first column form group
        column1_formgroup = self.create_c1_formgroup()

        # Create the second column form group
        column2_formgroup = self.create_c2_formgroup()

        # Create the third column (standalone widget as it only has 1 element)
        self.total_amount = QtWidgets.QLabel(text="$0.00")
        self.total_amount.setAlignment(Qt.AlignCenter)

        # Create the safeway location combo box widget
        self.safeway_label = QtWidgets.QLabel(text="Safeway Location:")
        self.safeway_combobox = QtWidgets.QComboBox()

        # Add the safeway label and combo box into its own form layout
        safeway_layout = QtWidgets.QFormLayout()
        safeway_layout.addRow(self.safeway_label, self.safeway_combobox)

        # Create the vertical spacers for each column
        self.vertical_spacer1 = QtWidgets.QFrame()
        self.vertical_spacer1.setFrameShape(QtWidgets.QFrame.VLine)
        self.vertical_spacer1.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.vertical_spacer2 = QtWidgets.QFrame()
        self.vertical_spacer2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vertical_spacer2.setFrameShape(QtWidgets.QFrame.VLine)

        # Create a horizontal layout to house all the column elements
        calc_h_layout = QtWidgets.QHBoxLayout()

        # Add the horizontal layouts/widgets into its own horizontal layout
        calc_h_layout.addLayout(column1_formgroup)
        calc_h_layout.addWidget(self.vertical_spacer1)
        calc_h_layout.addLayout(column2_formgroup)
        calc_h_layout.addWidget(self.vertical_spacer2)
        calc_h_layout.addWidget(self.total_amount)

        # Create a vertical layout to house all widgets/layouts
        calc_main_layout = QtWidgets.QVBoxLayout()

        # Add the layouts and widgets
        calc_main_layout.addWidget(self.calc_label)
        calc_main_layout.addLayout(calc_h_layout)
        calc_main_layout.addLayout(safeway_layout)

        # Set the main layout
        self.setLayout(calc_main_layout)

     # Creates the first column of the calculated amount widgets
    def create_c1_formgroup(self):

        # Create widget labels for column 1 of the calculated section
        self.days_label = QtWidgets.QLabel(text="Days:")
        self.adults_label = QtWidgets.QLabel(text="Adults:")
        self.children_label = QtWidgets.QLabel(text="Children")

        # Create spin box widgets for each label
        self.days_spinbox = QtWidgets.QSpinBox()
        self.adults_spinbox = QtWidgets.QSpinBox()
        self.children_spinbox = QtWidgets.QSpinBox()

        # Set min/max for each spinbox as per MHRC specs
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

        # Return the form group
        return c1_formgroup

    # Creates the second column widgets of the calculated section
    def create_c2_formgroup(self):

        # Create the widget labels for column 2 of the calculated section
        self.food_label = QtWidgets.QLabel(text="Food")
        self.diapers_label = QtWidgets.QLabel(text="Diapers")
        self.fuel_label = QtWidgets.QLabel(text="Fuel")

        # Create the checkboxes for each label
        self.food_checkbox = QtWidgets.QCheckBox()
        self.diapers_checkbox = QtWidgets.QCheckBox()
        self.fuel_checkbox = QtWidgets.QCheckBox()

        # Create a form layout to house the widgets in form-like fashion
        c2_formgroup = QtWidgets.QFormLayout()

        # Add the rows to the form group
        c2_formgroup.addRow(self.food_checkbox, self.food_label)
        c2_formgroup.addRow(self.diapers_checkbox, self.diapers_label)
        c2_formgroup.addRow(self.fuel_checkbox, self.fuel_label)

        c2_formgroup.setSpacing(15)

        # Return the form layout
        return c2_formgroup

    # Connect signals
    def connect_signals(self):

        # Connect signals for when the check boxes are clicked
        self.food_checkbox.stateChanged.connect(self.calculate_amount)
        self.diapers_checkbox.stateChanged.connect(self.calculate_amount)
        self.fuel_checkbox.stateChanged.connect(self.calculate_amount)

        # Connect signals for when the spin box values are changing 
        self.days_spinbox.valueChanged.connect(self.calculate_amount)
        self.children_spinbox.valueChanged.connect(self.calculate_amount)
        self.adults_spinbox.valueChanged.connect(self.calculate_amount)


    # Helper function for calculating amounts
    def calculate_amount(self):

        # Variables
        days = self.days_spinbox.value()
        adults = self.adults_spinbox.value()
        children = self.children_spinbox.value()
        food = self.food_checkbox.isChecked()
        fuel = self.fuel_checkbox.isChecked()
        diapers = self.diapers_checkbox.isChecked()

        # Call services calculation method and get amount 
        approved_amount = str( calculate_food_amount(days=days, adults=adults, children=children, food=food, fuel=fuel, diapers=diapers) )

        # Set the amount label to the current calculated value 
        self.total_amount.setText( "${}".format( approved_amount ) )

        return float(approved_amount)

    def get_category(self):
        return (self.food_checkbox.isChecked(), self.diapers_checkbox.isChecked(), self.fuel_checkbox.isChecked())

    def is_populated(self):

        food = self.food_checkbox.isChecked()
        fuel = self.fuel_checkbox.isChecked()
        diapers = self.diapers_checkbox.isChecked()
        location = self.safeway_combobox.currentText()

        return (food or fuel or diapers)

