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
esta_boton: int = 0
##--------------------------------------------------------------------------------------#
class Casilla:
    def __init__(self,
                tablero : tk.Canvas, 
                posicion : Tuple[int, int],
                dimension_tablero : int,
                al_cambiar: Callable[[], None], 
                ):
        self.tablero = tablero
        self.lado: int = dimension_tablero/int(menu_pre_juego.N)
        self.lienzo: tk.Canvas = tablero
        self.esq_superior_izq: Tuple[int, int] = posicion
        self.estado: int = 0 #estado varia entre 0,1 y 2 para indicar vacio, cruz y circunferencia, respectivamente.
        self.se_muestra : int = 0 #varia entre 0, 1 según si se muestra o no
        self.al_cambiar = al_cambiar
        self.casilla = 0
        self.figura : List[int] = []
        self.dibujar_casilla()

    def crear_cruz(self) -> None:
        """
        Dibuja la cruz negra en la casilla y la agrega a una lista.

        ### Parámetros:
        * `self`: Referencia a sí mismo.

        ### Retorno: 
        * `None`: No devuelve nada.
        """
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

    def crear_circulo(self) -> None:
        """
        Dibuja el círculo fucsia en la casilla y lo agrega a una lista.

        ### Parámetros:
        * `self`: Referencia a sí mismo.

        ### Retorno: 
        * `None`: No devuelve nada.
        """
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

    def eliminar_figura(self) -> None:
        """
        Elimina la cruz o el circulo que esté en la casilla.

        ### Parámetros:
        * `self`: Referencia a sí mismo.

        ### Retorno: 
        * `None`: No devuelve nada.
        """
        self.tablero.delete(self.figura[0])
        self.tablero.delete(self.figura[1])
        self.figura.pop(0)
        self.figura.pop(0)

    def dibujar_casilla(self) -> None:
        """
        Dibuja la casilla.

        ### Parámetros:
        * `self`: Referencia a sí mismo.

        ### Retorno: 
        * `None`: No devuelve nada.
        """
        global turno
        self.casilla: int = self.tablero.create_rectangle(self.esq_superior_izq[0], self.esq_superior_izq[1], self.esq_superior_izq[0] + self.lado, self.esq_superior_izq[1] + self.lado, fill= 'white', outline="black")
        self.tablero.tag_bind(
            self.casilla,
            "<Button-1>",
            lambda event: ((self.crear_cruz() if (turno == 1) else self.crear_circulo()) if (self.estado == 0 and self.se_muestra == 0) else None))

    def pintar_casilla(self, color) -> None:
        """
        Pinta la casilla de un color dado.

        ### Parámetros:
        * `self`: Referencia a sí mismo.
        * `color`: Color que se utilizará para pintar la casilla.

        ### Retorno: 
        * `None`: No devuelve nada.
        """
        self.tablero.itemconfig(self.casilla, fill=color)

class Tablero:
    def __init__(self,
                raiz: tk.Tk,
                M: int, N: int, x: float,
                al_ganar : Callable[[], None],
                al_procesar : Callable[[], None],
                al_tocar : Callable[[], None],
                al_dejar_tocar : Callable[[], None],
                ID : int, 
                al_mostrar_victoria : Callable[[], None]):

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
        self.al_mostrar_victoria = al_mostrar_victoria
        self.ID = ID
        self.casillas: List[List[Casilla]] = []
        self.marco: tk.Frame = tk.Frame(width= self.lado, height= self.lado/22, background= 'black')
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
                self.casillas[j].append(Casilla(self.tablero, (i * (self.lado / self.N), j * (self.lado / self.N)), (5 * espacio_tablero)/(4 + int(menu_pre_juego.N)), self.procesar_tablero))
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
        
        self.marco.place(x = 150 + self.x, y= 100 + self.x - self.lado/22)

    def procesar_tablero (self):
        """
        Procesa el tablero. 
        Básicamente revisa si el tablero tiene una figura ganadora de fila, columna o diagonal.

        ### Parámetros:
        * `self`: Referencia a sí mismo.

        ### Retorno: 
        * `None`: No devuelve nada.
        """
        gano_tablero: bool = False

        ##Verifica filas           (0)
        for j, fila in enumerate(self.casillas):
            for i in range(len(fila) - 1):
                if (fila[i].estado == 0 or fila[i].estado != fila[i + 1].estado):
                    break
                elif (fila[i].estado != 0 and fila[i].estado == fila[i + 1].estado and i == len(fila) - 2):
                    self.pintar_tablero(0, j)
                    gano_tablero = True
                else:
                    pass
        
        
        #Verifica columnas          (1)
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
                self.pintar_tablero(1,i)
                gano_tablero = True
            else:
                pass
        #Verifica diagonal    (2)    
        
        if (all((self.casillas[i][i].estado != 0 and self.casillas[0][0].estado == self.casillas[i][i].estado) for i in range(self.N))):
            self.pintar_tablero(2)
            gano_tablero = True
        else:
            pass

        #Verifica diagonal secundaria      (3)

        if (all((self.casillas[i][self.N - 1 - i].estado != 0 and self.casillas[0][self.N - 1].estado == self.casillas[i][self.N - 1 - i].estado) for i in range(self.N))):
            sleep(0.5)
            self.pintar_tablero(3)
            gano_tablero = True
        else:
            pass

        if gano_tablero:
            self.al_ganar()
            self.al_procesar(True)
        else:
            ##Llamado al procesamiento intertablero
            self.al_procesar()

    def eliminar_tablero (self):
        """
        Olvida el tablero.

        ### Parámetros:
        * `self`: Referencia a sí mismo.

        ### Retorno: 
        * `None`: No devuelve nada.
        """
        self.tablero.place_forget()
        self.marco.place_forget()

    def colocar_tablero (self):
        """
        Coloca el tablero de nuevo.
        Esta función se utiliza cuando se dejan de mostrar algunos tableros y luego se vuelven a mostrar.

        ### Parámetros:
        * `self`: Referencia a sí mismo.

        ### Retorno: 
        * `None`: No devuelve nada.
        """
        self.tablero.place(x = 150 + self.x, y = 100 + self.x)
        self.marco.place(x = 150 + self.x, y= 100 + self.x - self.lado/22)
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
                    e.se_muestra = 0
                    e.eliminar_figura()
        self.tablero.update()

    def pintar_tablero (self, victoria, lugar = 0):
        """
        Pinta las casillas de una figura ganadora. 
        Es capaz de saber dónde se ganó gracias a el parámetro `lugar`, que indica alguna referencia de columna o fila donde se ganó.

        ### Parámetros:
        * `self`: Referencia a sí mismo.
        * `victoria`: Identificador del tipo de victoria. 
        * `lugar`: Referencia a fila o columna donde ocurrió la victoria.

        ### Retorno: 
        * `None`: No devuelve nada.
        """
        if victoria == 0:
            for i in self.casillas[lugar]:
                i.pintar_casilla("pink")
        elif victoria == 1:
            for i in self.casillas:
                i[lugar].pintar_casilla("pink")
        elif victoria == 2:
            for i in range(0, self.N):
                self.casillas[i][i].pintar_casilla("pink")
        elif victoria == 3:
            for i in range(0, self.N):
                self.casillas[i][self.N - (i + 1)].pintar_casilla("pink")

    def mostrar_victoria_tablero (self):
        """
        Prepara el estado de todas las casillas para que no se pueda jugar mientras se muestra una victoria.

        ### Parámetros:
        * `self`: Referencia a sí mismo.

        ### Retorno: 
        * `None`: No devuelve nada.
        """
        for i in self.casillas:
            for j in i:
                j.se_muestra = 1

    def llamar_a_desaparecer_tableros (self):
        """
        Hace una llamada a la función desaparecer_tableros que básicamente desaparece todos los tableros excepto en el que hiciste click.

        ### Parámetros:
        * `self`: Referencia a sí mismo.

        ### Retorno: 
        * `None`: No devuelve nada.
        """
        self.al_tocar(self.ID)

    def llamar_a_reaparecer_tableros (self):
        """
        Hace una llamada a la función reaparecer_tableros que básicamente reaparece todos los tableros.

        ### Parámetros:
        * `self`: Referencia a sí mismo.

        ### Retorno: 
        * `None`: No devuelve nada.
        """
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
    global esta_boton

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
    texto_display_SV.set(" > ")
    for e in lista_tableros:
        e.eliminar_tablero()

    
    lista_tableros = []

    boton_regresar.place_forget()
    label_jugador_1.place_forget()
    label_jugador_2.place_forget()

    if esta_boton == 1:
        boton_continuar.place_forget()

    global turno
    global puntuacion
    global partida
    turno = 1
    puntuacion = [0,0]
    partida = 0
    esta_boton = 0
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

##Lista de tableros
lista_tableros : List[Tablero] = []

#jugador 1 display
jugador_1_text : tk.StringVar = tk.StringVar()

label_jugador_1: tk.Label = tk.Label(
    creador_raiz.raiz,
    textvariable= jugador_1_text,
    font=("Arial Black", 8),
    background='white',
    foreground="black",
    highlightthickness=0
)


#jugador 2 display
jugador_2_text : tk.StringVar = tk.StringVar()


label_jugador_2: tk.Label = tk.Label(
    creador_raiz.raiz,
    textvariable= jugador_2_text,
    font=("Arial Black", 8),
    background='white',
    foreground="black",
    highlightthickness=0
)

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

    ##Boton regresar
    boton_regresar.place(x=460, y=400)

    ##Posición del nombre del jugador 1 con respecto al tamaño del nombre
    if len(menu_pre_juego.jugador_1) >= 8:
        jugador_1_text.set(menu_pre_juego.jugador_1[0:8])
        label_jugador_1.place(x=452, y=95)
    elif 5 <= len(menu_pre_juego.jugador_1) < 8:
        jugador_1_text.set(menu_pre_juego.jugador_1)
        label_jugador_1.place(x=458, y=95)
    elif  3 <= len(menu_pre_juego.jugador_1) < 5:
        jugador_1_text.set(menu_pre_juego.jugador_1)
        label_jugador_1.place(x=465, y=95)
    elif  0 < len(menu_pre_juego.jugador_1) < 3: 
        jugador_1_text.set(menu_pre_juego.jugador_1)
        label_jugador_1.place(x=470, y=95)


    ##Posición del nombre del jugador 2 con respecto al tamaño del nombre
    if len(menu_pre_juego.jugador_2) >= 8:
        jugador_2_text.set(menu_pre_juego.jugador_2[0:8])
        label_jugador_2.place(x=522, y=95)
    elif 5 <= len(menu_pre_juego.jugador_2) < 8:
        jugador_2_text.set(menu_pre_juego.jugador_2)
        label_jugador_2.place(x=528, y=95)
    elif 3 <= len(menu_pre_juego.jugador_2) < 5:
        jugador_2_text.set(menu_pre_juego.jugador_2)
        label_jugador_2.place(x=535, y=95)
    elif 0 < len(menu_pre_juego.jugador_2) < 3:
        jugador_2_text.set(menu_pre_juego.jugador_2)
        label_jugador_2.place(x=540, y=95)

    ##Tablero:
    i : int = 0
    x : int = 0
    while i < int(menu_pre_juego.N):
        tablero : Tablero = Tablero(creador_raiz.raiz, (5 * espacio_tablero)/(4 + int(menu_pre_juego.N)), int(menu_pre_juego.N), x, ganar_tableros , procesar_intertableros, desaparecer_tableros, reaparecer_tableros, i, mostrar_victoria)
        lista_tableros.append(tablero)
        i += 1
        x += (5 * espacio_tablero)/(4 + int(menu_pre_juego.N))/5

def mostrar_victoria() -> None:
    """
    Hace un llamado a todos los tableros para que dispongan las casillas a no ser modificadas mientras se muestra una victoria.

    ### Parámetros:
    * `self`: Referencia a sí mismo.

    ### Retorno: 
    * `None`: No devuelve nada.
    """
    for i in lista_tableros:
        i.mostrar_victoria_tablero()
       
def reaparecer_tableros(x : int) -> None:
    """
    Hace un llamado a todos los tableros para que reaparezcan.

    ### Parámetros:
    * `self`: Referencia a sí mismo.
    * `x` : ID del tablero que la llamó.

    ### Retorno: 
    * `None`: No devuelve nada.
    """
    for e in lista_tableros:
        if e.ID != x:
            e.colocar_tablero()

def desaparecer_tableros(x : int) -> None:
    """
    Hace un llamado a todos los tableros excepto el de ID: `x` para que desparezcan.

    ### Parámetros:
    * `self`: Referencia a sí mismo.
    * `x` : ID del tablero que la llamó.

    ### Retorno: 
    * `None`: No devuelve nada.
    """
    for e in lista_tableros:
        if e.ID != x:
            e.eliminar_tablero()

def procesar_intertableros(ya_gano: bool = False) -> None: 
    """
    Procesa todas las posibles victorias en intertableros. 
    Recibe un parámetro que le indica si ya se ganó en un tablero para que no llamé a ganar_partida, sino que solo pinte la victoria.

    ### Parámetros:
    * `self`: Referencia a sí mismo.
    * `ya_gano`: Variable booleana que indica si ya se ganó en un tablero.

    ### Retorno: 
    * `None`: No devuelve nada.
    """
    gano_tablero: bool = False
    contador : int = 0
    empate : int = 1
    global partida

    #Verificar inter filas:         (0)

    for i in range(0, int(menu_pre_juego.N)):
        for j in range(0, int(menu_pre_juego.N)):
            contador = 1
            for k in range(0, len(lista_tableros) - 1):
                if lista_tableros[k].casillas[i][j].estado != lista_tableros[k + 1].casillas[i][j].estado or lista_tableros[k].casillas[i][j].estado == 0 or lista_tableros[k + 1].casillas[i][j].estado == 0:
                    break
                contador += 1
                if contador == len(lista_tableros):
                    empate = 0
                    pintar_tableros(0, i, j)
                    gano_tablero = True


    #Verificar inter diagonal principal 3D:                 (1)
                    
    for j in range(0, int(menu_pre_juego.N)):
        contador = 1
        for i in range(0, len(lista_tableros) - 1):
            if lista_tableros[i].casillas[i][j].estado != lista_tableros[i+1].casillas[i+1][j].estado or lista_tableros[i].casillas[i][j].estado == 0 or lista_tableros[i+1].casillas[i+1][j].estado == 0:
                break
            contador += 1
            if contador == len(lista_tableros):
                empate = 0
                pintar_tableros(1,0,j)
                gano_tablero = True
    
    #Verificar inter diagonal secundaria 3D:                 (2)
                    
    for j in range(0, int(menu_pre_juego.N)):
        contador = 1
        for i in range(0, len(lista_tableros) - 1):
            if lista_tableros[i].casillas[int(menu_pre_juego.N)- (1 + i)][j].estado != lista_tableros[i+1].casillas[int(menu_pre_juego.N) - (i + 2)][j].estado or lista_tableros[i].casillas[int(menu_pre_juego.N) - (i + 1)][j].estado == 0 or lista_tableros[i+1].casillas[int(menu_pre_juego.N)-(i + 2)][j].estado == 0:
                break
            contador += 1
            if contador == len(lista_tableros):
                empate = 0
                pintar_tableros(2,0,j)
                gano_tablero = True


    #Verificar inter diagonal principal plana:             (3)
    for i in range(0, int(menu_pre_juego.N)):
        contador = 1
        for j in range(0, len(lista_tableros) - 1):
            if lista_tableros[j].casillas[i][j].estado != lista_tableros[j+1].casillas[i][j+1].estado or lista_tableros[j].casillas[i][j].estado == 0 or lista_tableros[j+1].casillas[i][j+1].estado == 0:
                break
            contador += 1
            if contador == len(lista_tableros):
                empate = 0
                pintar_tableros(3,i,0)
                gano_tablero = True
    
    #Verificar inter diagonal secundaria plana:            (4)        
    for i in range(0, int(menu_pre_juego.N)):
        contador = 1
        for j in range(0, len(lista_tableros) - 1):
            if lista_tableros[j].casillas[i][int(menu_pre_juego.N)- (1 + j)].estado != lista_tableros[j+1].casillas[i][int(menu_pre_juego.N)- (j + 2)].estado or lista_tableros[j].casillas[i][int(menu_pre_juego.N)- (1 + j)].estado == 0 or lista_tableros[j+1].casillas[i][int(menu_pre_juego.N)- (j + 2)].estado == 0:
                break
            contador += 1
            if contador == len(lista_tableros):
                empate = 0
                pintar_tableros(4,i,0)
                gano_tablero = True


    ##Verificar la diagonal inter tablero:           (5)
    contador = 1
    for i in range(0, int(menu_pre_juego.N) - 1):
        if lista_tableros[i].casillas[i][i].estado != lista_tableros[i+1].casillas[i+1][i+1].estado or lista_tableros[i].casillas[i][i].estado == 0 or lista_tableros[i+1].casillas[i+1][i+1].estado == 0:
            break
        contador += 1
        if contador == len(lista_tableros):
            empate = 0
            pintar_tableros(5,0,0)
            gano_tablero = True

    
    #Verificar la diagonal secundaria intertablero:    (6)
    contador = 1
    for i in range(0, int(menu_pre_juego.N) - 1):
        if lista_tableros[i].casillas[i][int(menu_pre_juego.N) - (i+1)].estado != lista_tableros[i+1].casillas[i+1][int(menu_pre_juego.N)- (i + 2)].estado or lista_tableros[i].casillas[i][int(menu_pre_juego.N)- (i+1)].estado == 0 or lista_tableros[i+1].casillas[i+1][int(menu_pre_juego.N)- (i + 2)].estado == 0:
            break
        contador += 1
        if contador == len(lista_tableros):
            empate = 0
            pintar_tableros(6,0,0)
            gano_tablero = True

    #Verificar la diagonal terciaria intertablero:              (7)
    contador = 1
    for i in range(0, int(menu_pre_juego.N) - 1):
        if lista_tableros[i].casillas[int(menu_pre_juego.N) - (i+1)][i].estado != lista_tableros[i+1].casillas[int(menu_pre_juego.N)- (i + 2)][i+1].estado or lista_tableros[i].casillas[int(menu_pre_juego.N)- (i+1)][i].estado == 0 or lista_tableros[i+1].casillas[int(menu_pre_juego.N)- (i + 2)][i+1].estado == 0:
            break
        contador += 1
        if contador == len(lista_tableros):
            empate = 0
            pintar_tableros(7,0,0)
            gano_tablero = True
    
    #Verificar la diagonal cuaternaria intertablero:             (8)
    contador = 1
    for i in range(0, int(menu_pre_juego.N) - 1):
        if lista_tableros[i].casillas[int(menu_pre_juego.N) - (i+1)][int(menu_pre_juego.N) - (i+1)].estado != lista_tableros[i+1].casillas[int(menu_pre_juego.N)- (i + 2)][int(menu_pre_juego.N)- (i + 2)].estado or lista_tableros[i].casillas[int(menu_pre_juego.N)- (i+1)][int(menu_pre_juego.N)- (i+1)].estado == 0 or lista_tableros[i+1].casillas[int(menu_pre_juego.N)- (i + 2)][int(menu_pre_juego.N)- (i + 2)].estado == 0:
            break
        contador += 1
        if contador == len(lista_tableros):
            empate = 0
            pintar_tableros(8,0,0)
            gano_tablero = True

    if gano_tablero and ya_gano == False:
        ganar_tableros()
    else:
        pass

    #Verificar empate
    if all( all(all(i.estado != 0 for i in j) for j in k.casillas) for k in lista_tableros) and (empate == 1):
        sleep(1)
        texto_displayer("> ¡Empate!")

        if (turno == 2):
            if partida % 2 == 1: 
                turno = 1
                cambia_turno()
            partida += 1
            colocar_boton_continuar()
        else: 
            if partida % 2 == 0: 
                turno = 2
                cambia_turno()
            partida += 1
            colocar_boton_continuar()

def pintar_tableros(victoria : int, fila : int = 0, columna : int  = 0) -> None:
    """
    Pinta las casillas de los tableros según el tipo de victoria, la fila o la columna en la que se gane.
    La variable `victoria` se utiliza como un ID de los tipos de victoria.

    ### Parámetros:
    * `self`: Referencia a sí mismo.
    * `victoria`: ID del tipo de victoria.
    * `fila`: Hace referencia a la fila en la que se ganó.
    * `columna`: Hace referencia a la columna en la que se ganó.

    ### Retorno: 
    * `None`: No devuelve nada.
    """    
    if victoria == 0:
        for i in lista_tableros:
            i.casillas[fila][columna].pintar_casilla("pink")
    elif victoria == 1:
        for i in range(0, int(menu_pre_juego.N)):
            lista_tableros[i].casillas[i][columna].pintar_casilla("pink")
    elif victoria == 2:
        for i in range(0, int(menu_pre_juego.N)):
            lista_tableros[i].casillas[int(menu_pre_juego.N) - i - 1][columna].pintar_casilla("pink")
    elif victoria == 3:
        for i in range(0, int(menu_pre_juego.N)):
            lista_tableros[i].casillas[fila][i].pintar_casilla("pink")
    elif victoria == 4:
        for i in range(0, int(menu_pre_juego.N)):
            lista_tableros[i].casillas[fila][int(menu_pre_juego.N) - i - 1].pintar_casilla("pink")
    elif victoria == 5:
        for i in range(0, int(menu_pre_juego.N)):
            lista_tableros[i].casillas[i][i].pintar_casilla("pink")
    elif victoria == 6:
        for i in range(0, int(menu_pre_juego.N)):
            lista_tableros[i].casillas[i][int(menu_pre_juego.N) - i - 1].pintar_casilla("pink")
    elif victoria == 7:
        for i in range(0, int(menu_pre_juego.N)):
            lista_tableros[i].casillas[int(menu_pre_juego.N) - (i+1)][i].pintar_casilla("pink")
    elif victoria == 8:
        for i in range(0, int(menu_pre_juego.N)):
            lista_tableros[i].casillas[int(menu_pre_juego.N) - i - 1][int(menu_pre_juego.N) - i - 1].pintar_casilla("pink")

def ganar_tableros() -> None:
    """
    Se llama una vez cuando procesar_intertableros encuentra uno o más patrones de victoria. 
    Modifica la puntuación, el displayer, los turnos, la diposición de las casillas para que no se pueda seguir jugando y coloca un botón continuar para que sigas jugando.

    ### Parámetros:
    * No recibe parámetros.

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
        sleep(0.3)
        
        mostrar_victoria()

        colocar_boton_continuar()
    else: 
        texto_displayer(f" > ¡{menu_pre_juego.jugador_2} ha ganado!")
        puntuacion[1] += 1
        if partida % 2 == 0: 
            turno = 2
            cambia_turno()
        partida += 1
        actualizar_puntuacion(puntuacion)
        sleep(0.3)

        mostrar_victoria()

        colocar_boton_continuar()

def reiniciar_tableros() -> None:
    """
    Llama al método reiniciar_tablero de cada tablero.
    También llama al método pintar_casilla de todas las casillas de todos los tableros para que se vuelvan a pintar de blanco y deje de mostrar la figura de victoria.

    ### Parámetros:
    * No recibe parámetros.

    ### Retorno: 
    * `None`: No devuelve nada.
    """  
    for e in lista_tableros:
        e.reiniciar_tablero()

        for i in e.casillas:
            for j in i:
                j.pintar_casilla("white")
    
    boton_continuar.place_forget()

    global esta_boton
    esta_boton = 0

    for i in lista_tableros:
        for j in i.casillas:
            for k in j:
                k.se_muestra = 0

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

def colocar_boton_continuar() -> None:
    """
    Simplemente coloca el botón continuar.

    ### Parámetros:
    * No recibe parámetros.

    ### Retorno: 
    * `None`: No devuelve nada.
    """  
    boton_continuar.place(x=460, y=350)

    global esta_boton
    esta_boton = 1

def cambio_color_continuar1(evento) -> None:
    """
    Cambia de color el botón continuar.
    Pasa el color a magenta en el fondo y negro a las letras.

    ### Parámetros:
    * `evento`: Nombre de referencia para que tkinter identifique el evento.

    ### Retorno: 
    * `None`: No devuelve nada.
    """
    boton_continuar['bg']= 'magenta3'
    boton_continuar['fg']= 'black'

def cambio_color_continuar2(evento) -> None:
    """
    Cambia de color el botón continuar.
    Pasa el color a negro en el fondo y blanco a las letras.

    ### Parámetros:
    * `evento`: Nombre de referencia para que tkinter identifique el evento.

    ### Retorno: 
    * `None`: No devuelve nada.
    """
    boton_continuar['bg']= 'black'
    boton_continuar['fg']= 'white'

boton_continuar : tk.Button = tk.Button(creador_raiz.raiz, text='Continuar', font= ('Arial Black', 10), background="black", foreground="white", command= reiniciar_tableros)

boton_continuar.bind(
    '<Enter>',
    cambio_color_continuar1
    )

boton_continuar.bind(
    '<Leave>',
    cambio_color_continuar2
    )
