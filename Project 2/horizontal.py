import  sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Horizontal Box Layout")
        self.setGeometry(50, 50, 400, 400)
        self.UI()

    def UI(self):
        hbox = QHBoxLayout()
        btn1 = QPushButton("Button1")
        btn2 = QPushButton("Button2")
        btn3 = QPushButton("Button3")

        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        self.setLayout(hbox)
        self.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()