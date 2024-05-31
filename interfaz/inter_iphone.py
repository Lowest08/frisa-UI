import customtkinter
import numpy as np
import os
import sys
import subprocess
from tkinter import filedialog
import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image  # Add this import for image handling

blender_executable = "C:/Program Files/Blender Foundation/Blender 4.1.exe"

def Importar_archivo ():
    ruta_archivo = filedialog.askopenfilename()
    funcion = "importar"
    archivo_stl = ruta_archivo

    blender_executable = "C:/Program Files/Blender Foundation/Blender 4.1/blender-launcher.exe"
    comando_blender = [
        blender_executable,
        "--background",
        "--python",
        "Blender1.py",
        "--",
        funcion,
        archivo_stl
    ]
    proceso = subprocess.Popen(comando_blender)
    proceso.wait()

def pedir_metros():
    valor = str(simpledialog.askfloat("Entrada de Metros", "¿Cuántos metros?"))
    if valor is not None:
        messagebox.showinfo("Valor Introducido", f"Has introducido: {valor} metros")
        global metros_introducidos
        metros_introducidos = valor
    else:
        metros_introducidos = None

def Extrusion ():
    metros = str(metros_introducidos)
    funcion = "extrusion"
    blender_executable = "C:/Program Files/Blender Foundation/Blender 4.1/blender-launcher.exe"
    comando_blender = [
        blender_executable,
        "--background",
        "--python",
        "Blender1.py",
        "--",
        funcion,
        metros
    ]
    proceso = subprocess.Popen(comando_blender)
    proceso.wait()

def Ver ():
    funcion = "ver"
    blender_executable = "C:/Program Files/Blender Foundation/Blender 4.1/blender-launcher.exe"
    comando_blender = [
        blender_executable,
        "--background",
        "--python",
        "Blender1.py",
        "--",
        funcion
    ]
    proceso = subprocess.Popen(comando_blender)
    proceso.wait()

def guardar ():
    funcion = "guardar"
    blender_executable = "C:/Program Files/Blender Foundation/Blender 4.1/blender-launcher.exe"
    comando_blender = [
        blender_executable,
        "--background",
        "--python",
        "Blender1.py",
        "--",
        funcion
    ]
    proceso = subprocess.Popen(comando_blender)
    proceso.wait()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

frame_home = None
label_iphone_status = None
label_drone_status = None

def login():
    username = entry1.get()
    password = entry2.get()
    if username == "admin" and password == "password":
        tabhome()
    else:
        print("Invalid credentials")

def tabhome():
    global frame_home, label_iphone_status, label_drone_status
    frame.destroy()
    frame_home = customtkinter.CTkFrame(master=root)
    frame_home.pack(pady=20, padx=60, fill="both", expand=True)

    label_home = customtkinter.CTkLabel(master=frame_home, text="Control System", font=('roboto', 24))
    label_home.grid(row=0, column=0, columnspan=3, pady=12, padx=10)

    button_stop_connections = customtkinter.CTkButton(master=frame_home, text="Stop Connections", command=stop_connections)
    button_stop_connections.grid(row=4, column=1, columnspan=3, pady=12, padx=10)
    
    button_control_drone = customtkinter.CTkButton(master=frame_home, text="Control Drone", command=control_drone)
    button_control_drone.grid(row=5, column=2, pady=12, padx=10)
    
    button_iphone_software = customtkinter.CTkButton(master=frame_home, text="iPhone Software", command=iphone_software)
    button_iphone_software.grid(row=5, column=3, pady=12, padx=10)

    button_change_user = customtkinter.CTkButton(master=frame_home, text="Change user", command=change_user)
    button_change_user.grid(row=6, column=2, columnspan=3, pady=12, padx=10)

    button_blender = customtkinter.CTkButton(master=frame_home, text="CAD Scan", command=cad_scan)
    button_blender.grid(row=6, column=2, columnspan=3, pady=12, padx=10)

    # Load and display the image in the right corner
    image_path = "C:/Users/carbe/OneDrive/Imágenes/logo_tec.png"  # Specify the path to your image
    image = customtkinter.CTkImage(Image.open(image_path), size=(100, 100))
    image_label = customtkinter.CTkLabel(master=frame_home, image=image, text="")
    image_label.grid(row=0, column=3, pady=12, padx=10, sticky="ne")

def change_user():
    global frame_home
    frame_home.destroy()
    tablogin()

def cad_scan():
    Importar_archivo()
    pedir_metros()
    Extrusion()

def connect_to_iphone():
    label_iphone_status.config(text="iPhone: Connected")

def connect_to_drone():
    label_drone_status.config(text="Drone: Connected")

def stop_connections():
    sys.exit()

def control_drone():
    print("Redirecting to drone control page")
    os.startfile("C:\\Users\\carbe\\OneDrive\\Escritorio\\FreeFlight Pro.lnk")

def iphone_software():
    print("Redirecting to iPhone software page")
    os.startfile("C:\\Users\\Public\\Desktop\\ApowerMirror.lnk")

def tablogin():
    global frame, entry1, entry2
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame, text="Login System", font=('roboto', 24))
    label.pack(pady=12, padx=10)

    entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
    entry1.pack(pady=12, padx=10)

    entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
    entry2.pack(pady=12, padx=10)

    button = customtkinter.CTkButton(master=frame, text="Login", command=login)
    button.pack(pady=12, padx=10)

    checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
    checkbox.pack(pady=12, padx=10)

tablogin()
root.mainloop()
