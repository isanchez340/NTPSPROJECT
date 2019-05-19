# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HookCollectionOverlay.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(576, 431)
        self.formLayout_2 = QtGui.QFormLayout(Form)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.mLineEdit = QgsFilterLineEdit(Form)
        self.mLineEdit.setProperty("qgisRelation", _fromUtf8(""))
        self.mLineEdit.setObjectName(_fromUtf8("mLineEdit"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.mLineEdit)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.mLineEdit_2 = QgsFilterLineEdit(Form)
        self.mLineEdit_2.setProperty("qgisRelation", _fromUtf8(""))
        self.mLineEdit_2.setObjectName(_fromUtf8("mLineEdit_2"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.mLineEdit_2)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.comboBox)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.mLineEdit_3 = QgsFilterLineEdit(Form)
        self.mLineEdit_3.setProperty("qgisRelation", _fromUtf8(""))
        self.mLineEdit_3.setObjectName(_fromUtf8("mLineEdit_3"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.mLineEdit_3)
        self.mFieldComboBox_4 = QgsFieldComboBox(Form)
        self.mFieldComboBox_4.setObjectName(_fromUtf8("mFieldComboBox_4"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.mFieldComboBox_4)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.checkBox_4 = QtGui.QCheckBox(Form)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.gridLayout.addWidget(self.checkBox_4, 6, 0, 1, 1)
        self.mLineEdit_7 = QgsFilterLineEdit(Form)
        self.mLineEdit_7.setProperty("qgisRelation", _fromUtf8(""))
        self.mLineEdit_7.setObjectName(_fromUtf8("mLineEdit_7"))
        self.gridLayout.addWidget(self.mLineEdit_7, 6, 1, 1, 1)
        self.checkBox = QtGui.QCheckBox(Form)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout.addWidget(self.checkBox, 2, 0, 1, 1)
        self.mFieldComboBox_2 = QgsFieldComboBox(Form)
        self.mFieldComboBox_2.setObjectName(_fromUtf8("mFieldComboBox_2"))
        self.gridLayout.addWidget(self.mFieldComboBox_2, 2, 4, 1, 1)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.checkBox_3 = QtGui.QCheckBox(Form)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.gridLayout.addWidget(self.checkBox_3, 3, 0, 1, 1)
        self.mFieldComboBox_5 = QgsFieldComboBox(Form)
        self.mFieldComboBox_5.setObjectName(_fromUtf8("mFieldComboBox_5"))
        self.gridLayout.addWidget(self.mFieldComboBox_5, 3, 4, 1, 1)
        self.mFieldComboBox_3 = QgsFieldComboBox(Form)
        self.mFieldComboBox_3.setObjectName(_fromUtf8("mFieldComboBox_3"))
        self.gridLayout.addWidget(self.mFieldComboBox_3, 4, 4, 1, 1)
        self.mFieldComboBox = QgsFieldComboBox(Form)
        self.mFieldComboBox.setObjectName(_fromUtf8("mFieldComboBox"))
        self.gridLayout.addWidget(self.mFieldComboBox, 6, 4, 1, 1)
        self.mLineEdit_4 = QgsFilterLineEdit(Form)
        self.mLineEdit_4.setProperty("qgisRelation", _fromUtf8(""))
        self.mLineEdit_4.setObjectName(_fromUtf8("mLineEdit_4"))
        self.gridLayout.addWidget(self.mLineEdit_4, 2, 1, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(Form)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout.addWidget(self.checkBox_2, 4, 0, 1, 1)
        self.mLineEdit_5 = QgsFilterLineEdit(Form)
        self.mLineEdit_5.setProperty("qgisRelation", _fromUtf8(""))
        self.mLineEdit_5.setObjectName(_fromUtf8("mLineEdit_5"))
        self.gridLayout.addWidget(self.mLineEdit_5, 3, 1, 1, 1)
        self.mLineEdit_6 = QgsFilterLineEdit(Form)
        self.mLineEdit_6.setProperty("qgisRelation", _fromUtf8(""))
        self.mLineEdit_6.setObjectName(_fromUtf8("mLineEdit_6"))
        self.gridLayout.addWidget(self.mLineEdit_6, 4, 1, 1, 1)
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 4, 1, 1)
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 0, 1, 1, 1)
        self.formLayout_2.setLayout(6, QtGui.QFormLayout.SpanningRole, self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.formLayout_2.setLayout(7, QtGui.QFormLayout.LabelRole, self.horizontalLayout)
        self.scrollArea = QtGui.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 421, 85))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.pushButton_2 = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 0, 94, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton.setGeometry(QtCore.QRect(300, 0, 91, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.FieldRole, self.scrollArea)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_2.setText(_translate("Form", "Hook Collection Name", None))
        self.label.setText(_translate("Form", "Desctiption", None))
        self.label_4.setText(_translate("Form", "Status", None))
        self.label_3.setText(_translate("Form", "Execution Sequence", None))
        self.checkBox_4.setText(_translate("Form", "Hook 4", None))
        self.checkBox.setText(_translate("Form", "Hook 1", None))
        self.label_5.setText(_translate("Form", "Hook", None))
        self.checkBox_3.setText(_translate("Form", "Hook 2", None))
        self.checkBox_2.setText(_translate("Form", "Hook 3", None))
        self.label_6.setText(_translate("Form", "Status", None))
        self.label_7.setText(_translate("Form", "Hook Execution Sequence", None))
        self.pushButton_2.setText(_translate("Form", "Save", None))
        self.pushButton.setText(_translate("Form", "Cancel", None))

from qgsfieldcombobox import QgsFieldComboBox
from qgsfilterlineedit import QgsFilterLineEdit
