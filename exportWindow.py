import sys
import pandas as pd
from PyQt5.QtWidgets import (
    QWidget
)

class ExportWindow(QWidget):
    def __init__(self, dataFrame: pd.DataFrame):
        super().__init__()

        #Set Fields

        self.dataFrame = dataFrame

        #Functions Invoke

        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle('Export as CSV')