import time
import random

class MeyveSuyuOtomati:
    def init(self):
        self.otomat_status = "Kapalı"
        self.meyvesuyu_menusu = {"Elma Suyu": 3.50, "Portakal Suyu": 3.50, "Çilek Suyu": 3.50, "Nar Suyu": 3.50, "Şeftali Suyu": 3.50}
        self.hesaba_eklenen_meyvesuyu = []
        self.hesap_tutari = 0
        print(self.meyvesuyu_menusu.keys())

    def otomat_ac(self):
        if self.otomat_status == "Açık":
            print("Otomat zaten açık...")
        else:
            print("Otomat açılıyor...")
            time.sleep(1)
            self.otomat_status = "Açık"
            print("Otomat açıldı...")

    def otomat_kapat(self):
        if self.otomat_status == "Kapalı":
            print("Otomat zaten kapalı...")
        else:
            print("Otomat kapanıyor")
            time.sleep(1)
            self.otomat_status = "Kapalı"
            print("Otomat kapandı...")

    def menu_goruntuleme(self):
        print("---- MEYVE SUYU MENUSU ---- ")
        meyvesuyu_menusu1 = self.meyvesuyu_menusu
        for x, y in meyvesuyu_menusu1.items():
            print("Meyve Suyu Cesidi:", x, "Kucuk Boy Fiyatı:", y, "TL")
        print()
        print("Orta boy 7 TL  \nBuyuk boy 12 TL")

    def cesit_boyut_secimi(self):
        print("---- MEYVE SUYU MENUSU ---- ")
        for(x, y) in self.meyvesuyu_menusu.items():
            print("Meyve Suyu Cesidi:", x, "Kucuk Boy Fiyatı:", y, "TL")
        print()
        
        secilen_meyvesuyu = input("Lutfen istediginiz meyve suyu cesidini giriniz: ")
        
        self.hesaba_eklenen_meyvesuyu.append(secilen_meyvesuyu)
        
        boyut_secimi = input("Lutfen boyut(kucuk/ orta/ buyuk) seciniz: ")
        
        if boyut_secimi == "kucuk":
            self.hesap_tutari = self.meyvesuyu_menusu[secilen_meyvesuyu]
        
        elif boyut_secimi == "orta":
            self.hesap_tutari += 3.50 + self.meyvesuyu_menusu[secilen_meyvesuyu]
        
        elif boyut_secimi == "buyuk":
            self.hesap_tutari += 8.50 + self.meyvesuyu_menusu[secilen_meyvesuyu]

        print("Seciminiz: {}, {} boy, {} TL.".format(secilen_meyvesuyu, boyut_secimi, self.hesap_tutari))

    def bardak_sec(self):
        tercih = input("Geri donusturulebilir bardak icin a'ya plastik bardak icin b'ye basiniz.(Plastik bardak secimleri icin hesaba 5 Tl eklenir.)")

        if tercih == "a":
            print("Cevreyi koruma hassasiyetiniz icin tesekkur ederiz.")
        elif tercih == "b":
            print("Meyve suyunuz plastik bardakta hazirlaniyor.(+5 TL)")
            time.sleep(1)
            self.hesap_tutari +=5

    def fis_ciktisi(self):
        with open("hesap.txt", "a", encoding="utf-8") as file:
            file.write(str(time.ctime(time.time())))
            file.write(" \n ")
            file.write("Satın alınan meyve suyu: ")
            file.write(self.hesaba_eklenen_meyvesuyu[0])
            file.write(" \n ")
            file.write("Toplam tutar: ")
            file.write(str(self.hesap_tutari))
            file.write(" \n ")
        
        print("Fisiniz basariyla hazirlandi.")

    def karisik_meyvesuyu(self):
        print("Karisik Meyve Suyu Seçeneğini Seçtiniz...")
        print("Küçük Boy karisik meyve suyunuz hazirlaniyor...")
        print("Orta Boy kariisk meyve suyunuz hazirlaniyor...")
        print("Büyük Boy kariisk meyve suyunuz hazirlaniyor...")
        time.sleep(1)
        rastgele = random.choice(list(self.meyvesuyu_menusu))
        self.hesaba_eklenen_meyvesuyu.append(rastgele)
        self.hesap_tutari += self.meyvesuyu_menusu[rastgele]
        print("Karisik meyve suyunuz {} oldu... Afiyet olsun <3...".format(rastgele))

    def menuye_meyvesuyu_ekle(self):
        print("---- MEYVE SUYU MENUSU ----")
        for (x, y) in self.meyvesuyu_menusu.items():
            print("Meyve Suyu İsmi:", x, "----- Küçük Boy Fiyati:", y, "TL")
        print()
        eklenecek_meyvesuyu_ismi = input("Lütfen eklemek istediğiniz meyve suyunun ismini giriniz: ")
        eklenecek_meyvesuyu_fiyati = float(input("Lütfen eklemek istediğiniz meyve suyunun küçük boy fiyatini giriniz: "))
        self.meyvesuyu_menusu[eklenecek_meyvesuyu_ismi] = eklenecek_meyvesuyu_fiyati
        print("Meyve Suyu Menüsünün yeni hali: ")
        print("---- MEYVE SUYU MENÜSÜ ----")
        for (x, y) in self.meyvesuyu_menusu.items():
            print("Meyve Suyu İsmi:", x, "---- Küçük Boy Fiyati:", y, "TL")
        print()

    def fiyat_guncellemesi(self):
        print("---- MEYVE SUYU MENÜSÜ ----")
        for(x, y) in self.meyvesuyu_menusu.items():
            print("Meyve Suyu İsmi:", x, "---- Küçük Boy Fiyati:", y, "TL")
        print()
        secim = str(input("Menüdeki meyvesularindan fiyatini güncellemek istediğinzin ismini giriniz: ")) 
        yeni_fiyat = float(input("{} için yeni fiyati giriniz: ".format(secim)))
        self.meyvesuyu_menusu[secim] = yeni_fiyat
        print()
        print("Meyve Suyu Menüsünün yeni hali: ")
        print("---- MEYVE SUYU MENÜSÜ ----")
        for (x, y) in self.meyvesuyu_menusu.items():
            print("Meyve Suyu İsmi:", x, "---- Küçük Boy Fiyati:", y, "TL")
        print()

    def otomat_durumu(self):
        print("Otomat Durumu: {}".format(self.otomat_status))

otomat = MeyveSuyuOtomati()
otomat.init()

while(True):
    print("""
    *******************************************
    * ...Meyve Suyu Otomatına Hoş Geldiniz... *
    *                                         *
    * Otomatı Aç ...........................1 *
    * Otomatı Kapat.........................2 *
    * Menüyü Görüntüle......................3 *
    * Meyve Suyu ve Boyut Seç...............4 *
    * Bardak Seç............................5 *
    * Fişini Al.............................6 *
    * Meyve Suyu Eklemesi Yap...............7 *
    * Fiyat Güncellemesi Yap................8 *
    * Otomattan Çık.........................9 *
    * Otomat Durumu........................10 *
    *******************************************""")
    secim = input("Yapmak istediğiniz seçimi tuşlayınız: ")
    try:
        if secim == "1":
            otomat.otomat_ac()
        elif secim == "2":
            otomat.otomat_kapat()
        elif secim == "3":
            otomat.menu_goruntuleme()
        elif secim == "4":
            otomat.cesit_boyut_secimi()
        elif secim == "5":
            otomat.bardak_sec()
        elif secim == "6":
            otomat.fis_ciktisi()
        elif secim == "7":
            otomat.menuye_meyvesuyu_ekle()
        elif secim == "8":
            otomat.fiyat_guncellemesi()
        elif secim == "9":
            print("Otomat kapatılıyor... Teşekkür ederiz. Yine bekleriz :)")
            break
        elif secim == "10":
            otomat.otomat_durumu()
    except:
        print("Bir hata oluştu!")
