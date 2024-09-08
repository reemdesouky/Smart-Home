from tkinter import *
from tkvideo import tkvideo
from tkinter import messagebox
from subprocess import call

# Functions

def checkpass():
    enter = entry.get()
    with open('pass.txt') as file:
        passw = file.read()
    if enter == passw :                      
        window1.destroy()
        call(["python","app.py"])
    else :
        entry.delete(0,END)
        messagebox.showerror(title="ERROR!",message="INCORRECT PASSWORD")

def Back():
    window1.destroy()
    call(["python","enter.py"])

# Window

window1 = Tk()                  
window1.geometry("650x380")
window1.title("My Smart Home")

logo = PhotoImage(file='SH2.png')                 # logo stuff
window1.iconphoto(True, logo)

lbl = Label(window1)                                 # background
player = tkvideo("BG2.mp4", lbl, loop=1)
player.play()
lbl.place(x=0, y=0)

text = Label(window1,text="Enter the password, please!",
             font=("Arial",20,"bold"),
             fg="white",
             bg="black")
text.pack(pady=30)

entry = Entry(window1,
              width=20,
              font=("Arial",30),
              show="*" )
entry.pack(pady=60)

submit = Button(window1,                                         
                text="Submit",
                font=("Times New Roman",12),
                bd=5,
                command=checkpass)
submit.pack()

back = Button(window1,                                         
                text="Back",
                font=("Times New Roman",12),
                width=5,
                bd=5,
                command=Back)
back.pack(pady=5)

window1.mainloop()