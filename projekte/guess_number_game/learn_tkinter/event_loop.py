import tkinter as tk 

# Create a window object
window = tk.Tk()

# Create an event handler 
def handle_keypress(event):
  """Print the character associated to the key pressed"""
  print(event.char)

def handle_click(event):
  print("The button was clicked!")


# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

button = tk.Button(text="Click me!")
button.bind("<Button-1>", handle_click)
button.pack()

# Run the event loop 
window.mainloop()