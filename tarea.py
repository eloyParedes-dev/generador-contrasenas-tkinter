import tkinter as tk
import random
import string
from datetime import datetime

def registrar_actividad(longitud, nivel):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Abrimos el archivo en modo 'a' (append) para añadir líneas sin borrar lo anterior
    with open("registro_actividad.txt", "a") as archivo:
        archivo.write(f"Fecha: {fecha} | Longitud: {longitud} | Seguridad: {nivel}\n")

def checkPassword():
    password = entrada.get()
    size = len(password)
    
    # IMPORTANTE: Inicializamos res_texto con un valor por defecto
    res_texto = "No evaluado" 

    if size == 0:
        resultado.config(text="Ingrese una contraseña", fg="red")
        return # Aquí sí salimos porque no hay nada que evaluar

    # 1. Analizamos las características
    tiene_numero = any(char.isdigit() for char in password)
    tiene_mayus = any(char.isupper() for char in password)
    tiene_minus = any(char.islower() for char in password)
    tiene_esp = any(not char.isalnum() for char in password)
    
    # 2. Lógica de niveles (Actualizamos res_texto en cada camino)
    if size < 8:
        res_texto = "Débil"
        resultado.config(text="Débil (Muy corta)", fg="red")
    elif not tiene_numero:
        res_texto = "Media"
        resultado.config(text="Media (Falta número)", fg="orange")
    elif not tiene_mayus:
        res_texto = "Media"
        resultado.config(text="Media (Falta mayúscula)", fg="orange")
    elif not tiene_minus:
        res_texto = "Media"
        resultado.config(text="Media (Falta minúscula)", fg="orange")
    elif not tiene_esp:
        res_texto = "Media"
        resultado.config(text="Media (Falta carácter especial)", fg="orange")
    else:
        res_texto = "Fuerte"
        resultado.config(text="Fuerte", fg="green")
        
    # 3. Llamamos al registro (Ahora res_texto siempre existe)
    registrar_actividad(size, res_texto)

def genPassword():
    caracteres = string.ascii_lowercase # Empezamos solo con minúsculas
    largo_elegido = escala.get()

    # Si el usuario marcó Mayúsculas (var_mayus es 1)
    if var_mayus.get() == 1:
        caracteres += string.ascii_uppercase
        
    # Si el usuario marcó Números (var_nums es 1)
    if var_nums.get() == 1:
        caracteres += string.digits
    
    #Si el usuario marco Especiales (var_esp es 1)
    if var_esp.get() == 1:
        caracteres += string.punctuation
        
    # Generamos una contraseña de 12 caracteres al azar
    nueva_password = "".join(random.choice(caracteres) for i in range(largo_elegido))
    
    # Ponemos la nueva contraseña en el cuadro de entrada (Entry)
    entrada.delete(0, tk.END) # Limpiamos lo que haya primero
    entrada.insert(0, nueva_password) # Insertamos la nueva

def copiarPortapapeles():
    password = entrada.get()
    ventana.clipboard_clear() # Limpia el portapapeles
    ventana.clipboard_append(password) # Pega la contraseña

# Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Contraseñas Seguras")
ventana.geometry("600x400")

# 1. Título (Label)
titulo = tk.Label(ventana, text="Sistema de Contraseñas", font=("Arial", 14, "bold"), fg="#235")
titulo.grid(row=0, column=0, columnspan=2, pady=20)

# 2. Entrada de texto (Entry)
entrada = tk.Entry(ventana, width=30, font=("Courier", 12))
entrada.grid(row=1, column=0, padx=20, pady=5)

# 3. Botón (Button)
frame_botones = tk.Frame(ventana)
frame_botones.grid(row=2, column=1, sticky="n")

btn_evaluar = tk.Button(frame_botones, text="Evaluar", command=checkPassword, width=15)
btn_evaluar.pack(pady=5)
btn_generar = tk.Button(frame_botones, text="Generar", command=genPassword, width=15)
btn_generar.pack(pady=5)
btn_copiar = tk.Button(frame_botones, text="Copiar", command=copiarPortapapeles, width=15)
btn_copiar.pack(pady=5)

frame_opciones = tk.LabelFrame(ventana, text=" Configuración ", padx=10, pady=10)
frame_opciones.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

# Creamos las variables para guardar los estados
var_mayus = tk.IntVar()
var_nums = tk.IntVar()
var_esp = tk.IntVar()

# Creamos los cuadritos de selección (Checkbuttons)
check_mayus = tk.Checkbutton(frame_opciones, text="Mayúsculas", variable = var_mayus).pack(anchor =  "w")
check_nums = tk.Checkbutton(frame_opciones, text="Números", variable = var_nums).pack(anchor = "w")
check_esp = tk.Checkbutton(frame_opciones, text = "Caracteres Especiales", variable = var_esp).pack(anchor = "w")


# Definimos la escala (de 8 a 32, orientada horizontalmente)
escala = tk.Scale(frame_opciones, from_= 8, to=32, orient="horizontal", label="Longitud")
escala.set(12)
escala.pack(fill="x")

#lambda sirve para usar una funcion con parametros

# 4. Etiqueta para el resultado
resultado = tk.Label(ventana, text="Esperando evaluación...", font=("Arial", 10, "italic"))
resultado.grid(row=1, column=1, padx=20)

ventana.mainloop()