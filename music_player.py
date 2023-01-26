# Command Line Music Player
from pygame import mixer


# Functions
def load_music(song):
    print(f"Loading Song: {song}")
    mixer.music.load(song)


def play(song):
    print(f"Playing now: {song}")
    mixer.music.play()


def stop():
    print("Stop the music.")
    mixer.music.stop()


def pause(playing):
    if playing == "Yes":
        print("Pause playing.")
        mixer.music.pause()
    elif playing == "Pause":
        print("Resume playing.")
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
    print(f"Currently loaded song: {current_song}")
    print(f"Playing? {playing}")
    print("--------------")
    print()

    print("Menu")
    print("-------------")
    print("0 - Close the Program")
    print("1 - Play a song")
    print("2 - Stop playing")
    print("3 - Load a Song")


    if playing == "Yes":
        print("4 - Pause the song")
    elif playing == "Pause":
        print("4 - Unpause the song")
    else:
        print("4 - Pause (Does nothing now)")
        
    print()
    user_input = int(input("What to do? > "))
    print()

    if user_input == 0:
        print("End of Program")
        quit()

    elif user_input == 1:

        if current_song == "nothing":
            print("There is no song to play. Load a music file first.")
            continue

        play(current_song)
        playing = "Yes"

    elif user_input == 2:

        if current_song == "nothing":
            print("There is no song playing.")
            continue

        stop()
        playing = "No"

    elif user_input == 3:
        print("Loading a test song for now.")
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
            print("No music playing.")
            continue

        else:
            print("something went wrong")
            continue

    else:
        print("Please choose a valid menu option!")