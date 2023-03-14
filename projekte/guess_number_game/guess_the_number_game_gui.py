# Guess the Number Game with Tkinter
import random
import tkinter as tk

window = tk.Tk()
window.columnconfigure([0,1,2], weight=1, minsize=100)
window.rowconfigure([0, 1], weight=1, minsize=100)

# Header with Title
header_frm = tk.Frame(
    master=window,
    borderwidth=1
)
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
    width=100)
central_frm.grid(row=1, column=1)

start_btn = tk.Button(
    master=central_frm,
    text="PLAY",
    width=20,
    height=2,
    bg="black",
    fg="#fff",
    borderwidth=4,
    relief=tk.RAISED)
start_btn.pack(padx=2, pady=2)

log_lbl = tk.Label(
    master=central_frm,
    text="Log",
    width=20,
    height=5)
log_lbl.pack(padx=2, pady=2)

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
