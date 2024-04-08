import sys
import pandas as pd
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTableWidget,
    QTableWidgetItem
)

class ExportWindow(QWidget):
    def __init__(self, dataFrame: pd.DataFrame):
        super().__init__()

        #Set Fields

        self.dataFrame = dataFrame

        #Functions Invoke

        self.initWidgets()
        self.initLayouts()
        self.setActions()
        self.initUI()

        self.setTable()

    def initWidgets(self):
        self.tblData = QTableWidget()

        self.btnExport = QPushButton('Export as .csv file')

    def initLayouts(self):
        self.lytMain = QVBoxLayout()

        self.lytTable = QVBoxLayout()

        self.lytControl = QVBoxLayout()

        #Append widgets to layouts

        self.lytTable.addWidget(self.tblData)

        self.lytControl.addWidget(self.btnExport)

        #Append layouts to main layout

        self.lytMain.addLayout(self.lytTable)

        self.lytMain.addLayout(self.lytControl)

        #Set layout apperaence

        self.lytTable.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.lytControl.setAlignment(Qt.AlignmentFlag.AlignBottom)

    def setActions(self):
        self.btnExport.clicked.connect(self.export)

    def initUI(self):
        self.setGeometry(200, 200, 600, 400)
        self.setWindowTitle('Export')

        self.setLayout(self.lytMain)

    #Actions

    def export(self):
        self.dataFrame.to_csv('./outputs/data.csv')

        self.close()

    #Methods

    def setTable(self):
        rowCount = self.dataFrame.shape[0]
        colCount = self.dataFrame.shape[1]

        self.tblData.setRowCount(rowCount)
        self.tblData.setColumnCount(colCount)

        self.tblData.setHorizontalHeaderLabels(self.dataFrame.columns)

        for i in range(rowCount):
            for j in range(colCount):
                item = QTableWidgetItem(str(self.dataFrame.iloc[i, j]))

                self.tblData.setItem(i, j, item)