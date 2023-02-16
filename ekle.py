# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\kitap_ekle.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import resources
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(549, 740)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 551, 741))
        self.background.setStyleSheet("background-image: url(:/background/background.jpg);")
        self.background.setText("")
        self.background.setObjectName("background")
        self.Kitap_ekle = QtWidgets.QLabel(self.centralwidget)
        self.Kitap_ekle.setGeometry(QtCore.QRect(130, 80, 281, 41))
        self.Kitap_ekle.setMinimumSize(QtCore.QSize(281, 41))
        self.Kitap_ekle.setStyleSheet("background-color: rgba(255, 255, 255, 80);")
        self.Kitap_ekle.setObjectName("Kitap_ekle")
        self.kitap_adi_input = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.kitap_adi_input.setGeometry(QtCore.QRect(30, 230, 341, 51))
        self.kitap_adi_input.setObjectName("kitap_adi_input")
        self.yazar_adi_input = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.yazar_adi_input.setGeometry(QtCore.QRect(30, 360, 341, 51))
        self.yazar_adi_input.setObjectName("yazar_adi_input")
        self.kitap_konumu_inpt = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.kitap_konumu_inpt.setGeometry(QtCore.QRect(30, 510, 341, 51))
        self.kitap_konumu_inpt.setObjectName("kitap_konumu_inpt")
        self.Kitap_adi = QtWidgets.QLabel(self.centralwidget)
        self.Kitap_adi.setGeometry(QtCore.QRect(30, 190, 81, 31))
        self.Kitap_adi.setMinimumSize(QtCore.QSize(47, 13))
        self.Kitap_adi.setStyleSheet("background-color: rgba(255, 255, 255, 80);")
        self.Kitap_adi.setObjectName("Kitap_adi")
        self.yazar_adi = QtWidgets.QLabel(self.centralwidget)
        self.yazar_adi.setGeometry(QtCore.QRect(30, 320, 81, 31))
        self.yazar_adi.setMinimumSize(QtCore.QSize(47, 13))
        self.yazar_adi.setStyleSheet("background-color: rgba(255, 255, 255, 80);")
        self.yazar_adi.setObjectName("yazar_adi")
        self.Kitap_konumu = QtWidgets.QLabel(self.centralwidget)
        self.Kitap_konumu.setGeometry(QtCore.QRect(30, 470, 121, 31))
        self.Kitap_konumu.setMinimumSize(QtCore.QSize(47, 13))
        self.Kitap_konumu.setStyleSheet("background-color: rgba(255, 255, 255, 80);")
        self.Kitap_konumu.setObjectName("Kitap_konumu")
        self.Kaydet = QtWidgets.QPushButton(self.centralwidget)
        self.Kaydet.setGeometry(QtCore.QRect(230, 620, 141, 61))
        self.Kaydet.setStyleSheet("")
        self.Kaydet.setObjectName("Kaydet")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.Kaydet.clicked.connect(self.kaydet)
    def kaydet(self):
        """Main funtion to save the data to the database"""

        conn = sqlite3.connect('kutuphane.db')
        
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS kitaplar (
            kitap_adi text,
            yazar_adi text,
            kitap_konumu text
        )""")
        c.execute("INSERT INTO kitaplar VALUES (:kitap_adi, :yazar_adi, :kitap_konumu)",
                    {
                        'kitap_adi': self.kitap_adi_input.toPlainText(),
                        'yazar_adi': self.yazar_adi_input.toPlainText(),
                        'kitap_konumu': self.kitap_konumu_inpt.toPlainText()
                    })
        conn.commit()
        conn.close()

        print("kaydedildi")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Kitap Ekle", "Kitap Ekle"))
        self.Kitap_ekle.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#ffffff;\">Kitap Ekle</span></p></body></html>"))
        self.Kitap_adi.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Kitap Adı</span></p></body></html>"))
        self.yazar_adi.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Yazar Adı</span></p></body></html>"))
        self.Kitap_konumu.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Kitap Konumu</span></p></body></html>"))
        self.Kaydet.setText(_translate("MainWindow", "Kaydet"))

        

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())