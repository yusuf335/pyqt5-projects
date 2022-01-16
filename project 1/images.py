import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image")
        self.setGeometry(50,50,400,400)
        self.UI()

    def UI(self):
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('images/2942488.png'))
        self.image.move(150,50)
        removeButton = QPushButton("Remove", self)
        removeButton.move(150, 220)
        removeButton.clicked.connect(self.removeImage)
        showButton = QPushButton("Show", self)
        showButton.clicked.connect(self.showImage)
        showButton.move(260,220)
        self.show()

    def removeImage(self):
        self.image.close()

    def showImage(self):
        self.image.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()