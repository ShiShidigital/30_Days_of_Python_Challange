# Guess the Number Game with Tkinter
import random
import tkinter as tk


def play():
    # print Starting game...
    start_msg = "Start of Game"
    print(start_msg)
    writeToLog(start_msg)

    # print Player Turn
    turn_msg = "Player Turn"
    print(turn_msg)
    writeToLog(turn_msg)

    # change Play Button to "Player Turn"
    start_btn['text'] = "PLAYER TURN"
    start_btn['state'] = 'disabled'

    # player_guesses = player_turn 
    player_guesses = player_turn()
    print(f"Player Guesses: {player_guesses}")

    # print Computer Turn
    turn_msg = "Computer Turn"
    print(turn_msg)
    writeToLog(turn_msg)

    # change Play Button to "Computer Turn" 
    start_btn['text'] = "COMPUTER TURN"
    start_btn['state'] = 'disabled'

    # computer_guesses = computer_turn()
    computer_guesses = computer_turn()
    print(f"Computer Guesses: {computer_guesses}")

    # Result Message
    if player_guesses < computer_guesses:
        result_msg = f"Player: {player_guesses} Computer: {computer_guesses} \n The Player wins this Game!"
    elif player_guesses == computer_guesses:
        result_msg = f"Player: {player_guesses} Computer: {computer_guesses} \n It's a tie!"
    else:
        result_msg = f"Player: {player_guesses} Computer: {computer_guesses} \n The Computer wins this Game!"

    print(result_msg)
    writeToLog(result_msg)    

    # print End of game
    start_msg = "End of Game \n"
    print(start_msg)
    writeToLog(start_msg)

    # change Play Button to "Play"
    start_btn['text'] = "PLAY"
    start_btn['state'] = 'normal'


# Function for writing to Log
def writeToLog(msg):
    numlines = int(log_txt.index('end - 1 line').split('.')[0])
    log_txt['state'] = 'normal'

    if numlines == 20:
        log_txt.delete(1.0, 2.0)

    if log_txt.index('end-1c') != '1.0':
        log_txt.insert('end', '\n')

    log_txt.insert('end', msg)
    log_txt["state"] = 'disabled'


def player_turn():
    print("Player Turn Function")
    guesses = input("Number? > ")
    writeToLog(f"Player Guesses: {guesses}")
    return guesses


def computer_turn():
    print("Computer Turn Function")
    guesses = input("Number? > ")
    writeToLog(f"Computer Guesses: {guesses}")
    return guesses




window = tk.Tk()
window.columnconfigure([0,1,2], weight=1, minsize=100)
window.rowconfigure([0, 1], weight=1, minsize=100)


# Header with Title
header_frm = tk.Frame(
    master=window,
    borderwidth=1)
header_frm.grid(row=0, column=0, columnspan=3)

title_lbl = tk.Label(
    master=header_frm,
    text="GUESS THE NUMBER GAME",
    fg="white",
    bg="black",
    width=100,
    height=2)
title_lbl.pack(padx=5, pady=2)


# Central Frame with Buttons
central_frm = tk.Frame(
    master=window,
    width=200)
central_frm.grid(row=1, column=1)

start_btn = tk.Button(
    master=central_frm,
    command=play,
    text="PLAY",
    width=20,
    height=2,
    bg="black",
    fg="#fff",
    borderwidth=4,
    relief=tk.RAISED)
start_btn.pack(padx=2, pady=2, fill='both')

log_txt = tk.Text(
    master=central_frm,
    state='disabled',
    width=60,
    wrap='none',
    height=20,
    borderwidth=4,
    relief=tk.SUNKEN)
log_txt.pack(padx=2, pady=2, side="bottom", fill="both")


# Player Frame with Player Input/Display
player_frm = tk.Frame(
    master=window,
    width=200,
    borderwidth=4,
    relief=tk.GROOVE)
player_frm.grid(row=1, column=0, padx=2, pady=2, sticky="nswe")

player_name_lbl = tk.Label(
    master=player_frm,
    text="PLAYER",
    width=20,
    height=2)
player_name_lbl.pack(pady=2, padx=2)

player_guess_ent = tk.Entry(
    master=player_frm,
    width=5)
player_guess_ent.pack(pady=2, padx=2)

player_guess_btn = tk.Button(
    master=player_frm,
    text="Is this the secret number?")
player_guess_btn.pack(pady=2, padx=2)


# Computer Frame with Computer Input/Display
computer_frm = tk.Frame(
    master=window,
    width=200,
    borderwidth=4,
    relief=tk.GROOVE)
computer_frm.grid(row=1, column=2, padx=2, pady=2, sticky="nswe")

computer_name_lbl = tk.Label(
    master=computer_frm,
    text="COMPUTER",
    width=20,
    height=2)
computer_name_lbl.pack(pady=2, padx=2)

computer_text_lbl = tk.Label(
    master=computer_frm,
    text="Can you guess the Secret Number?",
    height=1)
computer_text_lbl.pack(pady=2, padx=2)

computer_answer_lbl = tk.Label(
    master=computer_frm,
    text="Press on Play, then I choose \na Secret Number between 1 and 100.",
    height=2,
    relief=tk.RIDGE,
    borderwidth=2)
computer_answer_lbl.pack(pady=2, padx=2)


window.mainloop()
