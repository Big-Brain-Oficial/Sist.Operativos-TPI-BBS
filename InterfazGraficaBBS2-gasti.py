import tkinter as tk
from tkinter import ttk, filedialog, PhotoImage
from Clases2BBS import Simulacion

#Clase de la interfaz Grafica

class InterfazGrafica:


    #Crea la primera presentacion que se ve del simulador, las proxims se iran creando en los metodos
    import tkinter as tk
from tkinter import ttk, filedialog, font
from Clases2BBS import Simulacion

class InterfazGrafica:

    def __init__(self, root):
        self.simulador = None
        self.root = root
        self.root.title('Simulador de Procesador')
        self.root.geometry("1000x400")  # Reducir altura de 600 a 400
        self.root.configure(bg="#E3F2FD")

        # Frame principal 
        self.main_frame = ttk.Frame(self.root, style="TFrame")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)

        # Frame superior para contener los títulos y botón
        top_frame = ttk.Frame(self.main_frame, style="TFrame")
        top_frame.pack(fill=tk.X, pady=(50, 20))  # Reducir padding inferior

        # Título principal
        self.label_titulo = ttk.Label(top_frame, 
                                 text="TPI - Sistemas Operativos",
                                 style="Title.TLabel")
        self.label_titulo.pack(pady=(0, 20))

        # Subtítulo
        self.label_subtitulo = ttk.Label(top_frame,
                                    text="BIG BRAIN SIX",
                                    style="Subtitle.TLabel")
        self.label_subtitulo.pack(pady=(0, 30))

        # Botón de cargar archivo
        self.button_cargarArchivo = ttk.Button(top_frame,
                                         text="Cargar Archivo de Simulación",
                                         style="Custom.TButton",
                                         command=self.tratamientoArchivo)
        self.button_cargarArchivo.pack(pady=(0, 20))

    def tratamientoArchivo(self):

        #Abre el archivo con el metodo de filedialog
        archv = filedialog.askopenfilename(title= 'Abrir un archivo', filetypes= [('Archivos CSV', '*.csv')])

        #Instanciamos el simulador con el archivo recibido 
        self.simulador = Simulacion(archv)
        self.interfazSimulacion()

    #Simulacion del procesador
    def interfazSimulacion(self):
        # Limpiar widgets anteriores
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        self.button_cargarArchivo.destroy()
        self.label_titulo.destroy()
        self.label_subtitulo.destroy()

        # Obtener dimensiones de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

            # Calcular posición x,y para el centro
        window_width = 1300
        window_height = 610
        position_x = (screen_width - window_width) // 2
        position_y = (screen_height - window_height) // 2
        

        self.root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")


        # Título con más espacio
        self.label_tituloSim = ttk.Label(self.main_frame, 
                                        text='Simulador de Procesador - BBS', 
                                        font=('Times New Roman', 20, 'bold'), 
                                        justify='center')
        self.label_tituloSim.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        # Tiempo y Quantum con más espacio
        self.label_tiempo = ttk.Label(self.main_frame, text='Tiempo: ')
        self.label_tiempo.grid(row=1, column=0, padx=20, pady=10)

        self.label_quantum = ttk.Label(self.main_frame, text='Quantum: ')
        self.label_quantum.grid(row=1, column=1, padx=20, pady=10)

        #Eliminar tambien las imagenes que agreguemos

        #Creamos todas las etiquetas de lo que vamos a mostrar por pantalla y su ubicaion

        #titulo
        self.label_tituloSim = ttk.Label(self.main_frame, text= 'Simulador de Procesador - BBS', font= ('Times New Roman', 20, 'bold'), justify='center')
        self.label_tituloSim.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        #Tiempo y Quantum
        self.label_tiempo = ttk.Label(self.main_frame, text= 'Tiempo: ')
        self.label_tiempo.grid(row=1, column=0, padx=5, pady=5)

        self.label_quantum = ttk.Label(self.main_frame, text= 'Quantum: ')
        self.label_quantum.grid(row=1, column=1, padx=5, pady=5)

        #Memoria 
        self.label_memoria = ttk.Label(self.main_frame, text='Memoria Principal')
        self.label_memoria.grid(row=2, column=0, padx=5, pady=5)

        #CPU
        self.label_cpu = ttk.Label(self.main_frame, text= 'Estado de la CPU')
        self.label_cpu.grid(row=2, column=1, padx=5, pady=5)

        #Cola de Listos
        self.label_colaListos = ttk.Label(self.main_frame, text= 'Cola de Listos: ')
        self.label_colaListos.grid(row=3, column=0, padx=5, pady=5)

        #Cola de Listos/Suspendidos
        self.label_colaSuspen = ttk.Label(self.main_frame, text='Cola de Suspendidos: ')
        self.label_colaSuspen.grid(row=3, column=1, padx=5, pady=5)

        #Separador ----> Informacion general / Pocesos
        ttk.Separator(self.main_frame, orient='horizontal').grid(row=5, column=0, columnspan=10, sticky= 'ew', pady=5)

        #Procesos Cargados 

        #Titulo
        self.label_procesosCargados = ttk.Label(self.main_frame, text= 'Procesos Cargados', font=('Times New Roman', 10))
        self.label_procesosCargados.grid(row=5, column=0, columnspan=10, pady=5)

        #Creamos treeview, estructura de arbol que nos permitira hacer una tabla en la pantalla
        self.tabla_procesos = ttk.Treeview(self.main_frame, columns=('id', 'tamaño', 'estado', 'tArribo', 'tIrrup', 'tRestante'))

        #Configuramos sus "marcos" horizontales y verticales
        self.tabla_procesos.heading('#0', text= 'ID') #se indexa segun id
        self.tabla_procesos.column('#0', width=0, stretch=tk.NO) #se oculta la barra horizontal

        #Definimos los nombres para los titulos de las columnas
        self.tabla_procesos.heading('id', text='ID')
        self.tabla_procesos.heading('tamaño', text='TAMAÑO')
        self.tabla_procesos.heading('estado', text='ESTADO')
        self.tabla_procesos.heading('tArribo', text='T. ARRIBO')
        self.tabla_procesos.heading('tIrrup', text='T. IRRUPCION')
        self.tabla_procesos.heading('tRestante', text='T. RESTANTE')

        #Creamos nuestra tabla en la interfaz
        self.tabla_procesos.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        #Creamos boton para ir recorriendo la simulacion
        self.button_avanzar = ttk.Button(self.main_frame, text='Siguiente Estado', command= self.avanzar)
        self.button_avanzar.grid(row=7, column=0, pady=5)
        self.button_avanzarEvento = ttk.Button(self.main_frame, text='Siguiente Evento', command= self.avanzarEvento)
        self.button_avanzarEvento.grid(row=7, column=1, pady=5)

        #self.avanzar()

    
    #Metodo para avanzar en la simulacion, se llama cada vez que se pulsa el boton
    def avanzar(self):

        self.simulador.avanzar() #Avanza la simulacion con el metodo de la clase Simulacion

        #Actualiza valores de Tiempo y Quantum
        self.label_tiempo.config(text= f'Tiempo: {self.simulador.clock}') #Muestra el clock del simulador
        self.label_quantum.config(text= f'Quantum: {self.simulador.quantum}') #Muestra el quantum del simulador

        #Estado de Memoria principal
        #Lo creamos en una variable para mayor prolijidad
        textoEstadoMem = 'Particiones\t\tID Proceso\t\tUSO/TOTAL\n'

        for particion in self.simulador.memoria.particiones:
            idP = None if particion.proceso is None else particion.proceso.id
            usado = 0 if particion.proceso is None else particion.proceso.tamaño
            total = particion.tamaño

            textoEstadoMem += f'{particion.id}\t\t\t{idP if particion.id != 1 else 'SO'}\t\t\t{usado}/{total}\n'

        
        #Inserto texto concatenado a la interfaz
        self.label_memoria.config(text=' \t\tMEMORIA PRINCIPAL \n\n' + textoEstadoMem)


        #Mostrar cola de listos 
        textoColaListos = 'Cola de Listos: ' + ' - '.join('P. ' + str(proceso.id) for proceso in self.simulador.cola_listos)
        self.label_colaListos.config(text= textoColaListos, justify='left')

        #Mostrar cola de listo/suspendido
        textoColaSuspend= 'Cola de Suspendidos: ' + ' - '.join('P. '+ str(proceso.id) for proceso in self.simulador.cola_suspendidos)
        self.label_colaSuspen.config(text= textoColaSuspend, justify='left')

        #Mostramos estado de la CPU
        procesoCPU = self.simulador.cpu.proceso
        textoCPU = 'ID Proceso\t\tTAMAÑO\t\tT. RESTANTE\n'
        if procesoCPU:
            textoCPU += f'{procesoCPU.id}\t\t\t{procesoCPU.tamaño}\t\t\t\t{procesoCPU.t_irrup_faltante}'
        else:
            textoCPU += ' - '

        self.label_cpu.config(text=' \t\t\tCPU \n\n' + textoCPU)

        #Actualizamos la tabla 

        #Borramos la informacion del arbol actual 
        self.tabla_procesos.delete(*self.tabla_procesos.get_children())

        #Actualizamos la informacion que muestra
        for proceso in sorted((self.simulador.cola_listos + self.simulador.cola_suspendidos + 
                              self.simulador.procesos_terminados + self.simulador.procesos_nuevos +
                                self.simulador.lista_procesos), key= lambda x: x.id):
            self.tabla_procesos.insert('', 'end', values=(proceso.id, proceso.tamaño,
                                                           proceso.estado, proceso.t_arribo, proceso.t_irrupcion,
                                                            proceso.t_irrup_faltante))


        #Si a no hay procesos restantes se pasa a mostrar el informe estadistico
        if not self.simulador.existen_procesos_restantes():
            self.button_avanzar.configure(state= tk.DISABLED)
            self.button_avanzarEvento.configure(state= tk.DISABLED)
            self.mostrarInforme()
        else: 
            self.simulador.incrementar_clock()


    #Metodo para mostrar una ventana con los Resultados de los informes estadisticos
    def mostrarInforme(self):

        #Creamos la ventama
        ventanaEstadisticas = tk.Toplevel(self.root, padx=30, pady=30)
        ventanaEstadisticas.title('INFORME ESTADISTICO')

        ttk.Label(ventanaEstadisticas, text= 'Informe de Estadisticas de la Simulacion', font= ('Times New Roman', 20)).pack()

        #Recorremos los procesos terminados
        for proceso in sorted(self.simulador.procesos_terminados, key= lambda x: x.id):

            ttk.Label(ventanaEstadisticas, text= f'Proceso {proceso.id}:\t Tiempo Retorno = {proceso.t_retorno}\t\t Tiempo Espera = {proceso.t_espera}\t\t Finalizado en: {proceso.t_finalizado}\n', font=('Arial', 12)).pack()
            
        
        #Calcular y Mostrar Promedios
        promedioEspera = self.simulador.t_espera_total / self.simulador.total_procesos
        promedioRetorno = self.simulador.t_retorno_total / self.simulador.total_procesos

        ttk.Label(ventanaEstadisticas, text=f'Tiempo de Retorno Promedio = {round(promedioRetorno, 3)}\n', font=('Arial', 12)).pack()
        ttk.Label(ventanaEstadisticas, text=f'Tiempo de Espera Promedio = {round(promedioEspera, 3)}\n', font=('Arial', 12)).pack()


    def avanzarEvento(self):
        vueltas = 0
        while (vueltas == 0) or (self.simulador.quantum != 3):
            self.avanzar()
            vueltas += 1

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazGrafica(root)
    root.mainloop()
