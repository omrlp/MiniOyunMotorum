 Nerede?
Bu örüntü projedeki oyun nesnelerinin ve karakterlerin üretim süreclerini soyutlamak adına projenin ana dizininde yer alan CharacterFactory ve EsyaFactory sınıflarında uygulanmıstır.

CharacterFactory.create_character(...) metodu, characters sınıfından yeni karakter nesneleri üretir.

EsyaFactory.create_esya(...) metodu, Esyalar sınıfından oyun içi eşyalar üretir.

İstemci kod olan game sınıfı (veya oyun başlangıcı), new mantığıyla doğrudan somut sınıfları çağırmak yerine nesneleri bu fabrikalardan ister.

 Neden?
Sorunum:: Örüntü uygulanmadan önce, eğer karakterlerin veya eşyaların nasıl oluşturulacağı, hangi varsayılan değerleri alacağı bilgisi doğrudan ana program akışına (game sınıfına veya oyunun yazıldığı yere) yazılsaydı, kodda sıkı bağımlılık olusacaktı. İleride yeni bir karakter türü eklemek veya nesne üretim mantığını değiştirmek istediğimizde, oyunun akıs kodunu da değistirmek zorunda kalacaktık (ki bu da Open/Closed Prensibi ihlali olmus olurdu).

Seçim Nedeni: Nesne üretme sorumluluğunu tamamen istemci sınıftan koparmak, üretimi tek bir merkezde yani fabrikada toplamak ve gelecekte oyuna yeni nesne tipleri eklendiğimde ana oyun motorunun koduna dokunmadan sistemi genişletebilmek için bu örüntüyü seçtim.

 Ne Kazandınız?
Gevşek Bağlılık (Esneklik): Oyun motoru (game) ve editor modları nesnelerin tam olarak arka planda nasıl inşa edildiğinin detaylarını bilmek zorunda kalmiyor. Sadece fabrikaya emir verip ve nesneyi teslim aliyor.

Kolay Genişletilebilirlik: İleride yeni bir karakter tipi veya eşya özelliği eklendiğimde değişiklik yapılacak tek yer ilgili Factory sınıfı olacak. Mevcut çalışan menu ve editor kodları bu değişiklikten etkilenmiyor.

Kod Tekrarının Önlenmesi: Oyunun başlangıcında veya gamemodeEditor içinde dinamik karakter eklenirken, karakter oluşturma mantığı tek bir çatı altında standartlastırılmıs oluyor.

Bakim: tek yerde toplandığı için bakım yapılması kolaylaşmış olacak.