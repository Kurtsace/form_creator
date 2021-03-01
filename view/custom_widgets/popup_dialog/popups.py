from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox

#Pop ups dialogs to show when thigns go wrong or to warn users 

#Warning message pop up 
def warning_popup(window_title="Warning Title", text="Warning text"):

    #Intantiate a message box 
    msg = QMessageBox()

    #Set window icon 
    #msg.setWindowIcon()

    #Set the window title 
    msg.setWindowTitle(window_title)

    #Set the text content to show 
    msg.setText(text)

    #Set the icon to warning 
    msg.setIcon(QMessageBox.Warning)

    #Set the standard buttons to show 
    msg.setStandardButtons(QMessageBox.Ok)

    #Show the dialog 
    msg.exec_()
    msg.show()


#Critical error message pop up 
def error_popup(window_title="Error Title", text="Error text", detailed_text="Error details"):

        #Intantiate a message box 
    msg = QMessageBox()

    #Set window icon 
    #msg.setWindowIcon()

    #Set the window title 
    msg.setWindowTitle(window_title)

    #Set the text content to show 
    msg.setText(text)

    #Set the detailed text
    msg.setDetailedText(detailed_text)

    #Set the icon to warning 
    msg.setIcon(QMessageBox.Critical)

    #Set the standard buttons to show 
    msg.setStandardButtons(QMessageBox.Ok)
    
    #Show the dialog 
    msg.exec_()
    msg.show()