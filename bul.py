
from PyQt5 import QtCore, QtGui, QtWidgets
import resources
import sqlite3
import sonuc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(548, 739)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 551, 741))
        self.background.setStyleSheet("background-image: url(:/background/background.jpg);")
        self.background.setText("")
        self.background.setObjectName("background")
        self.kitap_bul_yazisi = QtWidgets.QLabel(self.centralwidget)
        self.kitap_bul_yazisi.setGeometry(QtCore.QRect(140, 80, 271, 51))
        self.kitap_bul_yazisi.setMinimumSize(QtCore.QSize(221, 31))
        self.kitap_bul_yazisi.setStyleSheet("background-color: rgba(255, 255, 255, 80);")
        self.kitap_bul_yazisi.setObjectName("kitap_bul_yazisi")
        self.kitap_adi_input = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.kitap_adi_input.setGeometry(QtCore.QRect(20, 230, 341, 51))
        self.kitap_adi_input.setObjectName("kitap_adi_input")
        self.yazar_adi_input = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.yazar_adi_input.setGeometry(QtCore.QRect(20, 380, 341, 51))
        self.yazar_adi_input.setObjectName("yazar_adi_input")
        self.kitap_konumu_input = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.kitap_konumu_input.setGeometry(QtCore.QRect(20, 520, 341, 51))
        self.kitap_konumu_input.setObjectName("kitap_konumu_input")
        self.Kitap_adi = QtWidgets.QLabel(self.centralwidget)
        self.Kitap_adi.setGeometry(QtCore.QRect(20, 190, 81, 31))
        self.Kitap_adi.setMinimumSize(QtCore.QSize(47, 13))
        self.Kitap_adi.setStyleSheet("background-color: rgba(255, 255, 255, 80);")
        self.Kitap_adi.setObjectName("Kitap_adi")
        self.yazar_adi = QtWidgets.QLabel(self.centralwidget)
        self.yazar_adi.setGeometry(QtCore.QRect(20, 340, 81, 31))
        self.yazar_adi.setMinimumSize(QtCore.QSize(47, 13))
        self.yazar_adi.setStyleSheet("background-color: rgba(255, 255, 255, 80);")
        self.yazar_adi.setObjectName("yazar_adi")
        self.kitap_konumu = QtWidgets.QLabel(self.centralwidget)
        self.kitap_konumu.setGeometry(QtCore.QRect(20, 480, 121, 31))
        self.kitap_konumu.setMinimumSize(QtCore.QSize(47, 13))
        self.kitap_konumu.setStyleSheet("background-color: rgba(255, 255, 255, 80);")
        self.kitap_konumu.setObjectName("kitap_konumu")
        self.Kitap_ekle = QtWidgets.QPushButton(self.centralwidget)
        self.Kitap_ekle.setGeometry(QtCore.QRect(200, 610, 141, 61))
        self.Kitap_ekle.setStyleSheet("")
        self.Kitap_ekle.setObjectName("Kitap_ekle")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.Kitap_ekle.clicked.connect(self.bul)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Kitap Bul", "Kitap Bul"))
        self.kitap_bul_yazisi.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Kitap Bul</span></p></body></html>"))
        self.Kitap_adi.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Kitap Adı</span></p></body></html>"))
        self.yazar_adi.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Yazar Adı</span></p></body></html>"))
        self.kitap_konumu.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Kitap Konumu</span></p></body></html>"))
        self.Kitap_ekle.setText(_translate("MainWindow", "Kitap Bul"))

    def bul(self):
        baglanti = sqlite3.connect("kutuphane.db")
        cursor = baglanti.cursor()
        kitap_adi_input = self.kitap_adi_input.toPlainText()
        yazar_adi_input = self.yazar_adi_input.toPlainText()
        kitap_konumu_input = self.kitap_konumu_input.toPlainText()

        if kitap_adi_input == "":
            kitap_adi_input = None
        if yazar_adi_input == "":
            yazar_adi_input = None
        if kitap_konumu_input == "":
            kitap_konumu_input = None
        
        if kitap_adi_input is None and yazar_adi_input is None and kitap_konumu_input is None:
            print("Lütfen en az bir alanı doldurunuz.")

        elif kitap_adi_input is None and yazar_adi_input is None and kitap_konumu_input is not None:
            cursor.execute('SELECT * FROM kitaplar WHERE kitap_konumu = ?', (kitap_konumu_input,))

        elif kitap_adi_input is None and kitap_konumu_input is None and yazar_adi_input is not None:
            cursor.execute('SELECT * FROM kitaplar WHERE yazar_adi = ?', (yazar_adi_input,))

        elif yazar_adi_input is None and kitap_konumu_input is None and kitap_adi_input is not None:
            cursor.execute('SELECT * FROM kitaplar WHERE kitap_adi = ?', (kitap_adi_input,))

        elif kitap_adi_input is None and yazar_adi_input is not None and kitap_konumu_input is not None:
            cursor.execute('SELECT * FROM kitaplar WHERE yazar_adi = ? AND kitap_konumu = ?', (yazar_adi_input, kitap_konumu_input))

        elif yazar_adi_input is None and kitap_adi_input is not None and kitap_konumu_input is not None:
            cursor.execute('SELECT * FROM kitaplar WHERE kitap_adi = ? AND kitap_konumu = ?', (kitap_adi_input, kitap_konumu_input))

        elif kitap_konumu_input is None and kitap_adi_input is not None and yazar_adi_input is not None:
            cursor.execute('SELECT * FROM kitaplar WHERE kitap_adi = ? AND yazar_adi = ?', (kitap_adi_input, yazar_adi_input))

        else:
            cursor.execute('SELECT * FROM kitaplar WHERE kitap_adi = ? AND yazar_adi = ? AND kitap_konumu = ?', (kitap_adi_input, yazar_adi_input, kitap_konumu_input))
        
        
        kitaplar = cursor.fetchall()
        baglanti.close()
        with open("sonuç.txt","w+") as file:
            for i in kitaplar:
                #write the data to a file in different lines
                file.write(str(i))
                file.write("\n")
        self.sonuclandir()

    def sonuclandir(self):
        import sonuc
        self.window = QtWidgets.QMainWindow()
        self.ui = sonuc.Ui_MainWindow()
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