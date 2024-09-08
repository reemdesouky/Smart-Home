from tkinter import *
from tkvideo import tkvideo
#import cv2

def open_camera ():                         #open cv function
    exit()


main_window = Tk()                  
main_window.geometry("650x380")
main_window.title("My Smart Home")

logo = PhotoImage(file='SH2.png')                 #logo stuff
main_window.iconphoto(True, logo)

lbl = Label(main_window)                                 #background
player = tkvideo("BG2.mp4", lbl, loop=1)
player.play()
lbl.place(x=0, y=0)

button = Button(text="Enter the house",               #the button which opens the camera
                bd=5,
                width = 40,
                height=20,
                font=("Times New Roman",18),
                command=open_camera)
button.pack(pady=155)

main_window.mainloop()