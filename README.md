# Hava Aracı Stabilizasyon ve İzleme Sistemi

Bu proje, bir hava aracının dengede kalmasını sağlamak için IMU sensörü ve hava aracının bulunduğu bölgedeki bilgilere ulaşmak için Infrared Ranging sensörü, Thermal sensör ve iridium haberleşmesi kullanarak gerçek zamanlı verileri toplayan ve işleyen bir sistem geliştirmektedir.

## Proje Özeti

Sistem, IMU'dan alınan bilgilerle AC fırçasız motorlar ve servo motorları kullanarak hava aracını dengelemektedir. Ayrıca, sensör verileri ve kamera görüntüleri HTML sayfası üzerinden canlı olarak tarayıcıda gösterilmektedir.

## Özellikler

- **IMU Sensörü**: Hava aracının açısal hızını ve ivmesini ölçer
- **Infrared Ranging Sensörü**: Nesne mesafelerini ölçer
- **Thermal Sensör**: Ortam sıcaklık verilerini toplar
- **Iridium Haberleşmesi**: Uzun mesafe veri iletimi sağlar
- **Motor Kontrolü**: AC fırçasız motorlar ve servo motorlarla stabilizasyon
- **Canlı Web Arayüzü**: Gerçek zamanlı veri izleme ve görüntüleme

## Kullanılan Teknolojiler

### Donanım
- IMU Sensörü: MPU6050 veya benzeri
- Infrared Sensör: HC-SR04 veya benzeri
- Thermal Sensör: MLX90640 veya benzeri
- Iridium Modülü: Iridium 9603 veya benzeri
- Motorlar: BLDC motorlar ve servo motorlar

### Yazılım
- Python 3.x (Veri işleme)
- Arduino IDE (Donanım programlama)
- HTML/CSS/JavaScript (Web arayüzü)
- Flask (Web sunucusu)

## Kurulum

### Gereksinimler
- Python 3.x
- Arduino IDE
- Web tarayıcısı

### Python Kütüphaneleri
```bash
pip install -r requirements.txt
