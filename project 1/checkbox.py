import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Checkbox")
        self.setGeometry(50,50,400,400)
        self.UI()

    def UI(self):
        self.name = QLineEdit(self)
        self.name.setPlaceholderText("Name")
        self.name.move(150,50)
        self.surname = QLineEdit(self)
        self.surname.setPlaceholderText("Surname")
        self.surname.move(150,80)
        self.checkBox =QCheckBox("Remember me", self)
        self.checkBox.move(150,110)
        button = QPushButton("Submit",self)
        button.clicked.connect(self.submit)
        button.move(150,140)
        self.show()

    def submit(self):
        if (self.checkBox.isChecked()):
            print("Name: "+self.name.text()+ "\nSurname: "+self.surname.text()+ "\nRemeber me is checked")
        else:
            print("Name: " + self.name.text() + "\nSurname: " + self.surname.text() + "\nRemeber me is not checked")

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()