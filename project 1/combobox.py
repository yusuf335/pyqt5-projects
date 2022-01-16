import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Combo Box")
        self.setGeometry(250, 150, 500, 500)
        self.UI()

    def UI(self):
        self.combo = QComboBox(self)
        self.combo.move(150, 100)
        button = QPushButton("Save", self)
        button.move(150, 140)
        button.clicked.connect(self.getValue)
        self.combo.addItems(["--", "a", "b", "c", "d"])
        self.show()

    def getValue(self):
        value = self.combo.currentText()
        print(value)
        
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()