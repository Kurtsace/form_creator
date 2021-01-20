from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

# Dependents widget for son rise tab as follows:
#
# Add Dependents | QLabel
# Does the client have a spouse: o Yes  o No | Qlabel : QRadioButton QRadioButton
# Number of children: [        ] | QLabel : QSpinBox


class SRDependentsWidget(QtWidgets.QWidget):

    # Init
    def __init__(self, *args, **kwargs):

        #Super method
        super(SRDependentsWidget, self).__init__(*args, **kwargs)

        #Setup UI
        self.setup_ui()

    #Setup UI
    def setup_ui(self):

        #Create the main vertical layout 
        layout = QtWidgets.QVBoxLayout()

        #Create the main label 
        self.label = QtWidgets.QLabel("Add Dependents")

        #Create the row labels 
        self.partner_label = QtWidgets.QLabel("Has a partner:")
        self.children_label = QtWidgets.QLabel("Children")

        #Create a radio button group to avoid selection conflics 
        self.partner_rb_group = QtWidgets.QButtonGroup()

        #Create the radio buttons for selecting a partner
        self.partner_rb_yes = QtWidgets.QRadioButton(text="Yes")
        self.partner_rb_no = QtWidgets.QRadioButton(text="No")
        #self.partner_rb_no.setChecked()

        #Add the radio buttons to the radio button group
        self.partner_rb_group.addButton(self.partner_rb_yes)
        self.partner_rb_group.addButton(self.partner_rb_no)

        #Add the radio buttons into a horixontal layout 
        rb_h_layout = QtWidgets.QHBoxLayout()
        rb_h_layout.addWidget(self.partner_rb_yes)
        rb_h_layout.addWidget(self.partner_rb_no)

        #Create the spin box for the number of children
        self.children_spinbox = QtWidgets.QSpinBox()

        #Set min/max of the spinbox
        self.children_spinbox.setMinimum(0)
        self.children_spinbox.setMaximum(7)

        #Create a form layout to house all the rows 
        form_layout = QtWidgets.QFormLayout()

        #Add the rows 
        form_layout.addRow(self.label)
        form_layout.addRow(self.partner_label, rb_h_layout)
        form_layout.addRow(self.children_label, self.children_spinbox)

        #Add everything to the main layout 
        layout.addLayout(form_layout)

        #Set the main layout 
        self.setLayout(layout)
