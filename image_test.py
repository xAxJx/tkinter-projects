from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import urllib.request

root = Tk()

main = ttk.Frame(root)
main.grid()

label_message = StringVar(value='Change the size of the image.')

image_label = ttk.Label(main, textvariable=label_message)
image_label.grid(row = 0, columnspan = 2)

xsize = IntVar(value=50)
ysize = IntVar(value=50)

#image
image_object = Image.open('smiley-face.png') #create image object

global image_smile
image_smile = None

def image_size(image_object,x,y):   #function to resize object
    global image_smile
    image_object = image_object.resize((x,y), 1)
    image_smile = ImageTk.PhotoImage(image_object)
    image_show = ttk.Label(main, image=image_smile)
    image_show.grid(row = 1, column=0, columnspan=2)

    
    if (x >= 1) and (y >= 1):
        label_message.set('Width: ' + str(x) + ' Height: ' + str(y))

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

#image_show = ttk.Label(main, image=image_smile)
#image_show.grid(row = 1)

    
#button to manipulate images
button_x = ttk.Button(main, text='+ Width', command=resize_x)
button_x.grid(row=2)
button_y = ttk.Button(main, text='+ Height', command=resize_y)
button_y.grid(row=2, column=1)
button_xs = ttk.Button(main, text='- Width', command=resize_xs)
button_xs.grid(row=3)
button_ys = ttk.Button(main, text='- Height', command=resize_ys)
button_ys.grid(row=3, column=1)

#change image size using text fields

new_x = StringVar()
new_y = StringVar()

def enter_resize():
    #print(str(new_x.get()) + ',' + str(new_y.get()))
    intcheck = 1

    #check that input is digits only
    for a in str(new_x.get()):
        if a.isdigit()==False:
            intcheck = 0

    for a in str(new_y.get()):
        if a.isdigit()==False:
            intcheck = 0

    if intcheck == 0:
        label_message.set('Width and Height must be integers')
        return
    
    #resize from input
    if intcheck ==1 :
        if int(new_x.get()) >=1:
            xsize.set(int(new_x.get()))
            label_message.set('Width: ' + str(new_x.get()) + ' Height: ' + str(new_y.get()))
        else:
            label_message.set('Width and Height must be >= 1')
        if int(new_y.get()) >=1:
            ysize.set(int(new_y.get()))
            label_message.set('Width: ' + str(new_x.get()) + ' Height: ' + str(new_y.get()))
        else:
            label_message.set('Width and Height must be >= 1')

        image_size(image_object, xsize.get(), ysize.get())

enter_x = ttk.Entry(main, textvariable = new_x, width=10)
enter_x.grid(row=4)
enter_Y = ttk.Entry(main, textvariable = new_y, width=10)
enter_Y.grid(row=4, column=1)
enter_button =ttk.Button(main, text='Resize', command=enter_resize)
enter_button.grid(row=5, column=0, columnspan=3)



root.mainloop()
