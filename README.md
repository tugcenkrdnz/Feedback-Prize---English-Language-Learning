# 📝 English Language Learner Proficiency Grader

Bu proje, ana dili İngilizce olmayan öğrencilerin (ELL) yazdığı makaleleri analiz eden ve 6 farklı kriterde puanlayan bir Doğal Dil İşleme (NLP) uygulamasıdır.

## 🎯 Projenin Amacı
Öğrencilerin yazdığı metinleri; **Cohesion, Syntax, Vocabulary, Phraseology, Grammar** ve **Conventions** başlıkları altında 1.0 ile 5.0 arasında puanlayarak anında geri bildirim sağlamak.

## 🚀 Özellikler
- **Hızlı Tahmin:** `st.cache_resource` kullanımıyla model bellekte tutulur ve anlık sonuç üretir.
- **Gelişmiş Görselleştirme:** Puanlar Plotly bar grafikleriyle (Düşük: Kırmızı, Yüksek: Yeşil) görselleştirilir.
- **Otomatik Temizleme:** Metindeki fazla boşluklar ve satır sonları modelin beklentisine göre otomatik normalize edilir.
- **Hata Tespiti:** Yazım hatalarını metin içinde vurgulayarak öğrencinin kendi hatalarını fark etmesini sağlar (Yanlış yönlendirmeyi önlemek için otomatik öneri yapılmaz).

## 🚀 Canlı Uygulama (Demo)
Model dosyasını yerel olarak kurmak ve çalıştırmakla uğraşmadan, projenin canlı versiyonunu doğrudan tarayıcınız üzerinden test edebilirsiniz:

👉 **[Hugging Face Spaces - Canlı Uygulama]
(https://huggingface.co/spaces/Karadeniztk/Feedback-Prize-English-Language-Learning))**


## 🛠️ Kurulum ve Çalıştırma

### 1. Kütüphanelerin Yüklenmesi
Terminalinizi açın ve aşağıdaki komutu çalıştırarak gerekli bağımlılıkları yükleyin:
```bash
pip install -r requirements.txt

```

### 2. Uygulamayı Başlatma

`app.py` ve `feedback_prize_model.pkl` dosyalarının aynı dizinde olduğundan emin olduktan sonra terminale şu komutu yazın:

```bash
streamlit run app.py

```

## 📊 Model Mimarisi

* **Pipeline:** Metin işleme ve modelleme adımları Scikit-learn Pipeline içerisinde birleştirilmiştir.
* **Vektörleştirici:** `TfidfVectorizer` (Metni sayısal verilere dönüştürür).
* **Algoritma:** `MultiOutputRegressor` ile güçlendirilmiş `Ridge Regression`.
* **Performans:** Ortalama Hata Skoru (MCRMSE) yaklaşık **0.56** seviyesindedir.

## 📂 Dosya Yapısı

* `app.py`: Streamlit arayüz kodu.
* `feedback_prize_model.pkl`: Eğitilmiş ve kaydedilmiş makine öğrenmesi modeli.
* `requirements.txt`: Gerekli kütüphane listesi.
* `README.md`: Proje dökümantasyonu.
