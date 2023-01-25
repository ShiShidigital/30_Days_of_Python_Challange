# Log Progress on 30 days of Python to a choosen textfile
import datetime


def neuer_eintrag(file):
    d_t = datetime.datetime.now()
    current_date_time = \
      f"{d_t.day}.{d_t.month}.{d_t.year} - {d_t.hour:02}:{d_t.minute:02d}"
    print()

    print("Bitte beantworte die folgenden Fragen")

    tage = input(
      "Wieviele Tage hast Du nun die 30 Tage Python Challange geschafft? > ")
    projekt = input("An welchem Projekt hast Du heute gearbeitet? > ")
    genau = input("Was hast du genau gemacht? > ")
    gedanken = input("Deine Gedanken zum heutigen Tag... > ")
    mastodon = input("Hast Du einen Post auf Mastodon gemacht? (Link) > ")
    github = input("Hast Du heute etwas auf GitHub veröffentlicht? (Link) > ")

    print()
    print("Deine Einträge werden nun in deinem Log gespeichert ...")

    print(f"Öffne Datei {file}")
    logbook = open(file, mode="a", encoding="utf8")

    print("Schreibe Daten in die Datei ... ")
    logbook.write(f"\n{'-'*80}\n")
    logbook.write(f"{current_date_time} \n")
    logbook.write(f"Tag: {tage} \n")
    logbook.write(f"Projekt: {projekt} \n")
    logbook.write(f"Heute gemacht: {genau} \n")
    logbook.write(f"Gedanken dazu: {gedanken} \n")
    logbook.write(f"Mastodon: {mastodon} \n")
    logbook.write(f"GitHub: {github} \n")
    logbook.write(f"\n{'-'*80}\n")

    print("Datei wird geschlossen.")
    logbook.close()


print()
print("30 Tage Python Challange - Log")

file="30_days_pf_python_log.txt"

while True:
    print()
    print("Menu")
    print("-" * 20)
    print(f"1 - Schreibe einen neuen Eintrag in {file}")
    print("2 - Bestimme die Textdatei, in die Du schreiben möchtest.")
    print("0 - Program beenden")

    print()
    user_input = int(input("Wähle einen Menüpunkt > "))

    if user_input == 0:
        print("Program wird beendet.")
        quit()

    elif user_input == 1:
        print(f"Öffne '{file}' und schreibe einen neuen Eintrag.")
        neuer_eintrag(file)
        print(f"Neuer Eintrag wurde in {file} eingetragen.")

    elif user_input == 2:
        print("""
Gib den Namen der Textdatei ein, in welche Du schreiben möchtest. 
Wenn die Datei noch nicht existiert, dann wird eine neue Textdatei 
angelegt. Wenn die Textdatei existiert, werden neue Einträge dem 
vorhandenen Text am Ende hinzugefügt.
            """)
        
        while True:
            user_input = input("Textdatei Name > ")  # Nicht sicher! Texteingabe prüfen!
            
            if user_input.startswith("."):           # Besser mit Regex und Exceptions
                print("Das ist nicht erlaubt!!!")
                continue

            else: 
                file = user_input + ".txt"  
                break
            
    else:
        print("Keine valide Eingabe. Wähle einen Menüpunkt!")