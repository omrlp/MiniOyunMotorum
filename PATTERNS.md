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

Önceki bağımlı ve sıkı yapı:::
![Önceki Yapı](docs/diagrams/Once Diyagrami.drawio.png) 

Sonraki düzeltilmiş ve daha esnek yapı:::
![Sonraki Yapı](docs/diagrams/Sonra Diyagrami.drawio.png)

FAZ 2 için::: 
İKİ farklı decorator öruntusu kullandım
`characterdecorator` ve `esyadecorator` sınıflarında uygulandı.

secme sebebim:  Editörden eklenecek olan dinamik eşya bonuslarının (Can İksiri, Demir tuy vb.) karakterlerin statlarına sadece o vurus anında (gecici olarak) etki etmesi savaş bittiğinde karakter nesnesinin orijinal haline sadık kalması için seçtım

bana yararı : Her yeni eşya için koda elle yeni bir alt sınıf yazma zorunluluğunu (Sınıf Patlamasını) engellemıs oldu. + olarak can ve zırh formullerını bırbırıne bagladıgımda da bunu cok daha rahat çevirmiş olacagım.
![Sonraki Yapı](docs/diagrams/Sonra Diyagrami2.drawio.png)

guncel olarak esyadecorator classımı sılıp bunun yerıne command oruntusu kullanma kararı aldım. cunku decorator oruntum malesef tum esyalara aynı sarma ıslemlerını yapıyordu ve tek tek ayrı fonksıyonlar kurmam gereklıydı kı bu hıc dınamık olmayacktı. bu yuzden ABC command kullandıgım 'etkilesim' adında bır kod yazdım. ki bu isimizi cok daha esnek ve dınamıklıge uygun hale getırebıldı.
![Sonraki Yapı](docs/diagrams/Sonra Diyagrami3.drawio.png)


EVET kodumu hemen hemen bıtırmısım gıbı hıssedıyorum sahsen. bır cok farklı pattern kullandım ve solide uygun oldugunu dusunuyorum. ve tabi hala ai log phase3.md asamasını yapmadım. ama şimdi patternlerimden tekrar bahsederek sizi güncelleyecegım ve patterns.md dosyamızı tamamlamış olacagım. kullandıgım oruntulerı kısaca buraya sıralamam gerekirse :Observer (Gozlemci) öruntusu ,Factory Method (Fabrika),Strategy (Strateji) örüntüsü ,Registry (Kayıt Deposu) oruntusu kullandım.
Ve son olarak uzucu bır sekılde characterdecoratore veda ediyoruz. Aslında kesınlıkle işime yarayacagını dusunerek yazmıstım ama kenarda dururken onun gorevını zaten yapan bambaska kodlar devreye gırdı desem yeridir. karakter sec methodumda zaten gerekenı yapıyorum ve characterfactoryde de zaten uretımımı tamamıyoum. ustunu sarmak gıbı bır kaygım otomatıkmen ortadan kalkmıs oluyor. bu yuzden decoratoru kaldırdım ve hayalet gıbı kodumun ıcınde kalmasını ıstemedım.
![Sonraki Yapı](docs/diagrams/Sonra Diyagrami4.drawio.png)