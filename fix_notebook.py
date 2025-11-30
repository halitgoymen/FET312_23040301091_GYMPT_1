import json

# Senin dosyanın adı
notebook_filename = "FET312_23040301091_GYMPT_1.ipynb"

try:
    # 1. Dosyayı Oku
    with open(notebook_filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 2. Ameliyat: Sadece 'widgets' kısmını bul ve sil
    if 'metadata' in data and 'widgets' in data['metadata']:
        del data['metadata']['widgets']
        print("✅ Başarılı: 'widgets' verisi silindi.")
        print("Resimler ve çıktılar korundu.")
    else:
        print("ℹ️ Bilgi: Silinecek 'widgets' verisi zaten yok veya bulunamadı.")

    # 3. Dosyayı Kaydet
    with open(notebook_filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    
    print("💾 Dosya güncellendi. Şimdi git push yapabilirsin.")

except FileNotFoundError:
    print(f"❌ Hata: {notebook_filename} bulunamadı. Dosya adını kontrol et.")
except Exception as e:
    print(f"❌ Bir hata oluştu: {e}")