import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(150,200,300,400)
        self.setWindowTitle("Hello World!")

        self.show()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())



