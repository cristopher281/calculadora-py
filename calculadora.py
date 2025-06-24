import tkinter as tk
from tkinter import ttk
import math

memoria = 0

def escribir (valor):
    entrada.insert(tk.END, valor) # type: ignore
        
        
def limpiar ():
    entrada.delete(0, tk.END)

def borrar():
    if entrada.get():
        entrada.delete(len(entrada.get())-1)

def calcular():
    try:
        expresion = entrada.get()
        # Reemplazar funciones para eval
        expresion = expresion.replace('sin(', 'math.sin(math.radians(')
        expresion = expresion.replace('cos(', 'math.cos(math.radians(')
        expresion = expresion.replace('tan(', 'math.tan(math.radians(')
        expresion = expresion.replace('log(', 'math.log10(')
        expresion = expresion.replace('ln(', 'math.log(')
        expresion = expresion.replace('√(', 'math.sqrt(')
        expresion = expresion.replace('π', str(math.pi))
        expresion = expresion.replace('e', str(math.e))

        resultado = eval(expresion)
        limpiar()
        escribir(str(resultado))
    except:
        limpiar()
        escribir("Error")
        
# Funciones científicas
def seno():
    try:
        valor = float(entrada.get())
        resultado = math.sin(math.radians(valor))
        limpiar()
        escribir(str(resultado))
    except:
        limpiar()
        escribir("Error")

def coseno():
    try:
        valor = float(entrada.get())
        resultado = math.cos(math.radians(valor))
        limpiar()
        escribir(str(resultado))
    except:
        limpiar()
        escribir("Error")

def tangente():
    try:
        valor = float(entrada.get())
        resultado = math.tan(math.radians(valor))
        limpiar()
        escribir(str(resultado))
    except:
        limpiar()
        escribir("Error")

def logaritmo():
    try:
        valor = float(entrada.get())
        if valor > 0:
            resultado = math.log10(valor)
            limpiar()
            escribir(str(resultado))
        else:
            limpiar()
            escribir("Error")
    except:
        limpiar()
        escribir("Error")

def logaritmo_natural():
    try:
        valor = float(entrada.get())
        if valor > 0:
            resultado = math.log(valor)
            limpiar()
            escribir(str(resultado))
        else:
            limpiar()
            escribir("Error")
    except:
        limpiar()
        escribir("Error")

def exponencial():
    try:
        valor = float(entrada.get())
        resultado = math.exp(valor)
        limpiar()
        escribir(str(resultado))
    except:
        limpiar()
        escribir("Error")

def potencia():
    escribir("")

def raiz_cuadrada():
    try:
        valor = float(entrada.get())
        if valor >= 0:
            resultado = math.sqrt(valor)
            limpiar()
            escribir(str(resultado))
        else:
            limpiar()
            escribir("Error")
    except:
        limpiar()
        escribir("Error")

def factorial():
    try:
        valor = int(float(entrada.get()))
        if valor >= 0:
            resultado = math.factorial(valor)
            limpiar()
            escribir(str(resultado))
        else:
            limpiar()
            escribir("Error")
    except:
        limpiar()
        escribir("Error")

def porcentaje():
    try:
        valor = float(entrada.get())
        resultado = valor / 100
        limpiar()
        escribir(str(resultado))
    except:
        limpiar()
        escribir("Error")
# Funciones de memoria
def memoria_sumar():
    global memoria
    try:
        memoria += float(entrada.get())
        status_label.config(text="M+")
    except:
        pass

def memoria_restar():
    global memoria
    try:
        memoria -= float(entrada.get())
        status_label.config(text="M-")
    except:
        pass

def memoria_limpiar():
    global memoria
    memoria = 0
    status_label.config(text="MC")

def memoria_recuperar():
    limpiar()
    escribir(str(memoria))

def crear_boton(parent, texto, fila, columna, comando, color_fondo="#f0f0f0", color_texto="black", ancho=1, alto=1):
    """Crear un botón personalizado con estilo"""
    boton = tk.Button(
        parent,
        text=texto,
        command=comando,
        bg=color_fondo,
        fg=color_texto,
        font=("Arial", 12, "bold"),
        width=6,
        height=2,
        relief="raised",
        bd=2,
        activebackground="#e0e0e0"
    )
    boton.grid(row=fila, column=columna, columnspan=ancho, rowspan=alto, padx=2, pady=2, sticky="nsew")
    return boton

if __name__ == "__main__":
    # Crear ventana principal
    ventana = tk.Tk()
    ventana.title("Calculadora Científica")
    ventana.geometry("500x600")
    ventana.resizable(False, False)
    ventana.configure(bg="#2c3e50")

    # Configurar el grid
    for i in range(10):
        ventana.grid_rowconfigure(i, weight=1)
    for i in range(6):
        ventana.grid_columnconfigure(i, weight=1)

    # Frame para la pantalla
    frame_pantalla = tk.Frame(ventana, bg="#2c3e50")
    frame_pantalla.grid(row=0, column=0, columnspan=6, padx=10, pady=10, sticky="ew")

    # Label de estado (memoria)
    status_label = tk.Label(frame_pantalla, text="", bg="#2c3e50", fg="white", font=("Arial", 10))
    status_label.pack(anchor="ne")

    # Campo de entrada
    entrada = tk.Entry(
        frame_pantalla,
        width=30,
        font=("Arial", 16, "bold"),
        justify="right",
        bg="white",
        fg="black",
        bd=3,
        relief="sunken"
    )
    entrada.pack(fill="x", pady=5)
# Fila 1: Funciones de memoria y limpieza
    crear_boton(ventana, "MC", 1, 0, memoria_limpiar, "#cad93c", "white")
    crear_boton(ventana, "MR", 1, 1, memoria_recuperar, "#d3e73c", "white")
    crear_boton(ventana, "M+", 1, 2, memoria_sumar, "#e74c3c", "white")
    crear_boton(ventana, "M-", 1, 3, memoria_restar, "#e74c3c", "white")
    crear_boton(ventana, "C", 1, 4, limpiar, "#3f2801", "white")
    crear_boton(ventana, "←", 1, 5, borrar, "#aa6900", "white")

    # Fila 2: Funciones científicas superiores
    crear_boton(ventana, "sin", 2, 0, seno, "#a0afba", "white")
    crear_boton(ventana, "cos", 2, 1, coseno, "#70777c", "white")
    crear_boton(ventana, "tan", 2, 2, tangente, "#77797b", "white")
    crear_boton(ventana, "log", 2, 3, logaritmo, "#666e72", "white")
    crear_boton(ventana, "ln", 2, 4, logaritmo_natural, "#595c5f", "white")
    crear_boton(ventana, "(", 2, 5, lambda: escribir("("), "#95a5a6", "white")

    # Fila 3: Más funciones científicas
    crear_boton(ventana, "√", 3, 0, raiz_cuadrada, "#34db85", "white")
    crear_boton(ventana, "x²", 3, 1, lambda: escribir("**2"), "#34db6c", "white")
    crear_boton(ventana, "xʸ", 3, 2, potencia, "#34db60", "white")
    crear_boton(ventana, "x!", 3, 3, factorial, "#34db47", "white")
    crear_boton(ventana, "%", 3, 4, porcentaje, "#42db34", "white")
    crear_boton(ventana, ")", 3, 5, lambda: escribir(")"), "#95a5a6", "white")

    # Fila 4: Constantes y división
    crear_boton(ventana, "π", 4, 0, lambda: escribir(str(math.pi)), "#9b59b6", "white")
    crear_boton(ventana, "e", 4, 1, lambda: escribir(str(math.e)), "#9b59b6", "white")
    crear_boton(ventana, "exp", 4, 2, exponencial, "#3498db", "white")
    crear_boton(ventana, "7", 4, 3, lambda: escribir("7"), "#ecf0f1", "black")
    crear_boton(ventana, "8", 4, 4, lambda: escribir("8"), "#ecf0f1", "black")
    crear_boton(ventana, "9", 4, 5, lambda: escribir("9"), "#ecf0f1", "black")

    # Fila 5: Números y multiplicación
    crear_boton(ventana, "÷", 5, 0, lambda: escribir("/"), "#34495e", "white")
    crear_boton(ventana, "×", 5, 1, lambda: escribir("*"), "#34495e", "white")
    crear_boton(ventana, "-", 5, 2, lambda: escribir("-"), "#34495e", "white")
    crear_boton(ventana, "4", 5, 3, lambda: escribir("4"), "#ecf0f1", "black")
    crear_boton(ventana, "5", 5, 4, lambda: escribir("5"), "#ecf0f1", "black")
    crear_boton(ventana, "6", 5, 5, lambda: escribir("6"), "#ecf0f1", "black")

    # Fila 6: Números y suma
    crear_boton(ventana, "+", 6, 0, lambda: escribir("+"), "#34495e", "white")
    crear_boton(ventana, "±", 6, 1, lambda: entrada.insert(0, "-") if not entrada.get().startswith("-") else entrada.delete(0), "#34495e", "white")
    crear_boton(ventana, ".", 6, 2, lambda: escribir("."), "#34495e", "white")
    crear_boton(ventana, "1", 6, 3, lambda: escribir("1"), "#ecf0f1", "black")
    crear_boton(ventana, "2", 6, 4, lambda: escribir("2"), "#ecf0f1", "black")
    crear_boton(ventana, "3", 6, 5, lambda: escribir("3"), "#ecf0f1", "black")

    # Fila 7: Cero y igual
    crear_boton(ventana, "0", 7, 0, lambda: escribir("0"), "#ecf0f1", "black", ancho=3)
    crear_boton(ventana, "=", 7, 3, calcular, "#27ae60", "white", ancho=3)

    # Información en la parte inferior
    info_label = tk.Label(
        ventana,
        text="Calculadora Científica v1.0 | Tkinter",
        bg="#2c3e50",
        fg="#bdc3c7",
        font=("Arial", 8)
    )
    info_label.grid(row=8, column=0, columnspan=6, pady=5)
    
    # Iniciar el bucle principal
    ventana.mainloop()
    # Cerrar la ventana al salir
    ventana.destroy()
    print("Calculadora cerrada.")
    print("Memoria:", memoria)
    