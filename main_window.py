from PyQt5 import QtCore, QtGui, QtWidgets
from ui.main_window import Ui_MainWindow
from ui.child import Ui_Form

import sys


class MainWindow(object):
    ip = None
    username =None
    password = None
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.window = QtWidgets.QMainWindow()
        self.ui.setupUi(self.window)
        self.pre_connetions()
        self.window.show()
    def pre_connetions(self):
        self.ui.btn_restart.clicked.connect(self.child_window)
        self.ui.btn_auto.clicked.connect(self.child_window)
        self.ui.btn_edit.clicked.connect(self.child_window)
        self.ui.btn_web.clicked.connect(self.child_window)
    def test(self):
        self.ui.label.setText('192.168.1.1')

    def child_window(self):

        self.child  =QtWidgets.QWidget()
        self.child_ui = Ui_Form()
        self.child_ui.setupUi(self.child)
        self.ui.centralwidget.setEnabled(False)
        self.child.setFixedSize(253, 213)
        self.child.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.child.show()

    def save_(self):
        self.ip = self.child_ui.edt_ip.text()
        self.username = self.child_ui.edt_usename.text()
        self.password = self.child_ui.edt_password.text()
        if self.ip and self.username and self.password:
            self.connections()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    # main_window.window.show()
    sys.exit(app.exec_())
