import tkinter as tk
from PIL import Image, ImageTk
import os



wrong_try = 0

# generate all graphs in dir in order
path = './images'
files = os.listdir(path)


def display_image(num_attempts):
    #import pdb; pdb.set_trace()
    root = tk.Tk()
    root.title("hangman")
    root.geometry("400x800")

    start = os.path.join(path, f'{num_attempts+1}.png')
    start_img = Image.open(start)
    start_img = start_img.resize((400,800))
    start_img = ImageTk.PhotoImage(start_img)

    label = tk.Label(image=start_img)
    label.image = start_img
    label.pack()
    root.mainloop()





