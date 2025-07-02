from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import urllib.request

root = Tk()

main = ttk.Frame(root)
main.grid()
image_label = ttk.Label(main, text="This is an image.")
image_label.grid(row = 0, columnspan = 2)

xsize = IntVar(value=50)
ysize = IntVar(value=50)

#image
image_url = "https://uxwing.com/wp-content/themes/uxwing/download/emoji-emoticon/smiley-icon.png"

image_object = Image.open('smiley-face.png') #create image object

global image_smile
image_smile = None

def image_size(image_object,x,y):   #function to resize object
    global image_smile
    image_object = image_object.resize((x,y), 1)
    image_smile = ImageTk.PhotoImage(image_object)
    image_show = ttk.Label(main, image=image_smile)
    image_show.grid(row = 1)

image_size(image_object,xsize.get(),ysize.get())

#functions to resize image using buttons
def resize_x():
    xresize = xsize.get()
    xresize = xresize + 10
    xsize.set(xresize)

    image_size(image_object, xsize.get(), ysize.get())

def resize_y():
    yresize = ysize.get()
    yresize = yresize + 10
    ysize.set(yresize)

    image_size(image_object, xsize.get(), ysize.get())

def resize_xs():
    if xsize.get() > 10:
        xresize = xsize.get()
        xresize = xresize - 10
        xsize.set(xresize)

        image_size(image_object, xsize.get(), ysize.get())

def resize_ys():
    if  ysize.get() > 10:
        yresize = ysize.get()
        yresize = yresize - 10
        ysize.set(yresize)

        image_size(image_object, xsize.get(), ysize.get())

image_show = ttk.Label(main, image=image_smile)
image_show.grid(row = 1)

    
#button to manipulate images
button_x = ttk.Button(main, text='+ Width', command=resize_x)
button_x.grid(row=2)
button_y = ttk.Button(main, text='+ Height', command=resize_y)
button_y.grid(row=2, column=1)
button_xs = ttk.Button(main, text='- Width', command=resize_xs)
button_xs.grid(row=3)
button_ys = ttk.Button(main, text='- Height', command=resize_ys)
button_ys.grid(row=3, column=1)



root.mainloop()
