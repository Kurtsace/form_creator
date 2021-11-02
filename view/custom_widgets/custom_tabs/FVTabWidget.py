from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

# Tab widgets
from .common_widgets.SearchBarWidget import SearchBarWidget
from .common_widgets.ClientInfoWidget import ClientInfoWidget
from .fv_tab_widgets.FVCalcAmountWidget import FVCalcAmountWidget
from view.custom_widgets.popup_dialog.popups import warning_popup, info_popup

# Model
from model.client import client_info

# PDF
from services.pdf import create_food_voucher

# Settings 
from settings.settings import safeway_list

# Food voucher tab class
class FVTabWidget(QtWidgets.QWidget):

    # Init
    def __init__(self, *args, **kwargs):

        # Super method
        super(FVTabWidget, self).__init__(*args, **kwargs)

        # Set the tab name
        self.tab_name = "Food Voucher"

        # Setup UI
        self.setup_ui()

        # Connect signals
        self.connect_signals()

    # Setup UI method
    def setup_ui(self):

        # Create the main vertical layout
        layout = QtWidgets.QVBoxLayout()

        # Create a confirm label
        self.confirm_client_label = QtWidgets.QLabel("Confirm Client Info")

        # Instantiate the FV Client Info Widget
        self.client_info_widget = ClientInfoWidget(add_address_line=True)

        # Instantiate the FV Calc Amount Widget
        self.calc_amount_widget = FVCalcAmountWidget()

        # Create the create btn widget
        self.create_btn = QtWidgets.QPushButton(text="Create")

        # Create a vertical spacer
        spacer = QtWidgets.QSpacerItem(0, 1)

        # Add widgets to the main layout
        layout.addSpacerItem(spacer)
        layout.addWidget(self.client_info_widget)
        layout.addWidget(self.calc_amount_widget)
        layout.addWidget(self.create_btn)
        layout.addSpacerItem(spacer)

        # Set the main layout
        self.setLayout(layout)

    # Connect signals
    def connect_signals(self):

        self.create_btn.clicked.connect(self.create_form)

    def create_form(self):

        if self.client_info_widget.is_populated():

            gender = self.client_info_widget.get_selected_gender()
            if gender != '':

                client_info['gender'] = gender

                if self.calc_amount_widget.is_populated():

                    amount = self.calc_amount_widget.calculate_amount()
                    food, diapers, fuel = self.calc_amount_widget.get_category()
                    id_ = self.window().get_id()
                    location = self.calc_amount_widget.safeway_combobox.currentText()
                    fax_number = safeway_list[location]

                    create_food_voucher(amount, food, diapers, fuel, location, fax_number, id_)

                    info_popup("Form successfuly created")
                    
                    # Clear output fields 
                    self.parent().parent().parent().clear_client_info_fields()
                else:
                    # Show warning message
                    warning_popup("Approved amount form is incomplete!")

            else:
                # Show warning message
                warning_popup("Gender needs to be selected!")
        else:
            # Show warning
            warning_popup(
                "No client selected! Make sure to search for a request log first.")
