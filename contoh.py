import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


def display():
    app = QApplication([])
    mwin = QMainWindow()
    bar = mwin.menuBar()
    bar.setVisible(False)
    menu2 = bar.addMenu("Simulasi")
    tabungan = QAction("Tabungang Berjangka")
    menu2.addAction(tabungan)
    peminjaman = QAction("Peminjaman")
    menu2.addAction(peminjaman)
    anggaran = QAction("Anggaran bulanan")
    menu2.addAction(anggaran)
    menu1 = bar.addMenu("take")
    kila = QAction("kila")
    menu1.addAction(kila)

    def main_win():
        def stabungan():
            win = QWidget()
            layout = QVBoxLayout()
            label = QLabel("Selamat daatang\n di\n simulasi tabungan berjangka")
            label.setStyleSheet("font:15px;")
            label.setAlignment(Qt.AlignCenter)
            layout.addWidget(label)
            win.setLayout(layout)
            mwin.setCentralWidget(win)

        def speminjaman():
            win = QWidget()
            layout = QVBoxLayout()
            label = QLabel("selamat datang\n di\n simulasi peminjaman")
            label.setStyleSheet("font:15px;")
            label.setAlignment(Qt.AlignCenter)
            layout.addWidget(label)
            win.setLayout(layout)
            mwin.setCentralWidget(win)

        def sanggaran():
            win = QWidget()
            layout = QVBoxLayout()
            label = QLabel("selamat datang\n di\n simulasi anggaran bulanan")
            label.setStyleSheet("font:15px;")
            label.setAlignment(Qt.AlignCenter)
            layout.addWidget(label)
            win.setLayout(layout)
            mwin.setCentralWidget(win)
        bar.setVisible(True)
        tabungan.triggered.connect(stabungan)
        peminjaman.triggered.connect(speminjaman)
        anggaran.triggered.connect(sanggaran)
        cwin = QWidget()
        layout = QVBoxLayout()
        label = QLabel("Selamat Datang \n di\n Main Window")
        label.setStyleSheet("font:15px;")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        cwin.setLayout(layout)
        mwin.setMinimumSize(250, 200)
        mwin.setWindowTitle("Main Window")
        mwin.setCentralWidget(cwin)

    def alert_message(title, caps):
        alert = QMessageBox()
        alert.about(mwin, str(title), str(caps))

    def login_win():
        win = QWidget()
        def check_account():
            user = lineuser.text()
            pasw = linepass.text()
            if user == "admin" and pasw == "admin":
                main_win()
            else:
                alert_message("Login", "Your Username or Passwordisn't correct")
                lineuser.setText("")
                linepass.setText("")
            layout = QFormLayout()
            labeluser = QLabel("Username")
            lineuser = QLineEdit()
            labelpass = QLabel("Password")
            linepass = QLineEdit()
            linepass.setEchoMode(QLineEdit.Password)
            layout.addRow(labeluser, lineuser)
            layout.addRow(labelpass, linepass)
            button = QPushButton("Login")
            layout.addRow(button)
            button.clicked.connect(check_account)
            win.setLayout(layout)
            mwin.setCentralWidget(win)
            mwin.setWindowTitle("Login")
    login_win()
    mwin.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    display()
