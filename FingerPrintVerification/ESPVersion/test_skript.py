import requests
import threading
import time

ESP32_IP = '<ESP32_IP_ADDRESS>'
SERIAL_PORT = '/dev/ttyUSB0'


def send_request(command):
    url = f'http://{ESP32_IP}/{command}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error sending request: {e}")
        return None


def read_serial_data():
    while True:
        try:
            response = send_request("serial")
            if response:
                print(f"Serial Data: {response}")
        except Exception as e:
            print(f"Error reading serial data: {e}")
        time.sleep(1)


def verify_fingerprint():
    print("Verifying fingerprint...")
    result = send_request("verify")
    if result:
        print(result)


def add_fingerprint():
    print("Adding fingerprint...")
    result = send_request("add")
    if result:
        print(result)


def list_fingerprints():
    print("Listing fingerprints...")
    result = send_request("list")
    if result:
        print(result)


def main():
    serial_thread = threading.Thread(target=read_serial_data, daemon=True)
    serial_thread.start()

    while True:
        print("\nSelect an option:")
        print("1. Verify fingerprint")
        print("2. Add fingerprint")
        print("3. List fingerprints")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            verify_fingerprint()
        elif choice == '2':
            add_fingerprint()
        elif choice == '3':
            list_fingerprints()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
