import struct
import serial
import time

# Iridium seri bağlantısı
iridium = serial.Serial('/dev/ttyUSB0', 19200)
time.sleep(2)  # Seri portun hazır olması için bekleme süresi

def unpack_data(packet):
    # Veriyi çöz
    sensor_tag, location, error = struct.unpack('BBB', packet)
    return sensor_tag, location, error

def decode_location(location):
    # Konum bitlerini çözümle
    locations = []
    if location & 0x01:
        locations.append("Ön")
    if location & 0x02:
        locations.append("Arka")
    if location & 0x04:
        locations.append("Sağ")
    if location & 0x08:
        locations.append("Sol")
    if location & 0x10:
        locations.append("Üst")
    if location & 0x20:
        locations.append("Alt")
    if location & 0x40:
        locations.append("Merkez")
    return locations

try:
    while True:
        if iridium.in_waiting >= 3:  # 3 byte'lık paket bekleniyor
            packet = iridium.read(3)
            sensor_tag, location, error = unpack_data(packet)
            
            # Sensör etiketini çözümle
            sensor_name = chr(sensor_tag) + "1"
            
            # Konum bilgisini çözümle
            location_names = decode_location(location)
            location_str = ", ".join(location_names) if location_names else "Bilinmeyen"
            
            if error == 1:
                print(f"Hata: {sensor_name} sensörü ({location_str}) veri göndermiyor.")
            else:
                print(f"{sensor_name} sensörü ({location_str}): Çalışıyor.")
except KeyboardInterrupt:
    print("Program sonlandırıldı.")
finally:
    iridium.close()