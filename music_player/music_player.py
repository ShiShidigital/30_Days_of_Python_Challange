# Command Line Music Player
from pygame import mixer
from mutagen.mp3 import MP3


# Functions
def load_music(song):
    print(f"Loading Song: {song}")
    mixer.music.load(song)
    metadata = MP3(song)
    song_length_seconds = metadata.info.length
    song_length = f"{(song_length_seconds / 60):.2f}"
    return song_length


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


def update_timer():
    play_time_seconds = mixer.music.get_pos()
    current_play_time = f"{(play_time_seconds / 60000):.2f}"
    return current_play_time
  


# Initialising mixer
mixer.init()
# Initialising variables
test_song = "music.mp3"
current_song = "nothing"
song_length = 0
current_play_time = "00:00"
playing = "No"


print()
print("*** My Music Player ***")

while True:
    print()
    print()
    print("Information")
    print("--------------")
    print(f"Currently loaded song: {current_song}")
    print(f"Song length: {song_length}")
    print(f"Play Time: {current_play_time}")
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
        
    print("5 - Update timer")
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
        song_length = f"{load_music(test_song)} Minutes"
        print(song_length, "out of function")
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

    elif user_input == 5:
        current_play_time = update_timer()


    else:
        print("Please choose a valid menu option!")