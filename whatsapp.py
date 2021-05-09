
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from os import system
import datetime
from selenium import webdriver
import time
import threading


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(746, 648)
        MainWindow.setMaximumSize(746, 648)
        MainWindow.setMinimumSize(746, 648)
        MainWindow.setWindowIcon(QtGui.QIcon("images/chatbot_thumb.ico"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lineedit_isim = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_isim.setGeometry(QtCore.QRect(300, 320, 161, 31))
        self.lineedit_isim.setObjectName("lineedit_isim")

        self.label_wp_ismi = QtWidgets.QLabel(self.centralwidget)
        self.label_wp_ismi.setGeometry(QtCore.QRect(115, 320, 180, 31))
        self.label_wp_ismi.setObjectName("label_wp_ismi")
        self.label_wp_ismi.setStyleSheet("color : black;""border-radius:5px;""border-style:outset;""border-width:1px;""border-color:blue;""font:bold 15px;")

        self.buton_dinle = QtWidgets.QPushButton(self.centralwidget)
        self.buton_dinle.setGeometry(QtCore.QRect(320, 360, 121, 41))
        self.buton_dinle.setObjectName("buton_dinle")
        self.buton_dinle.setStyleSheet("border-radius:5px;""border-style:outset;""border-width:1px;""border-color:blue;""font:bold 12px;")
        self.buton_dinle.clicked.connect(self.calistir)

        self.buton_goster = QtWidgets.QPushButton(self.centralwidget)
        self.buton_goster.setGeometry(QtCore.QRect(270, 415, 91, 31))
        self.buton_goster.setObjectName("buton_goster")
        self.buton_goster.clicked.connect(self.goster_fonk)


        self.buton_temizle = QtWidgets.QPushButton(self.centralwidget)
        self.buton_temizle.setGeometry(QtCore.QRect(400, 415, 91, 31))
        self.buton_temizle.setObjectName("buton_temizle")
        self.buton_temizle.clicked.connect(self.temizle)
        

        self.foto_wallpaper = QtWidgets.QLabel(self.centralwidget)
        self.foto_wallpaper.setGeometry(QtCore.QRect(0, 0, 841, 631))
        self.foto_wallpaper.setText("")
        self.foto_wallpaper.setPixmap(QtGui.QPixmap("images/npreview_1280x1280.jpg"))
        self.foto_wallpaper.setObjectName("foto_wallpaper")

        self.foto_icon = QtWidgets.QLabel(self.centralwidget)
        self.foto_icon.setGeometry(QtCore.QRect(130, 0, 521, 321))
        self.foto_icon.setText("")
        self.foto_icon.setPixmap(QtGui.QPixmap("images/chatbot_thumb-removebg-preview.png"))
        self.foto_icon.setObjectName("foto_icon")

        self.combobox=QtWidgets.QComboBox(self.centralwidget)
        self.combobox.setObjectName("eth0combo")
        self.combobox.setGeometry(QRect(315, 460, 135, 35))
        self.combobox.addItem("Web Tarayıcısı")
        self.combobox.addItem("Google Chrome")
        self.combobox.addItem("Mozilla Firefox")
        self.combobox.setStyleSheet("color : black;""border-radius:5px;""border-style:outset;""border-width:1px;""border-color:blue;""font:bold 14px;")

        self.label_liscance = QtWidgets.QLabel(self.centralwidget)
        self.label_liscance.setGeometry(QtCore.QRect(480, 540, 331, 71))
        self.label_liscance.setObjectName("label_liscance")
        self.label_liscance.setStyleSheet("color:black;")
########################################---------Menubar and Raise-----########################################
        self.foto_wallpaper.raise_()
        self.lineedit_isim.raise_()
        self.label_wp_ismi.raise_()
        self.buton_dinle.raise_()
        self.buton_goster.raise_()
        self.buton_temizle.raise_()
        self.foto_icon.raise_()
        self.combobox.raise_()
        self.label_liscance.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setStyleSheet("border-radius:5px;""border-style:outset;""font:bold 15px;")
        self.menubar.setGeometry(QtCore.QRect(0, 0, 746, 21))
        self.menubar.setObjectName("menubar")

        self.menuNas_l_Kullan_l_r = QtWidgets.QMenu(self.menubar)
        self.menuNas_l_Kullan_l_r.setObjectName("menuNas_l_Kullan_l_r")
        self.menuNas_l_Kullan_l_r.triggered.connect(self.help_fnc_th)

        self.menuYap_mc = QtWidgets.QMenu(self.menubar)
        self.menuYap_mc.setObjectName("menuYap_mc")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBilgilendirme_Men_s = QtWidgets.QAction(MainWindow)
        self.actionBilgilendirme_Men_s.setObjectName("actionBilgilendirme_Men_s")
        self.actionberkay = QtWidgets.QAction(MainWindow)
        self.actionberkay.setObjectName("actionberkay")
        self.actionberkay.triggered.connect(self.yapimci_fonk_th)
        self.menuNas_l_Kullan_l_r.addAction(self.actionBilgilendirme_Men_s)
        self.menuYap_mc.addAction(self.actionberkay)
        self.menubar.addAction(self.menuNas_l_Kullan_l_r.menuAction())
        self.menubar.addAction(self.menuYap_mc.menuAction())
       
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
########################################---------Functions-----########################################   
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Whatsapp Bot v1.4"))
        self.lineedit_isim.setPlaceholderText(_translate("MainWindow", "Whatsappta kayıtlı olduğu isim"))
        self.label_wp_ismi.setText(_translate("MainWindow", "Kişinin Whatsapp ismi"))
        self.buton_dinle.setText(_translate("MainWindow", "Sessizce Dinle"))
        self.buton_goster.setText(_translate("MainWindow", "Sonuçları Göster"))
        self.buton_temizle.setText(_translate("MainWindow", "Sonuçları Temizle"))
        self.label_liscance.setText(_translate("MainWindow", "<html><head/><body><p>Whatsapp Bot v1.4 Distributed under the MIT License.<br>See LICENSE for more information.<br>Copyright (c) 2021</p></body></html>"))
        self.menuNas_l_Kullan_l_r.setTitle(_translate("MainWindow", "Nasıl Kullanılır"))
        self.menuYap_mc.setTitle(_translate("MainWindow", "Yapımcı"))
        self.actionBilgilendirme_Men_s.setText(_translate("MainWindow", "Bilgilendirme Menüsü"))
        self.actionberkay.setText(_translate("MainWindow", "Berkay Şen"))
    def temizle(self):
        system("del sonuclar.txt")
        system("type nul > sonuclar.txt")
    def goster_fonk(self): 
        system("start sonuclar.txt")
    def calistir(self,threadName):
        isimm=self.lineedit_isim.text()
        combo=self.combobox.currentText()
        def dinle_fonk(self,isimm,combo):
            if(isimm==""):
                msg3 = QMessageBox()
                msg3.setWindowTitle("Bilgilendirme kutusu")
                msg3.setBaseSize(300,300)
                msg3.setIcon(QMessageBox.Warning)
                msg3.setText("Takip edilmesi gereken kişinin rehberinizde kayıtlı olduğu ismini giriniz.")
                msg3.exec_()
            elif(combo=="Web Tarayıcısı"):
                msg3 = QMessageBox()
                msg3.setWindowTitle("Bilgilendirme kutusu")
                msg3.setBaseSize(300,300)
                msg3.setIcon(QMessageBox.Warning)
                msg3.setText("Öncelikle tarayıcı Seçmeniz gerekmektedir.")
                msg3.exec_()
            elif(combo=="Mozilla Firefox"):
                msg3 = QMessageBox()
                msg3.setWindowTitle("Bilgilendirme kutusu")
                msg3.setBaseSize(300,300)
                msg3.setIcon(QMessageBox.Information)
                msg3.setText("Program Yanıt Vermiyor Olarak Gözükebilir.Programı altta açık bırakıp kendi işlerinize devam edebilirsiniz.")
                msg3.exec_()
                path="geckodriver.exe"
                driver =webdriver.Firefox(executable_path=path)
                driver.get('https://web.whatsapp.com/')
                kontrol=True
                kontrol2=True
                kontrol3=False
                while True:
                    try:
                        tikla=driver.find_element_by_xpath("//span[text()='{}']".format(isimm))
                        tikla.click()
                        time.sleep(1)
                    except:
                        pass
                    try:
                        driver.find_element_by_xpath("//span[text()='çevrimiçi']")
                        if kontrol==True:
                            zaman=datetime.datetime.now()
                            zaman= str(zaman)
                            zaman=zaman.replace(":",".")
                            zaman=zaman[:16]
                            baslangic= time.time()
                            kontrol=False
                            kontrol2=True
                            kontrol3=True
                            file =open("sonuclar.txt", "a") 
                            file.write("Giris tarihi: "+zaman+"\n")
                            file.close()
                    except:
                        kontrol=True
                        if kontrol2==True:
                            zaman1=datetime.datetime.now()
                            zaman1= str(zaman1)
                            zaman1=zaman1.replace(":",".")
                            msg="Bu saatte kisi whatsapptan cikmistir efendim; "
                            msg=msg + zaman1
                            kontrol2=False
            elif(combo=="Google Chrome"):
                msg3 = QMessageBox()
                msg3.setWindowTitle("Bilgilendirme kutusu")
                msg3.setBaseSize(300,300)
                msg3.setIcon(QMessageBox.Information)
                msg3.setText("Program Yanıt Vermiyor Olarak Gözükebilir.Programı altta açık bırakıp kendi işlerinize devam edebilirsiniz.")
                msg3.exec_()
                path="chromedriver.exe"
                driver =webdriver.Chrome(executable_path=path)
                driver.get('https://web.whatsapp.com/')
                kontrol=True
                kontrol2=True
                kontrol3=False
                while True:
                    try:
                        tikla=driver.find_element_by_xpath("//span[text()='{}']".format(isimm))
                        tikla.click()
                        time.sleep(1)
                    except:
                        pass
                    try:
                        driver.find_element_by_xpath("//span[text()='çevrimiçi']")
                        if kontrol==True:
                            zaman=datetime.datetime.now()
                            zaman= str(zaman)
                            zaman=zaman.replace(":",".")
                            zaman=zaman[:16]
                            baslangic= time.time()
                            kontrol=False
                            kontrol2=True
                            kontrol3=True
                            file =open("sonuclar.txt", "a") 
                            file.write("Giris tarihi: "+zaman+"\n")
                            file.close()
                    except:
                        kontrol=True
                        if kontrol2==True:
                            zaman1=datetime.datetime.now()
                            zaman1= str(zaman1)
                            zaman1=zaman1.replace(":",".")
                            msg="Bu saatte kisi whatsapptan cikmistir efendim; "
                            msg=msg + zaman1
                            kontrol2=False
        t1 = threading.Thread(target=dinle_fonk, args = ("thread-1",isimm,combo))
        t1.start()
    def help_fnc_th(self,threadName):
        def help_fonk(self):
            msg3 = QMessageBox()
            msg3.setWindowTitle("Bilgilendirme kutusu")
            msg3.setBaseSize(300,300)
            msg3.setIcon(QMessageBox.Information)
            msg3.setText("""
            1-)Kişinin rehberinizde kayıtlı olan ismini yazdıktan sonra 'Sessizce Dinle' Butonuna basınız.
            2-)Chrome veya Mozilla Firefox Tarayıcınız açılacaktır.Direkt otomatik olarak whatsappweb sitesine yönlendirileceksiniz.
            3-)Sonrasında QR kodu okutup web tarayıcınızı aşağıya alınız.
            4-)Kişi giriş yaptığında bilgilendirme kutusu çıkacaktır ve giriş saatleri text dosyasına kaydedilecektir.'Sonuçları Göster' butonuna basıp görebilirsiniz.
            5-)İyi eğlenceler dilerim ;) -BERKAY ŞEN
            """)    
            msg3.exec_() 
        t3 = threading.Thread(target=help_fonk, args = ("thread-3",))
        t3.start()
    def yapimci_fonk_th(self):
        def yapimci_fonk(self):
            msg3 = QMessageBox()
            msg3.setWindowTitle("Bilgilendirme kutusu")
            msg3.setBaseSize(300,300)
            msg3.setIcon(QMessageBox.Information)
            msg3.setText("""
            Yazılımcı : Berkay Şen

            iletişim: brktrl@protonmail.ch
            Tüm Hakları saklıdır.Brktrl Copyright (c) 2021
            """)
            msg3.exec_()
        t4 = threading.Thread(target=yapimci_fonk, args = ("thread-4",))
        t4.start()
########################################---------Functions-----########################################

def ad(self):
    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        file=open("qss/Diffnes.qss","r")
        with file:
            qss=file.read()
            app.setStyleSheet(qss)
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

t2 = threading.Thread(target=ad, args = ("thread-2", ))
t2.start()

