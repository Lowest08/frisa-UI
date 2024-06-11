import subprocess
from tkinter import filedialog
import tkinter as tk
from tkinter import simpledialog, messagebox
import os

def Importar_archivo ():
    # Abrir el explorador de archivos y obtener la ruta del archivo seleccionado
    ruta_archivo = filedialog.askopenfilename()
    # Sirve para diferenciar funciones
    funcion = "importar"
    # Pedir la ruta del archivo .stl al usuario
    archivo_stl = ruta_archivo#("C:/Users/Angel/Desktop/Pruebas reales/1_interior/Untitled_Scan-2024-May-16.stl")
    #input("Por favor, ingrese la ruta completa del archivo .stl: "))

    # Ruta al ejecutable de Blender
    blender_executable = "C:/Program Files/Blender Foundation/Blender 4.1/blender.exe"
    # Comando para abrir Blender y ejecutar el script, pasando la ruta del archivo .stl como argumento
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

    #metros = str(metros_introducidos)
    funcion = "extrusion"
    # Ruta al ejecutable de Blender
    blender_executable = "C:/Program Files/Blender Foundation/Blender 4.1/blender.exe"
    # Comando para abrir Blender y ejecutar el script, pasando la ruta del archivo .stl como argumento
    comando_blender = [
        blender_executable,
        "--background",
        "--python",  # Ejecutar script de Python
        "Blender1.py",
        "--",
        funcion,
        #metros
    ]
    # Ejecutar Blender con el comando especificado
    proceso = subprocess.Popen(comando_blender)
    # Esperar a que el proceso de Blender termine
    proceso.wait()
def Ver ():
    funcion = "ver"
    # Ruta al ejecutable de Blender
    blender_executable = "C:/Program Files/Blender Foundation/Blender 4.1/blender.exe"
    # Comando para abrir Blender y ejecutar el script, pasando la ruta del archivo .stl como argumento
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
    blender_executable = "C:/Program Files/Blender Foundation/Blender 4.1/blender.exe"
    # Comando para abrir Blender y ejecutar el script, pasando la ruta del archivo .stl como argumento
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

Importar_archivo()
#pedir_metros()
Extrusion()
# Abre el archivo en modo de lectura ('r') y lee el contenido
ruta_archivo = os.path.abspath("C:/Users/Angel/PycharmProjects/Blender/.venv/Scripts/Volume.txt")
with open(ruta_archivo, "r") as archivo:
    variable_leida = archivo.read()

print("Volumen",":", variable_leida)
#Ver()
#guardar()
