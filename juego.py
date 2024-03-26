import tkinter as tk
from typing import List, Tuple, Callable
from time import sleep 
import creador_raiz
import menu_pre_juego

##Constantes del programa
##--------------------------------------------------------------------------------------#
turno: int = 1
partida : int = 0
espacio_tablero = 300
puntuacion: List[int] = [0,0]
##--------------------------------------------------------------------------------------#
class Casilla:
    def __init__(self,
                tablero : tk.Canvas, 
                posicion : Tuple[int, int],
                dimension_tablero : int,
                al_cambiar: Callable[[], None], al_tocar : Callable[[], None], al_dejar_tocar : Callable[[], None]):
        self.tablero = tablero
        self.lado: int = dimension_tablero/int(menu_pre_juego.N)
        self.lienzo: tk.Canvas = tablero
        self.esq_superior_izq: Tuple[int, int] = posicion
        self.estado: int = 0 #estado varia entre 0,1 y 2 para indicar vacio, cruz y circunferencia, respectivamente.
        self.al_cambiar = al_cambiar
        self.al_tocar = al_tocar
        self.al_dejar_tocar = al_dejar_tocar
        self.casilla = 0
        self.figura : List[int] = []
        self.dibujar_casilla()

    def crear_cruz(self):
        global turno
        linea_1 : int = self.tablero.create_line(self.esq_superior_izq[0] + self.lado / 5, self.esq_superior_izq[1] + self.lado / 5, 
                            self.esq_superior_izq[0] + self.lado * (4/5), self.esq_superior_izq[1] + self.lado * (4/5), fill = "black", width = self.lado / 5)
        linea_2 : int= self.tablero.create_line(self.esq_superior_izq[0] + self.lado * (4/5), self.esq_superior_izq[1] + self.lado / 5,
                            self.esq_superior_izq[0] + self.lado / 5, self.esq_superior_izq[1] + self.lado * (4/5), fill = "black", width = self.lado / 5)
        self.estado = 1
        
        
        self.tablero.update() 

        self.figura.append(linea_1)
        self.figura.append(linea_2)


        ##Cambia turno en et_turno:
        turno = 2
        cambia_turno()

        ##Procesa tablero
        self.al_cambiar()

    def crear_circulo(self):
        global turno
        circulo_1 : int = self.tablero.create_oval(self.esq_superior_izq[0] + self.lado / 6, self.esq_superior_izq[1] + self.lado / 6, 
                            self.esq_superior_izq[0] + self.lado * (5/6), self.esq_superior_izq[1] + self.lado * (5/6), fill = "maroon2")
        circulo_2 : int = self.tablero.create_oval(self.esq_superior_izq[0] + self.lado / 6 + self.lado / 5, self.esq_superior_izq[1] + self.lado / 6 + self.lado / 5, 
                            self.esq_superior_izq[0] + self.lado * (5/6) - self.lado/5, self.esq_superior_izq[1] + self.lado * (5/6) - self.lado / 5, fill = "white")
        self.estado = 2

        self.figura.append(circulo_1)
        self.figura.append(circulo_2)

        self.tablero.update() 

        ##Cambia turno en et_turno:
        turno = 1
        cambia_turno()

        ##Procesa tablero
        self.al_cambiar()

    def eliminar_figura(self):
        self.tablero.delete(self.figura[0])
        self.tablero.delete(self.figura[1])
        self.figura.pop(0)
        self.figura.pop(0)

    def dibujar_casilla(self):
        global turno
        self.casilla: int = self.tablero.create_rectangle(self.esq_superior_izq[0], self.esq_superior_izq[1], self.esq_superior_izq[0] + self.lado, self.esq_superior_izq[1] + self.lado, fill= 'white', outline="black")
        nada : int = 0
        self.tablero.tag_bind(
            self.casilla,
            "<Button-1>",
            lambda event: ((self.crear_cruz() if (turno == 1) else self.crear_circulo()) if (self.estado == 0) else nada))

        """
        self.tablero.tag_bind(
            self.casilla,
            "<Enter>",
            lambda e : self.al_tocar()
            )
        """
        
        """
        self.tablero.tag_bind(
            self.casilla,
            "<Leave>",
            lambda e : self.al_dejar_tocar()
            )
        """

class Tablero:
    def __init__(self, raiz, M, N, x, al_ganar : Callable, al_procesar : Callable, al_tocar : Callable, al_dejar_tocar : Callable, ID : int):
        """
        Define los atributos iniciales del tablero.

        ### Parámetros:
        * `raiz`: La ventana donde se coloca el tablero.
        * `M`: Las dimensión en píxeles del tablero.
        * `N`: Dimensión del tablero en casillas.

        ### Retorno: 
        * `None`: No devuelve nada.
        """
        self.tablero: tk.Canvas = tk.Canvas(raiz, width = M, height = M, background="black")
        self.x = x
        self.tablero.place(x = 150 + x, y = 100 + x)
        self.tablero.update()
        self.N : int = N
        self.raiz : tk.Tk = raiz
        self.lado: int = M
        self.al_ganar = al_ganar
        self.al_tocar = al_tocar
        self.al_dejar_tocar = al_dejar_tocar
        self.al_procesar = al_procesar
        self.ID = ID
        self.casillas: List[List[Casilla]] = []
        self.dibujar_tablero()

    def dibujar_tablero (self):
        """
        Dibuja el tablero en la raíz.

        ### Parámetros:
        * `self`: Referencia a sí mismo.

        ### Retorno: 
        * `None`: No devuelve nada.
        """
        j: int = 0
        while (j < self.N):
            self.casillas.append([])
            i: int = 0
            while (i < self.N):
                self.casillas[j].append(Casilla(self.tablero, (i * (self.lado / self.N), j * (self.lado / self.N)), (5 * espacio_tablero)/(4 + int(menu_pre_juego.N)), self.procesar_tablero, self.llamar_a_desaparecer_tableros, self.llamar_a_reaparecer_tableros))
                i += 1
            j += 1
        rec_1 : int = self.tablero.create_rectangle(0, self.lado - self.lado/18, self.lado/18, self.lado, fill="gray")
        
        self.tablero.tag_bind(
            rec_1,
            "<Button-1>",
            lambda e : self.al_tocar(self.ID)
            )
        
        self.tablero.tag_bind(
            rec_1,
            "<Button-3>",
            lambda e : self.al_dejar_tocar(self.ID)
            )

    def procesar_tablero (self):
        """
        Procesa el tablero. 
        Básicamente revisa si el tablero tiene una figura ganadora de fila, columna o diagonal.

        ### Parámetros:
        * `self`: Referencia a sí mismo.

        ### Retorno: 
        * `None`: No devuelve nada.
        """
        empate : int = 1
        for j, fila in enumerate(self.casillas):
            for i in range(len(fila) - 1):
                if (fila[i].estado == 0 or fila[i].estado != fila[i + 1].estado):
                    break
                elif (fila[i].estado != 0 and fila[i].estado == fila[i + 1].estado and i == len(fila) - 2):
                    self.ganar_tablero()
                    empate = 0
                else:
                    pass
        

        #Verifica columnas
        contador: int = 0
        for i in range(self.N):
            contador = 0
            for j in range(self.N - 1):
                if (self.casillas[j][i].estado == 0 or self.casillas[j][i].estado != self.casillas[j + 1][i].estado):
                    contador = 0
                elif (self.casillas[j][i].estado != 0 and self.casillas[j][i].estado == self.casillas[j + 1][i].estado):
                    contador += 1
                else:
                    contador = 0
            if (contador == self.N - 1):
                self.ganar_tablero()
                empate = 0
            else:
                pass
        #Verifica diagonal
        
        if (all((self.casillas[i][i].estado != 0 and self.casillas[0][0].estado == self.casillas[i][i].estado) for i in range(self.N))):
            self.ganar_tablero()
            empate = 0
        else:
            pass

        #Verifica diagonal secundaria

        if (all((self.casillas[i][self.N - 1 - i].estado != 0 and self.casillas[0][self.N - 1].estado == self.casillas[i][self.N - 1 - i].estado) for i in range(self.N))):
            sleep(0.5)
            self.ganar_tablero()
            empate = 0
        else:
            pass

        ##Llamado al procesamiento intertablero
        self.al_procesar()
        
        global partida
        #Verifica que no estén llenas las casillas:
        if  all( all(j.estado != 0 for j in i) for i in self.casillas) and empate == 1:
            sleep(1)
            texto_displayer("> ¡Empate!")
            partida += 1
            self.reiniciar_tablero()

    def ganar_tablero (self):
        """
        Se llama cuando se encuentra una figura ganadora en el tablero. 
        Esta función básicamente muestra un mensaje en un displayer y luego llama a otra función que reinicia el tablero.
        
        ### Parámetros:
        * `self`: Referencia a sí mismo.

        ### Retorno: 
        * `None`: No devuelve nada.
        """
        global partida
        global turno
        if (turno == 2): #El ganador fue el jugador 1
            texto_displayer(f" > ¡{menu_pre_juego.jugador_1} ha ganado!")
            puntuacion[0] += 1
            if partida % 2 == 1: 
                turno = 1
                cambia_turno()
            partida += 1
            actualizar_puntuacion(puntuacion)
            sleep(1)
            self.al_ganar()
        else:
            texto_displayer(f" > ¡{menu_pre_juego.jugador_2} ha ganado!")
            puntuacion[1] += 1
            if partida % 2 == 0: 
                turno = 2
                cambia_turno()
            partida += 1
            actualizar_puntuacion(puntuacion)
            sleep(1)
            self.al_ganar()

    def eliminar_tablero (self):
        """
        Olvida el tablero.

        ### Parámetros:
        * `self`: Referencia a sí mismo.

        ### Retorno: 
        * `None`: No devuelve nada.
        """
        self.tablero.place_forget()

    def colocar_tablero (self):
        self.tablero.place(x = 150 + self.x, y = 100 + self.x)
        self.tablero.update()

    def reiniciar_tablero (self):
        """
        Blanquea cada casilla del tablero para empezar otra partida.

        ### Parámetros:
        * `self`: Referencia a sí mismo.

        ### Retorno: 
        * `None`: No devuelve nada.
        """
        for row in self.casillas:
            for e in row: 
                if e.estado != 0:
                    e.estado = 0
                    e.eliminar_figura()
        self.tablero.update()

    def llamar_a_desaparecer_tableros (self):
        self.al_tocar(self.ID)

    def llamar_a_reaparecer_tableros (self):
        self.al_dejar_tocar(self.ID)

#Funciones para botones#
##-------------------------------------------------------------------------------------#

def eliminar_imagen_juego() -> None:
    """
    Elimina todos los objetos que se muestran en pantalla.

    ### Parámetros:
    * No recibe ningún parámetro.

    ### Retorno: 
    * `None`: No devuelve nada.
    """
    global lista_tableros

    et_turno.place_forget()
    lienzo_turno.delete(cruz_1)
    lienzo_turno.delete(cruz_2)
    lienzo_turno.delete(temp[0])
    lienzo_turno.delete(temp[1])
    temp.pop(0)
    temp.pop(0)
    lienzo_turno.place_forget()
    lienzo_display.delete(display)
    lienzo_display.place_forget()
    texto_puntuacion_SV.set("0  -  0")
    label_puntuacion.place_forget()
    label_display.place_forget()
    lienzo_cuadro.place_forget()
    texto_display_SV.set(" > ")
    for e in lista_tableros:
        e.eliminar_tablero()

    
    lista_tableros = []

    boton_regresar.place_forget()

    global turno
    global puntuacion
    global partida
    turno = 1
    puntuacion = [0,0]
    partida = 0
    creador_raiz.raiz.quit()

##--------------------------------------------------------------------------------------#

##Declaración de elementos:
#--------------------------------------------------------------------------------------#
##Fondo
fondo = tk.PhotoImage(file='images/Fondo2.png')
fondo_etiqueta = tk.Label(creador_raiz.raiz, highlightthickness=0, image=fondo)

## Display de Turno
et_turno = tk.Label(
    creador_raiz.raiz,
    text="Turno: ",
    font=("Arial Black", 20),
    background='white',
    highlightthickness=0,
)

## Turno Lienzo
lienzo_turno: tk.Canvas = tk.Canvas(creador_raiz.raiz, width=30,height=30, background='white', highlightthickness=0)
temp: List[int] = []

##Cruces
cruz_1 : int = 0
cruz_2 : int = 0

## Display de mensajes
lienzo_display: tk.Canvas = tk.Canvas(creador_raiz.raiz, width= 300, height= 45)

#text_displayer
texto_display_SV : tk.StringVar = tk.StringVar()
texto_display_SV.set(" > ")

label_display: tk.Label = tk.Label(
    creador_raiz.raiz,
    textvariable= texto_display_SV,
    font= ('Arial Black', 10),
    fg='white',
    background='black'
)

##Display
display : int = 0

# Display de contador
texto_puntuacion_SV : tk.StringVar = tk.StringVar()
texto_puntuacion_SV.set("0  -  0")
label_puntuacion: tk.Label = tk.Label(
    creador_raiz.raiz,
    textvariable= texto_puntuacion_SV,
    font=("Arial Black", 15),
    background='black',
    foreground="white",
    highlightthickness=0
)

##Cuadro negro superior
lienzo_cuadro: tk.Canvas = tk.Canvas(creador_raiz.raiz, width= 302, height= 20, background='black', highlightthickness=0)

##Lista de tableros
lista_tableros : List[Tablero] = []

def cambio_color_1(evento) -> None:
    """
    Cambia de color el botón regresar.
    Pasa el color a magenta en el fondo y negro a las letras.

    ### Parámetros:
    * `evento`: Nombre de referencia para que tkinter identifique el evento.

    ### Retorno: 
    * `None`: No devuelve nada.
    """
    boton_regresar['bg']= 'magenta3'
    boton_regresar['fg']= 'black'

def cambio_color_2(evento) -> None:
    """
    Cambia de color el botón regresar.
    Pasa el color a negro en el fondo y blanco a las letras.

    ### Parámetros:
    * `evento`: Nombre de referencia para que tkinter identifique el evento.

    ### Retorno: 
    * `None`: No devuelve nada.
    """
    boton_regresar['bg']= 'black'
    boton_regresar['fg']= 'white'

boton_regresar : tk.Button = tk.Button(creador_raiz.raiz, text='Regresar', font= ('Arial Black', 10), background="black", foreground="white", command= eliminar_imagen_juego)

boton_regresar.bind(
    '<Enter>',
    cambio_color_1
    )

boton_regresar.bind(
    '<Leave>',
    cambio_color_2
    )

#--------------------------------------------------------------------------------------#

def iniciar() -> None:
    """
    Coloca todos los elementos que se mostrarán en pantalla. 
    Además, hace la primera y única llamada al tablero que hay en todo el código.

    ### Parámetros:
    * No recibe parámetros.

    ### Retorno: 
    * `None`: No devuelve nada.
    """
    ##Seteo de elementos

    et_turno.place(x=30, y=5)
    lienzo_turno.place(x=135,y=13)

    ##Turno X
    cruz_1: int = lienzo_turno.create_line(5, 5, 25,25, width=8, fill="black")
    temp.append(cruz_1)
    cruz_2: int = lienzo_turno.create_line(5, 25, 25, 5, width=8, fill="black")
    temp.append(cruz_2)

    ## Display de mensajes
    lienzo_display.place(x=150, y=420)

    #text_displayer cero
    label_display.place(x=155, y=432)

    ##Display
    display: int = lienzo_display.create_rectangle(0,0,300,45, outline="black", fill='black')
    
    # Display de contador
    label_puntuacion.place(x= 483,y= 22)

    ##Cuadro negro superior
    lienzo_cuadro.place(x=150, y=80)

    ##Boton regresar
    boton_regresar.place(x=460, y=400)

    ##Tablero:
    i : int = 0
    x : int = 0
    while i < int(menu_pre_juego.N):
        tablero : Tablero = Tablero(creador_raiz.raiz, (5 * espacio_tablero)/(4 + int(menu_pre_juego.N)), int(menu_pre_juego.N), x, reiniciar_tableros , procesar_intertableros, desaparecer_tableros, reaparecer_tableros, i)
        lista_tableros.append(tablero)
        i += 1
        x += (5 * espacio_tablero)/(4 + int(menu_pre_juego.N))/5
    

def reaparecer_tableros(x : int):

    for e in lista_tableros:
        if e.ID != x:
            e.colocar_tablero()

def desaparecer_tableros(x : int):

    for e in lista_tableros:
        if e.ID != x:
            e.eliminar_tablero()

def procesar_intertableros(): 

    #Verificar inter filas:
    contador : int = 0

    for i in range(0, int(menu_pre_juego.N)):
        for j in range(0, int(menu_pre_juego.N)):
            contador = 1
            for k in range(0, len(lista_tableros) - 1):
                if lista_tableros[k].casillas[i][j].estado != lista_tableros[k + 1].casillas[i][j].estado or lista_tableros[k].casillas[i][j].estado == 0 or lista_tableros[k + 1].casillas[i][j].estado == 0:
                    break
                contador += 1
                if contador == len(lista_tableros):
                    ganar_tableros()


    #Verificar inter diagonal principal 3D:
                    
    for j in range(0, int(menu_pre_juego.N)):
        contador = 1
        for i in range(0, len(lista_tableros) - 1):
            if lista_tableros[i].casillas[i][j].estado != lista_tableros[i+1].casillas[i+1][j].estado or lista_tableros[i].casillas[i][j].estado == 0 or lista_tableros[i+1].casillas[i+1][j].estado == 0:
                break
            contador += 1
            if contador == len(lista_tableros):
                ganar_tableros()
    
    #Verificar inter diagonal secundaria 3D:
                    
    for j in range(0, int(menu_pre_juego.N)):
        contador = 1
        for i in range(0, len(lista_tableros) - 1):
            if lista_tableros[i].casillas[int(menu_pre_juego.N)- (1 + i)][j].estado != lista_tableros[i+1].casillas[int(menu_pre_juego.N) - (i + 2)][j].estado or lista_tableros[i].casillas[int(menu_pre_juego.N) - (i + 1)][j].estado == 0 or lista_tableros[i+1].casillas[int(menu_pre_juego.N)-(i + 2)][j].estado == 0:
                break
            contador += 1
            if contador == len(lista_tableros):
                ganar_tableros()


    #Verificar inter diagonal principal plana:         
    for i in range(0, int(menu_pre_juego.N)):
        contador = 1
        for j in range(0, len(lista_tableros) - 1):
            if lista_tableros[j].casillas[i][j].estado != lista_tableros[j+1].casillas[i][j+1].estado or lista_tableros[j].casillas[i][j].estado == 0 or lista_tableros[j+1].casillas[i][j+1].estado == 0:
                break
            contador += 1
            if contador == len(lista_tableros):
                ganar_tableros()
    
    #Verificar inter diagonal secundaria plana:         
    for i in range(0, int(menu_pre_juego.N)):
        contador = 1
        for j in range(0, len(lista_tableros) - 1):
            if lista_tableros[j].casillas[i][int(menu_pre_juego.N)- (1 + j)].estado != lista_tableros[j+1].casillas[i][int(menu_pre_juego.N)- (j + 2)].estado or lista_tableros[j].casillas[i][int(menu_pre_juego.N)- (1 + j)].estado == 0 or lista_tableros[j+1].casillas[i][int(menu_pre_juego.N)- (j + 2)].estado == 0:
                break
            contador += 1
            if contador == len(lista_tableros):
                ganar_tableros()


def ganar_tableros():
    global partida 
    global turno

    if (turno == 2): #El ganador fue el jugador 1
        texto_displayer(f" > ¡{menu_pre_juego.jugador_1} ha ganado!")
        puntuacion[0] += 1
        if partida % 2 == 1: 
            turno = 1
            cambia_turno()
        partida += 1
        actualizar_puntuacion(puntuacion)
        sleep(1)
        reiniciar_tableros()
    else: 
        texto_displayer(f" > ¡{menu_pre_juego.jugador_2} ha ganado!")
        puntuacion[1] += 1
        if partida % 2 == 0: 
            turno = 2
            cambia_turno()
        partida += 1
        actualizar_puntuacion(puntuacion)
        sleep(1)
        reiniciar_tableros()

def reiniciar_tableros():
    for e in lista_tableros:
        e.reiniciar_tablero()

def cambia_turno() -> None:
    """
    Hace el cambio de turno en pantalla, cambiando una cruz por un círculo o al revés.

    ### Parámetros:
    * No recibe parámetros.

    ### Retorno: 
    * `None`: No devuelve nada.
    """
    if (turno == 1):
        for e in temp:
            lienzo_turno.delete(e)
        temp.pop(0)
        temp.pop(0)
        cruz_1: int = lienzo_turno.create_line(5, 5, 25,25, width=8, fill="black")
        temp.append(cruz_1)
        cruz_2: int = lienzo_turno.create_line(5, 25, 25, 5, width=8, fill="black")
        temp.append(cruz_2)
    else:
        for e in temp:
            lienzo_turno.delete(e)
        temp.pop(0)
        temp.pop(0)
        circ_1: int = lienzo_turno.create_oval(3, 3, 27, 27, fill="magenta3")
        temp.append(circ_1)
        circ_2: int = lienzo_turno.create_oval(10, 10, 20, 20, fill="white")
        temp.append(circ_2)

def texto_displayer(texto: str) -> None:
    """
    Muestra un mensaje en el displayer que está debajo del tablero.

    ### Parámetros:
    * `texto`: Texto que se va a mostrar en el displayer.

    ### Retorno: 
    * `None`: No devuelve nada.
    """
    texto_display_SV.set(texto)

def actualizar_puntuacion(puntaje: List[int]) -> None:
    """
    Actualiza la puntuación en la parte superior derecha de la pantalla.

    ### Parámetros:
    * `puntaje`: Recibe la lista que contiene el puntaje actual.

    ### Retorno: 
    * `None`: No devuelve nada.
    """
    texto = f"{puntaje[0]}  -  {puntaje[1]}"
    texto_puntuacion_SV.set(texto)







    


