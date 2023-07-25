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
#import pyi_splash

# Update the text on the splash screen
#pyi_splash.update_text("Loading Object Creator")


VERSION = 'v0.1.1'


myappid = f'groupcreator.{VERSION}' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class MainWindowUi(QMainWindow):
    def __init__(self, app_data_path, opening_objects = None):
        
        super().__init__()
        uic.loadUi(aux.resource_path('gui/main_window.ui'), self)
        

        #Load empty object if not started with objects

     
        self.show()
        self.checkForUpdates(silent = True)

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

    main = MainWindowUi(app_data_path= app_data_path, opening_objects= sys.argv[1:],)
    main.show()
    main.activateWindow()

    app.exec_()


    return main

if __name__ == '__main__':
    m = main()

