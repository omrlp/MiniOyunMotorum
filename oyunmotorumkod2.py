
import string

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
    def update(self):
        pass

class characters(gameobjects):
    def __init__(self, character, zırh, hasar, can):
        self.character = character
        self.zırh = zırh
        self.hasar = hasar
        self.can = can
        def character_zırh(self):
            pass
        def character_hasar(self):
            pass
        def character_can(self):
            pass
        
class Esyalar(gameObjects):
    def __init__(self, esya):
        self.esya = esya

    def ozellikler(self):
        pass
    def etkihasar(self):
        pass
    def etkican(self):
        pass
    def etkizırh(self):
        pass
     
class CharacterFactory:
    @staticmethod
    def create_character(character, zırh, hasar, can):
        return characters(character, zırh, hasar, can)
     
class EsyaFactory:
    @staticmethod
    def create_esya(esya):
        return Esyalar(esya)  

karakterler.append(CharacterFactory.create_character("Sovalye", 3, 4, 30))
karakterler.append(CharacterFactory.create_character("Iblis", 1, 2, 45))
karakterler.append(CharacterFactory.create_character("Okcu", 0, 8, 20))
karakterler.append(CharacterFactory.create_character("Buyucu", 1, 6, 25))

print ("Oyuna Hosgeldiniz!")

while True:
    menu =game.menusecimi()
      
    if secim in game.menuler:
        game.menuler[secim]()
    else:
        print("Gecersiz secim, lutfen tekrar deneyin.")    
    

#if (menu == 1) #pvp için yaptım
	#print (" 1 numaralı oyuncu karakterini seçebilir:")
  
#else if (menu == 2) #editor modu içinyaptım
	#print ("yapmak istiginiz islemi seçebilirsiniz: (1 - yeni karakter ekleme / 2 - karakter silme / 3 - yeni eşya ekleme / 4 - eşya silme)")