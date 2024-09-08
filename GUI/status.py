from tkinter import *
from PIL import Image, ImageTk

# Functions

onbuttontemp = -1
def changetemp():
    global onbuttontemp
    if onbuttontemp == 1:                                 # add "ON" functions for temp
        tempoff.place_forget()
        tempon.place(x=500, y=50)
    else :
        tempon.place_forget()                             # add "OFF" functions for temp
        tempoff.place(x=500, y=50)
    onbuttontemp *= -1 

onbuttonpir = -1
def changepir():
    global onbuttonpir
    if onbuttonpir == 1:                                 # add "ON" functions for PIR
        piroff.place_forget()
        piron.place(x=500, y=150)
    else :                                                # add "OFF" functions for PIR
        piron.place_forget()
        piroff.place(x=500, y=150)
    onbuttonpir *= -1 

onbuttonspeed = -1
def changespeed():
    global onbuttonspeed
    if onbuttonspeed == 1:                                # add "ON" functions for speed
        speedoff.place_forget()
        speedon.place(x=500, y=250)
    else :                                                 # add "OFF" functions for speed
        speedon.place_forget()
        speedoff.place(x=500, y=250)
    onbuttonspeed *= -1 

# Window

window = Tk()
window.geometry("900x650")
window.title("My Smart Home")

logo = PhotoImage(file='SH2.png')            
window.iconphoto(True, logo)

bkimage = PhotoImage(file='bg3.jpg')   
lbl = Label(window, image=bkimage)                                 
lbl.place(x=0, y=0)

temp = Button(window,                                         
                text="Temp",
                font=("Times New Roman",20),
                width=8,
                bd=5)
temp.place(x=300, y=50)

tempon = Button(window,
                        text="ON",
                        font=("Times New Roman",20),
                        width=4,
                        bg="green",
                        bd=5,
                        command = changetemp)
tempon.place(x=500, y=50)
tempoff = Button(window,
                        text="OFF",
                        font=("Times New Roman",20),
                        width=4,
                        bg="red",
                        bd=5,
                        command=changetemp)



pir = Button(window,                                         
                text="PIR",
                font=("Times New Roman",20),
                width=8,
                bd=5)
pir.place(x=300, y=150)

piron = Button(window,                                         
                text="ON",
                font=("Times New Roman",20),
                width=4,
                bg="green",
                bd=5,
                command=changepir)
piron.place(x=500, y=150)
piroff = Button(window,                                         
                text="OFF",
                font=("Times New Roman",20),
                width=4,
                bg="red",
                bd=5,
                command=changepir)

speed = Button(window,                                         
                text="Speed",
                font=("Times New Roman",20),
                width=8,
                bd=5)
speed.place(x=300, y=250)

speedon = Button(window,                                         
                text="ON",
                font=("Times New Roman",20),
                width=4,
                bg="green",
                bd=5,
                command=changespeed)
speedon.place(x=500, y=250)
speedoff = Button(window,                                         
                text="OFF",
                font=("Times New Roman",20),
                width=4,
                bg="red",
                bd=5,
                command=changespeed)

time = Button(window,                                         
                text="Time",
                font=("Times New Roman",20),
                width=8,
                bd=5)
time.place(x=380, y=350)

back = Button(window,                                         
                text="Back",
                font=("Times New Roman",20),
                width=8,
                bd=5)
back.place(x=380, y=450)

window.mainloop()
