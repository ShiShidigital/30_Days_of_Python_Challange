# Log to 30 days of Python Log Text file
import datetime
import codecs # for utf-8

def neuer_eintrag(file):
    d_t = datetime.datetime.now()
    current_date_time = "{}.{}.{} - {:02}:{:02d}".format(d_t.day, d_t.month, d_t.year, d_t.hour, d_t.minute)
    print()

    print("Bitte beantworte die folgenden Fragen")

    tage = input("Wieviele Tage hast Du nun die 30 Tage Python Challange geschafft? > ")
    projekt = input("An welchem Projekt hast Du heute gearbeitet? > ")
    genau = input("Was hast du genau gemacht? > ")
    gedanken = input("Deine Gedanken zum heutigen Tag... > ")
    mastodon = input("Hast Du einen Post auf Mastodon gemacht? (Link) > ")
    github = input("Hast Du heute etwas auf GitHub veröffentlicht? (Link) > ")


    print("Deine Einträge werden nun in deinem Log gespeichert ...")

    print("Öffne Datei {}".format(file))
    logbook = codecs.open(file, "a", "utf-8")

    print("Schreibe Daten in die Datei ... ")
    logbook.write("\n" + "-" * 80 + "\n")
    logbook.write(current_date_time + "\n")
    logbook.write("Tag: " + tage + "\n")
    logbook.write("Projekt: " + projekt + "\n")
    logbook.write("Heute gemacht: " + genau + "\n")
    logbook.write("Gedanken dazu: " + gedanken + "\n")
    logbook.write("Mastodon: " + mastodon + "\n")
    logbook.write("GitHub: " + github + "\n")
    logbook.write("\n" + "-" * 80 + "\n")

    print("Datei wird geschlossen.")
    logbook.close()


print()
print("30 Tage Python Challange - Log")

file="30_days_of_python_log.txt"

while True:
    print()
    print("Menu")
    print("-" * 20)
    print("1 - Schreibe einen neuen Eintrag in {}".format(file))
    print("0 - Program beenden")

    print()
    user_input = int(input("Wähle einen Menüpunkt > "))

    if user_input == 0:
        print("Program wird beendet.")
        quit()

    elif user_input == 1:
        print("Öffne '{}' und schreibe einen neuen Eintrag.".format(file))
        neuer_eintrag(file)
        print("Neuer Eintrag wurde in {} eingetragen.".format(file))
        
    else:
        print("Keine valide Eingabe. Wähle einen Menüpunkt!")
