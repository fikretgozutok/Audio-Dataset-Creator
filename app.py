import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFileDialog,
    QComboBox,
    QListWidget
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

        self.cmbBoxClassNames = QListWidget()
        self.cmbBoxClassNames.setSelectionMode(QListWidget.MultiSelection)

    def initLayouts(self):
        self.lytMain = QVBoxLayout()

        self.lytSelectFile = QHBoxLayout()

        self.lytBody = QHBoxLayout()

        self.lytBodyLeft = QVBoxLayout()

        self.lytBodyRight = QVBoxLayout()

        #Append Widgets to Layout

        self.lytSelectFile.addWidget(self.lblClassNames)
        self.lytSelectFile.addWidget(self.btnSelectClassNamesFile)

        self.lytBodyLeft.addWidget(self.cmbBoxClassNames)

        #Append Layouts to Main Layout

        self.lytMain.addLayout(self.lytSelectFile)

        self.lytBody.addLayout(self.lytBodyLeft)
        self.lytBody.addLayout(self.lytBodyRight)

        self.lytMain.addLayout(self.lytBody)

    def setActions(self):
        self.btnSelectClassNamesFile.clicked.connect(self.selectClassNameFile)
    
    def initUI(self):
        self.setGeometry(100, 100, 500, 500)
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

            self.cmbBoxClassNames.addItems(self.classNames)


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

