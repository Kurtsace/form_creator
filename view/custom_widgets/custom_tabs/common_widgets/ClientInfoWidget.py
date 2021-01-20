from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

#Custom widget class that contains the client info fields as follows: 
#
#Confirm Client Info | Qlabel
#Case Number: [           ] | QLabel : QLineEdit (read only)
#Client Name: [           ] | QLabel : QLineEdit (read only)
#Date of Birth: [           ] | QLabel : QLineEdit (read only)
#Gender: o Male   o Female | QLabel : QRadioButton QRadioButton
#Nights: [1          ] | QLabel : QSpinBox
class ClientInfoWidget(QtWidgets.QWidget):

    #Init 
    def __init__(self, *args, **kwargs):

        #Call super 
        super(ClientInfoWidget, self).__init__(*args, **kwargs)

        #Setup UI
        self.setup_ui()

        #Connect the signals 
        self.connect_signals()

    #Setup UI
    def setup_ui(self):

        #Create the a main vertical layout
        layout = QtWidgets.QVBoxLayout()

        #Create the labels
        self.confirm_client_label = QtWidgets.QLabel(text="Confirm Client Info")
        self.case_number_label = QtWidgets.QLabel(text="Case Number:")
        self.client_name_label = QtWidgets.QLabel(text="Client Name:")
        self.dob_label = QtWidgets.QLabel(text="Date Of Birth:")
        self.gender_label = QtWidgets.QLabel(text="Gender:")
        self.nights_label = QtWidgets.QLabel(text="Nights:")

        #Create radio buttons
        self.male_radio_btn = QtWidgets.QRadioButton(text="Male")
        self.female_radio_btn = QtWidgets.QRadioButton(text="Female")

        #Create radio button groups to avoid conflicts 
        # with selection on similar radio buttons on the page
        self.gender_btn_group = QtWidgets.QButtonGroup()

        #Add the radio buttons to the group 
        self.gender_btn_group.addButton(self.male_radio_btn)
        self.gender_btn_group.addButton(self.female_radio_btn)

        #Create read only line edit boxes
        self.case_number_line = QtWidgets.QLineEdit()
        self.client_name_line = QtWidgets.QLineEdit()
        self.dob_line = QtWidgets.QLineEdit()
        
        #Set read only 
        self.case_number_line.setReadOnly(True)
        self.client_name_line.setReadOnly(True)
        self.dob_line.setReadOnly(True)

        #Create nights spin box 
        self.nights_spinbox = QtWidgets.QSpinBox()

        #Set min/max value for spin box 
        self.nights_spinbox.setMaximum(7)
        self.nights_spinbox.setMinimum(1)

        #Create a form layout 
        self.form_layout = QtWidgets.QFormLayout()

        #Create a radio button layout
        self.radio_btn_h_layout = QtWidgets.QHBoxLayout()
        self.radio_btn_h_layout.addWidget(self.male_radio_btn)
        self.radio_btn_h_layout.addWidget(self.female_radio_btn)

        #Create form group box 
        self.create_formgroup()

        #Add the form layout and the main label to the vertical layout
        layout.addWidget(self.confirm_client_label)
        layout.addLayout(self.form_layout)

        #Set the widget layout 
        self.setLayout(layout)
    
    #Create form group
    def create_formgroup(self):
        
        #Add the rows to the form layout 
        self.form_layout.addRow(self.case_number_label, self.case_number_line)
        self.form_layout.addRow(self.client_name_label, self.client_name_line)
        self.form_layout.addRow(self.dob_label, self.dob_line)
        self.form_layout.addRow(self.gender_label, self.radio_btn_h_layout)
        self.form_layout.addRow(self.nights_label, self.nights_spinbox)

    #Connect signals to the widgets 
    def connect_signals(self):
        pass