from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

# Custom widget class that contains the client info fields as follows:
#
# Confirm Client Info | Qlabel
# Client Name: [  ] | QLabel : QLineEdit (read only)
# Date of Birth: [  ] | QLabel : QLineEdit (read only)
# Address: [  ] | QLabel : QLineEdit

class FVClientInfoWidget(QtWidgets.QWidget):

    # Init
    def __init__(self, *args, **kwargs):

        # Super method
        super(FVClientInfoWidget, self).__init__(*args, **kwargs)

        # Setup UI
        self.setup_ui()

        #Connect signals to widgets 
        self.connect_signals()

    # Setup UI
    def setup_ui(self):

        # Create widget labels for confirm section
        self.confirm_client_label = QtWidgets.QLabel(text="Confirm Client Info")
        self.client_name_label = QtWidgets.QLabel(text="Client Name:")
        self.dob_label = QtWidgets.QLabel(text="Date Of Birth:")
        self.address_label = QtWidgets.QLabel(text="Address:")

        # Create line edit widgets for each label
        self.client_name_line = QtWidgets.QLineEdit()
        self.dob_line = QtWidgets.QLineEdit()
        self.address_line = QtWidgets.QLineEdit()

        # Set to read only
        self.client_name_line.setReadOnly(True)
        self.dob_line.setReadOnly(True)
        self.address_line.setReadOnly(True)

        # Create a form layout to house the confirm section
        confirm_client_formgroup = QtWidgets.QFormLayout()

        # Add the individual rows to the form group
        confirm_client_formgroup.addRow(self.confirm_client_label)
        confirm_client_formgroup.addRow(self.client_name_label, self.client_name_line)
        confirm_client_formgroup.addRow(self.dob_label, self.dob_line)
        confirm_client_formgroup.addRow(self.address_label, self.address_line)

        #Set the main layout to the created formgroup
        self.setLayout(confirm_client_formgroup)

    #Connect all the signals to the widgets
    def connect_signals(self):
        pass

    #Set client infor fields method 
    def set_fields(self, client_info):

        #Set each field to its corresponding label 
        self.client_name_line.setText(client_info.full_name)
        self.dob_line.setText(client_info.dob)
        self.address_line.setText(client_info.address)