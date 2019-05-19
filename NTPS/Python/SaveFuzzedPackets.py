# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SaveFuzzedPackets.ui'
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

class Ui_SaveFuzzedPackets(object):
    def setupUi(self, SaveFuzzedPackets):
        SaveFuzzedPackets.setObjectName(_fromUtf8("SaveFuzzedPackets"))
        SaveFuzzedPackets.resize(333, 115)
        self.gridLayout = QtGui.QGridLayout(SaveFuzzedPackets)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.FuzzedPCAPNamelabel = QtGui.QLabel(SaveFuzzedPackets)
        self.FuzzedPCAPNamelabel.setObjectName(_fromUtf8("FuzzedPCAPNamelabel"))
        self.gridLayout.addWidget(self.FuzzedPCAPNamelabel, 0, 0, 1, 1)
        self.NameLineEdit = QtGui.QLineEdit(SaveFuzzedPackets)
        self.NameLineEdit.setObjectName(_fromUtf8("NameLineEdit"))
        self.gridLayout.addWidget(self.NameLineEdit, 0, 1, 1, 2)
        self.DescriptionLabel = QtGui.QLabel(SaveFuzzedPackets)
        self.DescriptionLabel.setObjectName(_fromUtf8("DescriptionLabel"))
        self.gridLayout.addWidget(self.DescriptionLabel, 1, 0, 1, 1)
        self.DescriptionLineEdit = QtGui.QLineEdit(SaveFuzzedPackets)
        self.DescriptionLineEdit.setObjectName(_fromUtf8("DescriptionLineEdit"))
        self.gridLayout.addWidget(self.DescriptionLineEdit, 1, 1, 1, 2)
        self.SavePushButton = QtGui.QPushButton(SaveFuzzedPackets)
        self.SavePushButton.setObjectName(_fromUtf8("SavePushButton"))
        self.gridLayout.addWidget(self.SavePushButton, 2, 1, 1, 1)
        self.CancelePushButton = QtGui.QPushButton(SaveFuzzedPackets)
        self.CancelePushButton.setObjectName(_fromUtf8("CancelePushButton"))
        self.gridLayout.addWidget(self.CancelePushButton, 2, 2, 1, 1)

        self.retranslateUi(SaveFuzzedPackets)
        QtCore.QMetaObject.connectSlotsByName(SaveFuzzedPackets)

    def retranslateUi(self, SaveFuzzedPackets):
        SaveFuzzedPackets.setWindowTitle(_translate("SaveFuzzedPackets", "Save Fuzzed Packets", None))
        self.FuzzedPCAPNamelabel.setText(_translate("SaveFuzzedPackets", "Fuzzed PCAP Name", None))
        self.DescriptionLabel.setText(_translate("SaveFuzzedPackets", "Description", None))
        self.SavePushButton.setText(_translate("SaveFuzzedPackets", "Save", None))
        self.CancelePushButton.setText(_translate("SaveFuzzedPackets", "Cancel", None))

