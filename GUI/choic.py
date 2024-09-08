from tkinter import *
from tkvideo import tkvideo
from PIL import Image, ImageTk
from subprocess import call

# Functions

def Back():
    window3.destroy()
    call(["python","app.py"])

def Add():                         
    exit()

def Delete():
    exit()


# Window

window3 = Tk()
window3.geometry("650x380")
window3.title("My Smart Home")

logo = PhotoImage(file='SH2.png')            #logo stuff
window3.iconphoto(True, logo)

lbl = Label(window3)                                 #background
player = tkvideo("background.mp4", lbl, loop=1)
player.play()
lbl.place(x=0, y=0)

add = Button(window3,                                         #The buttons    
                text="Add member",
                font=("Times New Roman",15),
                bd=5,
                command=Add)
add.pack(pady=60)

delete = Button(window3,
                text="Delete member",
                font=("Times New Roman",15),
                bd=5,
                command=Delete)
delete.pack()

back = Button(window3,
                text="Back",
                font=("Times New Roman",15),
                bd=5,
                width=8,
                command=Back)
back.pack(pady=60)

window3.mainloop()