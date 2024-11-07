import tkinter as tk
from tkinter import ttk, filedialog, PhotoImage
from ClasesBBS import Simulacion

#Clase de la interfaz Grafica

class InterfazGrafica:


    #Crea la primera presentacion que se ve del simulador, las proxims se iran creando en los metodos
    def __init__(self, root):

        #Creamos la ventana
        self.simulador = None 
        self.root = root
        self.root.title('Simulador de Procesador') #Nombre de la ventana
        self.main_frame = ttk.Frame(root) 
        self.main_frame.grid(column= 0, row= 0) #Insertamos el mainframe en el borde sup izquierdo de la ventana

        #Añadimos el titulo de nuestro proyecto
        self.label_titulo1 = ttk.Label(self.main_frame, text= 'TPI - SISTEMAS OPERATIVOS', font= ('Times New Roman', 30, 'bold'))
        self.label_titulo1.grid(row=0, column= 1) #Pegamos el titulo en la primera linea de la ventana

        self.label_titulo2 = ttk.Label(self.main_frame, text= 'BIG BRAIN SIX', font= ('Times New Roman', 30, 'bold'))
        self.label_titulo2.grid(row=1, column= 0, columnspan=3) #Pegamos el titulo en la primera linea de la ventana


        #Creamos las imagenes
        self.logoUTN = PhotoImage(file='logoutn.png').subsample(10,10)
        self.label_logoUTN1 = ttk.Label(self.main_frame, image= self.logoUTN)
        self.label_logoUTN2 = ttk.Label(self.main_frame, image= self.logoUTN)
        self.label_logoUTN1.grid(column=0, row=0)
        self.label_logoUTN2.grid(column=2, row=0)

        self.logoEquipo = PhotoImage(file='logoEquipo.png').subsample(2,2)
        self.label_logoEquipo = ttk.Label(self.main_frame, image= self.logoEquipo)
        self.label_logoEquipo.grid(column=1, row=2)



        #Creamos boton para cargar archivo
        self.button_cargarArchivo = ttk.Button(self.main_frame, text = 'Cargar Archivo p/Simulacion', command= self.tratamientoArchivo, padding= '10', width= 30)
        self.button_cargarArchivo.grid(row= 3, column= 0, columnspan= 3, pady= 10)


    def tratamientoArchivo(self):

        #Abre el archivo con el metodo de filedialog
        archv = filedialog.askopenfilename(title= 'Abrir un archivo', filetypes= [('Archivos CSV', '*.csv')])

        #Instanciamos el simulador con el archivo recibido 
        self.simulador = Simulacion(archv)
        self.interfazSimulacion()

    #Simulacion del procesador
    def interfazSimulacion(self):

        #Eliminar las etiquetas y botones que ya estaban en pantalla
        self.button_cargarArchivo.destroy()
        self.label_titulo2.destroy()
        self.label_titulo1.destroy()
        self.label_logoUTN1.destroy()
        self.label_logoUTN2.destroy()
        self.label_logoEquipo.destroy()

        if self.simulador.banderaError: 
            
            alerta = tk.Toplevel(self.root, padx=30, pady=30)
            alerta.title('ADVERTENCIA!!')
            ttk.Label(alerta, text= 'El archivo que ingresaste tiene un error', font= ('Times New Roman', 20)).grid(column=0, row=0, columnspan= 4, padx=5, pady=5)
            ttk.Label(alerta, text= 'Revisar el archivo y volve a cargar', font= ('Times New Roman', 20)).grid(column=0, row=1, columnspan= 4, padx=5, pady=5)
        
        else:

            if self.simulador.procesosMas10 > 10:
                alerta = tk.Toplevel(self.root, padx=30, pady=30)
                alerta.title('ADVERTENCIA!!')
                ttk.Label(alerta, text= 'El archivo que ingresaste tiene mas de 10 procesos', font= ('Times New Roman', 20)).grid(column=0, row=0, columnspan= 4, padx=5, pady=5)
                ttk.Label(alerta, text= 'Se cargaron los 10 primeros discriminados por tamaño máximo e id respectivamente', font= ('Times New Roman', 20)).grid(column=0, row=1, columnspan= 4, padx=5, pady=5)
        

            self.logoUTN = PhotoImage(file='logoutn.png').subsample(15,15)
            self.label_logoUTN = ttk.Label(self.main_frame, image= self.logoUTN)
            self.label_logoUTN.grid(column=0, row=0, padx=10, pady=10)
            self.label_espacioBlanco = ttk.Label(self.main_frame, text= ' ')
            self.label_espacioBlanco.grid(row=0, column=2, padx=10, pady=10)

            #Creamos todas las etiquetas de lo que vamos a mostrar por pantalla y su ubicaion

            #titulo
            self.label_tituloSim = ttk.Label(self.main_frame, text= 'Simulador de Procesador - BBS', font= ('Times New Roman', 20, 'bold'), justify='center')
            self.label_tituloSim.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

            #Tiempo y Quantum
            self.label_tiempo = ttk.Label(self.main_frame, text= 'Tiempo: ', font=('Arial', 15))
            self.label_tiempo.grid(row=1, column=0, padx=5, pady=5)

            self.label_quantum = ttk.Label(self.main_frame, text= 'Quantum: ', font=('Arial', 15))
            self.label_quantum.grid(row=1, column=1, padx=5, pady=5)

            #Creamos estilo para las fuentes de la memoria y CPU
            style = ttk.Style()
            style.configure('EstiloM.TLabel', font=('Arial', 13), foreground= 'blue')

            style2 = ttk.Style()
            style2.configure('EstiloCPU.TLabel', font=('Arial', 15), foreground= 'violet') 

            #Memoria 
            self.label_memoria = ttk.Label(self.main_frame, text='Memoria Principal', style= 'EstiloM.TLabel')
            self.label_memoria.grid(row=2, column=0, padx=5, pady=5)

            #CPU
            self.label_cpu = ttk.Label(self.main_frame, text= 'Estado de la CPU', style= 'EstiloCPU.TLabel')
            self.label_cpu.grid(row=2, column=1, padx=5, pady=5)

            #Cola de Listos
            self.label_colaListos = ttk.Label(self.main_frame, text= 'Cola de Listos: ', font=('Arial', 15))
            self.label_colaListos.grid(row=3, column=0, padx=5, pady=5)

            #Cola de Listos/Suspendidos
            self.label_colaSuspen = ttk.Label(self.main_frame, text='Cola de Suspendidos: ', font=('Arial', 15))
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

            
            #Centramos el texto en cada columna
            for col in ("#1", "#2", "#3", "#4", "#5", "#6"):
                self.tabla_procesos.column(col, anchor=tk.CENTER)


            #Creamos nuestra tabla en la interfaz
            self.tabla_procesos.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

            #Creamos botones para ir recorriendo la simulacion
            self.button_avanzar = ttk.Button(self.main_frame, text='Siguiente Instante', command= self.avanzar)
            self.button_avanzar.grid(row=7, column=0, pady=5)
            self.button_avanzarEvento = ttk.Button(self.main_frame, text='Siguiente Evento', command= self.avanzarEvento)
            self.button_avanzarEvento.grid(row=7, column=1, pady=5)


    
    #Metodo para avanzar en la simulacion, se llama cada vez que se pulsa el boton
    def avanzar(self):

        self.simulador.avanzar() #Avanza la simulacion con el metodo de la clase Simulacion

        #Actualiza valores de Tiempo y Quantum
        self.label_tiempo.config(text= f'Tiempo: {self.simulador.clock} u.t.') #Muestra el clock del simulador
        self.label_quantum.config(text= f'Quantum: {self.simulador.quantum} u.t.') #Muestra el quantum del simulador

        #Estado de Memoria principal
        #Lo creamos en una variable para mayor prolijidad
        textoEstadoMem = 'Particiones\tID Proceso\tUSO/TOTAL\tFRAG. Interna\n'

        for particion in self.simulador.memoria.particiones:
            idP = None if particion.proceso is None else particion.proceso.id
            usado = 0 if particion.proceso is None else particion.proceso.tamaño
            total = particion.tamaño

            textoEstadoMem += f'{particion.id}\t\t{idP if particion.id != 1 else 'SO'}\t\t{usado}kb / {total}kb\t{total - usado if particion.proceso != None else '0'}kb\n'

        
        #Inserto texto concatenado a la interfaz
        self.label_memoria.config(text=' \t\tMEMORIA PRINCIPAL \n\n' + textoEstadoMem)


        #Mostrar cola de listos 
        textoColaListos = 'Cola de Listos: ' + ' - '.join('P. ' + str(proceso.id) for proceso in self.simulador.cola_listos if proceso.estado != 'running')
        self.label_colaListos.config(text= textoColaListos, justify='left')

        #Mostrar cola de listo/suspendido
        textoColaSuspend= 'Cola de Suspendidos: ' + ' - '.join('P. '+ str(proceso.id) for proceso in self.simulador.cola_suspendidos)
        self.label_colaSuspen.config(text= textoColaSuspend, justify='left')

        #Mostramos estado de la CPU
        procesoCPU = self.simulador.cpu.proceso
        textoCPU = 'ID Proceso\t\tTAMAÑO\t\tT. RESTANTE\n'
        if procesoCPU:
            textoCPU += f'{procesoCPU.id}\t\t\t{procesoCPU.tamaño}kb\t\t\t{procesoCPU.t_irrup_faltante} u.t.'
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
            self.tabla_procesos.insert('', 'end', values=(proceso.id, f'{proceso.tamaño}kb',
                                                           proceso.estado, f'{proceso.t_arribo} u.t.', f'{proceso.t_irrupcion} u.t.',
                                                            f'{proceso.t_irrup_faltante} u.t.'))


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

        if self.simulador.total_procesos == 0:
            
            ttk.Label(ventanaEstadisticas, text= 'No hay ningun proceso cargado', font= ('Times New Roman', 20)).grid(column=0, row=0, columnspan= 4, padx=5, pady=5)
        
        else:

            ttk.Label(ventanaEstadisticas, text= 'Informe de Estadisticas de la Simulacion', font= ('Times New Roman', 20)).grid(column=0, row=0, columnspan= 4, padx=5, pady=5)

            #Recorremos los procesos terminados
            linea = 1
            for proceso in sorted(self.simulador.procesos_terminados, key= lambda x: x.id):

                ttk.Label(ventanaEstadisticas, text= f'Proceso {proceso.id}:', font=('Arial', 12)).grid(column=0, row= linea, padx=10, pady=10)
                ttk.Label(ventanaEstadisticas, text= f'Tiempo Retorno = {proceso.t_retorno} u.t.', font=('Arial', 12)).grid(column=1, row=linea, padx=10, pady=10)
                ttk.Label(ventanaEstadisticas, text= f'Tiempo Espera = {proceso.t_espera} u.t.', font=('Arial', 12)).grid(column=2, row=linea, padx=10, pady=10)
                ttk.Label(ventanaEstadisticas, text= f'Finalizado en: {proceso.t_finalizado} u.t.', font=('Arial', 12)).grid(column=3, row=linea, padx=10, pady=10)
                linea += 1
                
            
            #Calcular y Mostrar Promedios
            promedioEspera = self.simulador.t_espera_total / self.simulador.total_procesos
            promedioRetorno = self.simulador.t_retorno_total / self.simulador.total_procesos
            rendimiento = self.simulador.total_procesos / self.simulador.clock 

            ttk.Label(ventanaEstadisticas, text=f'Tiempo de Retorno Promedio = {round(promedioRetorno, 3)} u.t.', font=('Arial', 12)).grid(column=0, row=11, padx=10, pady=10, columnspan=4)
            ttk.Label(ventanaEstadisticas, text=f'Tiempo de Espera Promedio = {round(promedioEspera, 3)} u.t.', font=('Arial', 12)).grid(column=0, row=12, padx=10, pady=10, columnspan=4)
            ttk.Label(ventanaEstadisticas, text=f'El Rendimiento obtenido en: {self.simulador.clock} u.t. es de {round(rendimiento, 3)} procesos/u.t.', font=('Arial', 12)).grid(column=0, row=13, padx=10, pady=10, columnspan=4)


    def avanzarEvento(self):
        vueltas = 0
        while (vueltas == 0) or (self.simulador.quantum != 3):
            self.avanzar()
            vueltas += 1


