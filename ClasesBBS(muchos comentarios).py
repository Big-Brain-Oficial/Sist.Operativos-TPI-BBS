import csv

#Definicion de constantes
TAM_MAX_PROC = 250
ESTADO_LISTO = 'ready'
ESTADO_SUSPENDIDO = 'suspended'
ESTADO_EJECUCION = 'running'
ESTADO_NUEVO = 'new'
ESTADO_TERMINADO = 'exit'
QUANTUM = 3

class Memoria: 
    #Particiones de la memoria
    def __init__(self):
        self.particiones = [
            Particion(1, 100, '0k', Proceso(0, 100, 0, 0)),          #Particion del sistema operativo
            Particion(2, 250, '100k'),
            Particion(3, 150, '350k'),
            Particion(4, 50, '400k')
        ]
    
    #Metodo para asignar un programa para una particion
    def asignar_procesos(self, proceso, particion):
        #proceso.estado = ESTADO_LISTO
        particion.proceso = proceso

#Clase que contiene el programa en ejecucion, "Estado del Procesador"
class CPU:  
    def __init__(self):
        self.proceso = None
    
    def ejecutar_proceso(self, proceso):
        proceso.estado = ESTADO_EJECUCION
        self.proceso = proceso
    
    def liberar_proceso(self):
        self.proceso = None

class Particion:
    def __init__(self, id, tam, dir, proceso = None):
        self.id = id
        self.tamaño = tam
        self.direccion = dir
        self.proceso = proceso
        self.fragmentacion = tam

class Proceso: 
    def __init__(self, id, tam, ta, ti):
        self.id = id
        self.tamaño = tam
        self.estado = '-'
        self.t_arribo = ta #Tiempo que tarda el proceso en llegar
        self.t_irrupcion = ti #Tiempo total que tarda el proceso usando la CPU
        self.t_irrup_faltante = ti #Tiempo que le falta al proceso haciendo uso de la CPU
        self.t_retorno = 0 #Tiempo que trasncure un proceso entre la cola de listos y ejecucion
        self.t_espera = 0 #Tiempo que trasncure un proceso entre la cola de listos
        self.t_finalizado = 0

class Simulacion:
    def __init__(self, nom_archivo):
        self.cpu = CPU()
        self.memoria = Memoria()
        self.clock = 0
        self.quantum = QUANTUM
        self.procesos_terminados = [] #Procesos con estado terminado
        self.procesos_nuevos = [] #Procesos con estado new (llega con TA, pero no estan en memoria)
        self.cola_listos = [] #Procesos con estado ready (estan en memoria)
        self.cola_suspendidos = [] #Procesos con estado suspendedido (esperando lugar para ejecutarse)
        self.t_retorno_total = 0
        self.t_espera_total = 0 
        self.procesosMas10 = 0 #Guarda el total de procesos y sirve para preguntar si hay mas de 10
        self.banderaError = False #Indica si hay un error en el archivo de entrada
        self.archivoError = False #Pone en verdadero cuando no selecciona ningun archivo
        self.lista_procesos = self.leer_desde_entrada(nom_archivo) #Lista de procesos a tratar
        self.total_procesos = len(self.lista_procesos) #Cantidad total de procesos 

    #Metodo utilizado para obtener TODOS los procesos del archivo, devuelve un array con todos los procesos leidos del archivo
    #Al comienzo, todos los procesos se encuentran sin ningun estado. 
    #Cuando llega el tiempo de arribo de cada proceso, pasan a estado "new", para luego tratar los demas estados.
    def leer_desde_entrada(self, nom_archivo):
        lista_procesos = []
        listaProcesosTotales = 0
        
        try:
            with open(nom_archivo, newline='') as archivo: 
                reader = csv.reader(archivo) #Reader son las filas(lineas) del archivo
                next(reader, None) #Next salta la fila

                for row in reader: #Itera por filas 

                    if not row:    #Si la fila esta vacia, salta a la siguiente fila
                        continue

                    try: #Mientras no haya ningun error, ejecuta este bloque
                        id, tam, tarribo, tirrupcion = map(int, row) #Convierte los valores de una cadena a enteros, separandolo por cada nombre en si 
                        listaProcesosTotales += 1
                        #Se va a cargar el proceso mientras sea menor a la particion maxima y haya menos de 10 procesos
                        if(tam <= TAM_MAX_PROC) and (len(lista_procesos) < 10): 
                            lista_procesos.append(Proceso(id, tam, tarribo, tirrupcion))
                    except: #Si hay un error, ejecuta esta linea
                        self.banderaError = True
        except: 
            self.archivoError = True #Si no se carga ningun archivo se pone en verdadero
    
        self.procesosMas10 = listaProcesosTotales #Asigno de la variable local dentro del metodo a un atributo de la clase Simulacion (self.procesosMas10) 
        
        return lista_procesos

    #Metodo que obtiene los procesos nuevos, es decir cuyo tiempo de arribo coincide con el reloj. 
    #En nuestro caso, recorre la de procesos y devuelve otra lista pero solo con los procesos que sean nuevos
    def cargar_procesos(self, lista, clock): 

        #Es una funcion que devuelve true si (t_arribo) es menor o igual al tiempo actual del reloj (clock), caso contrario false
        def nuevo(proceso):
            return proceso.t_arribo <= clock
        
        #La funcion filter recorre la lista y selecciona solo los procesos para los cuales la función nuevo devuelve True
        procesos_nuevos = list(filter(nuevo, lista))
        
        #Los procesos que ingresan a la lista de procesos_nuevos, son borrados de la lista original para evitar duplicaciones.
        for proceso in procesos_nuevos: 
            if(proceso in lista):
                lista.remove(proceso)
                proceso.estado = ESTADO_NUEVO
        
        return procesos_nuevos
    
    #Metodo que verifica si aun hay procesos por ejecutarse, devuelve falso cuando todos sean 0
    def existen_procesos_restantes(self):
        return (len(self.lista_procesos) > 0) or (len(self.cola_listos) > 0) or (len(self.cola_suspendidos) > 0)
    
    #Metodo para incrementar el clock, se utiliza para poder avanzar el tiempo desde la interfaz grafica
    def incrementar_clock(self):
        self.clock += 1
    

    #Metodo que para avanzar la simulacion.
    #Realiza la asignacion a memoria, control de CPU, etc. correspondiente con el valor del clock.
    def avanzar(self):
        proceso_actual = None #Corresponde el primer proceso de la cola de listos

        self.procesos_nuevos.extend(self.cargar_procesos(self.lista_procesos, self.clock))

        if(self.cpu.proceso is not None):
            self.quantum -= 1
            self.cpu.proceso.t_irrup_faltante -= 1

            if(self.cpu.proceso.t_irrup_faltante == 0): #pregunta si el proceso termino
                self.quantum = QUANTUM
                self.cpu.proceso.estado = ESTADO_TERMINADO
                self.cpu.proceso.t_finalizado = self.clock #guarda el tiempo en el que termino el proceso
                self.cola_listos.remove(self.cpu.proceso)
                self.procesos_terminados.append(self.cpu.proceso)
                
                for particion in self.memoria.particiones: 
                    if(particion.proceso == self.cpu.proceso): 
                        particion.proceso = None
                self.cpu.liberar_proceso()
            
            #Elif se ejecuta si no se cumplio la condicion anterior y se cumple la siguiente
            elif(self.quantum == 0 and len(self.cola_listos) > 1 ):
                self.quantum = QUANTUM
                self.cpu.proceso.estado = ESTADO_LISTO
                self.cola_listos.remove(self.cpu.proceso)
                self.cola_listos.append(self.cpu.proceso)
                self.cpu.liberar_proceso()


        for proceso in self.procesos_nuevos:
            if (len(self.cola_suspendidos) + len(self.cola_listos) == 5): 
                break
            self.cola_suspendidos.append(proceso)
            proceso.estado = ESTADO_SUSPENDIDO

        for proceso in self.cola_suspendidos:
            if(proceso in self.procesos_nuevos):
                self.procesos_nuevos.remove(proceso)

        #Asignacion de Memoria 
        
        for proceso in self.cola_suspendidos:
            worstfit_libre = None        

            #Aplicamos algoritmo WorstFit para los de la cola de Suspendido
            for particion in self.memoria.particiones[1:]:   

                #Busqueda de peor particion libre
                if ((worstfit_libre is None) and (particion.proceso is None)):
                    if (particion.tamaño >= proceso.tamaño):
                        worstfit_libre = particion
                elif (particion.proceso is None):
                    if ((particion.tamaño >= proceso.tamaño) and (particion.tamaño > worstfit_libre.tamaño)):
                        worstfit_libre = particion
                
            
            if worstfit_libre is not None:
                self.memoria.asignar_procesos(proceso, worstfit_libre)
                self.cola_listos.append(proceso)
                proceso.estado = ESTADO_LISTO
                #Asignamos a la cola de listos los procesos que encontraron un lugar en la memoria


        for proceso in self.cola_listos:
            if(proceso in self.cola_suspendidos):
                self.cola_suspendidos.remove(proceso)

        #Asignacion de proceso a CPU 
        
        if len(self.cola_listos) > 0:
            proceso_actual = self.cola_listos[0]
        
        if ((self.cpu.proceso != proceso_actual) and (proceso_actual is not None)):
            self.cpu.ejecutar_proceso(proceso_actual)



        #Control de Tiempos de retorno y espera

        for proceso in self.cola_listos:
            if proceso.estado == ESTADO_LISTO:
                proceso.t_retorno += 1
                proceso.t_espera += 1 

                self.t_retorno_total += 1
                self.t_espera_total += 1

            elif proceso.estado == ESTADO_EJECUCION:
                proceso.t_retorno += 1

                self.t_retorno_total += 1
                


