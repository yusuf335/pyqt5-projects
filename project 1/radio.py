import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Radio")
        self.setGeometry(50,50,400,400)
        self.UI()

    def UI(self):
        self.male = QRadioButton('Male',self)
        self.male.move(150,80)
        self.male.setChecked(True)
        self.female = QRadioButton('Female', self)
        self.female.move(150, 100)
        button = QPushButton("Submit", self)
        button.clicked.connect(self.getValues)
        button.move(150,120)
        self.show()
    def getValues(self):
        if self.male.isChecked():
            print("male")
        else:
            print("female")

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()