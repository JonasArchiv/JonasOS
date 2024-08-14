import time
import serial
import adafruit_fingerprint

SERIAL_PORT = '/dev/serial0'  # Default serial port for Raspberry Pi GPIO
fingerprint_names = {}


def initialize_sensor():
    uart = serial.Serial(SERIAL_PORT, baudrate=57600, timeout=1)
    return adafruit_fingerprint.Adafruit_Fingerprint(uart)


def verify_fingerprint(finger):
    print("Place your finger on the sensor...")
    while finger.get_image() != adafruit_fingerprint.OK:
        pass
    if finger.image_2_tz(1) != adafruit_fingerprint.OK:
        print("Fingerprint not found.")
        return False
    if finger.finger_fast_search() != adafruit_fingerprint.OK:
        print("No match found.")
        return False

    fingerprint_id = finger.finger_id
    if fingerprint_id in fingerprint_names:
        print(f"Found fingerprint ID {fingerprint_id} with confidence {finger.confidence}")
        print(f"Associated Name: {fingerprint_names[fingerprint_id]}")
    else:
        print(f"Found fingerprint ID {fingerprint_id} but no associated name found.")
    return True


def add_fingerprint(finger):
    print("Place your finger on the sensor for enrollment...")
    for fingerimg in range(1, 3):
        print(f"Waiting for image {fingerimg}...")
        while True:
            i = finger.get_image()
            if i == adafruit_fingerprint.OK:
                print("Image taken")
                break
            elif i == adafruit_fingerprint.NOFINGER:
                print(".", end="")
            elif i == adafruit_fingerprint.IMAGEFAIL:
                print("Imaging error")
                return False
            else:
                print("Other error")
                return False

        print("Templating...")
        if finger.image_2_tz(fingerimg) != adafruit_fingerprint.OK:
            print("Error in templating")
            return False

        if fingerimg == 1:
            print("Remove finger")
            time.sleep(1)
            while i != adafruit_fingerprint.NOFINGER:
                i = finger.get_image()

    print("Creating model...")
    if finger.create_model() != adafruit_fingerprint.OK:
        print("Failed to create model")
        return False

    new_id = finger.library_size + 1
    print("Storing model...")
    if finger.store_model(new_id) != adafruit_fingerprint.OK:
        print("Failed to store model")
        return False

    name = input("Enter the name to associate with this fingerprint: ")
    fingerprint_names[new_id] = name
    print(f"Fingerprint enrolled successfully with ID {new_id} and Name: {name}")
    return True


def main():
    finger = initialize_sensor()
    while True:
        print("\nSelect an option:")
        print("1. Verify Fingerprint")
        print("2. Add Fingerprint")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            verify_fingerprint(finger)
        elif choice == '2':
            add_fingerprint(finger)
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == '__main__':
    main()
