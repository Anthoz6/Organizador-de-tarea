import tkinter as tk
from tkinter import *
# Explicit imports to satisfy Flake8
from customtkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import ImageTk

class CheckBox:

    def __init__(self, root, task, delete_callback, select_callback, edit_callback):
        self.frame = tk.Frame(listbox, bg="white")
        self.frame.pack(anchor="w")
        
        self.check_var = tk.IntVar()
        self.check_label = tk.Label(self.frame, image=check_off_image, bg="#1B1B22")
        self.check_label.pack(side="left", padx=(5, 10), pady=5)
        self.check_label.bind("<Button-1>", self.toggle)
        
        self.text_label = tk.Label(self.frame, text=task, width=40, bg="#1B1B22", fg="white", font=("Comfortaa Regular", 12))
        self.text_label.pack(side="left", padx=9, pady=5)
        self.text_label.bind("<Button-1>", self.toggle)
        
        self.edit_button = tk.Button(self.frame, text="Editar", command=self.edit_task, font=("Comfortaa Regular", 8))
        self.edit_button.pack(side="left", padx=(5, 10))
        
        self.task = task
        self.delete_button = tk.Button(self.frame, text="Eliminar Tarea", command=self.delete_task, font=("Comfortaa Regular", 8))
        self.delete_button.pack(side="right")
        self.delete_callback = delete_callback
        self.select_callback = select_callback
        self.edit_callback = edit_callback
        self.update_background_color()

    def toggle(self, event=None):
        self.check_var.set(not self.check_var.get())
        self.update_background_color()
        self.update_image()
        self.select_callback(self.task)

    def edit_task(self):
        self.edit_callback(self.task)
        self.frame.destroy()
        
    def delete_task(self):
        self.delete_callback(self.task)
        self.frame.destroy()

    def update_background_color(self):
        bg_color = "#1B1B22" if self.check_var.get() else "#1B1B22"
        self.frame.configure(bg=bg_color)

    def update_image(self):
        if self.check_var.get():
            self.check_label.configure(image=check_on_image)
        else:
            self.check_label.configure(image=check_off_image)



window = Tk()
window.geometry("1366x768")
window.configure(bg = "#1E1E1E")

check_boxes = {}
selected_tasks = set()


def add_task(event=None):
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        create_check_box(task)
        entry.delete(0, tk.END)

def edit_task(task):
    selected_task = listbox.get(0, tk.END)
    if task in selected_task:
        listbox.delete(selected_task.index(task))
    if task in check_boxes:
        check_boxes[task].frame.destroy()
    if task in selected_tasks:
        selected_tasks.remove(task)
    entry.delete(0, tk.END)
    entry.insert(tk.END, task)
    entry.focus_set()

def delete_task(task):
    selected_task = listbox.get(0, tk.END)
    if task in selected_task:
        listbox.delete(selected_task.index(task))
    if task in check_boxes:
        check_boxes[task].frame.destroy()
    if task in selected_tasks:
        selected_tasks.remove(task)

def create_check_box(task):
    check_boxes[task] = CheckBox(listbox, task, delete_task, select_task, edit_task)

def select_task(task):
    if task in selected_tasks:
        selected_tasks.remove(task)
    else:
        selected_tasks.add(task)

def delete_selected_tasks():
    for task in list(selected_tasks):
        delete_task(task)

def update_task(task_text):
    if task_text in check_boxes:
        check_boxes[task_text].text_label.config(text=entry.get())
        # También actualizamos la tarea en el listbox
        for i in range(listbox.size()):
            if listbox.get(i) == task_text:
                listbox.delete(i)
                listbox.insert(i, entry.get())
                
canvas = Canvas(
    window,
    bg = "#1E1E1E",
    height = 768,
    width = 1366,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    4.0,
    0.0,
    350.0,
    978.0,
    fill="#212121",
    outline="")

img= tk.PhotoImage(file="fondo.png")
lbl_img = tk.Label(window, bg = "#212121", image = img)
lbl_img.pack(side = "right")

canvas.create_text(
    442.0,
    680.0,
    anchor="nw",
    text="¡Comencemos!",
    fill="#FFFFFF",
    font=("Comfortaa Regular", 20 * -1)
)

canvas.create_text(
    64.0,
    203.0,
    anchor="nw",
    text="Tareas a realizar",
    fill="#FFFFFF",
    font=("Comfortaa Regular", 20 * -1)
)

img2 = tk.PhotoImage(file="icong.png")
lbl_img = tk.Label(window, bg = "#212121", image = img2)
lbl_img.place(x=57, y=90)

canvas.create_text(
    137.0,
    130.0,
    anchor="nw",
    text="¿qué haremos hoy?",
    fill="#FFFFFF",
    font=("Comfortaa Regular", 17 * -1)
)

canvas.create_text(
    137.0,
    107.0,
    anchor="nw",
    text="Hola,",
    fill="#FFFFFF",
    font=("Comfortaa Regular", 16 * -1)
)

entry = Entry(window,width=54,fg="#F0F0F0",border=0,bg="#787986",font=("Comfortaa Regular",12,"bold"))
entry.place(x=440,y=678)

# Crear un Listbox para la lista de tareas dentro del Frame
listbox = tk.Listbox(window, width=143, height=34, bg="#1B1B22", selectmode=tk.MULTIPLE, relief="flat")
listbox.place(relx=0.310, rely=0.05, relwidth=0.63, relheight=0.8)


# Configurar la entrada para agregar tareas con Enter
entry.bind("<Return>", add_task)
delete_button = CTkButton(window, text="Eliminar Tarea", bg_color= "#787986", fg_color= "#787986", hover_color="#5B5C66" ,font=("Comfortaa Regular", 13), command=delete_selected_tasks)
delete_button.place(x=1100,y=685)

# Imágenes para casilla de verificación
check_off_image = tk.PhotoImage(file="1.png")
check_on_image = tk.PhotoImage(file="2.png")
window.resizable(False, False)

window.mainloop()