# --- Python ile Otomatik HTML Sayfası Oluşturucu ---

print("Lütfen web siteniz için aşağıdaki bilgileri doldurun:")
print("-" * 40)

# Görseldeki temel sorular
ad_soyad = input("Adınız ve Soyadınız nedir? ")
biyografi = input("Kısa biyografiniz (Hakkınızda): ")
dersler_input = input("Aldığınız dersleri (virgülle ayırarak) yazın: ")

# FAZLADAN EKLENEN SORULAR
yas = input("Yaşınız kaç? ")
sehir = input("Yaşadığınız şehir? ")
uzmanlik = input("Uzmanlık alanınız veya hobiniz nedir? ")
eposta = input("İletişim için e-posta adresiniz: ")

# Dersleri virgüllerden ayırıp HTML listesi (li) haline getirme
ders_listesi = dersler_input.split(",")
dersler_html = ""
for ders in ders_listesi:
    dersler_html += f"<li>{ders.strip()}</li>"

# HTML Şablonu ve CSS Tasarımı
html_sablonu = f"""
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>{ad_soyad} - Kişisel Sayfa</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f0f2f5;
            display: flex;
            justify-content: center;
            padding: 50px;
        }}
        .card {{
            background: white;
            width: 500px;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            border-top: 8px solid #007bff;
        }}
        h1 {{ color: #333; margin-bottom: 5px; }}
        .info {{ color: #666; font-style: italic; margin-bottom: 20px; }}
        h3 {{ color: #007bff; border-bottom: 1px solid #eee; padding-bottom: 5px; }}
        p {{ line-height: 1.6; color: #444; }}
        ul {{ padding-left: 20px; }}
        li {{ margin-bottom: 5px; color: #555; }}
        .footer {{ margin-top: 30px; font-size: 0.8em; color: #888; text-align: center; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>{ad_soyad}</h1>
        <div class="info">{yas} yaşında | {sehir} | {uzmanlik}</div>
        
        <h3>Biyografi</h3>
        <p>{biyografi}</p>
        
        <h3>Aldığım Dersler</h3>
        <ul>
            {dersler_html}
        </ul>
        
        <div class="footer">
            İletişim: {eposta}
        </div>
    </div>
</body>
</html>
"""

# Dosyayı aynı klasöre index.html olarak kaydetme
try:
    with open("index.html", "w", encoding="utf-8") as dosya:
        dosya.write(html_sablonu)
    print("\n" + "="*40)
    print("BAŞARILI: 'index.html' dosyası klasörünüzde oluşturuldu.")
    print("Dosyayı tarayıcınızda açarak sonucu görebilirsiniz.")
    print("="*40)
except Exception as hata:
    print(f"Dosya oluşturulurken bir hata oluştu: {hata}")
