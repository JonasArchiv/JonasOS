import serial
import time

SERIAL_PORT = '/dev/serial0'  # Adjust your Pi's serial port
BAUD_RATE = 9600


def initialize_sensor():
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)
    return ser


def send_command(ser, command):
    ser.write(command)
    time.sleep(0.1)


def read_response(ser):
    response = ser.read_all()
    return response


def verify_fingerprint(ser):
    print("Place your finger on the sensor...")
    command_verify = b'\x00\x01'  # Adjust command
    send_command(ser, command_verify)
    response = read_response(ser)
    print(f"Verify Response: {response.decode('utf-8', errors='ignore')}")  # Decode response if necessary


def add_fingerprint(ser):
    print("Place your finger on the sensor for enrollment...")
    command_enroll = b'\x00\x02'  # Adjust command
    send_command(ser, command_enroll)
    response = read_response(ser)
    print(f"Enroll Response: {response.decode('utf-8', errors='ignore')}")  # Decode response if necessary


def list_fingerprints(ser):
    command_list = b'\x00\x03'  # Adjust command
    send_command(ser, command_list)
    response = read_response(ser)
    print(f"List Response: {response.decode('utf-8', errors='ignore')}")


def main():
    ser = initialize_sensor()
    while True:
        print("\nSelect an option:")
        print("1. Verify Fingerprint")
        print("2. Add Fingerprint")
        print("3. List Fingerprints")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            verify_fingerprint(ser)
        elif choice == '2':
            add_fingerprint(ser)
        elif choice == '3':
            list_fingerprints(ser)
        elif choice == '4':
            ser.close()
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == '__main__':
    main()
