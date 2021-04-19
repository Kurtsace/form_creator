
# PyQt5 imports
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QThreadPool

# Other imports
from services.workers import ScraperWorker
from view.custom_widgets.popup_dialog import popups
from services.scraper import get_client_info

# Search Bar Widget class to use for searching for request log ID's


class SearchBarWidget(QtWidgets.QWidget):

    # Init
    def __init__(self, parent, *args, **kwargs):

        # Call super init method
        super(SearchBarWidget, self).__init__(*args, **kwargs)

        # Setup UI
        self.setup_ui()

        # Set parent widget
        self.parent = parent

        # Connect signals
        self.connect_signals()

    # Set up UI
    def setup_ui(self):

        # Create a main vertical layout
        layout = QtWidgets.QVBoxLayout()

        # Create a horizontal layout for the search bar and button
        search_layout = QtWidgets.QHBoxLayout()

        # Create a label
        self.label = QtWidgets.QLabel(text="Enter a Request Log ID")

        # Create a button and a line edit (search bar)
        self.search_btn = QtWidgets.QPushButton(text="Search")
        self.search_bar = QtWidgets.QLineEdit()

        # Disable search btn by default
        self.search_btn.setEnabled(False)

        # Create an integer only validator for the search line
        # This will only allow numbers greater than 0 to be typed into the search bar
        validator = QtGui.QIntValidator(bottom=0, parent=self)

        # Set the validator for the line edit
        self.search_bar.setValidator(validator)

        # Add the button and search bar to the horizontal search layout
        search_layout.addWidget(self.search_bar)
        search_layout.addWidget(self.search_btn)

        # Set the margins of the main layout
        layout.addStretch(1)
        layout.setSpacing(5)

        # Add the label and search widgets to the main layout
        layout.addWidget(self.label)
        layout.addLayout(search_layout)

        # Set the layout of the widget
        self.setLayout(layout)

     # Connect signals
    def connect_signals(self):

        self.search_btn.clicked.connect(self.search_client)
        self.search_bar.textChanged.connect(self.search_text_changed)

    # Search client info method
    def search_client(self):

        # Disable the search button and change the text
        self.search_btn.setEnabled(False)
        self.search_btn.setText("Searching")

        # Get the client info first
        # Run in a separate thread to prevent crashing of the main window
        id_ = self.search_bar.text()

        # Create a worker thread
        scraper_thread = ScraperWorker(get_client_info, id_)

        # Connect the signals to the worker thread
        # Signal for when the thread is finished
        scraper_thread.signals.finished.connect(self.set_client_fields)

        # Signal for when an error has occured, i.e when the client is not found
        scraper_thread.signals.client_not_found_error.connect(self.show_error)

        # Signal for when a traceback occurs regarding the chromedriver
        scraper_thread.signals.error.connect(self.show_traceback_error)

        # Begin the thread
        self.parent.threadpool.start(scraper_thread)

    # Show error method
    def show_error(self):

        # Pop up a dialog for the error message
        popups.error_popup(text="Client not found!",
                           detailed_text="Make sure the Request Log ID has already been created or is within bounds")

    # Show error method
    def show_traceback_error(self, signal):

        print(signal)

        # Pop up a dialog for the error message
        popups.error_popup(text="A critical error has occured.",
                           detailed_text=signal)

    # Set client fields

    def set_client_fields(self):

        # Enable the search btn and change the text back
        self.search_btn.setEnabled(True)
        self.search_btn.setText("Search")

        # Call the parents set client fields method
        self.parent.set_client_info_fields()

    # Search bar text changed
    def search_text_changed(self):

        # Disable the search button if the search field is empty
        if (not self.search_bar.text()):
            self.search_btn.setEnabled(False)
        else:
            self.search_btn.setEnabled(True)

    # Get id 
    def get_id(self):
        return self.search_bar.text()