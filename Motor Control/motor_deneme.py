import time
import RPi.GPIO as GPIO

# GPIO Ayarları
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)  # Motor 1 PWM sinyali
GPIO.setup(15, GPIO.OUT)  # Motor 2 PWM sinyali

# PWM Ayarları
pwm_motor1 = GPIO.PWM(14, 50)  # 50 Hz PWM frekansı
pwm_motor2 = GPIO.PWM(15, 50)

# Motorları başlat (duty cycle = 5, motorlar duruyor)
pwm_motor1.start(5)
pwm_motor2.start(5)

try:
    print("Motorlar çok yavaş hızda çalıştırılıyor...")
    time.sleep(5)
    # Motor 1'i çok yavaş hızda çalıştır (duty cycle = 6)
    pwm_motor1.ChangeDutyCycle(6)
    time.sleep(5)  # 5 saniye boyunca çalıştır

    # Motor 1'i durdur
    pwm_motor1.ChangeDutyCycle(5)
    time.sleep(1)  # 1 saniye bekle

    # Motor 2'yi çok yavaş hızda çalıştır (duty cycle = 6)
    pwm_motor2.ChangeDutyCycle(6)
    time.sleep(5)  # 5 saniye boyunca çalıştır

    # Motor 2'yi durdur
    pwm_motor2.ChangeDutyCycle(5)
    time.sleep(1)  # 1 saniye bekle

    print("Motor testi tamamlandı.")

except KeyboardInterrupt:
    print("Test durduruldu.")

finally:
    # Motorları durdur ve GPIO'yu temizle
    pwm_motor1.ChangeDutyCycle(5)
    pwm_motor2.ChangeDutyCycle(5)
    time.sleep(1)
    pwm_motor1.stop()
    pwm_motor2.stop()
    GPIO.cleanup()
    print("GPIO temizlendi ve program sonlandırıldı.")
