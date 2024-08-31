import cv2
import numpy as np
from pyzbar.pyzbar import decode


def read_qr_code_from_image(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    decoded_objects = decode(gray_image)
    if decoded_objects:
        return decoded_objects[0].data.decode('utf-8')
    else:
        return "Kein QR-Code gefunden"


def read_qr_code_from_webcam():
    cap = cv2.VideoCapture(0)
    print("Drücke 'q', um das Programm zu beenden.")

    results = []

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Fehler beim Zugriff auf die Webcam.")
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        decoded_objects = decode(gray_frame)

        for obj in decoded_objects:
            qr_text = obj.data.decode('utf-8')
            results.append(qr_text)
            print(f"QR-Code gefunden: {qr_text}")

        cv2.imshow("JonasOS - QR-Code Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return results


# webcam_qr_code_text = read_qr_code_from_webcam()
# print(f"Alle QR-Codes aus der Webcam: {webcam_qr_code_text}")
