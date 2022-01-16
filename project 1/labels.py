import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Labels")
        self.setGeometry(50,50,400,400)
        self.UI()

    def UI(self):
        text1 = QLabel("Hello", self)
        text2 = QLabel("World", self)
        text1.move(100, 50)
        text2.move(200, 50)
        self.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()