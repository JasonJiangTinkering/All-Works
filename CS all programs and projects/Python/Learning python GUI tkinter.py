#Jason Jiang 7/12/19 #4
#goal: learning key methods within python's gui system: tkinter
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import BOTTOM

import tkinter
import tkinter.messagebox

def myWorld(x):
    print(x)
    print("Hello World")

root = tkinter.Tk()
root.title('Test')
root.geometry('200x100')
test = int(10)

mbtn = ttk.Menubutton(text='hello world')
mbtn.pack()

w = ttk.Button(root, text='test')
w.bind('<Button-1>', myWorld)
w.pack()

myimg = PhotoImage(file = r"C:\CS all programs and projects\Python\imgTest.png")
y = ttk.Button(root, text ="ITS WORKING", image =myimg, compound = "left")
y.pack(side = BOTTOM)
root.mainloop()

#what i learned:
#u start the main create a main window by making a var with tkinter.Tk()
#.title("string")-> set title bar of window to string
#.geometry("lengthxwidth")-> set size to length x width in px(default)
#.bind('event', command)-> binds an event of this widget to a command
#.pack-> put the widget into the main window/ aligns it
#var.mainloop()-> runs gui, var is what u set the main window to
#LEFT + PhotoImage and other things made by the program must be put into the globel workspace before being called
#PhotoImage(file ="") has to have the whole path starting from C: use r to show start of path
#if a widget has text and a image use compound to say which way the image is aligned

