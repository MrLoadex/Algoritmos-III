import ctypes
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random

# Cargar la biblioteca compartida
securityLib = ctypes.CDLL('./security.dll')

# Configuración de tipos de retorno
securityLib.fully_assemble.restype = ctypes.c_char_p
securityLib.partially_assemble.restype = ctypes.c_char_p
securityLib.desactive.restype = ctypes.c_char_p
securityLib.cancelZone.restype = ctypes.c_char_p
securityLib.activePanic.restype = ctypes.c_char_p
securityLib.callToEmergency.restype = ctypes.c_char_p

# Configuración de tipos de argumento
securityLib.cancelZone.argtypes = [ctypes.c_int]

# Funciones de la DLL
def fully_assemble():
    result = (securityLib.fully_assemble()).decode('utf-8')
    messagebox.showinfo("Resultado", result)

def partially_assemble():
    result = (securityLib.partially_assemble()).decode('utf-8')
    messagebox.showinfo("Resultado", result)

def desactive():
    result = (securityLib.desactive()).decode('utf-8')
    messagebox.showinfo("Resultado", result)

def cancel_zone():
    zone = random.randint(1, 10)
    result = (securityLib.cancelZone(zone)).decode('utf-8')
    messagebox.showinfo("Resultado", result)

def active_panic():
    result = (securityLib.activePanic()).decode('utf-8')
    messagebox.showinfo("Resultado", result)

def call_to_emergency():
    result = (securityLib.callToEmergency()).decode('utf-8')
    messagebox.showinfo("Resultado", result)

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz de Seguridad")

# Crear un frame principal
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Configurar la cuadrícula para que sea 2x3
frame.columnconfigure(0, weight=1, uniform="button")
frame.columnconfigure(1, weight=1, uniform="button")
frame.rowconfigure(0, weight=1, uniform="button")
frame.rowconfigure(1, weight=1, uniform="button")
frame.rowconfigure(2, weight=1, uniform="button")

# Crear los botones
buttons = [
    ("Armado Total", fully_assemble),
    ("Armado Parcial", partially_assemble),
    ("Desactivar", desactive),
    ("Cancelar Zona", cancel_zone),
    ("Pánico", active_panic),
    ("Emergencia Médica", call_to_emergency)
]

# Agregar los botones al frame
for idx, (text, command) in enumerate(buttons):
    button = ttk.Button(frame, text=text, command=command)
    button.grid(row=idx // 2, column=idx % 2, sticky=(tk.W, tk.E, tk.N, tk.S))

# Hacer que los botones sean cuadrados
for i in range(2):
    frame.grid_columnconfigure(i, minsize=100)  # Ajustar el tamaño mínimo para hacer los botones cuadrados
for i in range(3):
    frame.grid_rowconfigure(i, minsize=100)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
