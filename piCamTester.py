# capture_image.py
import time
from picamera2 import Picamera2, Preview

def main():
    picam2 = Picamera2()
    config = picam2.create_preview_configuration()
    picam2.configure(config)

    # Optional: preview with QTGL window (on desktop)
    picam2.start_preview(Preview.QTGL)

    picam2.start()
    time.sleep(2)  # allow sensor to adjust to lighting
    picam2.capture_file("photo.jpg")
    print("Captured photo.jpg")

    picam2.stop_preview()
    picam2.close()

if __name__ == "__main__":
    main()
