#Form Creator 
#Created by: Kurt Palo 
#For: HCC (MHRC)

#Import selenium
from selenium import webdriver

#Import PYQT5 modules
import PyQt5
from PyQt5 import QtWidgets, Qt, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMessageBox

#Import modules
import threading
import os 
import logging
import sys
import enum
import json
import resource

#Import classes 
from PDF import PDF
from Client import Client
from Ui import Ui

#Enumeration
class Tab(enum.Enum):
    SA = 1
    FV = 2
    SR = 3

#Emmiter for signals --QMessageBox cannot run in a thread, so this is an alternative 
#Messy but it works for now 
class ErrorShow(QObject):
    showError = pyqtSignal()

    def __init__(self):
        QObject.__init__(self)

    #Show error method 
    def popUpError(self):
        self.showError.emit()

#Salvation Army related functions 
#Get request log item for SA tab
def getRequestLogSA():

    #Ensure input is valid
    id = window.searchLine.text()

    if any(c.isalpha() for c in id) or id == "":
        #Show error pop up
        popUp(QMessageBox.Warning, "Requested ID cannot be empty and must be in number format only!", "Error")
        logging.info("Invalid format for ID")

        return

    else: 
        #Start a thread to run the scraper --prevents crashing the main window
        try: 
            #Initialize the thread 
            logging.info("Starting thread for scrapeClientInfo()")
            x = threading.Thread(target=scrapeClientInfo, args=(id, Tab.SA))

            #Begin the thread
            x.start()
            logging.info("Thread successfuly initialized for scrapeClientInfo")

        except:
            popUp(QMessageBox.Critical, "Thread has failed to start! Contact support", "Critical")
            logging.error("scrapeClientInfo thread has failed to start. Dumping stack trace:", exc_info=True)

#Set the output fields to client text for SA tab
def setFieldsSA(client):

    logging.info("Setting client fields for the Ui | Tab: Salvation Army")
    #Set case number line 
    window.caseNumLine.setText(client.caseNum)

    #Set name line 
    window.nameLine.setText(client.fullName)

    #Set dob line 
    window.dobLine.setText(client.dob)

#Create an auth form and export it with client info --Will export onto the dekstop under Auth Forms
def createAuthForm():

    #Make sure client is instantiated
    global client
    if not client == None:

        logging.info("Creating auth form")

        #Make sure all fields are popluated before making a form
        if not client.fullName == "" and ( window.maleRadioBtn.isChecked() or window.femaleRadioBtn.isChecked() ) and not window.nightSpinBox.value() == 0:
            
            #Get gender selected and assign it to the client
            if window.maleRadioBtn.isChecked():
                client.gender = window.maleRadioBtn.text()
            else: 
                client.gender = window.femaleRadioBtn.text()

            #Get the nights staying 
            nights = window.nightSpinBox.value()

            #Instantiate the PDF 
            pdf = PDF(client)

            #Create and export the PDF to the same directory as the executable 
            pdf.createAuthForm(nights)

            #Cleanse all input fields 
            clearFields()

            #Show message saying PDF has been made 
            popUp(QMessageBox.Information, "Form has been successfully created!", "Success")

            #Set client to none 
            client = None
            
        else: 
            popUp(QMessageBox.Warning, "Ensure all fields are popluated!", "Error")
            logging.warning("Some fields empty. No form created")

    else: 
        popUp(QMessageBox.Warning, "Fields are empty. Search for a Log first!", "Error")
        logging.warning("No ID inputted for search. No form created")



#Food Voucher related functions
#Get request log for item for FV tab
def getRequestLogFV():
    #Ensure input is valid
    id = window.searchLine_2.text()

    if any(c.isalpha() for c in id) or id == "":
        #Show error pop up
        popUp(QMessageBox.Warning, "Requested ID cannot be empty and must be in number format only!", "Error")
        logging.info("Invalid format for ID")

        return

    else: 
        #Start a thread to run the scraper --prevents crashing the main window
        try: 
            #Initialize the thread 
            logging.info("Starting thread for scrapeClientInfo()")
            global x
            x = threading.Thread(target=scrapeClientInfo, args=(id, Tab.FV))

            #Begin the thread
            x.start()
            logging.info("Thread successfuly initialized for scrapeClientInfo")

        except:
            popUp(QMessageBox.Critical, "Thread has failed to start! Contact support", "Critical")
            logging.error("scrapeClientInfo thread has failed to start. Dumping stack trace:", exc_info=True)

#Create a food voucher and export it --Will export onto desktop under Food Vouchers
def createFoodVoucher():

    #Make sure client is instantiated
    global client
    if not client == None:

        logging.info("Creating food voucher")

        #Make sure all fields are popluated before making a form
        if not client.fullName == "" and ( window.foodCheckBox.isChecked() or window.diapersCheckBox.isChecked() or window.fuelCheckBox.isChecked()) and not window.safewayComboBox.currentIndex() == -1:
            
            #Variables
            food = window.foodCheckBox.isChecked()
            diapers = window.diapersCheckBox.isChecked()
            fuel = window.fuelCheckBox.isChecked()
            location = window.safewayComboBox.currentText()
            fax = safewayList[location]
            id = window.searchLine_2.text()

            #Calculate amount
            amount = calculateAmount()

            #Instantiate the PDF 
            pdf = PDF(client)

            #Create and export the PDF to the same directory as the executable 
            pdf.createFoodVoucher(amount, food, diapers, fuel, location, fax, id )

            #Cleanse all input fields 
            clearFields()

            #Show message saying PDF has been made 
            popUp(QMessageBox.Information, "Form has been successfully created!", "Success")

            #Set client to none 
            client = None
            
        else: 
            popUp(QMessageBox.Warning, "Ensure all fields are popluated!", "Error")
            logging.warning("Some fields empty. No form created")

    else: 
        popUp(QMessageBox.Warning, "Fields are empty. Search for a Log first!", "Error")
        logging.warning("No ID inputted for search. No form created")

#Calculate amount approved
def calculateAmount():

    #Variables 
    days = window.daysSpinBox.value()
    adults = window.adultsSpinBox.value()
    children = window.childrenSpinBox.value()
    food = window.foodCheckBox.isChecked()
    fuel = window.fuelCheckBox.isChecked()
    diapers = window.diapersCheckBox.isChecked()

    global diapersApplied

    #Approved amount 
    amount = 0

    #Calculate for food only if it has been selected
    if food:
        #Calculate amount of only 1 adult selected
        if adults == 1:
            amount += days * (adults * 6.41) + (children * 3.85)
        else:
            amount += days * 11.34 + (children * 3.85)
    
    if diapers: 
        amount += 15

    #Set amount shown on GUI
    window.approvedAmountLabel.setText( "${:.2f}".format(round(amount, 2)) )

    return amount

#Set the output fields to client text for SR tab
def setFieldsFV(client):
    
    logging.info("Setting client fields for the Ui | Tab: SonRise")
    
    #Set name line 
    window.nameLineFV.setText(client.fullName)

    #Set dob line 
    window.dobLineFV.setText(client.dob)

    #Set address line 
    window.addressLineFV.setText(client.address)

    #Set current amount
    calculateAmount()



#Son Rise related functions 
#Get request log item for SR tab 
def getRequestLogSR():
    #Ensure input is valid
    id = window.searchLineSR.text()

    if any(c.isalpha() for c in id) or id == "":
        #Show error pop up
        popUp(QMessageBox.Warning, "Requested ID cannot be empty and must be in number format only!", "Error")
        logging.info("Invalid format for ID")

        return

    else: 
        #Start a thread to run the scraper --prevents crashing the main window
        try: 
            #Initialize the thread 
            logging.info("Starting thread for scrapeClientInfo()")
            x = threading.Thread(target=scrapeClientInfo, args=(id, Tab.SR))

            #Begin the thread
            x.start()
            logging.info("Thread successfuly initialized for scrapeClientInfo")

        except:
            popUp(QMessageBox.Critical, "Thread has failed to start! Contact support", "Critical")
            logging.error("scrapeClientInfo thread has failed to start. Dumping stack trace:", exc_info=True)

#Set the output fields to client text for SR tab
def setFieldsSR(client):

    logging.info("Setting client fields for the Ui | Tab: Salvation Army")

    #Set case number line 
    window.caseNumLineSR.setText(client.caseNum)

    #Set name line 
    window.nameLineSR.setText(client.fullName)

    #Set dob line 
    window.dobLineSR.setText(client.dob)

#Create an auth form and export it with client info --Will export onto the dekstop under Auth Forms
def createAuthFormSR():

    #Make sure client is instantiated
    global client
    if not client == None:

        logging.info("Creating auth form")

        #Make sure all fields are popluated before making a form
        if not client.fullName == "" and ( window.maleRadioBtnSR.isChecked() or window.femaleRadioBtnSR.isChecked() ) and not ( window.nightSpinBoxSR.value() == 0):
            
            #Get gender selected and assign it to the client
            if window.maleRadioBtnSR.isChecked():
                client.gender = window.maleRadioBtnSR.text()
            else: 
                client.gender = window.femaleRadioBtnSR.text()

            #Get the nights staying 
            nights = window.nightSpinBoxSR.value()

            #Is there a spouse
            spouse = window.spouseRBYes.isChecked()

            #How many children
            children = window.childSRSpinBox.value()

            #Instantiate the PDF 
            pdf = PDF(client)

            #Create and export the PDF to the same directory as the executable 
            pdf.createAuthFormSR(spouse, children, nights)

            #Cleanse all input fields 
            clearFields()

            #Show message saying PDF has been made 
            popUp(QMessageBox.Information, "Form has been successfully created!", "Success")

            #Set client to none 
            client = None
            
        else: 
            popUp(QMessageBox.Warning, "Ensure all fields are popluated!", "Error")
            logging.warning("Some fields empty. No form created")

    else: 
        popUp(QMessageBox.Warning, "Fields are empty. Search for a Log first!", "Error")
        logging.warning("No ID inputted for search. No form created")



#Scraper functions
#Scrape client info for the specified tab
def scrapeClientInfo(id, tab):

    global client

    #Set Salvation Army tab elements 
    if tab == Tab.SA:
        #Temporarily disable search button, create button and search box
        window.searchButtonSA.setEnabled(False)
        window.searchButtonSA.setText("Searching")
        window.searchLine.setReadOnly(True)
        window.createFormBtn.setEnabled(False)

        #Get the client info from the parsed and scraped data
        client = getClientInfo(id)

        #Set the fields to show client info if not None
        if not client == None:
            setFieldsSA(client)

        #Enable the disabled buttons again
        window.searchButtonSA.setText("Search")
        window.searchButtonSA.setEnabled(True)
        window.searchLine.setReadOnly(False)
        window.createFormBtn.setEnabled(True)
    
    #Set Food voucher tab elements 
    elif tab == Tab.FV:
        #Temporarily disable search button, create button and search box
        window.searchButtonFV.setEnabled(False)
        window.searchButtonFV.setText("Searching")
        window.searchLine_2.setReadOnly(True)
        window.createFormBtn_2.setEnabled(False)

        #Get the client info from the parsed and scraped data and assign
        client = getClientInfo(id)

        #Set the fields to show client info if not None
        if not client == None:
            setFieldsFV(client)

        #Enable the disabled buttons again
        window.searchButtonFV.setText("Search")
        window.searchButtonFV.setEnabled(True)
        window.searchLine_2.setReadOnly(False)
        window.createFormBtn_2.setEnabled(True)

    elif tab == Tab.SR:
        #Temporarily disable search button, create button and search box
        window.searchButtonSR.setEnabled(False)
        window.searchButtonSR.setText("Searching")
        window.searchLineSR.setReadOnly(True)
        window.createFormBtn_3.setEnabled(False)

        #Get the client info from the parsed and scraped data
        client = getClientInfo(id)

        #Set the fields to show client info if not None
        if not client == None:
            setFieldsSR(client)

        #Enable the disabled buttons again
        window.searchButtonSR.setText("Search")
        window.searchButtonSR.setEnabled(True)
        window.searchLineSR.setReadOnly(False)
        window.createFormBtn_3.setEnabled(True)

#Get a list containing all of the scraped client info from the ID
def getClientInfo(id):

    #Target url to be opened 
    url = "http://collaboration.mbgov.ca/sites/MHCD/Security_Info/HCC/EIA/Lists/Request%20Log%2010/DispForm.aspx?ID={}".format(id)

    #Path of the web driver  
    driverPath = "W:/houhcc/Form Creator Resources/Webdriver/chromedriver.exe"

    #Make sure we are able to find the driver and load it 
    if not os.path.exists(driverPath):
        logging.info("Chromedriver not found!")
        popUp(QMessageBox.Critical, "Chromedriver not found. Contact support", "Critical")
        return

    logging.info("Loading chromedriver and setting capabilities")

    #Start a chrome driver path --disable extensions to prevent privilege escalation errors
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_experimental_option('useAutomationExtension', False)
    chromeOptions.headless = True

    try:
        driver = webdriver.Chrome(executable_path = driverPath, options = chromeOptions, desired_capabilities = chromeOptions.to_capabilities())
    except: 
        logging.critical("Error while loading chromedriver. Dumping stack trace:", exc_info=True)
        popUp(QMessageBox.Critical, "Critical error while loading chromedriver. Make sure you have at least version 80 of chrome installed. Contact support", "Critical")
        return None
    
    logging.info("Successfuly loaded webdriver and set capabilities")

    #Hide the window 
    driver.set_window_position(-1000, -1000)

    #Navigate to the ID page --No auth header needed 
    driver.get(url)

    #Scrape the data needed by xpath --SPFieldText items within the table only
    logging.info("Scraping data for ID: {}".format(id))
    clientInfo = driver.find_elements_by_xpath("//*[@id='SPFieldText']")

    #Get the text for each element
    clientInfo = [c.text for c in clientInfo]
    
    #Close the connection to the driver
    driver.quit()
    
    #Make sure the ID requested exists and/or has valid details 
    if len(clientInfo) == 0:
        client = None 

        #Emit the signal
        error.popUpError()
        logging.warning("ID not found")
    
    else:
        #Create a client with the info
        address = clientInfo[4]

        #Check if there is a suite number
        if clientInfo[5] != '':
            address = clientInfo[5] + " - " + address

        client = Client(clientInfo[0], clientInfo[1], clientInfo[2], clientInfo[3], address)
        logging.info("Client found and created: \n{}".format(client.toString()))

    return client



#Misc functions 
#Clear the output fields for both tabs
def clearFields():

    #Clear search bar
    window.searchLine.setText("")
                    
    #Clear case number line 
    window.caseNumLine.setText("")

    #Clear name line 
    window.nameLine.setText("")

    #Clear dob line 
    window.dobLine.setText("")

    #Clear FV search bar
    window.searchLine_2.setText("")

    #Clear client name 
    window.nameLineFV.setText("")

    #Clear DOB
    window.dobLineFV.setText("")

    #Clear address
    window.addressLineFV.setText("")

    #Clear SR search bar 
    window.searchLineSR.setText("")
                    
    #Clear case number line 
    window.caseNumLineSR.setText("")

    #Clear name line 
    window.nameLineSR.setText("")

    #Clear dob line 
    window.dobLineSR.setText("")


    logging.info("Cleared fields")

#Pop up message box for errors 
def popUp(setIcon, text, title):
    
    #Create a QMessageBox
    msg = QMessageBox()

    #Set the icon warning type 
    msg.setIcon(setIcon)

    #Set window icon
    msg.setWindowIcon(QIcon(":/Images/icon.png"))

    #Set text and title
    msg.setText(text)
    msg.setWindowTitle(title)
    msg.setStandardButtons(QMessageBox.Ok)

    #Show the box
    msg.exec_()

#Slot for the emitter
@pyqtSlot()
def showMessageBox():
    popUp(QMessageBox.Warning, "ID not found. Ensure it exists within the request log!", "Error")

#Main 
if __name__ == "__main__": 

    #Variables
    global client
    client = None
    user = os.getlogin()
    global diapersApplied
    diapersApplied = False

    #Logging config
    logPath = "W:/houhcc/Form Creator Resources/Logs/"

    if os.path.exists(logPath):
        logging.basicConfig(filename= "{}/{}.log".format(logPath, user), filemode= 'a', level= logging.INFO, format= '%(asctime)s:%(levelname)s:%(message)s')
    else:
        logPath = "{}/{}.log".format(os.getcwd(), os.getlogin())
        logging.basicConfig(filename= logPath, filemode= 'a', level= logging.INFO, format= '%(asctime)s:%(levelname)s: %(message)s')

    #Set initial log message 
    logging.info('{} has opened the application'.format(user))

    #Create an app instance of the main window, pass in sys args if any
    app = QtWidgets.QApplication(sys.argv)

    #Create an instance of the main window
    logging.info("Instantiating Ui variables...")
    appWindow = Ui()
    window = appWindow.ui

    #Radio Button groups
    spouseGroup = QtWidgets.QButtonGroup()
    spouseGroup.setExclusive(True)
    spouseGroup.addButton(window.spouseRBNo)
    spouseGroup.addButton(window.spouseRBYes)

    malefemaleGroup = QtWidgets.QButtonGroup()
    malefemaleGroup.setExclusive(True)
    malefemaleGroup.addButton(window.femaleRadioBtnSR)
    malefemaleGroup.addButton(window.maleRadioBtnSR)

    #Instantiate error signal
    error = ErrorShow()

    #Connect the signal
    logging.info("Connecting signals...")
    error.showError.connect(showMessageBox)
    logging.info('Error signal connected')

    #Connect functions to the button signals
    #On search salvation army click
    window.searchButtonSA.clicked.connect(getRequestLogSA)
    logging.info("Search button for Salvation Army tab connected")

    #On create salvation army clicked
    window.createFormBtn.clicked.connect(createAuthForm)
    logging.info("Create form button connected")

    #On search food voucher clicked 
    window.searchButtonFV.clicked.connect(getRequestLogFV)
    logging.info("Search button for Food Voucher tab connected")

    #On create food voucher clicked 
    window.createFormBtn_2.clicked.connect(createFoodVoucher)
    logging.info("Create food voucher button connected")

    #On search SR button clicked
    window.searchButtonSR.clicked.connect(getRequestLogSR)

    #On create Son Rise created 
    window.createFormBtn_3.clicked.connect(createAuthFormSR)

    #Connect index changed for Food Voucher spin boxes 
    window.daysSpinBox.valueChanged.connect(calculateAmount)
    window.adultsSpinBox.valueChanged.connect(calculateAmount)
    window.childrenSpinBox.valueChanged.connect(calculateAmount)
    logging.info("Spin Box signals connected")

    #Connect check box state changed signals 
    window.foodCheckBox.stateChanged.connect(calculateAmount)
    window.diapersCheckBox.stateChanged.connect(calculateAmount)
    window.fuelCheckBox.stateChanged.connect(calculateAmount)
    logging.info("Check Box signals connected")

    logging.info("All signals successfuly connected")

    #Read and parse JSON file containing safeway lists
    logging.info("Importing JSON list")
    stream = QtCore.QFile(":/Data/Safeway-List.json")
    stream.open(QtCore.QIODevice.ReadOnly)
    text = QtCore.QTextStream(stream).readAll()
    stream.close()
    
    safewayList = json.loads(text)
    logging.info("JSON list imported")

    #Populate drop down list of safeway location
    logging.info("Popluating Safeway drop down list")
    window.safewayComboBox.addItems(safewayList)
    logging.info("Safeway drop down list populated")


    #Start the application
    app.exec_()
