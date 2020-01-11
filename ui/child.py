# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\child.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(251, 228)
        self.formLayout_2 = QtWidgets.QFormLayout(Form)
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.formLayout)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label)
        self.edt_ip = QtWidgets.QLineEdit(Form)
        self.edt_ip.setObjectName("edt_ip")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.edt_ip)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.edt_usename = QtWidgets.QLineEdit(Form)
        self.edt_usename.setObjectName("edt_usename")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.edt_usename)
        self.edt_password = QtWidgets.QLineEdit(Form)
        self.edt_password.setObjectName("edt_password")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.edt_password)
        self.btn_save = QtWidgets.QPushButton(Form)
        self.btn_save.setObjectName("btn_save")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.btn_save)
        self.btn_cancel = QtWidgets.QPushButton(Form)
        self.btn_cancel.setObjectName("btn_cancel")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.btn_cancel)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "IP"))
        self.label_2.setText(_translate("Form", "Username"))
        self.label_3.setText(_translate("Form", "Password"))
        self.btn_save.setText(_translate("Form", "Save"))
        self.btn_cancel.setText(_translate("Form", "Cancel"))
