# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SubmitFeedback.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

#Form Creator 
#Created by: Kurt Palo 
#For: HCC (MHRC)


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMessageBox
from fpdf import FPDF
import logging, os
import datetime

class Ui_feedbackDialog(object):
    def setupUi(self, feedbackDialog):
        self.feedbackDialog = feedbackDialog
        feedbackDialog.setObjectName("feedbackDialog")
        feedbackDialog.resize(400, 300)
        feedbackDialog.setMinimumSize(QtCore.QSize(400, 300))
        feedbackDialog.setMaximumSize(QtCore.QSize(400, 300))
        feedbackDialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget = QtWidgets.QWidget(feedbackDialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 381, 281))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBox = QtWidgets.QTextEdit(self.widget)
        self.textBox.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.textBox.setObjectName("textBox")
        self.verticalLayout.addWidget(self.textBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.submitForm = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.submitForm.setFont(font)
        self.submitForm.setMinimumSize(QtCore.QSize(0, 25))
        self.submitForm.setStyleSheet("QPushButton:pressed { \n"
        "    border-radius: 4px; \n"
        "    background-color: rgb(66, 133, 200);\n"
        "}\n"
        "\n"
        "QPushButton {\n"
        "    border: none;\n"
        "    border-radius: 4px;\n"
        "    background-color: rgb(85, 170, 255);\n"
        "    font: 75 10pt \"Arial\"; \n"
        "    color: rgb(255, 255, 255);    \n"
        "    font-weight: bold;\n"
        "}")
        self.submitForm.setObjectName("submitForm")
        self.horizontalLayout.addWidget(self.submitForm)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(feedbackDialog)
        QtCore.QMetaObject.connectSlotsByName(feedbackDialog)

        #Set window icon
        feedbackDialog.setWindowIcon(QIcon(":/Images/icon.png"))

        self.submitForm.clicked.connect(self.submit)

    def retranslateUi(self, feedbackDialog):
        _translate = QtCore.QCoreApplication.translate
        feedbackDialog.setWindowTitle(_translate("feedbackDialog", "Submit Feedback"))
        self.submitForm.setText(_translate("feedbackDialog", "Submit"))

    def submit(self):

        #Make sure feedback is non empty before submitting
        if self.textBox.toPlainText() == "":

            #Show message box to inform user 
            #Create a QMessageBox
            msg = QMessageBox()

            #Set the icon warning type 
            msg.setIcon(QMessageBox.Warning)

            #Set window icon
            msg.setWindowIcon(QIcon(":/Images/icon.png"))

            #Set text and title
            msg.setText("Feedback is empty!")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok)

            #Show the message
            msg.exec()
        else: 

            #Create the feedback pdf
            filename = "W:/houhcc/Form Creator Resources/Feedback/{}-Feedback-{}".format(os.getlogin(), datetime.datetime.now().strftime("%d%m%Y-%H%M"))
            self.createForm(filename)

            #Show message box to confirm
            #Create a QMessageBox
            msg = QMessageBox()

            #Set the icon warning type 
            msg.setIcon(QMessageBox.Information)

            #Set window icon
            msg.setWindowIcon(QIcon("W:/houhcc/Form Creator Resources/Icons/icon.png"))

            #Set text and title
            msg.setText("Thanks for your feedback!")
            msg.setWindowTitle("Success")
            msg.setStandardButtons(QMessageBox.Ok)

            #Show the message
            msg.exec()

            #Close the dialog 
            self.feedbackDialog.close()
        
    def createForm(self, filename):
            
            #Write the feedback to pdf file
            feedback = self.textBox.toPlainText()

            #Instantiate a PDF object
            pdf = FPDF()
            
            #Add a page 
            pdf.add_page()

            #Set the font 
            pdf.set_font("Arial", size = 12)

            #Feedback
            pdf.cell(200, 10, txt="Feedback by {}:".format(os.getlogin()), ln = 1, align='L')
            pdf.multi_cell(200, 10, txt=feedback)

            #Output the pdf
            pdf.output('{}.pdf'.format(filename), 'F')
