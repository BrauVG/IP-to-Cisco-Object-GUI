import tkinter as tk
from tkinter import scrolledtext
import pyperclip
import re

def convertir_a_cisco(texto):
    # Dividir el texto por cualquier delimitador no numérico que no sea un punto
    ips = re.split(r'[^0-9.]+', texto)
    # Filtrar elementos vacíos y convertir a objetos Cisco
    resultado = "\n".join([f"network-object host {ip}" for ip in ips if ip])
    return resultado

def procesar_texto():
    texto = text_input.get("1.0", tk.END)
    resultado = convertir_a_cisco(texto)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, resultado)

def copiar_resultado():
    resultado = text_output.get("1.0", tk.END)
    pyperclip.copy(resultado)

def crear_interfaz():
    ventana = tk.Tk()
    ventana.title("Convertidor de IPs a Objetos Cisco")
    
    # Definir el tamaño inicial de la ventana
    ventana.geometry('800x600')

    # Actualizar la geometría para posicionarla correctamente
    ventana.update_idletasks()
    
    # Posicionar la ventana en la esquina superior izquierda
    ventana.geometry('+300+50')
    
    # Usar grid para organizar la interfaz en columnas
    ventana.columnconfigure(0, weight=1)
    ventana.columnconfigure(1, weight=1)

    # Cuadro de entrada de texto
    label_input = tk.Label(ventana, text="Introduce las IPs (una por línea):")
    label_input.grid(row=0, column=0, padx=10, pady=5, sticky='n')

    global text_input
    text_input = scrolledtext.ScrolledText(ventana, width=40, height=30)
    text_input.grid(row=1, column=0, padx=10, pady=5, sticky='n')

    # Cuadro de resultado
    label_output = tk.Label(ventana, text="Resultado:")
    label_output.grid(row=0, column=1, padx=10, pady=5, sticky='n')

    global text_output
    text_output = scrolledtext.ScrolledText(ventana, width=40, height=30)
    text_output.grid(row=1, column=1, padx=10, pady=5, sticky='n')

    # Botón para procesar
    boton_procesar = tk.Button(ventana, text="Procesar", command=procesar_texto)
    boton_procesar.grid(row=2, column=0, pady=10)
    
    # Botón para copiar el resultado
    boton_copiar = tk.Button(ventana, text="Copiar resultado", command=copiar_resultado)
    boton_copiar.grid(row=2, column=1, pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    crear_interfaz()
