# BLM101_22360859064_FerideSaygiYalcinkaya
Öğrenci Bilgileri 


Ad Soyad:Feride Saygı Yalçınkaya


Öğrenci Numarası:22360859064


Grup: 5. Grup (Ağlar, İnternet ve HTML) 


Proje Konusu:

Ağlar, İnternet ve HTML: Python ile Otomatik HTML Sayfası Oluşturucu 

Bu proje, internetin temel çalışma mantığını (İstemci-Sunucu ilişkisi), WWW ve İnternet farkını ve markup dillerini (HTML/XML) ele alan 
teorik bir sunum ile Python kullanarak
dinamik bir HTML dosyası oluşturma uygulamasını kapsamaktadır.



Proje İçeriği ve Sunum:

Sunum Dosyası:  ...... 

YouTube Sunum Videosu: ........

Python Projesi: Otomatik HTML Oluşturucu 


Kodun Amacı ve Çalışma Mantığı:

Bu program, Python'un String (Dizgi) işleme ve Dosya Yazma (File Write) yeteneklerini kullanarak kullanıcıdan aldığı verileri
statik bir web sitesine dönüştürür.

Veri Toplama: Program konsol üzerinden kullanıcıya ad, dersler ve biyografi gibi sorular yöneltir.

HTML Yapılandırma: Alınan yanıtlar,HTML etiketleri arasına yerleştirilerek bir web sayfası iskeleti oluşturulur.

Stil Ekleme: Sayfanın görsel olarak daha iyi görünmesi için basit CSS renklendirmeleri koda dahil edilir.

Dosya Çıktısı: Program tüm bu verileri birleştirerek dizinde otomatik olarak bir index.html dosyası oluşturur.


Nasıl Çalıştırılır? 

1)Bilgisayarınızda Python yüklü olduğundan emin olun.

2)src/ klasörü altındaki .py uzantılı dosyayı çalıştırın.

3)Konsoldaki soruları yanıtlayın.

4)Aynı klasörde oluşan index.html dosyasını herhangi bir tarayıcıda açarak sonucu görüntüleyin.
Kod Açıklaması ve Algoritma Mantığı
Bu proje, Python programlama dilinin temel yeteneklerini kullanarak dinamik bir web içeriği (HTML) üretmek amacıyla geliştirilmiştir.



1. Kullanılan Teknolojiler ve Kütüphaneler

Python: Programın ana mantığı ve veri işleme süreçleri için kullanılmıştır.


Python Standart Kütüphanesi: Herhangi bir dış kütüphane kurulumuna gerek duyulmadan, yerleşik input() ve open() fonksiyonları kullanılmıştır.



HTML5 & CSS3: Çıktı dosyasının yapısı ve görsel tasarımı için tercih edilmiştir.


2. Algoritma ve Çalışma Mantığı
Programın çalışma süreci şu adımlardan oluşmaktadır:

Veri Girişi: input() fonksiyonu ile kullanıcıdan kişisel bilgiler ve ders listesi alınır.

Veri İşleme (Parsing): Kullanıcının virgülle ayırarak girdiği dersler, .split(",") metodu ile bir listeye dönüştürülür.
Ardından bir for döngüsü kullanılarak her ders HTML'deki <li> (liste elemanı) etiketleri arasına yerleştirilir.

Şablon Oluşturma: Python'daki f-string yapısı kullanılarak, kullanıcıdan alınan değişkenler önceden hazırlanmış HTML/CSS iskeletine dinamik olarak yerleştirilir.

Dosya Yazma (File Write): Hazırlanan string verisi, utf-8 kodlamasıyla index.html ismiyle yerel dizine kaydedilir.
Bu aşamada try-except bloğu kullanılarak olası dosya yazma hataları kontrol edilir.

3. Kodun Amacı
Bu uygulama, bir bilgisayar mühendisinin temel becerilerinden olan "veriyi işleme" ve "veriyi farklı bir formatta (HTML) sunma" mantığını kavramak için hazırlanmıştır
