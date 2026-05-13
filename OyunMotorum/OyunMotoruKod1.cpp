#include <iostream>
#include <string>

using namespace std;

class gameMenu // esnek olmasý için menuleri class olarak tanýmlamak istedim. bu sayede yeni eklemelerde iþler cok daha olay ilerleyebilir.
{
	int menu_secimi()
	{
		int sayi = 1;
		while (sayi <= 0 && sayi >= 3)// amacým sayý kontrolu yaparak yanlýs durumlarda tekrar sayý gýrýlmesýný saglamaktý.
		{
            cout << "Girmek istediginiz menuyu seciniz : ";
			cin >> sayi;
			return sayi;
		}
			
	}
}
;

class gameObjects //tum objeler guncellenebilir olacagý için interface e updateable fonksiynu tanýmladým
{
	virtual void updateable() = 0;
	virtual ~gameObjects() {}// bunu bellek sýzýntýsý icin yazdým
};

class Characters : public gameObjects {//burada abstract class yoluyla karakterlerimin özellikleri için methodlar tanýmlýyorum
public:
	string character;
	int zýrh;
	double hasar;
	double can;
	void character_zýrh() = 0;
	void character_hasar() = 0;
	void character_can() = 0;

	Characters(string character, int zýrh, double hasar, double can);
};

class Esyalar: gameObjects {
	string character;
	void ozellikler() = 0;
};

int main()
{
	Characters("Sovalye", 3, 4, 30);
	Characters("Iblis", 1, 2, 45);
	Characters("Okcu", 0, 8, 20);
	Characters("Buyucu", 1, 6, 25);
	int counter = 4;

	GameObjects()
	cout << "Oyuna Hosgeldiniz!";
	int menu =	menu_secimi();

	if (menu == 1)// pvp için yaptým
	{
		cout << " 1 numaralý oyuncu karakterini seçebilir:"


    }
	else if (menu == 2)// editor modu içinyaptým
	{
		cout << "yapmak istiginiz islemi seçebilirsiniz: (1 - yeni karakter ekleme / 2 - karakter silme / 3 - yeni eþya ekleme / 4 - eþya silme)"
	}
	

}
