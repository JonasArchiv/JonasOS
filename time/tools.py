import time


def stopwatch():
    print("Stoppuhr gestartet. Drücke Enter um zu beenden.")
    start_time = time.time()
    input()
    elapsed_time = time.time() - start_time
    print(f"Zeit: {time.strftime('%H:%M:%S', time.gmtime(elapsed_time))}")


def timer(seconds):
    print(f"Timer für {seconds} Sekunden gestartet.")
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer_format = '{:02d}:{:02d}'.format(mins, secs)
        print(f"Verbleibende Zeit: {timer_format}", end='\r')
        time.sleep(1)
        seconds -= 1
    print("\nZeit abgelaufen!")


def main():
    while True:
        print("\n1: Stoppuhr starten")
        print("2: Timer einstellen")
        print("3: Exit")

        choice = input("Wähle eine Option: ")

        if choice == '1':
            stopwatch()
        elif choice == '2':
            seconds = int(input("Gib die Zeit in Sekunden ein: "))
            timer(seconds)
        elif choice == '3':
            print("Programm beendet.")
            break
        else:
            print("Ungültige Auswahl.")


if __name__ == "__main__":
    main()
