import time
import board
import busio
import adafruit_bno055

# I2C arayüzünü başlat
i2c = busio.I2C(board.SCL, board.SDA)

# BNO055 sensörünü başlat (I2C adresi 0x28 veya 0x29 olabilir)
sensor = adafruit_bno055.BNO055_I2C(i2c, address=0x28)

def get_direction(yaw):
    """Yaw açısını yön bilgisine çevirir."""
    if yaw is None:
        return "Bilinmeyen Yön"

    if 337.5 <= yaw < 360 or 0 <= yaw < 22.5:
        return "Kuzey (N)"
    elif 22.5 <= yaw < 67.5:
        return "Kuzeydoğu (NE)"
    elif 67.5 <= yaw < 112.5:
        return "Doğu (E)"
    elif 112.5 <= yaw < 157.5:
        return "Güneydoğu (SE)"
    elif 157.5 <= yaw < 202.5:
        return "Güney (S)"
    elif 202.5 <= yaw < 247.5:
        return "Güneybatı (SW)"
    elif 247.5 <= yaw < 292.5:
        return "Batı (W)"
    elif 292.5 <= yaw < 337.5:
        return "Kuzeybatı (NW)"
    else:
        return "Bilinmeyen Yön"

print("BNO055 ile Yön Tayini Başladı...")

while True:
    yaw, pitch, roll = sensor.euler  # Euler açılarından Yaw değeri alınır

    if yaw is None:
        print("Sensör verisi okunamadı!")
    else:
        direction = get_direction(yaw)  # Yön bilgisini al
        print(f"Yaw: {yaw:.2f}°  (Yön: {direction})")
        print(f"Pitch: {pitch:.2f}°  Roll: {roll:.2f}°\n")

    time.sleep(0.5)  # 500ms bekleme süresi

