from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
app = QApplication(sys.argv)
win = QWidget()
def display():  # function
    parent = QVBoxLayout()  # untuk mengatur layer belakang
    label = QLabel(
        "<h1><font color=blue>Anggaran Bulanan</font></h1>")
    label.setAlignment(Qt.AlignCenter)
    parent.addWidget(label)
    win.setLayout(parent)
    win.setGeometry(100, 100, 300, 200)
    win.show()
    win.setWindowTitle("Anggaran_bulanan")
if __name__ == '__main__':
    display()
