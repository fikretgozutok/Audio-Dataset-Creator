import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget
)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('Audio Dataset Creator')



def run():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()

