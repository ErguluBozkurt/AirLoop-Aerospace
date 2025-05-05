import time
import board
import busio
import adafruit_bno055
import math

# I2C arayüzünü başlat
i2c = busio.I2C(board.SCL, board.SDA)

# BNO055 sensörünü belirtilen I2C adresiyle başlat (0x28 veya 0x29 olabilir)
sensor = adafruit_bno055.BNO055_I2C(i2c, address=0x28)

print("BNO055 Euler Açıları(Euler Angles) Okuma Başladı...")
print("BNO055 İvme(Acceleration) Ölçümü Başladı...")
print("BNO055 Lineer İvme(Linear Acceleration) Ölçümü Başladı...")
print("BNO055 Quaternion Ölçümü Başladı...")
print("BNO055 Açısal Hız(Jiroskop/Gyroscope) Ölçümü Başladı...")
print("BNO055 ile Yer Çekimi İvmesi(Gravity) Ölçümü Başladı...")

while True:
    yaw, roll, pitch = sensor.euler
    acc_x, acc_y, acc_z = sensor.linear_acceleration
    lin_acc_x, lin_acc_y, lin_acc_z = sensor.linear_acceleration
    qua_w, qua_x, qua_y, qua_z = sensor.quaternion
    gyr_x, gyr_y, gyr_z = sensor.gyro
    grav_x, grav_y, grav_z = sensor.gravity
    
    
    
    if yaw is None or pitch is None or roll is None:
        print("Sensör verisi okunamadı!")
    else:
        print(f"Euler Açıları = Yaw: {yaw:.2f}°, Pitch: {pitch:.2f}°, Roll: {roll:.2f}°")
    time.sleep(1)  
    
    if acc_x is None or acc_y is None or acc_z is None:
        print("Sensör verisi okunamadı!")
    else:
        print(f"İvme = X: {acc_x:.3f} m/s²  Y: {acc_y:.3f} m/s²  Z: {acc_z:.3f} m/s²")
    time.sleep(1)  
    
    if lin_acc_x is None or lin_acc_y is None or lin_acc_z is None:
        print("Sensör verisi okunamadı!")
    else:
        print(f"Lineer İvme = X: {lin_acc_x:.3f} m/s²  Y: {lin_acc_y:.3f} m/s²  Z: {lin_acc_z:.3f} m/s²")
    time.sleep(1)
    
    if qua_w is None or qua_x is None or qua_y is None or qua_z is None:
        print("Sensör verisi okunamadı!")
    else:
        print(f"Quaternion = W: {qua_w:.3f}  X: {qua_x:.3f}  Y: {qua_y:.3f}  Z: {qua_z:.3f}")
    time.sleep(1)
    
    if gyr_x is None or gyr_y is None or gyr_z is None:
        print("Sensör verisi okunamadı!")
    else:
        print(f"Açısal Hız = X: {gyr_x:.3f} dps  Y: {gyr_y:.3f} dps  Z: {gyr_z:.3f} dps")
    time.sleep(1)
    
    if grav_x is None or grav_y is None or grav_z is None:
        print("Sensör verisi okunamadı!")
    else:
        gravity_magnitude = math.sqrt(grav_x**2 + grav_y**2 + grav_z**2)
        print(f"Yer Çekimi Eksenler = X: {grav_x:.3f} m/s²  Y: {grav_y:.3f} m/s²  Z: {grav_z:.3f} m/s²")
        print(f"Yer Çekimi İvmesi = {gravity_magnitude:.3f} m/s²\n")

    time.sleep(1)  
