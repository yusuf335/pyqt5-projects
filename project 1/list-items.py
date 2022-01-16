import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("List")
        self.setGeometry(50, 50, 400, 400)
        self.UI()

    def UI(self):
        self.addrecord = QLineEdit(self)
        self.addrecord.move(20, 40)
        self.listwidget = QListWidget(self)
        self.listwidget.move(20, 80)
        list = ["Batman"]
        self.listwidget.addItems(list)

        btnAdd = QPushButton("Add", self)
        btnAdd.clicked.connect(self.addFunc)
        btnAdd.move(300, 80)
        btnDelete = QPushButton("Delete", self)
        btnDelete.clicked.connect(self.deleteFunc)
        btnDelete.move(300, 120)
        btnGet = QPushButton("Get ", self)
        btnGet.clicked.connect(self.getFunc)
        btnGet.move(300, 160)
        btnDeleteAll = QPushButton("Delete All", self)
        btnDeleteAll.clicked.connect(self.deleteallFunc)
        btnDeleteAll.move(300, 200)

        self.show()

    def addFunc(self):
        value = self.addrecord.text()
        print(value)
        self.listwidget.addItem(value)
        self.addrecord.setText("")

    def deleteFunc(self):
        id = self.listwidget.currentRow()
        print(id)
        self.listwidget.takeItem(id)

    def getFunc(self):
        value = self.listwidget.currentItem().text()
        print(value)

    def deleteallFunc(self):
           self.listwidget.clear()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()