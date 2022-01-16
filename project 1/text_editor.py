import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font = QFont("Poppins", 12)

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Text Editor")
        self.setGeometry(50,50,500,500)
        self.UI()

    def UI(self):
        self.editor = QTextEdit(self)
        self.editor.move(150, 80)
        self.editor.setAcceptRichText(False)
        button = QPushButton("Send", self)
        button.move(315, 280)
        button.clicked.connect(self.getValue)
        self.show()

    def getValue(self):
        value = self.editor.toPlainText()
        print(value)

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()