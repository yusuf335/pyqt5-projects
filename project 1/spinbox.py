import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font = QFont("Poppins", 12)

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Spin")
        self.setGeometry(50,50,400,400)
        self.UI()

    def UI(self):
        self.spinBox = QSpinBox(self)
        self.spinBox.move(150, 80)
        self.spinBox.setFont(font)
        self.spinBox.setRange(10,20)
        self.spinBox.setPrefix("$ ")
        self.spinBox.setSingleStep(5)
        self.spinBox.valueChanged.connect(self.getValue)
        button = QPushButton("Submit", self)
        button.move(150, 150)
        button.clicked.connect(self.buttonValue)

        self.show()

    def getValue(self):
        value = self.spinBox.value()
        print(value)

    def buttonValue(self):
        value = self.spinBox.value()
        print(value)

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()