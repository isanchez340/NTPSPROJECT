# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QueueErrorMessage.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_QueueErrorMessage(object):
    def setupUi(self, QueueErrorMessage):
        QueueErrorMessage.setObjectName(_fromUtf8("QueueErrorMessage"))
        QueueErrorMessage.resize(393, 144)
        self.gridLayout = QtGui.QGridLayout(QueueErrorMessage)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.QueueErrorMessageText = QtGui.QTextBrowser(QueueErrorMessage)
        self.QueueErrorMessageText.setObjectName(_fromUtf8("QueueErrorMessageText"))
        self.gridLayout.addWidget(self.QueueErrorMessageText, 0, 0, 1, 1)
        self.Okbutton = QtGui.QPushButton(QueueErrorMessage)
        self.Okbutton.setObjectName(_fromUtf8("Okbutton"))
        self.gridLayout.addWidget(self.Okbutton, 1, 1, 1, 1)

        self.retranslateUi(QueueErrorMessage)
        QtCore.QMetaObject.connectSlotsByName(QueueErrorMessage)

    def retranslateUi(self, QueueErrorMessage):
        QueueErrorMessage.setWindowTitle(_translate("QueueErrorMessage", "Queue Error Message", None))
        self.QueueErrorMessageText.setHtml(_translate("QueueErrorMessage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">The queue has reached its capacity. No new packets will be</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\"> excepted until there is space available.</span></p></body></html>", None))
        self.Okbutton.setText(_translate("QueueErrorMessage", "Ok", None))

