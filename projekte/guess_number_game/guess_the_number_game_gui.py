# Guess the Number Game with Tkinter
import random
import tkinter as tk

window = tk.Tk()

header_frm = tk.Frame(
    master=window,
    border=2
)

title_lbl = tk.Label(
    master=header_frm,
    text="GUESS THE NUMBER GAME",
    fg="white",
    bg="black",
    width=100,
    height=2)
title_lbl.pack(fill=tk.BOTH, expand=True)


central_frm = tk.Frame(
    master=window,
    width=25
)

start_btn = tk.Button(
    master=central_frm,
    text="PLAY",
    width=20,
    height=5,
    bg="black",
    fg="#f2f2f2",
    borderwidth=4,
    relief=tk.RAISED)
start_btn.pack()


player_frm = tk.Frame(
    master=window,
    width=100,
    borderwidth=4,
    relief=tk.GROOVE)

player_name_lbl = tk.Label(
    master=player_frm,
    text="PLAYER",
    width=20,
    height=2,)

player_guess_lbl = tk.Label(
    master=player_frm,
    text="Guess the Number here:",
    height=2)

player_guess_ent = tk.Entry(
    master=player_frm,
    width=5)

player_name_lbl.pack()
player_guess_lbl.pack()
player_guess_ent.pack()


computer_frm = tk.Frame(
    master=window,
    width=100,
    borderwidth=4,
    relief=tk.GROOVE)

computer_name_lbl = tk.Label(
    master=computer_frm,
    text="COMPUTER",
    width=20,
    height=2)

computer_question_btn = tk.Button(
    master=computer_frm,
    text="Is your guessed number right?",
    height=2,
    bg="black",
    fg="white")

computer_answer_lbl = tk.Label(
    master=computer_frm,
    text="Wrong! Number too high.")

computer_name_lbl.pack()
computer_question_btn.pack()
computer_answer_lbl.pack()



header_frm.pack(fill=tk.X, expand=True)

player_frm.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
central_frm.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
computer_frm.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


window.mainloop()
