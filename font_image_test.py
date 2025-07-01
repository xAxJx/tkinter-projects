from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import random

root = Tk()

main = ttk.Frame(root, height = 200, width = 400)
main.grid()

root.title('Fonts and Images')

font_size = IntVar(value=12)
font_color = StringVar(value="#000000")
#print(font_color.get())

image_label = ttk.Label(main, text='This is some text.', foreground=font_color.get(), font=("Arial", font_size.get()))
image_label.grid(row = 0)

def font_up():
    print("BIGGER!")
    change_font = font_size.get()
    font_size.set(change_font + 2)
    image_label.config(font=("Arial", font_size.get()))

def font_down():
    print("smaller!")
    change_font = font_size.get()
    if change_font <= 4:
        font_size.set(4)
    else:
        font_size.set(change_font - 2)
        image_label.config(font=("Arial", font_size.get()))

def font_colors():
    color = font_color.get()

    color_set=["0","0","0","0","0","0"]
    for i in range(len(color_set)):
        rand_value = random.randint(0,15)
        if rand_value == 10:
            color_set[i] = "A"
        elif rand_value == 11:
            color_set[i] = "B"
        elif rand_value == 12:
            color_set[i] = "C"
        elif rand_value == 13:
            color_set[i] = "D"
        elif rand_value == 14:
            color_set[i] = "E"
        elif rand_value == 15:
            color_set[i] = "F"
        else:
            color_set[i] = "0"
    
    color = "#" + color_set[0] + color_set[1] + color_set[2] + color_set[3] + color_set[4] + color_set[5]
    print(color)
    font_color.set(color)
    image_label.config(foreground=font_color.get())

size_up = ttk.Button(main, text='Bigger', command=font_up)
size_up.grid(row = 1, column = 0, sticky="e")
size_down = ttk.Button(main, text='Smaller', command=font_down)
size_down.grid(row = 1, column = 1, sticky="w")
color_change = ttk.Button(main, text='Color', command=font_colors)
color_change.grid(row=1, column = 2)

#buttons to change font styles

#image
#button to manipulate images

root.mainloop()
