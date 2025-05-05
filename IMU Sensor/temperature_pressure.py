import time
import board
import busio
import adafruit_bmp280

# I2C arayüzünü başlat
i2c = busio.I2C(board.SCL, board.SDA)

# BMP280 sensörünü belirlenen I2C adresiyle başlat
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)

# Opsiyonel: Deniz seviyesinde basınç (hava durumuna göre ayarlanabilir)
bmp280.sea_level_pressure = 1013.25  # hPa

print("BMP280 Sensör Testi")

while True:
    # Sıcaklık ve basınç değerlerini al
    temperature = bmp280.temperature  # Santigrat cinsinden sıcaklık
    pressure = bmp280.pressure * 100  # Pascal cinsine çevirmek için 100 ile çarpıyoruz
    altitude = bmp280.altitude
    # Sonuçları ekrana yazdır
    print(f"Sıcaklık: {temperature:.2f}°C \t Basınç: {pressure:.2f} Pa \t Yükseklik: {altitude} m")
    
    time.sleep(2)  # 2 saniye bekle
