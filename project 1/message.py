import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font = QFont("Poppins", 12)

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Message")
        self.setGeometry(50,50,400,400)
        self.UI()

    def UI(self):
        button = QPushButton("Click Me", self)
        button.setFont(font)
        button.move(150, 80)
        button.clicked.connect(self.messageBox)
        self.show()

    def messageBox(self):
        # mbox = QMessageBox.question(self, "Warning!!!", "Are you sure to exit?",
        #                             QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        #
        # if mbox == QMessageBox.Yes:
        #     print("Yes")
        #     sys.exit()
        # elif mbox == QMessageBox.No:
        #     print("No")
        # else:
        #     print("Cancel")

        mbox = QMessageBox.information(self, "Info", "You logged Out!")

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()