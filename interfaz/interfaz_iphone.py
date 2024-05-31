import customtkinter
import numpy as np
import os
import sys
import subprocess
from tkinter import filedialog
import tkinter as tk
from tkinter import simpledialog, messagebox

blender_executable = "C:/Program Files/Blender Foundation/Blender 4.1.exe"
#"C:\Users\carbe\OneDrive\Escritorio\Blender 4.1.lnk"

def Importar_archivo ():
    # Abrir el explorador de archivos y obtener la ruta del archivo seleccionado
    ruta_archivo = filedialog.askopenfilename()
    # Sirve para diferenciar funciones
    funcion = "importar"
    # Pedir la ruta del archivo .stl al usuario
    archivo_stl = ruta_archivo#("C:/Users/Angel/Desktop/Pruebas reales/1_interior/Untitled_Scan-2024-May-16.stl")
    #input("Por favor, ingrese la ruta completa del archivo .stl: "))

    # Ruta al ejecutable de Blender
    blender_executable = "C:/Program Files/Blender Foundation/Blender 4.1/blender-launcher.exe"      # Comando para abrir Blender y ejecutar el script, pasando la ruta del archivo .stl como argumento
    comando_blender = [
        blender_executable,
        "--background",
        "--python",  # Ejecutar script de Python
        "Blender1.py",
        "--",
        funcion,
        archivo_stl  # Pasar la ruta del archivo .stl como argumento
    ]

    # Ejecutar Blender con el comando especificado
    proceso = subprocess.Popen(comando_blender)
    # Esperar a que el proceso de Blender termine
    proceso.wait()

# Crear una función para solicitar un número en una ventana emergente
def pedir_metros():
    # Solicitar al usuario que introduzca un número mediante un diálogo simple
    valor = str(simpledialog.askfloat("Entrada de Metros", "¿Cuántos metros?"))
    # Comprobar si el usuario ha introducido un valor (puede cancelar el diálogo)
    if valor is not None:
        # Mostrar el valor en un mensaje de información
        messagebox.showinfo("Valor Introducido", f"Has introducido: {valor} metros")
        # Guardar el valor en una variable global
        global metros_introducidos
        metros_introducidos = valor
    else:
        # Si el usuario cancela, establecer el valor como None
        metros_introducidos = None

def Extrusion ():

    metros = str(metros_introducidos)
    funcion = "extrusion"
    # Ruta al ejecutable de Blender
    blender_executable = "C:/Program Files/Blender Foundation/Blender 4.1/blender-launcher.exe"    # Comando para abrir Blender y ejecutar el script, pasando la ruta del archivo .stl como argumento
    comando_blender = [
        blender_executable,
        "--background",
        "--python",  # Ejecutar script de Python
        "Blender1.py",
        "--",
        funcion,
        metros
    ]
    # Ejecutar Blender con el comando especificado
    proceso = subprocess.Popen(comando_blender)
    # Esperar a que el proceso de Blender termine
    proceso.wait()

def Ver ():
    funcion = "ver"
    # Ruta al ejecutable de Blender
    blender_executable = "C:/Program Files/Blender Foundation/Blender 4.1/blender-launcher.exe"    # Comando para abrir Blender y ejecutar el script, pasando la ruta del archivo .stl como argumento
    comando_blender = [
        blender_executable,
        "--background",
        "--python",  # Ejecutar script de Python
        "Blender1.py",
        "--",
        funcion
    ]
    # Ejecutar Blender con el comando especificado
    proceso = subprocess.Popen(comando_blender)
    # Esperar a que el proceso de Blender termine
    proceso.wait()
def guardar ():
    funcion = "guardar"
    # Ruta al ejecutable de Blender
    blender_executable = "C:/Program Files/Blender Foundation/Blender 4.1/blender-launcher.exe"    # Comando para abrir Blender y ejecutar el script, pasando la ruta del archivo .stl como argumento
    comando_blender = [
        blender_executable,
        "--background",
        "--python",  # Ejecutar script de Python
        "Blender1.py",
        "--",
        funcion
    ]
    # Ejecutar Blender con el comando especificado
    proceso = subprocess.Popen(comando_blender)
    # Esperar a que el proceso de Blender termine
    proceso.wait()


customtkinter.set_appearance_mode("dark")  # Login initial parameters
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

frame_home = None  # Define frame_home as a global variable
label_iphone_status = None  # Define label_iphone_status as a global variable
label_drone_status = None  # Define label_drone_status as a global variable

def login():
    username = entry1.get()
    password = entry2.get()
    # Dummy authentication, replace with your actual authentication logic
    if username == "admin" and password == "password":
        tabhome()  # If authenticated, go to the home page
    else:
        print("Invalid credentials")

def tabhome():
    global frame_home, label_iphone_status, label_drone_status  # Need to declare global variables
    frame.destroy()  # Destroy the login frame
    frame_home = customtkinter.CTkFrame(master=root)
    frame_home.pack(pady=20, padx=60, fill="both", expand=True)

    label_home = customtkinter.CTkLabel(master=frame_home, text="Control System", font=('roboto', 24))
    label_home.grid(row=0, column=0, columnspan=3, pady=12, padx=10)

    #button_iphone = customtkinter.CTkButton(master=frame_home, text="Connect to iPhone", command=connect_to_iphone)
    #button_iphone.grid(row=1, column=0, pady=12, padx=10)

    #button_drone = customtkinter.CTkButton(master=frame_home, text="Connect to Drone", command=connect_to_drone)
    #button_drone.grid(row=1, column=1, pady=12, padx=10)

    #label_status = customtkinter.CTkLabel(master=frame_home, text="Connection Status:", font=('roboto', 14))
    #label_status.grid(row=2, column=0, columnspan=3, pady=12, padx=10)

    #label_iphone_status = customtkinter.CTkLabel(master=frame_home, text="iPhone: Disconnected")
    #label_iphone_status.grid(row=3, column=0, pady=6, padx=10)

    #label_drone_status = customtkinter.CTkLabel(master=frame_home, text="Drone: Disconnected")
    #label_drone_status.grid(row=3, column=1, pady=6, padx=10)

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


def change_user():
    global frame_home
    frame_home.destroy()  # Destroy the home frame
    tablogin()  # Go back to the login page


def cad_scan():   
    Importar_archivo()
    pedir_metros()
    Extrusion()
        #Ver()
        #guardar()


def connect_to_iphone():
    label_iphone_status.config(text="iPhone: Connected")


def connect_to_drone():
    label_drone_status.config(text="Drone: Connected")

def stop_connections():
    sys.exit()

def control_drone():
    # Functionality to control the drone (Redirect to a new page or frame)
    print("Redirecting to drone control page")

    #os.startfile("C:\\Users\\Public\\Desktop\\Google Chrome.lnk")
    os.startfile("C:\\Users\\carbe\\OneDrive\\Escritorio\\FreeFlight Pro.lnk")


def iphone_software():
    # Functionality to access iPhone software (Redirect to a new page or frame)
    print("Redirecting to iPhone software page")
    
    os.startfile("C:\\Users\\Public\\Desktop\\ApowerMirror.lnk")

def tablogin():
    global frame, entry1, entry2  # Need to declare these as global to access them outside of this function
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

# Initially, show the login page
tablogin()

root.mainloop()