"""
PROYECTO: Sistema Inteligente de Contraseñas Seguras
CURSO: Programación I
DESCRIPCIÓN: Aplicación con interfaz gráfica para generar contraseñas personalizadas 
y evaluar su seguridad mediante análisis de caracteres y detección de patrones.
"""

import tkinter as tk
import random
import string
from datetime import datetime

# --- FUNCIONES DE LÓGICA ---

def registrar_actividad(longitud, nivel):
    """
    Registra en un archivo de texto la fecha, longitud y nivel de seguridad.
    Usa el modo 'a' (append) para no borrar registros previos.
    """
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Abrimos el archivo en modo 'a' (append) para añadir líneas sin borrar lo anterior
    with open("registro_actividad.txt", "a") as archivo:
        archivo.write(f"Fecha: {fecha} | Longitud: {longitud} | Seguridad: {nivel}\n")

def checkPassword():
    """
    Analiza la contraseña del Entry, verifica requisitos mínimos y patrones simples.
    Actualiza la etiqueta de resultado y guarda la actividad.
    """
    password = entrada.get()
    size = len(password)
    
    # IMPORTANTE: Inicializamos res_texto con un valor por defecto para el registro
    res_texto = "No evaluado" 

    if size == 0:
        resultado.config(text="Ingrese una contraseña", fg="red")
        return # Aquí sí salimos porque no hay nada que evaluar

    # 1. Analizamos las características de los caracteres
    tiene_numero = any(char.isdigit() for char in password) # Busca al menos un número
    tiene_mayus = any(char.isupper() for char in password) # Busca al menos una mayúscula
    tiene_minus = any(char.islower() for char in password) # Busca al menos una minúscula
    tiene_esp = any(not char.isalnum() for char in password) # Busca símbolos especiales

    # Definición de secuencias comunes para detectar patrones inseguros
    secuencias = ["123", "abc", "qwerty", "password", "admin"]
    es_secuencia = any(s in password.lower() for s in secuencias)

    # Revisar si un mismo carácter se repite más de 3 veces (ej: "aaaa")
    es_repetitiva = any(password.count(char) > 3 for char in password)
    
    # 2. Lógica de niveles de seguridad (Jerarquía de validación)
    # Priorizamos las advertencias de patrones simples por ser riesgos altos
    if es_secuencia or es_repetitiva:
        res_texto = "Insegura"
        resultado.config(text="Insegura (Patrón simple detectado)", fg="red")
    elif size < 8:
        res_texto = "Débil"
        resultado.config(text="Débil (Muy corta)", fg="red")
    elif not tiene_numero:
        res_texto = "Media"
        resultado.config(text = "Media (Falta número)", fg = "orange")
    elif not tiene_mayus:
        res_texto = "Media"
        resultado.config(text = "Media (Falta mayúscula)", fg = "orange")
    elif not tiene_minus:
        res_texto = "Media"
        resultado.config(text = "Media (Falta minúscula)", fg = "orange")
    elif not tiene_esp:
        res_texto = "Media"
        resultado.config(text = "Media (Falta carácter especial)", fg = "orange")
    elif size >= 8 and tiene_numero and tiene_mayus and tiene_minus and tiene_esp:
        res_texto = "Fuerte"
        resultado.config(text = "Fuerte", fg = "green")
        
    # 3. Llamamos al registro para guardar la evaluación actual
    registrar_actividad(size, res_texto)

def genPassword():
    """
    Genera una contraseña aleatoria uniendo caracteres de las categorías seleccionadas.
    La longitud se obtiene del widget Scale.
    """
    caracteres = string.ascii_lowercase # Base obligatoria: letras minúsculas
    largo_elegido = escala.get()

    # Condicionales para expandir el pool de caracteres según los Checkbuttons
    if var_mayus.get() == 1:
        caracteres += string.ascii_uppercase
        
    if var_nums.get() == 1:
        caracteres += string.digits
    
    if var_esp.get() == 1:
        caracteres += string.punctuation
        
    # Generación aleatoria usando comprensión de listas
    nueva_password = "".join(random.choice(caracteres) for i in range(largo_elegido))
    
    # Actualización del cuadro de texto (Entry)
    entrada.delete(0, tk.END) # Limpiamos el contenido anterior
    entrada.insert(0, nueva_password) # Insertamos la nueva contraseña

def copiarPortapapeles():
    """Copia el texto del Entry al portapapeles del sistema."""
    password = entrada.get()
    ventana.clipboard_clear() # Limpia el portapapeles
    ventana.clipboard_append(password) # Pega la contraseña

# --- CONFIGURACIÓN DE LA INTERFAZ GRÁFICA ---

# Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Contraseñas Seguras")
ventana.geometry("600x400")

# 1. Título principal centrado
titulo = tk.Label(ventana, text="Sistema de Contraseñas", font=("Arial", 14, "bold"), fg="#235")
titulo.grid(row=0, column=0, columnspan=2, pady=20)

# 2. Campo de entrada para escribir o recibir la contraseña generada
entrada = tk.Entry(ventana, width=30, font=("Courier", 12))
entrada.grid(row=1, column=0, padx=20, pady=5)

# 3. Agrupación de botones de acción en un Frame lateral
frame_botones = tk.Frame(ventana)
frame_botones.grid(row=2, column=1, sticky="n")

btn_evaluar = tk.Button(frame_botones, text="Evaluar", command=checkPassword, width=15)
btn_evaluar.pack(pady=5)
btn_generar = tk.Button(frame_botones, text="Generar", command=genPassword, width=15)
btn_generar.pack(pady=5)
btn_copiar = tk.Button(frame_botones, text="Copiar", command=copiarPortapapeles, width=15)
btn_copiar.pack(pady=5)

# Panel de Configuración usando LabelFrame para mejor organización visual
frame_opciones = tk.LabelFrame(ventana, text=" Configuración ", padx=10, pady=10)
frame_opciones.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

# Variables especiales de Tkinter para capturar el estado de los Checkbuttons
var_mayus = tk.IntVar()
var_nums = tk.IntVar()
var_esp = tk.IntVar()

# Creación de los cuadritos de selección (Checkbuttons)
check_mayus = tk.Checkbutton(frame_opciones, text="Mayúsculas", variable = var_mayus).pack(anchor =  "w")
check_nums = tk.Checkbutton(frame_opciones, text="Números", variable = var_nums).pack(anchor = "w")
check_esp = tk.Checkbutton(frame_opciones, text = "Caracteres Especiales", variable = var_esp).pack(anchor = "w")

# Escala visual para seleccionar la longitud (de 8 a 32 caracteres)
escala = tk.Scale(frame_opciones, from_= 8, to=32, orient="horizontal", label="Longitud")
escala.set(12) # Valor inicial por defecto
escala.pack(fill="x")

# 4. Etiqueta dinámica para mostrar el resultado de la evaluación
resultado = tk.Label(ventana, text="Esperando evaluación...", font=("Arial", 10, "italic"))
resultado.grid(row=1, column=1, padx=20)

# Mantiene la ventana abierta y escuchando eventos
ventana.mainloop()