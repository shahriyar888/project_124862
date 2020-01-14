from PyQt5 import QtCore, QtGui, QtWidgets
from ui.main_window import Ui_MainWindow
from ui.child import Ui_Form
import re
from seleniumwire import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import time

import sys


class MainWindow(object):
    ip = None
    username =None
    password = None
    rtime = None
    on=False
    auto_c = False
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.window = QtWidgets.QMainWindow()
        self.ui.setupUi(self.window)
        self.pre_connetions()
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--disable-gpu')
        self.ui.lbl_profile.setText('')

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.auto_restart_timer)


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
        self.ui.btn_restart.clicked.connect(self.on_off_triger)
        self.ui.btn_auto.clicked.disconnect()
        self.ui.btn_auto.clicked.connect(self.auto_starter)
        self.ui.btn_web.clicked.disconnect()
        self.ui.btn_web.clicked.connect(self.web_view)
    def web_view(self):
        self.brouwser = webdriver.Chrome()
        self.brouwser.get('http://{}/'.format(self.ip))
        username = self.brouwser.find_element_by_id('ID')
        password = self.brouwser.find_element_by_id('PASSWORD')
        login_btn = self.brouwser.find_element_by_id('wan_change_mode')
        username.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        login_btn.click()
    def on_off(self):
        if self.on:
            self.ui.btn_restart.setText('Off')
        else:
            self.ui.btn_restart.setText('on')

    def on_off_triger(self):

        try:
            self.brouwser = webdriver.Chrome(chrome_options=self.chrome_options)
            self.brouwser.get('http://{}/'.format(self.ip))
            username = self.brouwser.find_element_by_id('ID')
            password = self.brouwser.find_element_by_id('PASSWORD')
            login_btn = self.brouwser.find_element_by_id('wan_change_mode')
            username.clear()
            username.send_keys(self.username)
            password.send_keys(self.password)
            login_btn.click()
            wan_link = self.brouwser.find_element_by_id('navi-wan')
            wan_link.click()

            # tabs > ul > li.ui-state-default.ui-corner-top.ui-tabs-selected.ui-state-active > a
            print('ran till here')
            time.sleep(2)
            if self.on :
                self.brouwser.switch_to.frame(self.brouwser.find_element_by_tag_name('iframe'))


                print(self.brouwser.find_elements_by_class_name('btn'))
                select = Select(self.brouwser.find_element_by_id('_flightMode'))
                select.select_by_index(1)
                submit = self.brouwser.find_elements_by_id('wan_change_mode')[0]
                submit.click()
                time.sleep(2)
                self.brouwser.refresh()
                self.on=False
                self.on_off()
            else:
                self.brouwser.switch_to.frame(self.brouwser.find_element_by_tag_name('iframe'))
                select = Select(self.brouwser.find_element_by_id('_flightMode'))
                select.select_by_index(0)
                submit = self.brouwser.find_elements_by_id('wan_change_mode')[0]
                submit.click()
                self.brouwser.close()
                self.on = True
                self.on_off()
            self.brouwser.close()
        except:pass



    def auto_starter(self):
        if not self.auto_c:
            try:
                self.count_down = int(self.ui.edt_time.text())
                if self.count_down>0:
                    self.rtime  = self.count_down
                    self.timer.start(1000)
                    self.ui.btn_auto.setText('Cancel')
                    self.ui.btn_restart.setEnabled(False)
                    self.ui.btn_web.setEnabled(False)
                    self.ui.btn_edit.setEnabled(False)
                    self.ui.edt_time.setEnabled(False)

                    self.auto_c =True

            except:
                pass
        else:
            self.timer.stop()
            self.count_down = None
            self.ui.btn_restart.setEnabled(True)
            self.ui.btn_web.setEnabled(True)
            self.ui.btn_edit.setEnabled(True)
            self.ui.edt_time.setEnabled(True)
            self.ui.btn_auto.setText('Auto')
            self.auto_c = False


    def auto_restart_timer(self):
        if self.rtime<=0:
            self.restart()
            self.rtime = self.count_down

        else:
            self.rtime -=1
            self.ui.lbl_profile.setText(str(self.rtime))

    def restart(self):
        try:
            self.brouwser = webdriver.Chrome(chrome_options=self.chrome_options)
            self.brouwser.get('http://{}/'.format(self.ip))
            username = self.brouwser.find_element_by_id('ID')
            password = self.brouwser.find_element_by_id('PASSWORD')
            login_btn = self.brouwser.find_element_by_id('wan_change_mode')
            username.clear()
            username.send_keys(self.username)
            password.send_keys(self.password)
            login_btn.click()
            wan_link = self.brouwser.find_element_by_id('navi-wan')
            wan_link.click()
           

           
            #tabs > ul > li.ui-state-default.ui-corner-top.ui-tabs-selected.ui-state-active > a
            print('ran till here')
            time.sleep(2)
            self.brouwser.switch_to.frame(self.brouwser.find_element_by_tag_name('iframe'))
            
            print(self.brouwser.find_elements_by_class_name('btn'))
            select = Select(self.brouwser.find_element_by_id('_flightMode'))
            select.select_by_index(1)
            submit = self.brouwser.find_elements_by_id('wan_change_mode')[0]
            submit.click()
            time.sleep(2)
            self.brouwser.refresh()
            time.sleep(2)
            self.brouwser.switch_to.frame(self.brouwser.find_element_by_tag_name('iframe'))
            select = Select(self.brouwser.find_element_by_id('_flightMode'))
            select.select_by_index(0)
            submit = self.brouwser.find_elements_by_id('wan_change_mode')[0]
            submit.click()
            self.brouwser.close()
            self.on=True
            self.on_off()

        except:
            pass






    def child_window(self):


        self.child  =QtWidgets.QWidget()
        self.child_ui = Ui_Form()
        self.child_ui.setupUi(self.child)
        self.child_connection()
        self.ui.centralwidget.setEnabled(False)
        self.child.setFixedSize(253, 213)
        self.child.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        if self.ip and self.username and self.password:
            self.child_ui.edt_ip.setText(self.ip)
            self.child_ui.edt_usename.setText(self.username)
            self.child_ui.edt_password.setText(self.password)
        else:
            self.child_ui.edt_ip.setText('192.168.0.1')
            self.child_ui.edt_usename.setText('admin')
            self.child_ui.edt_password.setText('admin')
        self.child.show()

    def save_(self):
        self.ip = self.child_ui.edt_ip.text()
        self.username = self.child_ui.edt_usename.text()
        self.password = self.child_ui.edt_password.text()
        if self.ip and self.username and self.password:
            self.brouwser = webdriver.Chrome(chrome_options=self.chrome_options)
            self.connections()
            self.child.hide()
            self.ui.label.setText(self.ip)
            self.ui.centralwidget.setEnabled(True)
            try:
                self.brouwser.get('http://{}/'.format(self.ip))
                self.ui.label.setStyleSheet('color :green;')
                #if self.brouwser.last_request.response.status_code ==200 or self.brouwser.last_request.response.status_code ==401:
                self.ui.label.setStyleSheet('color :green;')
                # else:
                #     self.ui.label.setStyleSheet('color :red;')
                self.brouwser.close()
                self.on_off_triger()
            except:
                self.ui.label.setStyleSheet('color :red;')
                try:
                    self.brouwser.close()
                except:
                    pass



        else:
            pass #invalid ip address

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
    try:
        app = QtWidgets.QApplication(sys.argv)
        main_window = MainWindow()
        # main_window.window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)
        sys.exit(222)
