import sys
import os
import secrets
import string
import pandas as pd
from exportWindow import ExportWindow
from gtts import gTTS
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
    QLineEdit,
    QMessageBox
)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        #Set Fields

        self.outputDir = 'outputs'
        self.dataFrame = pd.DataFrame(columns = [
            'class_list',
            'file_path',
            'audio_script',
            'description'
        ])

        #Function Invokes

        self.setOutputDir()

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

        #Set Layout Apperaence

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
        self.btnExport.clicked.connect(self.export)
    
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
        
        data = {
            'class_list': (",".join(map(str, selectedClasses)) if len(selectedClasses) != 0 else None),
            'audio_script': (audioScript if audioScript != '' else None),
            'description': (description if description != '' else None)
        }

        if None in list(data.values()):
            self.showMessage('Fields can not be empty!', 'Error!', QMessageBox.Icon.Warning)
            return
        
        audioFile = self.createAudio(audioScript)

        if not audioFile:
            self.showMessage('Audio file generation error!', 'Error!', QMessageBox.StandardButton.Ok)
            return
        
        data['file_path'] = (audioFile),

        self.dataFrame.loc[len(self.dataFrame)] = data

        self.txtBoxScript.setText("")
        self.txtBoxDescription.setText("")

        self.listClassNames.clearSelection()
        

    def export(self):
        self.exportWindow = ExportWindow(self.dataFrame)
        self.exportWindow.show()

    #Methods
            
    def readClassNamesFromFile(self, filePath: str) -> list:
        
        with open(filePath, 'r') as file:
            content = file.readlines()
            content = [l.strip() for l in content]

            return content
        
    def createAudio(self, script: str) ->  str | None:

        if not script:
            return

        tts = gTTS(script, lang = 'tr')

        filePath = os.path.join(self.outputDir, self.generateFileName())
        filePath = f'{filePath}.mp3'

        tts.save(filePath)

        return filePath

    def generateFileName(self, length = 16) -> str:
        alphabet = string.ascii_letters + string.digits
        fileName = ''.join(secrets.choice(alphabet) for _ in range(length))
        return fileName
    
    def setOutputDir(self) -> None:
        if not os.path.exists(self.outputDir):
            os.mkdir(self.outputDir)

    def showMessage(self, msg: str, windowTitle: str, icon: QMessageBox.Icon) -> None:
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(icon)
        self.msgBox.setWindowTitle(windowTitle)
        self.msgBox.setText(msg)
        self.msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.msgBox.setDefaultButton(QMessageBox.StandardButton.Ok)

        returnValue = self.msgBox.exec()

        if returnValue == QMessageBox.StandardButton.Ok:
            self.msgBox.close()

        

        


def run():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()

