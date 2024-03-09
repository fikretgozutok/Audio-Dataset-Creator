import sys
import os
import pandas as pd
from gtts import gTTS
from PyQt5.QtWidgets import (
    QWidget, 
    QApplication, 
    QBoxLayout, 
    QVBoxLayout, 
    QHBoxLayout,
    QFileDialog,
    QLabel,
    QPushButton
)

class MainApp(QWidget):
    def __init__(self):
        super().__init__()

        self.__clasNamesFilePath = ""

        self.setWindow()
        self.setWidgets()
        self.setEvents()
        self.setLayouts()
        self.appendWidgets2Layouts()
        self.setUI()
        

    def setWindow(self):
        self.setWindowTitle("Audio Dataset Creator")
        self.setGeometry(100,100, 500,500)

    def setWidgets(self):
        self.lblFileDialog = QLabel("Select class names file:")
        self.btnOpenFileDialog = QPushButton("Select")

    def setEvents(self):
        self.btnOpenFileDialog.clicked.connect(self.openFileDialog)

    def setLayouts(self):
        self.lytFileDialog = QHBoxLayout(self)

    def appendWidgets2Layouts(self):
        self.lytFileDialog.addWidget(self.lblFileDialog)
        self.lytFileDialog.addWidget(self.btnOpenFileDialog)
    
    def setUI(self):
        mainLayout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
        mainLayout.addChildLayout(self.lytFileDialog)
        self.setLayout(mainLayout)

    def openFileDialog(self):
        self.__clasNamesFilePath, _ = QFileDialog.getOpenFileName()
        print(self.__clasNamesFilePath)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainApp = MainApp()
    mainApp.show()
    sys.exit(app.exec_())