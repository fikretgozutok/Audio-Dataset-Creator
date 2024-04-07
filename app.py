import sys
from gtts import gTTS
import pandas as pd
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFileDialog,
    QListWidget,
    QLineEdit
)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initWidgets()
        self.initLayouts()
        self.setActions()
        self.initUI()

    def initWidgets(self):
        self.lblClassNames = QLabel('...')
        self.btnSelectClassNamesFile = QPushButton('Select File')

        self.listClassNames = QListWidget()
        self.listClassNames.setSelectionMode(QListWidget.MultiSelection)

        self.txtBoxScript = QLineEdit()
        self.txtBoxDescription = QLineEdit()

        self.txtBoxScript.setPlaceholderText('Type Audio Script...')
        self.txtBoxDescription.setPlaceholderText('Type Description...')

        self.btnAdd = QPushButton('Add')
        self.btnExport = QPushButton('Export')

        self.btnAdd.setEnabled(False)
        self.btnExport.setEnabled(False)

    def initLayouts(self):
        self.lytMain = QVBoxLayout()

        self.lytSelectFile = QHBoxLayout()

        self.lytBody = QHBoxLayout()

        self.lytBodyLeft = QVBoxLayout()

        self.lytBodyRight = QVBoxLayout()

        self.lytControl = QHBoxLayout()

        #Set Layout Appareance

        self.lytBodyRight.setAlignment(Qt.AlignmentFlag.AlignTop)

        #Append Widgets to Layout

        self.lytSelectFile.addWidget(self.lblClassNames)
        self.lytSelectFile.addWidget(self.btnSelectClassNamesFile)

        self.lytBodyLeft.addWidget(self.listClassNames)

        self.lytBodyRight.addWidget(self.txtBoxScript)
        self.lytBodyRight.addWidget(self.txtBoxDescription)

        self.lytControl.addWidget(self.btnAdd)
        self.lytControl.addWidget(self.btnExport)

        #Append Layouts to Main Layout

        self.lytMain.addLayout(self.lytSelectFile)

        self.lytBody.addLayout(self.lytBodyLeft, stretch = 40)
        self.lytBody.addLayout(self.lytBodyRight, stretch = 60)

        self.lytMain.addLayout(self.lytBody)

        self.lytMain.addLayout(self.lytControl)

    def setActions(self):
        self.btnSelectClassNamesFile.clicked.connect(self.selectClassNameFile)
        self.btnAdd.clicked.connect(self.add)
    
    def initUI(self):
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('Audio Dataset Creator')

        self.setLayout(self.lytMain)

    #Actions
    def selectClassNameFile(self):
        fileDialog = QFileDialog()
        fileDialog.setWindowTitle('Select Class Name File')
        fileDialog.setFileMode(QFileDialog.ExistingFile)
        fileDialog.setNameFilter('Text Files (*.txt)')

        if fileDialog.exec_():
            selectedFile = fileDialog.selectedFiles()[0]
            
            self.classNames = self.readClassNamesFromFile(selectedFile)

            self.lblClassNames.setText(f'{len(self.classNames)} class(es) found!')

            self.listClassNames.addItems(self.classNames)

            self.btnAdd.setEnabled(True)
            self.btnExport.setEnabled(True)

    def add(self):
        selectedClasses = [i.text() for i in self.listClassNames.selectedItems()]
        audioScript = self.txtBoxScript.text()
        description = self.txtBoxDescription.text()

        print(selectedClasses, audioScript, description)

    def export(self):
        pass

    #Methods
            
    def readClassNamesFromFile(self, filePath: str) -> list:
        
        with open(filePath, 'r') as file:
            content = file.readlines()
            content = [l.strip() for l in content]

            return content


def run():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()

