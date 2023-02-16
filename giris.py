from PyQt5 import QtCore, QtGui, QtWidgets
import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 740)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 551, 741))
        self.background.setStyleSheet("background-image: url(:/background/background.jpg);")
        self.background.setText("")
        self.background.setObjectName("background")
        self.kutuphane_yazisi = QtWidgets.QLabel(self.centralwidget)
        self.kutuphane_yazisi.setGeometry(QtCore.QRect(150, 100, 271, 51))
        self.kutuphane_yazisi.setMinimumSize(QtCore.QSize(221, 31))
        self.kutuphane_yazisi.setStyleSheet("background-color: rgba(255, 255, 255, 80);")
        self.kutuphane_yazisi.setObjectName("kutuphane_yazisi")
        self.Kitap_ekle = QtWidgets.QPushButton(self.centralwidget)
        self.Kitap_ekle.setGeometry(QtCore.QRect(120, 520, 141, 61))
        self.Kitap_ekle.setStyleSheet("")
        self.Kitap_ekle.setObjectName("Kitap_ekle")
        self.Kitap_bul = QtWidgets.QPushButton(self.centralwidget)
        self.Kitap_bul.setGeometry(QtCore.QRect(300, 520, 141, 61))
        self.Kitap_bul.setObjectName("Kitap_bul")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 210, 271, 251))
        self.label.setStyleSheet("image: url(:/Logo/198-1985648_transparent-background-atom-clipart-hd-png-download-removebg-preview.png);\n"
"background-color: rgba(255, 255, 255, 60);")
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Kutuphane", "Kutuphane"))
        self.kutuphane_yazisi.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt; color:#ffffff;\">Sanal Kütüphane</span></p></body></html>"))
        self.Kitap_ekle.setText(_translate("MainWindow", "Kitap Ekle"))
        self.Kitap_bul.setText(_translate("MainWindow", "Kitap Bul"))
 # when you click the kitap bul button button, it will open bul.py
        self.Kitap_bul.clicked.connect(self.bul)
        self.Kitap_ekle.clicked.connect(self.ekle)
    def bul(self):
        import bul
        self.window = QtWidgets.QMainWindow()
        self.ui = bul.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def ekle(self):
        import ekle
        self.window = QtWidgets.QMainWindow()
        self.ui = ekle.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())