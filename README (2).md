# hospital-stay-prediction
Makine Öğrenmesi ile hasta kalma süresi tahmini (Random Forest)
## Hastanede Kalış Süresi Tahmini
Bu repo, Global AI Hub Makine Öğrenmesi Bootcamp kapsamında yapılan bir proje çalışmasını içermektedir. Projenin temel amacı, hastaların hastanede kalış süresini (length of stay) geçmiş verilere dayanarak tahmin edebilen gözetimli bir makine öğrenmesi modeli geliştirmektir.

## Giriş
Projede kullanılan veri seti, sağlık kayıtlarından oluşmakta ve çeşitli hasta bilgilerinin yanı sıra hastanede ne kadar süreyle kaldıklarını içermektedir. Hedef değişken lengthofstay olup, bu değeri etkileyen değişkenler analiz edilerek tahmin modeli oluşturulmuştur.

Kapsanan adımlar:

-Verinin temizlenmesi ve dönüştürülmesi

-Keşifsel veri analizi (EDA)

-Özellik mühendisliği

-Modelleme (Random Forest, XGBoost, vb.)

-Performans karşılaştırması

-Sonuçların yorumlanması ve görselleştirme

## Metrikler
Modelleme sürecinde aşağıdaki metrikler kullanılmış ve yorumlanmıştır:

Mean Absolute Error (MAE)

Mean Squared Error (MSE)

R² Score

Elde edilen sonuçlar doğrultusunda en iyi model X olmuştur (detaylar notebook’ta grafiklerle sunulmuştur). Ayrıca +5 gün ve üzeri kalış sürelerinin etiketlenerek sınıflandırıldığı alternatif bir hedef yaklaşımı da denenmiş ve sonuçları karşılaştırılmıştır.

## Ekler

Projeye ait bir Streamlit uygulaması geliştirilmiş ve `UI/streamlit_app.py` dosyası altında sunulmuştur. Bu arayüz, kullanıcıdan giriş verilerini alarak hastanede kalış süresi tahmini yapmaktadır.

**Ek klasörler:**

- `UI/`: Streamlit dosyası içerir.
- `dataset/`: Gerekli verileri (örneğin `train.csv`) içerir.
- `requirements.txt`: Kullanılan Python kütüphanelerini listeler.
- `hospital-stay-prediction.ipynb`: Projenin tüm adımlarını içeren Kaggle Notebook dosyasıdır.


## Sonuç ve Gelecek Çalışmalar
Bu projede gözetimli öğrenme yöntemleriyle başarılı tahminler yapılabilmiştir. Ancak geliştirilebilecek yönler şunlardır:

Gerçek zamanlı veri ile model güncellenebilir.

Bir web arayüzü (örneğin Streamlit) ile canlı tahmin sistemi yapılabilir.

Model farklı ülke verilerine adapte edilerek genellenebilir.

Hasta gruplarına özel (örneğin yaşlılar, çocuklar) modeller geliştirilebilir.

Gelecekte bu projeyi genişletmeyi ve üretime alınabilir hâle getirmeyi planlıyorum.

## Linkler
Proje kapsamında kullanılan ve geliştirilen notebook'lar:

- [Ana Proje Not Defteri - EDA ve Modelleme] (https://www.kaggle.com/code/habibeaslan/hospital-stay-prediction)




