from tkinter import *
from tkvideo import tkvideo
from PIL import Image, ImageTk
import cv2
import numpy as np
import face_recognition
import os
from tkinter import messagebox
from subprocess import call
import serial
import time


def open_home_pass(password):              
    
    def check_password(entry, password):
        if (entry.get() == password): 
            window1.destroy()
            open_home_app(password)  
        else:
            entry.delete(0, END)  
            pass_is_wrong()
            messagebox.showerror(title="ERROR!", message="INCORRECT PASSWORD")

    window1 = Tk()                  
    window1.geometry("650x380")
    window1.title("My Smart Home")
    
    logo = PhotoImage(file='SH2.png')  # logo stuff
    window1.iconphoto(True, logo)
    
    lbl = Label(window1)  # background
    player = tkvideo("BG2.mp4", lbl, loop=1)
    player.play()
    lbl.place(x=0, y=0)
    
    text = Label(window1, text="Enter the password, please!",
                 font=("Arial", 20, "bold"),
                 fg="white",
                 bg="black")
    text.pack(pady=30)
    
    entry = Entry(window1,
                  width=20,
                  font=("Arial", 30),
                  show="*" )
    entry.pack(pady=60)

    # Lambda function to replace checkpass()
    submit = Button(window1,                                         
                text="Submit",
                font=("Times New Roman", 12),
                bd=5,
                command=lambda: (check_password(entry, password)))

    submit.pack()
    window1.mainloop()


def open_home_app(password):   

    def add_to_database():      # add a user to a database
       face_detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
       vid = cv2.VideoCapture(0)
       while True :
          ret , frame  = vid.read()
          if not ret :
             break
          faces = face_detect.detectMultiScale(frame, 1.3, 5)
          for (x, y, w, h) in faces:
              cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
          frame = cv2.resize(frame,(800,600))
          cv2.rectangle(frame,(40,570),(760,30),(255, 255, 255), 4)
          cv2.putText(frame,"press (c) to take a photo when recognized..",(60,550),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
          cv2.imshow("Camera",frame)
          if cv2.waitKey(20) & 0xFF == ord("c"):
            cv2.imwrite("D:/programming_Vscode/python projects/Family/image.jpg", frame)
            break
       vid.release()
       cv2.destroyAllWindows()
       open_home_app(password)


    def change_password(password):

        def Back():
            window4.destroy()
            open_home_app(password)
        def change():
            password = entry.get()
            messagebox.showinfo(message="Changed successfully")
            window4.destroy()
            with open("PASSWORD.txt", "w") as file:
                file.write(password)
            open_home_app(password)

        window4 = Tk()                  
        window4.geometry("650x380")
        window4.title("My Smart Home")
        logo = PhotoImage(file='SH2.png')                 
        window4.iconphoto(True, logo)
        lbl = Label(window4)                                 
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
    
    def Open_system():
        Run_house_system()

    window2 = Tk()
    window2.geometry("650x380")
    window2.title("My Smart Home")
    logo = PhotoImage(file='SH2.png')            
    window2.iconphoto(True, logo)
    lbl = Label(window2)                                 
    player = tkvideo("background.mp4", lbl, loop=1)
    player.play()
    lbl.place(x=0, y=0)
    button1 = Button(window2,                                        
                text="Change Password",
                font=("Times New Roman",15),
                bd=5,command= lambda : (window2.destroy(),change_password(password)))
    button1.pack(pady=60)
    button2 = Button(window2,
                text="Change Database",
                font=("Times New Roman",15),
                bd=5,command= lambda : (window2.destroy(), add_to_database()))
    button2.pack()
    button3 = Button(window2,
                text="Run house system",
                width=20,
                font=("Times New Roman",15),
                bd=5,command= Open_system)
    button3.pack(pady=60)
    image = Image.open("noti2.png")
    resized_image = image.resize((40, 40))
    logo2 = ImageTk.PhotoImage(resized_image)
    button4 = Button(window2,
                 image=logo2,
                 width=40,
                 height=40,
                 bd=5)
    button4.place(x=0, y=0)
    window2.mainloop()

def open_camera(password):
    main_window.destroy()
    family_folder = "Family" 
    known_face_encodings = []
    known_face_names = []

    for filename in os.listdir(family_folder):
        if ( filename.endswith(".jpg") or filename.endswith(".png") ):
            family_image = face_recognition.load_image_file(os.path.join(family_folder, filename))
            family_encoding = face_recognition.face_encodings(family_image)[0]  
            known_face_encodings.append(family_encoding)
            known_face_names.append(os.path.splitext(filename)[0])  

    face_detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    vid = cv2.VideoCapture(0)
    name = "Unknown"
    while True:
        ret, frame = vid.read()
        if not ret:
           break
        faces = face_detect.detectMultiScale(frame, 1.3, 5)
        for (x, y, w, h) in faces:
           cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
           face_only = frame[y:y + h, x:x + w]
           rgb_face = cv2.cvtColor(face_only, cv2.COLOR_BGR2RGB)
           face_encodings = face_recognition.face_encodings(rgb_face)
           if face_encodings:
               face_encoding = face_encodings[0]
               matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.6)
               face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
               best_match_index = np.argmin(face_distances)
               if matches[best_match_index]:
                    name = known_face_names[best_match_index]
               else:
                    name = "Unknown"
               cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        frame = cv2.resize(frame, (1000, 800))
        cv2.rectangle(frame, (30, 780), (970, 20), (255, 255, 255), 5)
        cv2.rectangle(frame, (20, 790), (980, 10), (0, 0, 255), 5)
        cv2.putText(frame, "TEAM 6 House", (40, 720), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        cv2.putText(frame, "please wait for recognition...", (40, 760), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        cv2.imshow("Team 6 smart home camera", frame)
        if cv2.waitKey(20) & 0xFF == ord("x"):
              break
    vid.release()
    cv2.destroyAllWindows()
    if name in known_face_names :
        open_home_app(password)
    else :
        choose_method_of_password(password)
def pass_is_wrong():
    s.write(bytes('0',  'utf-8'))
    time.sleep(0.05)

def Run_house_system():
    s.write(bytes('1',  'utf-8'))
    time.sleep(0.05)

    while True:
        arduino_data = s.readline().decode('utf-8').strip()
        break 
    print(arduino_data)

def choose_method_of_password(password):

    def by_laptop():
        root.destroy()
        open_home_pass(password)
    def by_keypad():
        s.write(bytes('3'+password,'utf-8'))
        time.sleep(0.05)
        while True:
            if s.in_waiting > 0:
              response = s.readline().decode('utf-8').strip()
              if response == "correct":
               print("Access granted: The password is correct...")
               print("done")
               open_servo()
               root.destroy()
               open_home_app(password)
               break
              elif response == "incorrect":
               print("Access denied: The password is incorrect, try again..")

    root = Tk()
    root.geometry("650x380")  
    root.title("My Smart Home")
    logo = PhotoImage(file='SH2.png')           
    root.iconphoto(True, logo)
    lbl = Label(root)                                
    player = tkvideo("background.mp4", lbl, loop=1)
    player.play()
    lbl.place(x=0, y=0)
    button1 =Button(root,
                    text="enter the password with Laptop",
                    width=30, height=3,font=("Arial",10,"bold"),bg="white", fg="black"
                    ,command=by_laptop)
    button2 =Button(root,
                    text="Enter the password with Keypad", 
                    width=30, height=3,font=("Arial",10,"bold"),bg="white", fg="black"
                    ,command=by_keypad)
    button1.pack(pady=(100, 10))  
    button2.pack(pady=(10, 40))  
    root.mainloop()

# code start from here 
with open("PASSWORD.txt", "r") as file:
    password = file.read().strip()


s = serial.Serial(port="COM5", baudrate=115200, timeout=0.1)
time.sleep(3)
if not s.is_open:
    s.open()
print("done")

main_window = Tk()                  
main_window.geometry("650x380")
main_window.title("House of Team 6")

logo = PhotoImage(file='SH2.png')                 
main_window.iconphoto(True, logo)

lbl = Label(main_window)                                
player = tkvideo("BG2.mp4", lbl, loop=1)
player.play()
lbl.place(x=0, y=0)

button1 = Button(text="Enter the house",               
                bd=5,
                width=40,
                height=20,
                font=("Times New Roman",18),
                command=lambda: open_camera(password))
button1.pack(pady=150)
main_window.mainloop()
