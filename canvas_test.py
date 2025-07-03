from tkinter import *
from tkinter import ttk
from tkinter import colorchooser

global color

def mousepos(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y

def addline(event):
    canvas.create_line((lastx, lasty, event.x, event.y), fill=color)
    mousepos(event)

def choose_color():
    global color
    newcolor = colorchooser.askcolor()
    color = newcolor[1]
    color_swatch.config(background=newcolor[1])
        

root = Tk()

main = ttk.Frame(root)
main.grid()

testcolor = StringVar(value='black')

color = 'black'

canvas = Canvas(main, width=300, height=300, background="white")
canvas.grid(column=0, columnspan=2)
#canvas.create_line(10,5,200,50)


canvas.bind("<Button-1>", mousepos)
canvas.bind("<B1-Motion>", addline)

button = ttk.Button(main, text="Choose Color", command=choose_color)
button.grid(row=1, column=0, sticky='e')
#canvas.create_window(10,10, anchor='nw', window=button)

color_swatch = ttk.Label(main, width=2, text=" ", background=color)
color_swatch.grid(row=1, column=1, sticky='w', padx=15)

s = ttk.Style()
s.theme_use('xpnative')

main.columnconfigure(0, weight=1)
main.columnconfigure(1, weight=1)
main.columnconfigure(2, weight=1)

root.mainloop()
