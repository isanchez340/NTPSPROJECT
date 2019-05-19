# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Notification.ui'
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

class Ui_NotificationOverlay(object):
    def setupUi(self, NotificationOverlay):
        NotificationOverlay.setObjectName(_fromUtf8("NotificationOverlay"))
        NotificationOverlay.resize(923, 289)
        self.gridLayout = QtGui.QGridLayout(NotificationOverlay)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(NotificationOverlay)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(NotificationOverlay)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        self.label_2 = QtGui.QLabel(NotificationOverlay)
        self.label_2.setMinimumSize(QtCore.QSize(0, 141))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(NotificationOverlay)
        self.pushButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 4, 2, 1, 1)

        self.retranslateUi(NotificationOverlay)
        QtCore.QMetaObject.connectSlotsByName(NotificationOverlay)

    def retranslateUi(self, NotificationOverlay):
        NotificationOverlay.setWindowTitle(_translate("NotificationOverlay", "Notification", None))
        self.label_3.setText(_translate("NotificationOverlay", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">The system has restored to the previous proxy settings</span></p></body></html>", None))
        self.label_4.setText(_translate("NotificationOverlay", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">and it will stop appending packet information to the live traffic PCAP file</span></p></body></html>", None))
        self.label_2.setText(_translate("NotificationOverlay", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Proxy behavior has been disabled.</span></p></body></html>", None))
        self.pushButton.setText(_translate("NotificationOverlay", "OK", None))

