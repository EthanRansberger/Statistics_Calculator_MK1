# -*- coding: utf-8 -*-
"""
*****************************************************************************
 * Copyright (c) 2023 Tolsimir
 *
 * The program "Object Creator" and all subsequent modules are licensed
 * under the GNU General Public License version 3.
 *****************************************************************************
"""
 

from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QMessageBox, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QTabWidget, QDial, QSlider, QScrollBar, QGroupBox, QToolButton, QComboBox, QPushButton, QLineEdit, QLabel, QCheckBox, QDoubleSpinBox, QListWidget, QFileDialog
from PyQt5 import uic, QtGui, QtCore
from PIL import Image
from PIL.ImageQt import ImageQt
import traceback
import sys


import io, os
from os import getcwd
from os.path import splitext, split, abspath,join, exists

import requests


import ctypes
import auxiliaries as aux
import widgets as wdg
#import pyi_splash

# Update the text on the splash screen
#pyi_splash.update_text("Loading Object Creator")


VERSION = 'v0.1.1'


myappid = f'groupcreator.{VERSION}' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class MainWindowUi(QMainWindow):
    def __init__(self, app_data_path):
        
        super().__init__()
        uic.loadUi(aux.resource_path('gui/main_window.ui'), self)
        self.setWindowIcon(QtGui.QIcon(aux.resource_path("gui/icon.png")))
        self.setWindowTitle(f'Statistics Calculator - {VERSION}')

        

     
        self.show()


        #### re-integrate after a release
        #self.checkForUpdates(silent = True)

    def checkForUpdates(self, silent = False):
        try:
            response = requests.get("https://api.github.com/repos/ethanransberger/Statistics_Calculator_MK1/releases/latest")
        except requests.exceptions.ConnectionError:
            return

        # check if there is a higher version on git
      
        git_version = response.json()['tag_name']

        if not versionCheck(git_version):
            if not silent:
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("No update available")
                msg.setText(f"Stat calculator {VERSION} is up to date!")
                msg.setStandardButtons(QMessageBox.Ok)

                msg.exec_()

            return

        url = response.json()['html_url']
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("New version available!")
        msg.setTextFormat(QtCore.Qt.RichText)

        msg.setText(f"Object Creator {git_version} is now available! <br> \
                Your version: {VERSION} <br> \
                <a href='{url}'>Click here to go to download page. </a> <br> <br> \
                Alternatively, would you like to update automatically? <br> \
                This only works if the program has been installed via the installer.")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)


        reply = msg.exec_()

        # Only in the .exe program the updater can be used
        if reply == QMessageBox.Yes:
            try:
                os.execl('updater.exe', 'updater.exe')
            except FileNotFoundError:
                return


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("error message:\n", tb)


    sys._excepthook(exc_type, exc_value, exc_tb)
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setWindowTitle("Error Trapper")
    msg.setText("Runtime error:")
    msg.setInformativeText(tb)
    msg.exec_()
    #sys.exit()

sys._excepthook = sys.excepthook
sys.excepthook = excepthook

def versionCheck(version):

    version = version[1:].split('.')
    version_this = VERSION[1:].split('.')

    for i in range(len(version_this),len(version)):
        version_this.append(0)

    for i, val in enumerate(version):

        if int(val) > int(version_this[i]):
            return True

    return False


def main():
    # if not QApplication.instance():
    #     app = QApplication(sys.argv)
    # else:
    #     app = QApplication.instance()

    #pyi_splash.close()
    app = QApplication(sys.argv)

    app_data_path = join(os.environ['APPDATA'],'Group Creator')
    if not exists(app_data_path):
        os.makedirs(app_data_path)

    main = MainWindowUi(app_data_path= app_data_path)
    main.show()
    main.activateWindow()

    app.exec_()


    return main

if __name__ == '__main__':
    m = main()

