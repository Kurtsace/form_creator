from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

# Custom widgets
from .common_widgets.ClientInfoWidget import ClientInfoWidget
from .common_widgets.SearchBarWidget import SearchBarWidget
from .sr_tab_widgets.SRDependentsWidget import SRDependentsWidget
from .common_widgets.NightSpinboxWidget import NightSpinboxWidget

# Pop up dialog
from ..popup_dialog.popups import warning_popup

# PDF creator
from services.pdf import create_auth_form_sr

# Client info
from model.client import client_info

# Son Rise Village tab widget class


class SRTabWidget(QtWidgets.QWidget):

    # Init
    def __init__(self, *args, **kwargs):

        # Super method
        super(SRTabWidget, self).__init__(*args, **kwargs)

        # Set the tab name
        self.tab_name = "Son Rise Village"

        # Setup UI
        self.setup_ui()

        # Connect signals
        self.connect_signals()

    # Setup UI
    def setup_ui(self):

        # Create main vertical layo ut
        layout = QtWidgets.QVBoxLayout()

        # Instantiate the client info widget
        self.client_info_widget = ClientInfoWidget()

        # Instantiate a night spin box widget
        self.night_spinbox_widget = NightSpinboxWidget()

        # Instantiate a dependents widget
        self.dependents_widget = SRDependentsWidget()

        # Create the create btn widget
        self.create_btn = QtWidgets.QPushButton(text="Create")

        # Create a vertical spacer
        spacer = QtWidgets.QSpacerItem(0, 1)

        # Add the widgets to the layout
        layout.addSpacerItem(spacer)
        layout.addWidget(self.client_info_widget)
        layout.addWidget(self.night_spinbox_widget)
        layout.addWidget(self.dependents_widget)
        layout.addWidget(self.create_btn)
        layout.addSpacerItem(spacer)

        # Set the layout
        self.setLayout(layout)

    # Connect signals method
    def connect_signals(self):

        # Connect create btn
        self.create_btn.clicked.connect(self.create_form)

    # Create form method
    def create_form(self):

        # Make sure there is a client selected
        if self.client_info_widget.is_populated():

            # Check if gender has been selected as well
            gender = self.client_info_widget.get_selected_gender()
            if(gender != ''):

                # Call create auth form
                client_info['gender'] = gender
                children = self.dependents_widget.get_children()
                nights = self.night_spinbox_widget.value()
                spouse = self.dependents_widget.has_spouse()
                create_auth_form_sr(spouse, children, nights)

            else:
                # Show warning message
                warning_popup("Gender needs to be selected!")
        else:
            # Show warning
            warning_popup(
                "No client selected! Make sure to search for a request log first.")
