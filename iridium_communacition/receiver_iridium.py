import struct
import serial
import time

# Sensör verilerini simüle etme
sensor_data = {
    "BNO1": {"location": 0x01 | 0x02, "error": 0},  # Hem ön hem arka
    "BMP1": {"location": 0x02, "error": 0},         # Sadece arka
    "AMG1": {"location": 0x03, "error": 1},        # Hata durumu (ön ve arka)
    "IR1": {"location": 0x04, "error": 0},         # Sadece sağ
    "CAM1": {"location": 0x05, "error": 0}         # Ön ve sağ (0x01 | 0x04)
}

# Iridium seri bağlantısı
iridium = serial.Serial('/dev/ttyUSB0', 19200)
time.sleep(2)  # Seri portun hazır olması için bekleme süresi

def pack_data(sensor_tag, location, error):
    # Veriyi paketle
    packet = struct.pack('BBB', sensor_tag, location, error)
    return packet

for sensor_tag, values in sensor_data.items():
    packet = pack_data(ord(sensor_tag), values["location"], values["error"])
    iridium.write(packet)

iridium.close()