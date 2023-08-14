from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QMessageBox, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QTabWidget, QDial, QSlider, QScrollBar, QGroupBox, QToolButton, QComboBox, QPushButton, QLineEdit, QLabel, QCheckBox, QDoubleSpinBox, QListWidget, QFileDialog
from PyQt5 import uic, QtGui, QtCore
from PIL import Image
from PIL.ImageQt import ImageQt
import traceback
import sys

class groupBox_Variable(QWidget):
    def __init__(self, varbox):
        super
        self.varbox=varbox

        self.distributionType = self.findChild(QComboBox,'comboBox_distribution')
        distlst = ["normal","non-normal"]
        self.distributionType.addItems(distlst)
        self.distributionType.setCurrentIndex(0)

        


    def changeDistributionType(self):
        newDistribtuionType=self.distributionType.currentText()