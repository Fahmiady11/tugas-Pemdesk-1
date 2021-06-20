from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import menu


def display():  # function
    app = QApplication(sys.argv)
    win = QWidget()
    parent = QVBoxLayout()
    label = QLabel("<h1><font color=blue>LOGIN</font></h1>")
    label.setAlignment(Qt.AlignCenter)

    label2 = QLabel("Username :")
    label3 = QLabel("Password :")

    button = QPushButton("Masuk")

    user = QLineEdit()
    pwd = QLineEdit()
    pwd.setEchoMode(QLineEdit.Password)

    from1 = QFormLayout()
    from1.addRow(label2, user)
    from1.addRow(label3, pwd)

    def log1(label2, label3):
        print(label2)
        if label2 == "fahmi" and label3 == "fahmiady":
            menu.display()
        else:
            print("error")

    def log():
        user1 = str(user.text())
        pwd1 = str(pwd.text())
        log1(user1, pwd1)

    button.clicked.connect(log)
    parent.addWidget(label)
    parent.addLayout(from1)
    parent.addWidget(button)
    #######################
    win.setLayout(parent)
    win.setGeometry(100, 100, 300, 200)
    win.show()
    win.setWindowTitle("Login")
    sys.exit(app.exec_())


if __name__ == '__main__':
    display()
