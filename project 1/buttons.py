import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Labels")
        self.setGeometry(50,50,400,400)
        self.UI()

    def UI(self):
        self.text = QLabel("Hello", self)
        enterButton = QPushButton("Enter", self)
        exitButton = QPushButton("Exit", self)
        self.text.move(180,50)
        enterButton.move(100,80)
        exitButton.move(200,80)
        enterButton.clicked.connect(self.enterFunc)
        exitButton.clicked.connect(self.exitFunc)
        self.show()

    def enterFunc(self):
        self.text.setText("World!")
        self.text.resize(180,20)
    def exitFunc(self):
        self.text.setText("Hello")
        self.text.resize(180,20)

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()