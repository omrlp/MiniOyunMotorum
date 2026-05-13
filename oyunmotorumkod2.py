
import string
from unicodedata import name

class game:
    
    def __init__(self):
        self.karakterler = []
        self.esyalar = []
        self.menuler = {1: self.gamemodePVP, 2: self.gamemodeEditor, 3: self.exitgame}
 
  
    def exitgame(self):
        print ("Oyundan cikiliyor...")
        exit()    
     
    def menusecimi(self):
        print("Lütfen bir menü seçeneği belirleyin: (1 - PVP / 2 - Editor / 3 - Cikis)")
        secim = input("Seciminizi giriniz: ")
        return int(secim)
        
    
class gamemodeEditor:
    def __init__(self):
        pass
    def editorsecimi(self):
        print ("yapmak istiginiz islemi seçebilirsiniz: (1 - yeni karakter ekleme / 2 - karakter silme / 3 - yeni eşya ekleme / 4 - eşya silme)")
        
    def karakterekle(self):
        print ("Karakter ekleme moduna gectiniz.")
        karakter = input("Karakter adini giriniz: ")
        zırh = int(input("Karakterin zırh degerini giriniz: "))
        hasar = int(input("Karakterin hasar degerini giriniz: "))
        can = int(input("Karakterin can degerini giriniz: "))
        self.karakterler.append(CharacterFactory.create_character(karakter, zırh, hasar, can))
        
        
    
class gamemodePVP:
    def __init__(self):
        pass
    
class gameobjects:
    def __init__(self, name):
        self.name = name

class characters(gameobjects):
    def __init__(self, zırh, hasar, can):
        super().__init__(name)
        self.zırh = zırh
        self.hasar = hasar
        
        
class Esyalar(gameobjects):
    def __init__(self, name):
        super().__init__(name)
     
class CharacterFactory:
    @staticmethod
    def create_character(character, zırh, hasar, can):
        return characters(character, zırh, hasar, can)
     
class EsyaFactory:
    @staticmethod
    def create_esya(esya):
        return Esyalar(esya)  
     
     
motor = game()     
motor.karakterler.append(CharacterFactory.create_character("Sovalye", 3, 4, 30))
motor.karakterler.append(CharacterFactory.create_character("Iblis", 1, 2, 45))
motor.karakterler.append(CharacterFactory.create_character("Okcu", 0, 8, 20))
motor.karakterler.append(CharacterFactory.create_character("Buyucu", 1, 6, 25))

print ("Oyuna Hosgeldiniz!")

while True:
    secim =game.menusecimi()
      
    if secim in game.menuler:
        game.menuler[secim]()
    else:
        print("Gecersiz secim, lutfen tekrar deneyin.")    
    

#if (menu == 1) #pvp için yaptım
	#print (" 1 numaralı oyuncu karakterini seçebilir:")
  
#else if (menu == 2) #editor modu içinyaptım
	#print ("yapmak istiginiz islemi seçebilirsiniz: (1 - yeni karakter ekleme / 2 - karakter silme / 3 - yeni eşya ekleme / 4 - eşya silme)")