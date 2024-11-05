import tkinter as tk
from tkinter import ttk
from InterfazGraficaBBS2 import InterfazGrafica

def main():
    # Creamos la ventana principal
    root = tk.Tk()
    
    # Configuración inicial de la ventana - primera ventana
    root.geometry("1000x400")  
    
    # Configurar el estilo global
    style = ttk.Style()
    style.configure("TFrame", background="#E3F2FD")
    style.configure("TLabel", background="#E3F2FD")
    style.configure("Title.TLabel", 
                   font=("Helvetica", 36, "bold"), 
                   background="#E3F2FD",
                   padding=20)
    style.configure("Subtitle.TLabel", 
                   font=("Helvetica", 24, "bold"), 
                   background="#E3F2FD",
                   padding=15)
    
    # Instanciamos la Interfaz grafica
    app = InterfazGrafica(root)
    
    # Bucle principal
    root.mainloop()

if __name__ == "__main__":
    main()