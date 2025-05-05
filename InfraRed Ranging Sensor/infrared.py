import time
import threading
import spidev

# MCP3008 SPI bağlantısı için ayarlar
spi = spidev.SpiDev()
spi.open(0, 0)  # SPI bus 0, device 0
spi.max_speed_hz = 1350000  # SPI hızı

# Sensörün bağlı olduğu MCP3008 kanalı
SENSOR_KANALI = 0

# Sensör modeline göre kalibrasyon değerleri
MODEL = 20150  # GP2Y0A02YK0F için

# Mesafe verisini tutacak global değişken
distance = 0.0

def read_adc(channel):
    # MCP3008'den analog değeri okur
    if channel < 0 or channel > 7:
        return -1
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

def get_distance():
    # Sensörden mesafe ölçümü yapar
    adc_value = read_adc(SENSOR_KANALI)
    voltage = adc_value * 3.3 / 1024  # ADC değerini voltaja çevir (3.3V referans)
    
    # Sensörün voltajını mesafeye çevir (GP2Y0A02YK0F için formül)
    if MODEL == 20150:
        distance = 65 * (voltage ** -1.10)  # GP2Y0A02YK0F için formül
    else:
        distance = 0  # Diğer modeller için uygun formül eklenmeli
    
    return distance

def update_distance():
    global distance
    while True:
        distance = get_distance()  # Mesafe ölçümü
        time.sleep(1)  # 1 saniyede bir güncelle

# Mesafe verisini güncelleme thread'i başlat
distance_thread = threading.Thread(target=update_distance)
distance_thread.daemon = True
distance_thread.start()

# Ana program
try:
    while True:
        # Mesafe verisini ekrana yazdır
        print(f"Mean distance: {distance:.2f} cm")
        time.sleep(1)  # 1 saniyede bir ekrana yazdır

except KeyboardInterrupt:
    print("Program sonlandırıldı.")
finally:
    spi.close()