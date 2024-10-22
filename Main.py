import tkinter as tk
from InterfazGraficaBBS import InterfazGrafica

def main():

    #Creamos la ventana principal
    root = tk.Tk()

    #Instanciamos la Interfaz grafica y le pasamos la ventana como parametro
    app = InterfazGrafica(root)

    #Bucle principal de la ventana
    root.mainloop()

#Verifica que el codigo sea llamado directamente
if __name__ == "__main__":
   main() 