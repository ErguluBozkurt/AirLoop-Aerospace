#### ÇALIŞTIRMADAN ÖNCE HTML KODU ÇALIŞTIRILMALIDIR


from flask import Flask, Response
from picamera2 import Picamera2
from PIL import Image
import io

app = Flask(__name__)

# Picamera2'yi başlat
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()

def generate_frames():
    while True:
        # Kameradan bir kare al
        frame = picam2.capture_array()

        # Görüntüyü PIL Image formatına dönüştür ve RGBA -> RGB dönüşümü yap
        image = Image.fromarray(frame).convert('RGB')

        # Görüntüyü JPEG formatına dönüştür
        buf = io.BytesIO()
        image.save(buf, format='JPEG')
        frame_bytes = buf.getvalue()

        # Frame'i byte olarak yield et
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='192.168.43.18', port=5000)

