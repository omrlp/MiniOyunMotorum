
import string
from unicodedata import name

karakterler = []
esyalar = []

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
            
    def editorsecimi(self):
        print ("yapmak istiginiz islemi seçebilirsiniz: (1 - yeni karakter ekleme / 2 - karakter silme / 3 - yeni eşya ekleme / 4 - eşya silme)")
        
    def karakterekle(self):
        print ("Karakter ekleme moduna gectiniz.")
        karakter = input("Karakter adini giriniz: ")
        zırh = int(input("Karakterin zırh degerini giriniz: "))
        hasar = int(input("Karakterin hasar degerini giriniz: "))
        can = int(input("Karakterin can degerini giriniz: "))
        self.karakterler.append(CharacterFactory.create_character(karakter, zırh, hasar, can))
        
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
        self.esyalar.append(EsyaFactory.create_esya(esya))
        
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
    def __init__(self):
        pass
    def run(self):
        print ("PVP moduna gectiniz.")
    
class gameobjects:
    def __init__(self, name):
        self.name = name

class characters(gameobjects):
    def __init__(self, name, zırh, hasar, can):
        super().__init__(name)
        self.zırh = zırh
        self.hasar = hasar
        self.can = can
        
        
class Esyalar(gameobjects):
    def __init__(self, name):
        super().__init__(name)
     
class CharacterFactory:
    @staticmethod
    def create_character(name ,zırh, hasar, can):
        return characters(name, zırh, hasar, can)
     
class EsyaFactory:
    @staticmethod
    def create_esya(esya):
        return Esyalar(esya)  
     
     


oyun = game()     
karakterler.append(CharacterFactory.create_character("Sovalye", 3, 4, 30))
karakterler.append(CharacterFactory.create_character("Iblis", 1, 2, 45))
karakterler.append(CharacterFactory.create_character("Okcu", 0, 8, 20))
karakterler.append(CharacterFactory.create_character("Buyucu", 1, 6, 25))

print ("Oyuna Hosgeldiniz!")

oyun.menucalistir()

    