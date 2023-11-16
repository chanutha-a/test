import sys
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi




class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("homepage.ui", self)


