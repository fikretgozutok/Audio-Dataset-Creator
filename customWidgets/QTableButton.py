from PyQt5.QtWidgets import QPushButton

class QTableButton(QPushButton):
    def __init__(self, rowIndex: int, txt: str = None):
        super().__init__()

        #Set Fields
        self.__rowIndex: int = rowIndex

        self.setText(txt)

     #Encapsulation

    def getRowIndex(self):
        return self.__rowIndex
