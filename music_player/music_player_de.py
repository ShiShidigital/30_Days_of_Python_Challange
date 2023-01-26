# Command Line Music Player
from pygame import mixer


# Functions
def load_music(song):
    print(f"Musik wird geladen: {song}")
    mixer.music.load(song)


def play(song):
    print(f"Diese Datei wird jetzt abgespielt: {song}")
    mixer.music.play()


def stop():
    print("Musik abspielen beenden")
    mixer.music.stop()


def pause(playing):
    if playing == "Yes":
        print("Pause.")
        mixer.music.pause()
    elif playing == "Pause":
        print("Weiterspielen.")
        mixer.music.unpause()
    else:
        print(f"Error: Playing invalid: {playing} should be 'Yes' or 'Pause'")
  


# Initialising mixer
mixer.init()
# Initialising variables
test_song = "music.mp3"
current_song = "nothing"
playing = "No"


print()
print("*** My Music Player ***")

while True:
    print()
    print()
    print("Information")
    print("--------------")
    print(f"Geladene Musikdatei: {current_song}")
    print(f"Playing? {playing}")
    print("--------------")
    print()

    print("Menu")
    print("-------------")
    print("0 - Program schließen")
    print("1 - Musik abspielen")
    print("2 - Musik stoppen")
    print("3 - Musik laden")


    if playing == "Yes":
        print("4 - Pause")
    elif playing == "Pause":
        print("4 - Weiterspielen")
    else:
        print("4 - Pause (Tut jetzt nichts)")
        
    print()
    user_input = int(input("Wähle Menupunkt? > "))
    print()

    if user_input == 0:
        print("Ende des Programms")
        quit()

    elif user_input == 1:

        if current_song == "nothing":
            print("Keine Musik geladen.")
            continue

        play(current_song)
        playing = "Yes"

    elif user_input == 2:

        if current_song == "nothing":
            print("E spielt keine Musik")
            continue

        stop()
        playing = "No"

    elif user_input == 3:
        print("Lade Testmusik")
        load_music(test_song)
        current_song = test_song
        playing = "No"

    elif user_input == 4:
        if playing == "Yes":
            pause(playing)
            playing = "Pause"

        elif playing == "Pause":
            pause(playing)
            playing = "Yes"

        elif playing == "No":
            print("Es spielt keine Musik.")
            continue

        else:
            print("something went wrong")
            continue

    else:
        print("Wähle einen Menupunkt!")