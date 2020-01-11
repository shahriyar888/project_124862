# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(253, 213)
        MainWindow.setMaximumSize(QtCore.QSize(253, 215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(9999, 99999))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.btn_restart = QtWidgets.QPushButton(self.centralwidget)
        self.btn_restart.setEnabled(True)
        self.btn_restart.setObjectName("btn_restart")
        self.gridLayout.addWidget(self.btn_restart, 4, 1, 1, 1)
        self.btn_web = QtWidgets.QPushButton(self.centralwidget)
        self.btn_web.setEnabled(True)
        self.btn_web.setObjectName("btn_web")
        self.gridLayout.addWidget(self.btn_web, 4, 2, 1, 1)
        self.btn_edit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_edit.setEnabled(True)
        self.btn_edit.setObjectName("btn_edit")
        self.gridLayout.addWidget(self.btn_edit, 1, 2, 1, 1)
        self.lbl_profile = QtWidgets.QLabel(self.centralwidget)
        self.lbl_profile.setEnabled(True)
        self.lbl_profile.setObjectName("lbl_profile")
        self.gridLayout.addWidget(self.lbl_profile, 1, 0, 1, 2)
        self.btn_auto = QtWidgets.QPushButton(self.centralwidget)
        self.btn_auto.setEnabled(True)
        self.btn_auto.setObjectName("btn_auto")
        self.gridLayout.addWidget(self.btn_auto, 2, 2, 1, 1)
        self.edt_time = QtWidgets.QLineEdit(self.centralwidget)
        self.edt_time.setEnabled(True)
        self.edt_time.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.edt_time.setObjectName("edt_time")
        self.gridLayout.addWidget(self.edt_time, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 253, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "0.0.0.0"))
        self.btn_restart.setText(_translate("MainWindow", "Restart"))
        self.btn_web.setText(_translate("MainWindow", "Web View"))
        self.btn_edit.setText(_translate("MainWindow", "Edit profile"))
        self.lbl_profile.setText(_translate("MainWindow", "TextLabel"))
        self.btn_auto.setText(_translate("MainWindow", "Auto"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
