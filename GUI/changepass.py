from tkinter import *
from tkvideo import tkvideo
from tkinter import messagebox
from subprocess import call

# Functions

def Back():
    window4.destroy()
    call(["python","app.py"])

def change():
    with open('pass.txt','w') as file:
        file.write(entry.get())
    messagebox.showinfo(message="Changed successfully")
    window4.destroy()
    call(["python","app.py"])

# window

window4 = Tk()                  
window4.geometry("650x380")
window4.title("My Smart Home")

logo = PhotoImage(file='SH2.png')                 # logo stuff
window4.iconphoto(True, logo)

lbl = Label(window4)                                 # background
player = tkvideo("background.mp4", lbl, loop=1)
player.play()
lbl.place(x=0, y=0)

text = Label(window4,text="Enter the NEW password",
             font=("Arial",20,"bold"),
             fg="black",
             bg="pink")
text.pack(pady=30)

entry = Entry(window4,
              width=20,
              font=("Arial",30))
entry.pack(pady=60)

submit = Button(window4,                                         
                text="Change",
                font=("Times New Roman",12),
                bd=5,
                command=change)
submit.pack()

back = Button(window4,                                         
                text="Back",
                font=("Times New Roman",12),
                width=5,
                bd=5,
                command=Back)
back.pack(pady=5)

window4.mainloop()