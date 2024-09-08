from tkinter import *
from tkvideo import tkvideo
from PIL import Image, ImageTk
from subprocess import call

# Functions

def back():
    window2.destroy()
    call(["python","enter.py"])

def choices():
    window2.destroy()
    call(["python","choic.py"])

def changepassw():
    window2.destroy()
    call(["python","changepass.py"])

num = 1
def notification():                                  
    global num
    if num == 1:
        tab0.place(x=55,y=10)
    else:
        tab0.place_forget()
    num = num*-1

nnum = 1
def statu():                                  
    global nnum
    if nnum == 1:
        tab1.place(x=400,y=40)
    else:
        tab1.place_forget()
    nnum = nnum*-1

# Window

window2 = Tk()
window2.geometry("650x380")
window2.title("My Smart Home")

logo = PhotoImage(file='SH2.png')            #logo stuff
window2.iconphoto(True, logo)

lbl = Label(window2)                                 #background
player = tkvideo("background.mp4", lbl, loop=1)
player.play()
lbl.place(x=0, y=0)

with open('notif.txt') as file:
    info = file.read()

tab0 = Label(window2,text= info,font=("Times New Roman",12),width=15,wraplength=150)

with open('statu.txt') as file:
    info2 = file.read()

tab1 = Label(window2,text= info2,font=("Times New Roman",12),width=15,wraplength=150)

button0 = Button(window2,                                         #The buttons    
                text="Status",
                font=("Times New Roman",15),
                width=8,
                bd=5,
                command=statu)
button0.pack(pady=40)

button1 = Button(window2,
                text="Change Database",
                font=("Times New Roman",15),
                bd=5,
                command=choices)
button1.pack()

button2 = Button(window2,
                text="Change Password",
                font=("Times New Roman",15),
                bd=5,
                command=changepassw)
button2.pack(pady=40)

button3 = Button(window2,
                text="Back",
                font=("Times New Roman",15),
                width=8,
                bd=5,
                command=back)
button3.pack()

image = Image.open("noti2.png")
resized_image = image.resize((40, 40))
logo2 = ImageTk.PhotoImage(resized_image)


button4 = Button(window2,
                 image=logo2,
                 width=40,
                 height=40,
                 bd=5,
                 command=notification)
button4.place(x=0, y=0)

window2.mainloop()

