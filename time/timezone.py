from datetime import datetime
import pytz


def get_current_time_germany():
    berlin_tz = pytz.timezone('Europe/Berlin')
    berlin_time = datetime.now(berlin_tz)
    return berlin_time.strftime('%d-%m-%Y %H:%M:%S')


def get_time_in_timezone(timezone):
    target_tz = pytz.timezone(timezone)
    target_time = datetime.now(target_tz)
    return target_time.strftime('%d-%m-%Y %H:%M:%S')


def convert_time_to_local(from_timezone, time_str):
    target_tz = pytz.timezone(from_timezone)
    local_tz = pytz.timezone('Europe/Berlin')
    target_time = datetime.strptime(time_str, "'%d-%m-%Y %H:%M:%S'")
    target_time = target_tz.localize(target_time)
    local_time = target_time.astimezone(local_tz)
    return local_time.strftime('%d-%m-%Y %H:%M:%S')


def convert_time_between_timezones(from_timezone, to_timezone, time_str):
    from_tz = pytz.timezone(from_timezone)
    to_tz = pytz.timezone(to_timezone)
    from_time = datetime.strptime(time_str, "'%d-%m-%Y %H:%M:%S'")
    from_time = from_tz.localize(from_time)
    to_time = from_time.astimezone(to_tz)
    return to_time.strftime('%Y-%m-%d %H:%M:%S')


def list_all_timezones_with_time():
    times = {}
    for tz in pytz.all_timezones:
        times[tz] = get_time_in_timezone(tz)
    return times


def main():
    print("1: Aktuelle Zeit in Deutschland anzeigen")
    print("2: Aktuelle Zeit in einer anderen Zeitzone anzeigen")
    print("3: Uhrzeit einer anderen Zeitzone in Deutsche Zeit umrechnen")
    print("4: Uhrzeit in einer Zeitzone in eine andere Zeitzone umrechnen")
    print("5: Liste aller Zeitzonen mit Uhrzeit anzeigen")

    choice = input("Wähle eine Option: ")

    if choice == '1':
        print(f"Aktuelle Zeit in Deutschland: {get_current_time_germany()}")
    elif choice == '2':
        timezone = input("Gib die Zeitzone an: ")
        print(f"Zeit in {timezone}: {get_time_in_timezone(timezone)}")
    elif choice == '3':
        from_timezone = input("Gib die Zeitzone an: ")
        time_str = input("Gib die Zeit in der Form DD-MM-YYYY HH:MM:SS an: ")
        print(f"Umgerechnete Zeit in Deutsche: {convert_time_to_local(from_timezone, time_str)}")
    elif choice == '4':
        from_timezone = input("Gib die Ausgangszeitzone an: ")
        to_timezone = input("Gib die Zielzeitzone an: ")
        time_str = input("Gib die Zeit in der Form DD-MM-YYYY HH:MM:SS an: ")
        print(f"Umgerechnete Zeit in {to_timezone}: {convert_time_between_timezones(from_timezone, to_timezone, time_str)}")
    elif choice == '5':
        times = list_all_timezones_with_time()
        for tz, time in times.items():
            print(f"{tz}: {time}")
    else:
        print("Ungültige Auswahl. Bitte wähle eine gültige Option.")


if __name__ == "__main__":
    print("Timezone System - JonasOS")
    main()
