import tkinter as tk
import random
import string

def checkPassword(): #Funcion para evaluar la contrasena
    password = entrada.get()
    size = len(password)
    
    tiene_numero = any(char.isdigit() for char in password) #Verifica si tiene numero
    tiene_mayus = any(char.isupper() for char in password)
    tiene_minus = any(char.islower() for char in password)
    tiene_esp = any(not char.isalnum() for char in password)
    
    if size == 0:
        resultado.config(text = "Ingrese una contraseña", fg = "red")
    elif size < 8:
        resultado.config(text = "Débil (Muy corta)", fg = "red")
    elif size >= 8 and not tiene_numero:
        resultado.config(text = "Media (Falta número)", fg = "orange")
    elif size >= 8 and not tiene_mayus:
        resultado.config(text = "Media (Falta mayúscula)", fg = "orange")
    elif size >= 8 and not tiene_minus:
        resultado.config(text = "Media (Falta minúscula)", fg = "orange")
    elif size >= 8 and not tiene_esp:
        resultado.config(text = "Media (Falta carácter especial)", fg = "orange")
    elif size >= 8 and tiene_numero and tiene_mayus and tiene_minus and tiene_esp:
        resultado.config(text = "Fuerte", fg = "green")

def genPassword():
    caracteres = string.ascii_lowercase # Empezamos solo con minúsculas
    largo_elegido = escala.get()

    # Si el usuario marcó Mayúsculas (var_mayus es 1)
    if var_mayus.get() == 1:
        caracteres += string.ascii_uppercase
        
    # Si el usuario marcó Números (var_nums es 1)
    if var_nums.get() == 1:
        caracteres += string.digits
        
    # Generamos una contraseña de 12 caracteres al azar
    nueva_password = "".join(random.choice(caracteres) for i in range(largo_elegido))
    
    # Ponemos la nueva contraseña en el cuadro de entrada (Entry)
    entrada.delete(0, tk.END) # Limpiamos lo que haya primero
    entrada.insert(0, nueva_password) # Insertamos la nueva

# Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Contraseñas Seguras")
ventana.geometry("600x400")

# 1. Título (Label)
titulo = tk.Label(ventana, text = "Evaluador de Seguridad", font = ("Arial", 14, "bold"))
titulo.grid(row = 0, column = 0, pady = 10)

# 2. Entrada de texto (Entry)
entrada = tk.Entry(ventana, width = 20)
entrada.grid(row = 1, column = 0, pady = 5)

# 3. Botón (Button)
boton_evaluar = tk.Button(ventana, text = "Evaluar Contraseña", command = checkPassword)
boton_evaluar.grid(row = 2, column = 0, pady = 10)

# Creamos las variables para guardar los estados
var_mayus = tk.IntVar()
var_nums = tk.IntVar()

# Creamos los cuadritos de selección (Checkbuttons)
check_mayus = tk.Checkbutton(ventana, text="Incluir Mayúsculas", variable=var_mayus)
check_nums = tk.Checkbutton(ventana, text="Incluir Números", variable=var_nums)

# Los acomodamos en el grid
check_mayus.grid(row=3, column=0, sticky="w") # "w" de West para que se alineen a la izquierda
check_nums.grid(row=4, column=0, sticky="w")

# Definimos la escala (de 8 a 32, orientada horizontalmente)
escala = tk.Scale(ventana, from_=8, to=32, orient="horizontal", label="Longitud")
escala.set(12) # Valor por defecto
escala.grid(row=5, column=0, pady=10, sticky="we")

#lambda sirve para usar una funcion con parametros

# 4. Etiqueta para el resultado
resultado = tk.Label(ventana, fg="blue")
resultado.grid(row = 1, column = 1, pady = 10)

ventana.mainloop()