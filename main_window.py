from PyQt5 import QtCore, QtGui, QtWidgets
from ui.main_window import Ui_MainWindow
from ui.child import Ui_Form
import re
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options

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
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-gpu')
        self.brouwser = webdriver.Chrome(chrome_options=chrome_options)

        self.window.show()
    def pre_connetions(self):
        try:
            self.ui.btn_restart.clicked.disconnect()
            self.ui.btn_auto.clicked.disconnect()
            self.ui.btn_edit.clicked.disconnect()
            self.ui.btn_web.clicked.disconnect()
        except:
            pass


        self.ui.btn_restart.clicked.connect(self.child_window)
        self.ui.btn_auto.clicked.connect(self.child_window)
        self.ui.btn_edit.clicked.connect(self.child_window)
        self.ui.btn_web.clicked.connect(self.child_window)
    def child_connection(self):
        self.child_ui.btn_save.clicked.connect(self.save_)
        self.child_ui.btn_cancel.clicked.connect(self.cancel_)
    def connections(self):
        self.ui.btn_restart.clicked.disconnect()
        self.ui.btn_restart.clicked.connect(self.test)
    def test(self):
        self.ui.label.setText('192.168.1.1')

    def child_window(self):


        self.child  =QtWidgets.QWidget()
        self.child_ui = Ui_Form()
        self.child_ui.setupUi(self.child)
        self.child_connection()
        self.ui.centralwidget.setEnabled(False)
        self.child.setFixedSize(253, 213)
        self.child.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.child.show()

    def save_(self):
        self.ip = self.child_ui.edt_ip.text()
        self.username = self.child_ui.edt_usename.text()
        self.password = self.child_ui.edt_password.text()
        if self.ip and self.username and self.password:
            if self.is_valid_ip():
                self.connections()
                self.child.hide()
                self.ui.label.setText(self.ip)
                self.ui.centralwidget.setEnabled(True)
                try:
                    self.brouwser.get('http://{}/'.format(self.ip))
                    self.ui.label.setStyleSheet('color :green;')
                    if self.brouwser.last_request.response.status_code ==200 or self.brouwser.last_request.response.status_code ==401:
                        self.ui.label.setStyleSheet('color :green;')
                    else:
                        self.ui.label.setStyleSheet('color :red;')
                except:
                    self.ui.label.setStyleSheet('color :red;')



            else:
                pass #invalid ip address
        else:
            pass #filds are empty
    def cancel_(self):
        self.child.hide()
        self.ui.centralwidget.setEnabled(True)

    def is_valid_ip(self):



        regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''

        # pass the regular expression
        # and the string in search() method
        if (re.search(regex, self.ip)):
            return True

        else:
            return False

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    # main_window.window.show()
    sys.exit(app.exec_())
