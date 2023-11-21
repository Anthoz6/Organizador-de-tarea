import subprocess
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image
import ast
import os
from customtkinter import *

carpeta_principal = os.path.dirname(__file__)
print(carpeta_principal)

Sign_up=CTk()
Sign_up.title("SignUp")
Sign_up.iconbitmap("1.png")
Sign_up.geometry("925x500+300+200")
Sign_up.configure(bg="#F0F0F0")
Sign_up.resizable(False,False)

set_appearance_mode("light")

def signup ():
    username_sign_up = user_Sign_up.get() 
    password_sign_up = code_Sign_up.get()
    conform_password_sign_up = conform_code_Sign_up.get()
    
    if password_sign_up == conform_password_sign_up:
        try:
            file=open("dataset.txt","r+")
            d=file.read()
            r=ast.literal_eval(d)
            
            dict2={username_sign_up:password_sign_up}
            r.update(dict2)
            file.truncate(0)
            file.close()
            
            file=open("dataset.txt","w")
            w=file.write(str(r))
            
            messagebox.showinfo("Signup","Sucessfully sign up")
        
        except:
            file=open("dataset.txt","w")
            pp=str({"username_sign_up":"password_sign_up"})
            file.write(pp)
            file.close()
    else:
        messagebox.showerror("Invalid","Both Password, should match")
              
        
#------------------------------------------------------------------------

def __signIn__():

    ruta_scriptIn = ruta_scriptIn = 'main.py'        
    
    subprocess.Popen(['python', ruta_scriptIn])
    
    Sign_up.destroy()

#------------------------------------------------------------------------

frame = CTkFrame(master=Sign_up,
                width=1000,
                height=1000,
                corner_radius=10,
                bg_color="#F0F0F0",
                fg_color="#F0F0F0",
                                )
frame.pack(padx=0,pady=0)

#------------------------------------------------------------------------
#Gif code

gifImage = "gatocompu.gif"

openImage = Image.open(gifImage)

frames = openImage.n_frames

imageObject = [PhotoImage(file=gifImage,format=f"gif -index {i}") for i in range(frames)]

count = 0
 

showAnimation = None

def animation(count):
    global showAnimation
    newImage = imageObject[count]
    gif_Label.configure(image=newImage)
    count+=1
    if count == frames:
        count = 0
    showAnimation = Sign_up.after(50,lambda: animation(count))

gif_Label = Label(Sign_up,image="")
gif_Label.place(x=50,y=90,height=250)

animation(count)

#------------------------------------------------------------------------
#heading_Sign_up
frame=Frame(Sign_up,width=350,height=390,bg="#F0F0F0")
frame.place(x=480,y=20)

heading_Sign_up=Label(frame,text="Sign up",fg="#222629",bg="#F0F0F0",font=("Cat Mark",35,"bold"))
heading_Sign_up.place(x=100,y=20)
#------------------------------------------------------------------------
def on_enter(e):
    user_Sign_up.delete(0,"end")
def on_leave(e):
    if user_Sign_up.get()=="":
        user_Sign_up.insert(0,"User")

user_Sign_up = Entry(frame,width=25,fg="black",border=0,bg="#F0F0F0",font=("Comfortaa Regular",10))
user_Sign_up.place(x=30,y=100)
user_Sign_up.insert(0,"Username")
user_Sign_up.bind("<FocusIn>",on_enter)
user_Sign_up.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=1,bg="black").place(x=25,y=125)

#------------------------------------------------------------------------

def on_enter(e):
    code_Sign_up.delete(0,"end")
def on_leave(e):
    if code_Sign_up.get()=="":
        code_Sign_up.insert(0,"Password")

code_Sign_up = Entry(frame,width=25,fg="black",border=0,bg="#F0F0F0",font=("Comfortaa Regular",10))
code_Sign_up.place(x=30,y=170)
code_Sign_up.insert(0,"Password")
code_Sign_up.bind("<FocusIn>",on_enter)
code_Sign_up.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=1,bg="black").place(x=25,y=195)

#------------------------------------------------------------------------

def on_enter(e):
    conform_code_Sign_up.delete(0,"end")
def on_leave(e):
    if conform_code_Sign_up.get()=="":
        conform_code_Sign_up.insert(0,"Confirm Password")

conform_code_Sign_up = Entry(frame,width=25,fg="black",border=0,bg="#F0F0F0",font=("Comfortaa Regular",10))
conform_code_Sign_up.place(x=30,y=240)
conform_code_Sign_up.insert(0,"Confirm Password")
conform_code_Sign_up.bind("<FocusIn>",on_enter)
conform_code_Sign_up.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=1,bg="black").place(x=25,y=265)

#------------------------------------------------------------------------

CTkButton(master=Sign_up,width=200,text="Sign up",bg_color="white",fg_color="#57a1f8",cursor="hand2", font=("Comfortaa Regular",18), command=signup).place(x=545,y=320)
label=Label(frame,text="I have an account",fg="black",bg="#F0F0F0",font=("Comfortaa Regular",8))
label.place(x=90,y=345)

signin=Button(frame,width=6,text="Sign in",border=0,bg="#F0F0F0",cursor="hand2",fg="#57a1f8", font=("Comfortaa Regular",8), command= __signIn__)
signin.place(x=200, y=345)

Sign_up.mainloop()