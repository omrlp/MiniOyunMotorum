#include <iostream> //ilk yazdığım başarısız kod burada:
#include <string>
class gameMenu // esnek olması için menuleri class olarak tanımlamak istedim. bu sayede yeni eklemelerde işler cok daha olay ilerleyebilir.
{
	int menu_secimi()
	{
		int sayi = 1;
		while (sayi <= 0 && sayi >= 3)// amacım sayı kontrolu yaparak yanlıs durumlarda tekrar sayı gırılmesını saglamaktı.
		{
            cout << "Girmek istediginiz menuyu seciniz : ";
			cin >> sayi;
			return sayi;
		}
			
	}
}
;

class gameObjects //tum objeler guncellenebilir olacagı için interface e updateable fonksiynu tanımladım
{
	void updateable() = 0;
};

class Characters : gameObjects {//burada abstract class yoluyla karakterlerimin özellikleri için methodlar tanımlıyorum
	string character;
	string enum irk = ("İnsanlar", "Rakunlar", "Ikıranlar"); // ırklar  İnsanlar ,Rakunlar ve Ikıranlar olarak 3e ayrılacak bır enum tanımlamam lazım dıye dusundum
	int zırh;
	double hasar;
	double can;
	void character_zırh() = 0;
	void character_hasar() = 0;
	void character_can() = 0;

	Characters(string character, int zırh, double hasar, double can);
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

	if (menu == 1)// pvp için yaptım
	{
		cout << " 1 numaralı oyuncu karakterini seçebilir:"


    }
	else if (menu == 2)// editor modu içinyaptım
	{
		cout << "yapmak istiginiz islemi seçebilirsiniz: (1 - yeni karakter ekleme / 2 - karakter silme / 3 - yeni eşya ekleme / 4 - eşya silme)"
	}
	

}

/* 
Fark ettiğim Hatalarım 

1-) öncelikle oldukça fazla yazım hatası var ::::, methodların ve claassların main içinde kullanımında yazım hataları var dongulerin ve classların kodlarında yazım hataları var.

2-) SOLİD e uygun degil inanilmaz katı bır yapısı var :::: en kolayından gamemode classının ıcıne yeni bir menü eklenmesı durumunda bır suru ıf ile değişiklik yapılması gerekecek bu bır felakete yol açacak .

3-)nesneler(en azından karakterler) elle manuel oluşturuluyor bu bence engellenmeli ve daha farklı bır yolu olmalı. ayrıca ounun basından berı olacak bu yuzden sınıflar ıcınde bu ıslemler halledılse daha guzel olurdu

4-)void character_zırh() = 0;
void character_hasar() = 0;
void character_can() = 0;
kodlarının acıklamaları yok ve main içinde her karakter için acıklamalarının yapılması mainin içini gereksiz şişirmiş olmayacak mı ?

5-) menü 2 için yazılmış bir class kodu yok aslında menulerin ayrı ınterfaceler ıcınde yer alması daha mantıklı olurdu cunku menu 1 oyunun kendısı olurken menu 2 editor gorevı gorecek yenı karakter ve esyalaee ekleme ve eski karakterleri silme gibi iki görevi olacak.bunu interface sorunu olarak görüyorum. spesifik olarak solidin arayüz ayrımı prensibine girdiğinden emin değilim.

AI fark ettiği hatalarım :
1. Teknik ve Yazılımsal Hatalar
Döngü Mantığı Hatası: while (sayi <= 0 && sayi >= 3) ifadesi matematiksel olarak imkansızdır. Bir sayı aynı anda hem 0'dan küçük hem de 3'ten büyük olamaz. Bu yüzden döngü hiç çalışmaz. Doğrusu || (veya) operatörü olmalıydı.

Namespace Eksikliği: std::cout ve std::cin yerine doğrudan cout yazmışsın. Ya başına std:: eklemeli ya da üst kısma using namespace std; yazmalısın.

Virtual Fonksiyon Hatası: C++'ta bir fonksiyonu "pure virtual" (arayüz) yapmak için virtual anahtar kelimesini kullanmalısın. Örn: virtual void updateable() = 0;.

Erişim Belirleyiciler (Access Specifiers): C++'ta class içindeki her şey varsayılan olarak private'tır. main içinden bu fonksiyonlara ulaşamazsın. public: etiketini eklemelisin.

Enum Tanımlama Hatası: string enum irk = ... şeklinde bir tanımlama C++'ta yoktur. enum kendi başına bir tiptir.

Noktalı Virgül ve Yazım Yanlışları: Bazı cout satırlarının sonunda ; eksik. Ayrıca main içinde GameObjects() şeklinde bir çağırma yapmışsın ama bu bir sınıf ismi, fonksiyon değil.


***(aslında bu bahsettiği tüm hatalar benim 1. maddede bahsettiğim yazım hatalarım)

2. Sert Kodlama (Hardcoding) Sorunu
Karakterleri main içinde tek tek elle oluşturuyorsun. Yarın 100 karakter eklemek istersen main fonksiyonun okunmaz hale gelir.
Çözüm: Factory (Fabrika) Tasarım Örüntüsü. Karakter üretimini bir "Factory" sınıfına devretmelisin.

***(tam olarak 3. maddede bahsettiğim sorun ele alınmısş)

3. Karmaşık Karakter Yapısı
Karakterlerin zırh, hasar gibi özellikleri doğrudan sınıf içinde ama bu özelliklerin hesaplanma mantığı (örneğin büyücü zırhı ile şövalye zırhı farkı) ileride karmaşaya yol açar.
Çözüm: Strategy (Strateji) Tasarım Örüntüsü. Farklı saldırı veya savunma tiplerini ayrı sınıflar olarak tanımlayıp karakterlere "enjekte" edebilirsin.

***(açıkçası bunu göze katmamıştım. bu yorum bence yeni bir bakış açısı oldu)


4. Menü Yönetimi
if-else bloklarıyla menü yönetmek, seçenekler arttıkça (3, 4, 10 seçenek...) kodu içinden çıkılmaz bir hale getirir.
Çözüm: Command (Komut) Tasarım Örüntüsü. Her menü seçeneğini bir komut nesnesi olarak tanımlarsan, yeni bir mod eklediğinde sadece yeni bir sınıf oluşturman yeterli olur.

***(bu durumu da 2. maddede söylemeye çalışmıştım)
*/
