import sys
from timeos.tools import stopwatch, timer
from timeos.timezone import get_current_time_germany, get_time_in_timezone, convert_time_to_local, \
    convert_time_between_timezones, list_all_timezones_with_time
from qr_code_os.qr_generator import create_custom_qr_code
from qr_code_os.qr_read import read_qr_code_from_image, read_qr_code_from_webcam
from EMail_Component.send_mail_functions import send_email
from EMail_Component.get_mail_functions import fetch_unseen_emails, search_emails, fetch_emails_from_folder
from wol.wol import wake_on_lan, add_device, load_config, save_config
from config import get_email_config


def main():
    while True:
        print("\nWähle eine Option:")
        print("1. Stoppuhr starten")
        print("2. Timer einstellen")
        print("3. Aktuelle Zeit in Deutschland anzeigen")
        print("4. Zeit in spezifischer Zeitzone anzeigen")
        print("5. Zeit in lokale Zeit umrechnen")
        print("6. Zeit zwischen Zeitzonen umrechnen")
        print("7. Alle Zeitzonen mit Zeit auflisten")
        print("8. QR-Code erstellen")
        print("9. QR-Code aus Bild lesen")
        print("10. QR-Code von Webcam lesen")
        print("11. E-Mail senden")
        print("12. Ungelesene E-Mails abrufen")
        print("13. E-Mails durchsuchen")
        print("14. E-Mails aus Ordner abrufen")
        print("15. Wake on LAN")
        print("16. Gerät für Wake on LAN hinzufügen")
        print("17. Beenden")

        choice = input("Wähle eine Option: ")

        if choice == '1':
            stopwatch()
        elif choice == '2':
            seconds = int(input("Gib die Zeit in Sekunden ein: "))
            timer(seconds)
        elif choice == '3':
            print(f"Aktuelle Zeit in Deutschland: {get_current_time_germany()}")
        elif choice == '4':
            timezone = input("Gib die Zeitzone an: ")
            print(f"Zeit in {timezone}: {get_time_in_timezone(timezone)}")
        elif choice == '5':
            from_timezone = input("Gib die Zeitzone an: ")
            time_str = input("Gib die Zeit im Format DD-MM-YYYY HH:MM:SS an: ")
            print(f"Umgerechnete Zeit in lokale Zeit: {convert_time_to_local(from_timezone, time_str)}")
        elif choice == '6':
            from_timezone = input("Gib die Ausgangszeitzone an: ")
            to_timezone = input("Gib die Zielzeitzone an: ")
            time_str = input("Gib die Zeit im Format DD-MM-YYYY HH:MM:SS an: ")
            print(
                f"Umgerechnete Zeit in {to_timezone}: {convert_time_between_timezones(from_timezone, to_timezone, time_str)}")
        elif choice == '7':
            times = list_all_timezones_with_time()
            for tz, time in times.items():
                print(f"{tz}: {time}")
        elif choice == '8':
            data = input("Gib die Daten für den QR-Code ein: ")
            size = int(input("Gib die Größe des QR-Codes ein: "))
            body_color = input("Gib die Farbe des QR-Codes ein: ")
            bg_color = input("Gib die Hintergrundfarbe ein: ")
            logo_path = input("Gib den Pfad zum Logo ein (optional): ")
            create_custom_qr_code(data, size, body_color, bg_color, logo_path)
        elif choice == '9':
            image_path = input("Gib den Pfad zum Bild ein: ")
            print(f"QR-Code Daten: {read_qr_code_from_image(image_path)}")
        elif choice == '10':
            print(f"QR-Codes von der Webcam: {read_qr_code_from_webcam()}")
        elif choice == '11':
            email_key = input("Gib den Schlüssel der E-Mail-Konfiguration ein: ")
            email_config = get_email_config(email_key)
            to_address = input("Gib die E-Mail-Adresse des Empfängers ein: ")
            subject = input("Gib den Betreff der E-Mail ein: ")
            body = input("Gib den Text der E-Mail ein: ")
            send_email(email_config, to_address, subject, body)
        elif choice == '12':
            email_key = input("Gib den Schlüssel der E-Mail-Konfiguration ein: ")
            email_config = get_email_config(email_key)
            fetch_unseen_emails(email_config)
        elif choice == '13':
            email_key = input("Gib den Schlüssel der E-Mail-Konfiguration ein: ")
            email_config = get_email_config(email_key)
            search_criteria = input("Gib die Suchkriterien ein: ")
            search_emails(email_config, search_criteria)
        elif choice == '14':
            email_key = input("Gib den Schlüssel der E-Mail-Konfiguration ein: ")
            email_config = get_email_config(email_key)
            folder_name = input("Gib den Ordnernamen ein: ")
            fetch_emails_from_folder(email_config, folder_name)
        elif choice == '15':
            config_filename = 'wol/config.json'
            config = load_config(config_filename)
            id = input("Gib die Geräte-ID ein: ")
            if id in config:
                device_info = config[id]
                wake_on_lan(device_info['mac'])
            else:
                print("Geräte-ID nicht gefunden.")
        elif choice == '16':
            config_filename = 'wol/config.json'
            config = load_config(config_filename)
            add_device(config, config_filename)
        elif choice == '17':
            sys.exit()
        else:
            print("Ungültige Auswahl, bitte versuche es erneut.")


if __name__ == "__main__":
    print("Running JonasOS v1.0")
    print("Hallo! Ich bin JonasOS. Der Personal Assistant von Jonas Heilig.")
    print("Wie kann ich helfen?")
    main()
