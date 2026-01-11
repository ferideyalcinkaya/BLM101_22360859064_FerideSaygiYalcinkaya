# BLM101 - Bilgisayar Mühendisliğine Giriş Dönem Projesi

## 👤 Öğrenci Bilgileri
* **Adı Soyadı:** Feride Saygı Yalçınkaya
* **Öğrenci** Numarası: 22360859064
* **Bölüm:** Bilgisayar Mühendisliği

---

## 📚 Proje Konusu
**Grup 5: Ağlar, İnternet ve HTML**
Bu proje kapsamında; İnternet ve Web (WWW) arasındaki farklar, HTML/XML işaretleme dilleri ve İstemci-Sunucu ilişkisi incelenmiştir. Pratik uygulama olarak "Python ile Otomatik HTML Sayfası Oluşturucu" geliştirilmiştir.

---

## 🎥 Sunum ve Uygulama Videosu
Proje sunumuna ve kodun çalışma detaylarına aşağıdaki bağlantıdan ulaşabilirsiniz:

👉 https://www.youtube.com/watch?v=VBpAuDv4hRQ

---

## 💻 Proje Açıklaması: Python ile Otomatik HTML Sayfası Oluşturucu

### Kod Ne Yapıyor?
Bu program, kullanıcıdan konsol üzerinden aldığı bilgilerle (İsim, dersler, biyografi vb.) dinamik olarak bir **index.html** dosyası oluşturur. Temel amacı, Python'un "String" (metin) işleme ve "File Write" (dosyaya yazma) yeteneklerini kullanarak statik bir web sitesi iskeleti üretmektir.

### Algoritma Mantığı
1.  **Girdi Toplama:** `input()` fonksiyonları ile kullanıcıdan isim, alınan dersler ve biyografi bilgileri alınır.
2.  **HTML Yapılandırması:** Python içerisinde bir string değişkeni oluşturularak standart HTML5 etiketleri (`<html>`, `<head>`, `<body>`) tanımlanır.
3.  **CSS Entegrasyonu:** Web sayfasının görsel olarak düzenli durması için basit CSS kodları (renklendirme, başlık hizalama) string içine gömülür.
4.  **Dosya Yazımı:** `open("index.html", "w")` komutu ile bir dosya oluşturulur ve hazırlanan metin bu dosyanın içine yazılarak kaydedilir.

### Kullanılan Kütüphaneler
* `os`: (Opsiyonel) Dosya işlemleri kontrolü için.
* Ekstra bir kütüphane kurulumu gerektirmez, standart Python kütüphaneleri yeterlidir.

### Nasıl Çalıştırılır?
1.  Bilgisayarınızda Python'un yüklü olduğundan emin olun.
2.  `src` veya `kodlar` klasörü içindeki `.py` uzantılı dosyayı bir terminal veya IDE (VS Code, PyCharm vb.) üzerinden çalıştırın.
3.  Konsoldaki soruları yanıtlayın.
4.  Program bittiğinde, aynı klasörde oluşan `index.html` dosyasını herhangi bir internet tarayıcısıyla açarak sonucu görüntüleyebilirsiniz.
