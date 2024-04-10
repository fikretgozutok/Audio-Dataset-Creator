from PyQt5.QtWidgets import QPushButton

class QTableButton(QPushButton):
    def __init__(self, rowIndex: int = None, txt: str = None):
        super().__init__(txt)

        #Set Fields
        self.__rowIndex: int = rowIndex

     #Encapsulation

    def getRowIndex(self):
        return self.__rowIndex
