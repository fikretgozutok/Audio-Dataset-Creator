import pandas as pd
from functools import partial
from customWidgets.QTableButton import QTableButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
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

        self.setBtnExportSelectionMode()
        self.expandDataFrame()
        self.setTable()

    def initWidgets(self) -> None:
        self.tblData = QTableWidget()

        self.btnExport = QPushButton('Export as .csv file')

    def initLayouts(self) -> None:
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

    def setActions(self) -> None:
        self.btnExport.clicked.connect(self.export)

    def initUI(self) -> None:
        self.setGeometry(200, 200, 600, 400)
        self.setWindowTitle('Export')

        self.setWindowIcon(QIcon('ico.ico'))

        self.setLayout(self.lytMain)

    #Actions

    def export(self) -> None:
        self.dataFrame.to_csv('./outputs/data.csv')

        self.close()

    #Methods

    def setTable(self) -> None:

        self.tblData.clear()

        rowCount = self.dataFrame.shape[0]
        colCount = self.dataFrame.shape[1]

        self.tblData.setRowCount(rowCount)
        self.tblData.setColumnCount(colCount)

        self.tblData.setHorizontalHeaderLabels(self.dataFrame.columns)

        for i in range(rowCount):
            for j in range(colCount):

                if j == (colCount - 1):
                    btnDelete = QTableButton(rowIndex = i, txt = 'Delete!')
                    btnDelete.clicked.connect(partial(self.deleteRecord, btnDelete.getRowIndex()))
                    self.tblData.setCellWidget(i, j, btnDelete)
                else:
                    item = QTableWidgetItem(str(self.dataFrame.iloc[i, j]))
                    self.tblData.setItem(i, j, item)

    def deleteRecord(self, rowIndex: int) -> None:
        self.dataFrame.drop(rowIndex, inplace = True)
        self.setTable()
        self.setBtnExportSelectionMode()

    def expandDataFrame(self):
        self.dataFrame[' '] = None

    def setBtnExportSelectionMode(self) -> None:
        self.btnExport.setEnabled(True if len(self.dataFrame) > 0 else False)