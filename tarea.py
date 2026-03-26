import tkinter as tk

def checkPassword():
    password = entrada.get()
    if len(password) < 8:
        resultado["text"] = "Contrasena corta"
    else:
        resultado["text"] = "Contrasena larga" 

# Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Contraseñas Seguras")
ventana.geometry("400x300")

# 1. Título (Label)
titulo = tk.Label(ventana, text = "Evaluador de Seguridad", font = ("Arial", 14, "bold"))
titulo.pack(pady = 10)

# 2. Entrada de texto (Entry)
entrada = tk.Entry(ventana, width = 30)
entrada.pack(pady = 5)

# 3. Botón (Button)
boton_evaluar = tk.Button(ventana, text = "Evaluar Contraseña", command = checkPassword)
boton_evaluar.pack(pady = 10)
#lambda sirve para usar una funcion con parametros

# 4. Etiqueta para el resultado
resultado = tk.Label(ventana, fg="blue")
resultado.pack(pady = 10)

#5. Ponerlos a la izquierda
titulo.grid(row = 0, column = 0)
entrada.grid(row = 1, column = 0)
boton_evaluar.grid(row = 2, column = 0)
resultado.grid(row = 1, column = 1)

ventana.mainloop()
