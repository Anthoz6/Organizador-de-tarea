from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image
import subprocess
import ast
from customtkinter import *

root=CTk()
root.title("Login")
root.geometry("925x500+300+200")
root.configure(bg="#F0F0F0")
root.resizable(False,False)

set_appearance_mode("light")

#------------------------------------------------------------------------
# Función de ingreso
def signin():
    username = user.get()
    password = code.get()

    try:
        with open("dataset.txt", "r") as file:
            content = file.read()
            data = ast.literal_eval(content)

            # Asegurémonos de que data sea un diccionario
            if not isinstance(data, dict):
                data = {}

            # Verificar si el usuario existe y la contraseña coincide
            if username in data and data[username] == password:
                messagebox.showinfo("Signin", "Successfully signed in")
                __signIn__()
            else:
                messagebox.showerror("Invalid", "Invalid username or password")
    except FileNotFoundError:
        messagebox.showerror("Error", "Dataset file not found.")
    except Exception as e:
        messagebox.showerror("Error", f"Error during signin: {str(e)}")
        

#------------------------------------------------------------------------
def __signIn__():

    ruta_scriptIn = ruta_scriptIn = 'pagge2.py'     
    
    subprocess.Popen(['python', ruta_scriptIn])
    
    root.destroy()
       
#------------------------------------------------------------------------
def __signup__():
    
    ruta_script = ruta_script = 'Sign_up.py'
    
    subprocess.Popen(['python', ruta_script])
    
    root.destroy()
    
#------------------------------------------------------------------------
    
frame = CTkFrame(master=root,
                width=1000,
                height=1000,
                corner_radius=10,
                bg_color="#F0F0F0",
                fg_color="#F0F0F0",
                                )
frame.pack(padx=0,pady=0)
    
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
    showAnimation = root.after(50,lambda: animation(count))

gif_Label = Label(root,image="")
gif_Label.place(x=50,y=90,height=250)

animation(count)

frame=Frame(root,width=350,height=350,bg="#F0F0F0")
frame.place(x=480,y=70)

heading=Label(frame,text="Sign in",fg="#222629",bg="#F0F0F0",font=("Cat Mark",35,"bold"))
heading.place(x=100,y=0)

#------------------------------------------------------------------------
#Usuario
def on_enter(e):
    user.delete(0,"end")
    
def on_leave(e):
    name = user.get()
    if name == "":
        user.insert(0,"Username")
        
        
user = Entry(frame,width=25,fg="black",border=0,bg="#F0F0F0",font=("Comfortaa Regular",10))
user.place(x=30,y=98)
user.insert(0,"Username")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=1,bg="black").place(x=25,y=124)



#------------------------------------------------------------------------
#Contraseña
def on_enter(e):
    code.delete(0,"end")
    
def on_leave(e):
    name = code.get()
    if name == "":
        code.insert(0,"Password")


        
code = Entry(frame,width=25,fg="black",border=0,bg="#F0F0F0",show="*",font=("Comfortaa Regular",10))
code.place(x=30,y=170)
code.insert(0,"Password")
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=1,bg="black").place(x=25,y=195)

#------------------------------------------------------------------------
#Sign up

CTkButton(master=root,width=150,height=38,text="Sign in",cursor="hand2",bg_color= "white", fg_color="#57a1f8",command=signin, font=("Comfortaa Regular",18)).place(x=567,y=304)
label=Label(frame,text="Don't have an account?",fg="#222629",bg="#F0F0F0",font=("Comfortaa Regular",8))
label.place(x=50,y=288)

sign_up = Button(frame,width=8,text="Sign up",bg="#F0F0F0", border=0, cursor="hand2", command=__signup__,fg="#57a1f8", font=("Comfortaa Regular",9))
sign_up.place(x=198,y=287)

#------------------------------------------------------------------------


root.mainloop()