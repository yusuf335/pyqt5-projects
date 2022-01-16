import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Labels")
        self.setGeometry(50,50,400,400)
        self.UI()

    def UI(self):
        self.nameTextBox = QLineEdit(self)
        self.nameTextBox.setPlaceholderText("Name")
        self.nameTextBox.move(150,50)
        self.passTextBox = QLineEdit(self)
        self.passTextBox.setPlaceholderText("Password")
        self.passTextBox.setEchoMode(QLineEdit.Password)
        self.passTextBox.move(150,80)
        self.button = QPushButton("Save", self)
        self.button.move(150,130)
        self.button.clicked.connect(self.getValues)
        self.show()

    def getValues(self):
        name = self.nameTextBox.text()
        password = self.passTextBox.text()
        self.setWindowTitle("Name: "+name)

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()