import tkinter as tk 
import random

def d6():
  lbl_die_result["text"] = str(random.randint(1, 6))

window = tk.Tk()

btn_roll_die = tk.Button(text="Roll", height=3, command=d6)
btn_roll_die.pack(fill="both", expand=True)

lbl_die_result = tk.Label(text="0", height=3)
lbl_die_result.pack(fill="both", expand=True)

window.mainloop()