import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer

font = QFont("Poppins", 12)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Timer")
        self.setGeometry(50,50,400,400)
        self.UI()

    def UI(self):
        self.colorLabel = QLabel(self)
        self.colorLabel.setStyleSheet("background-color:green")
        self.colorLabel.resize(200, 200)
        self.colorLabel.move(100,100)
        #################################Buttons###################
        btnStart = QPushButton("Start", self)
        btnStart.move(100, 320)
        btnStart.clicked.connect(self.start)
        btnStop = QPushButton("Stop", self)
        btnStop.clicked.connect(self.stop)
        btnStop.move(200, 320)

        ##############################Timer########################
        self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.changeColor)
        self.value = 0

        self.show()

    def changeColor(self):
        if self.value == 0:
            self.colorLabel.setStyleSheet("background-color:red")
            self.value = 1
        else:
            self.colorLabel.setStyleSheet("background-color:green")
            self.value = 0

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()