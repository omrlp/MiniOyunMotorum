
import string
from unicodedata import name
from abc import ABC, abstractmethod

karakterler = []
esyalar = []

class gozlemci(ABC):
    def guncelle(self, mesaj):
        pass
    
class savasspikeri(gozlemci):
    def guncelle(self, mesaj):
        print(f"SPİKER: {mesaj}")
        
class saldırıstratejisi(ABC):
    def saldır(self, saldiran, savunan, spiker):
        pass
            
class normalsaldiri(saldırıstratejisi):
    def saldır(self, saldiran, savunan, spiker):
        spiker.guncelle(f"{saldiran.name} normal saldırı yapıyor...")
        savunan.hasaral(saldiran.hasar)
        
class kritiksaldiri(saldırıstratejisi):
    def saldır(self, saldiran, savunan, spiker):
        kritikhasar = saldiran.hasar * 2
        spiker.guncelle(f"{saldiran.name} kritik saldırı yapıyor! Hasar: {kritikhasar}")
        savunan.hasaral(kritikhasar)  
        
class cancalmasaldiri(saldırıstratejisi):
    def saldır(self, saldiran, savunan, spiker):
        cancalma = int(saldiran.hasar * 0.5)
        spiker.guncelle(f"{saldiran.name} can çalma saldırısı yapıyor! Hasar: {saldiran.hasar}, Can Çalma: {cancalma}")
        savunan.hasaral(saldiran.hasar)
        saldiran.can += cancalma
        spiker.guncelle(f"{saldiran.name} {cancalma} can çaldı! Güncel can: {saldiran.can}")                         

class etkilesim(ABC):
    def uygula(self, kullanan, hedef):
        pass
    
class esyaetkisi(etkilesim):
    def __init__(self, kime, etken , miktar):
        self.kime = kime
        self.etken = etken
        self.miktar = miktar
    
    def uygula(self, kullanan, hedef):
        hedefkarakter = kullanan if self.kime == "kendi" else hedef
        mevcutdeger = getattr(hedefkarakter, self.etken)    
        yenideger = mevcutdeger + self.miktar
        setattr(hedefkarakter, self.etken, yenideger)
        
        durum = "artırıldı" if self.miktar > 0 else "azaltıldı"
        hedefisim = "kendi" if self.kime == "kendi" else "dusmanın"  
        print(f"{hedefisim} {self.etken} degeri {durum} ({mevcutdeger} -> {yenideger})")

class game:
    
    def __init__(self):
        self.menuler = {1:{"isim": "Cikis", "class": None} , 2: {"isim": "Editor", "class": gamemodeEditor()}, 3: {"isim": "PVP", "class": gamemodePVP()}}

    def exitgame(self):
        print ("Oyundan cikiliyor...")
        exit()    
     
    def menusecimi(self):
        print("Lütfen bir menü seçeneği belirleyin: (1 - Cikis / 2 - Editor / 3 - PVP )")
        secim = input("Seciminizi giriniz: ")
        return int(secim)
        
    def menucalistir(self):
        while True:
            secim = self.menusecimi()
            
            if secim == 1:
                self.exitgame()
                
            secilenmode = self.menuler.get(secim)
            
            if secilenmode and secilenmode["class"] :
                secilenmode["class"].run()
            else:
                print("Gecersiz secim, lutfen tekrar deneyin.")
class gamemodeEditor:
    def __init__(self):
        pass
    
    def run(self):
        self.editorsecimi()
        secim = input("Seciminizi giriniz: ")
        if secim == "1":
            self.karakterekle()
        if secim == "2":
            self.karaktersil()    
        if secim == "3":
            self.esyaekle()
        if secim == "4":
            self.esyasil()
            
    def editorsecimi(self):
        print ("yapmak istiginiz islemi seçebilirsiniz: (1 - yeni karakter ekleme / 2 - karakter silme / 3 - yeni eşya ekleme / 4 - eşya silme)")
        
    def karakterekle(self):
        print ("Karakter ekleme moduna gectiniz.")
        karakter = input("Karakter adini giriniz: ")
        zırh = int(input("Karakterin zırh degerini giriniz: "))
        hasar = int(input("Karakterin hasar degerini giriniz: "))
        can = int(input("Karakterin can degerini giriniz: "))
        
        print("Strateji secimi: (1 - Normal / 2 - Kritik / 3 - Can Çalma)")
        stratejisecimi = input("Strateji numarasini giriniz: ")
        stratejiharitası = {"1": "Normal", "2": "Kritik", "3": "Can Çalma"}
        strateji = stratejiharitası.get(stratejisecimi, "Normal")

        karakterler.append(CharacterFactory.create_character(karakter, zırh, hasar, can, strateji))
    
    def karaktersil(self):    
        print ("Karakter silme moduna gectiniz.")
        for i, karakter in enumerate(karakterler):
            print(f"{i + 1}. {karakter.name}")
        secim = int(input("Silmek istediginiz karakterin numarasini giriniz: "))
        if 0 < secim <= len(karakterler):
            del karakterler[secim - 1]
            print("Karakter silindi.")
        else:
            print("Gecersiz secim.")
            
    def esyaekle(self):
        print ("Esya ekleme moduna gectiniz.")
        esya = input("Eklemek istediginiz esyanin adini giriniz: ")
        yeniesya = EsyaFactory.create_esya(esya)
        
        while True:
            etki = input("Esya etkisi eklemek istiyor musunuz? (E/H): ")
            if etki.lower() == 'e':
                kime = input("Etki kime uygulanacak? (kendi/dusman): ")
                etken = input("Hangi ozellik etkileniyor? (zırh/hasar/can): ")
                miktar = int(input("Etki miktarini giriniz (pozitif veya negatif): "))
                yenietki = esyaetkisi(kime, etken, miktar)
                yeniesya.etkiekle(yenietki)
            elif etki.lower() == 'h':
                break
            else:
                print("Gecersiz secim, lutfen tekrar deneyin.")
        esyalar.append(yeniesya)      
        
        
    def esyasil(self):
        print ("Esya silme moduna gectiniz.")
        for i, esya in enumerate(esyalar):
            print(f"{i + 1}. {esya.name}")
        secim = int(input("Silmek istediginiz esyanin numarasini giriniz: "))
        if 0 < secim <= len(esyalar):
            del esyalar[secim - 1]
            print("Esya silindi.")
        else:
            print("Gecersiz secim.")                
        
        
class gamemodePVP:
    def __init__(self,esyalimit=2):
        self.esyalimit = esyalimit
        self.hazirsavasesyalari = []
        
    def run(self):
        print ("PVP moduna Hoşgeldiniz.")
        
        if len(karakterler) < 2:
            print("Savaşabilmek için sistemde en az 2 karakter olmalı! Lütfen önce Editör'den ekleyin.")
            return
        if not esyalar:
            print("Savaşabilmek için sistemde en az 1 eşya olmalı! Lütfen önce Editör'den ekleyin.")
            return
        self.savasikur()
        
    def savasikur(self):
        print("-----1. OYUNCU KARAKTER SEÇİMİ-----")
        player1 = self.karaktersec()
        self.esyasec(player1)
        print("-----2. OYUNCU KARAKTER SEÇİMİ-----")
        player2 = self.karaktersec()
        self.esyasec(player2)
        
        spiker = savasspikeri()
        player1.spikerekle(spiker)
        player2.spikerekle(spiker)
        
        self.Arena(player1, player2)

    def karaktersec(self):
        for i, karakter in enumerate(karakterler):
            print(f"{i + 1}. {karakter.name} (Zırh: {karakter.zırh}, Hasar: {karakter.hasar}, Can: {karakter.can})")
        secim = int(input("Karakter numarasını giriniz: "))
        stratejisozlugu = {"Normal": normalsaldiri(), "Kritik": kritiksaldiri(), "Can Çalma": cancalmasaldiri()}
        secilenstrateji = stratejisozlugu.get(karakterler[secim - 1].stratejiadı, normalsaldiri())
        
        if 0 < secim <= len(karakterler):
            return savaskarakteri(karakterler[secim - 1], secilenstrateji)
        else:
            print("Geçersiz seçim, varsayılan olarak ilk karakter seçildi.")
            return savaskarakteri(karakterler[0], secilenstrateji)
        
    def esyasec(self, oyuncu):
        print(f"{oyuncu.name} için eşya seçim hakkı sayınız: {self.esyalimit} adet")
        for i in range(self.esyalimit):
            print("Mevcut eşyalar:")
            for j, esya in enumerate(esyalar):
                print(f"{j + 1}. {esya.name}")
            secim = int(input("Eşya numarasını giriniz (seçim yapmazsanız 0): "))
            if secim == 0:
                break   
            if 0 < secim <= len(esyalar):
                oyuncu.envanter.append(esyalar[secim - 1])   
        print(f"{oyuncu.name} envanteri hazırlandı.")
        
    def turoyna(self, saldiran, savunan):
        print(f"\n[{saldiran.name} turu!] (can durumu: {saldiran.can} / hasar durumu: {saldiran.hasar})")
        if saldiran.envanter:
            print("Envanterinizdeki eşyalar:")
            for i, esya in enumerate(saldiran.envanter):
                print(f"{i + 1}. {esya.name}")
            secim = int(input("Kullanmak istediğiniz eşya numarasını giriniz (kullanmazsanız 0): "))
            if 0 < secim <= len(saldiran.envanter):
                secilen_esya = saldiran.envanter.pop(secim - 1)
                secilen_esya.etkileriuygula(saldiran, savunan)
        if savunan.can > 0:
            spikernesnesi = saldiran.spikerler[0] if saldiran.spikerler else savasspikeri()
            saldiran.strateji.saldır(saldiran, savunan, spikernesnesi)
        
    def Arena(self,p1,p2):
        print(f"\n╔══════════════════════════════════════════╗")
        print(f"║              {p1.name} VS {p2.name}              ║")
        print(f"╚══════════════════════════════════════════╝")
        tur=1;
        while p1.can > 0 and p2.can > 0:
            self.turoyna(p1, p2)
            if p2.can <= 0:
                print(f"\n{p2.name} yenildi (Y-Y) ! KAZANAN : {p1.name} (^O^) !")
                break
            self.turoyna(p2, p1)
            if p1.can <= 0:
                print(f"\n{p1.name} yenildi (Y-Y) ! KAZANAN : {p2.name} (^O^) !")
                break
            tur +=1
        print ("\nSavaş sona erdi. Teşekkürler!")
    

class savaskarakteri:
    def __init__(self, karakter, strateji):
        self.karakter = karakter
        self.name = karakter.name
        self.zırh = karakter.zırh
        self.can = karakter.can + (karakter.zırh * 10)
        self.hasar = karakter.hasar
        self.envanter = []
        self.spikerler = []
        self.strateji = strateji
        
    def spikerekle(self, spiker):
        self.spikerler.append(spiker)
        
    def hasaral(self, miktar):
        self.can -= miktar
        for spiker in self.spikerler:
            spiker.guncelle(f"{self.name} {miktar} hasar aldı! Kalan can: {self.can}")        

class characterdecorator(object):
    def __init__(self, karakter):
        self._karakter = karakter
    
    @property    
    def name(self):
        return self._karakter.name   
    @property
    def zırh(self):
        return self._karakter.zırh
    @property
    def hasar(self):
        return self._karakter.hasar
    @property
    def can(self):
        return self._karakter.can
    @can.setter
    def can(self, value):
        self._karakter.can = value  
        

    
class gameobjects:
    def __init__(self, name):
        self.name = name

class characters(gameobjects):
    def __init__(self, name, zırh, hasar, can,stratejiadı = "Normal"):
        super().__init__(name)
        self.zırh = zırh
        self.hasar = hasar
        self.can = can
        self.stratejiadı = stratejiadı
                
class Esyalar(gameobjects):
    def __init__(self, name):
        super().__init__(name)
        self.etkiler = []   
        
    def etkiekle(self, etki):
        self.etkiler.append(etki)   
        
    def etkileriuygula(self, kullanan, hedef):
        print(f"[  ^o^  {kullanan.name} {self.name} isimli esyayi kullandi!]")
        for etki in self.etkiler:
            etki.uygula(kullanan, hedef)     
     
class CharacterFactory:
    @staticmethod
    def create_character(name ,zırh, hasar, can, stratejiadı = "Normal"):
        return characters(name, zırh, hasar, can, stratejiadı)
     
class EsyaFactory:
    @staticmethod
    def create_esya(esya):
        return Esyalar(esya)  
     

oyun = game()     
karakterler.append(CharacterFactory.create_character("Sovalye", 3, 4, 30, "Normal"))
karakterler.append(CharacterFactory.create_character("Iblis", 1, 2, 45, "Kritik"))
karakterler.append(CharacterFactory.create_character("Okcu", 0, 8, 20, "Normal"))
karakterler.append(CharacterFactory.create_character("Buyucu", 1, 6, 25, "Can Çalma"))
iksir = EsyaFactory.create_esya("Can İksiri")
iksir.etkiekle(esyaetkisi("kendi", "can", 5))
esyalar.append(iksir)
sopa = EsyaFactory.create_esya("Tanrının Sopası")
sopa.etkiekle(esyaetkisi("dusman", "can", -5))
esyalar.append(sopa)
tuy = EsyaFactory.create_esya("Demir Tüy")
tuy.etkiekle(esyaetkisi("kendi", "hasar", 2))
esyalar.append(tuy)
sise = EsyaFactory.create_esya("Saka Şisesi")
sise.etkiekle(esyaetkisi("kendi", "can", 12))
sise.etkiekle(esyaetkisi("kendi", "hasar", -1))
esyalar.append(sise)

print ("Oyuna Hosgeldiniz!")

oyun.menucalistir()

    