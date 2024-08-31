import json
from ipaddress import ip_address
from wakeonlan import send_magic_packet


def load_config(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_config(filename, config):
    with open(filename, 'w') as file:
        json.dump(config, file, indent=4)


def wake_on_lan(mac_address):
    send_magic_packet(mac_address)
    print(f"Wake-on-LAN Magic Packet gesendet an {mac_address}.")


def add_device(config, filename):
    id = input("Eindeutige ID für das Gerät: ")
    if id in config:
        print("ID existiert bereits.")
        return

    name = input("Namen des Geräts: ")
    mac_address = input("MAC-Adresse des Geräts: ")
    ip_address = input("IP-Adresse des Geräts: ")

    config[id] = {
        "name": name,
        "mac": mac_address,
        "ip": ip_address
    }

    save_config(filename, config)
    print(f"Gerät {name} mit ID {id} erfolgreich hinzugefügt.")


def main():
    config_filename = 'config.json'
    config = load_config(config_filename)

    print("Wake on LAN System - JonasOS")

    while True:
        action = input("Wählen Sie eine Aktion: (1) Gerät anschalte (2) Gerät hinzufügen (3) Skript Beenden: ")

        if action == "1":
            id = input("ID eingeben: ")
            if id not in config:
                print(f"ID {id} nicht gefunden.")
                continue

            device_info = config[id]
            mac_address = device_info.get('mac')
            ip_address = device_info.get('ip')

            if mac_address:
                print(
                    f"Gerät: ID {id}, Name {device_info.get('name')}, MAC-Adresse {mac_address}, IP-Adresse {ip_address}")
                wake_on_lan(mac_address)
            else:
                print(f"MAC-Adresse bei ID {id} nicht gefunden.")

        elif action == "2":
            add_device(config, config_filename)

        elif action == "3":
            break

        else:
            print("Ungültige Eingabe.")


if __name__ == "__main__":
    main()
