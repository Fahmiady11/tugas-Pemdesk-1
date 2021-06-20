from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import AnggaranBulanan
import peminjaman
import TabunganBerjangka
import sys
def display():
    app = QApplication(sys.argv)
    mW = QMainWindow()
    menubar = mW.menuBar()
    menubar.setVisible(False)
    fileM = menubar.addMenu("File")
    file1 = QAction("Simulasi Anggaran Bulanan")
    file2 = QAction("Simulasi Peminjaman")
    file3 = QAction("Simulasi Tabungan Berjangka")
    fileM.addAction(file1)
    fileM.addAction(file2)
    fileM.addAction(file3)
    # keluar
    exitAct = QAction('&Exit')
    exitAct.setShortcut('Ctrl+Q')
    exitAct.setStatusTip('Exit application')
    menubar.addAction(exitAct)
    exitAct.triggered.connect(app.quit)
    def menu():  # function
        menubar.setVisible(True)
        parent = QVBoxLayout()
        file1.triggered.connect(angBul)
        file2.triggered.connect(pemin)
        file3.triggered.connect(tabBer)
        ##################################
        cwin = QWidget()
        label=QLabel("SELAMAT DATANG DI MENU")
        label.setAlignment(Qt.AlignCenter)
        parent.addWidget(label)
        cwin.setLayout(parent)
        cwin.setGeometry(100, 100, 400, 400)
        cwin.setWindowTitle("Menu")
        mW.setCentralWidget(cwin)
    def angBul():
        AnggaranBulanan.display()
    def pemin():
        peminjaman.display()
    def tabBer():
        TabunganBerjangka.display()
    def login():  # function
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
            if label2 == "fahmi" and label3 == "fahmiady":
                menu()
            else:
                user.setText("")
                pwd.setText("")
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
        mW.setCentralWidget(win)
        mW.setWindowTitle("Login")
    login()
    mW.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    display()
