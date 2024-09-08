from tkinter import *
from tkvideo import tkvideo
from PIL import Image, ImageTk
from subprocess import call

# Functions

def Back():
    window.destroy()
    call(["python","app.py"])

def Run():                                         # You can edit the functions
    exit()

def Close():
    exit()

def Info():
    exit()

# Window

window = Tk()
window.geometry("650x380")
window.title("My Smart Home")

logo = PhotoImage(file='SH2.png')            #logo stuff
window.iconphoto(True, logo)

lbl = Label(window)                                 #background
player = tkvideo("background.mp4", lbl, loop=1)
player.play()
lbl.place(x=0, y=0)

run = Button(window,                                         #The buttons    
                text="Run the system",
                font=("Times New Roman",15),
                bd=5,
                command=Run)
run.pack(pady=40)

close = Button(window,
                text="Close the system",
                font=("Times New Roman",15),
                bd=5,
                command=Close)
close.pack()


info = Button(window,
                text="System information",
                font=("Times New Roman",15),
                bd=5,
                command=Info)
info.pack(pady = 40)

back = Button(window,
                text="Back",
                font=("Times New Roman",15),
                bd=5,
                width=8,
                command=Back)
back.pack()

window.mainloop()