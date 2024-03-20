import tkinter as tk
from typing import List, Tuple, Callable, Union
import menu_pre_juego

##Constantes del programa

turno: int = 1
partida : int = 0

def iniciar_juego(raiz, dimensiones, jugador_1, jugador_2):

    global turno
    global partida

    turno = 1
    partida = 0
    M : int = 300 #pixeles del tablero
    puntuacion: List[int] = [0,0]
    dimensiones = int(dimensiones)

    class Casilla:
        def __init__(self,
                    tablero : tk.Canvas, 
                    posicion : Tuple[int, int],
                    al_cambiar: Callable[[], None]):
            self.tablero = tablero
            self.lado: int = M/dimensiones
            self.lienzo: tk.Canvas = tablero
            self.esq_superior_izq: Tuple[int, int] = posicion
            self.estado: int = 0 #estado varia entre 0,1 y 2 para indicar vacio, cruz y circunferencia, respectivamente.
            self.al_cambiar = al_cambiar
            self.dibujar_casilla()

        def crear_cruz(self):
            global turno
            self.tablero.create_line(self.esq_superior_izq[0] + self.lado / 5, self.esq_superior_izq[1] + self.lado / 5, 
                                self.esq_superior_izq[0] + self.lado * (4/5), self.esq_superior_izq[1] + self.lado * (4/5), fill = "black", width = self.lado / 5)
            self.tablero.create_line(self.esq_superior_izq[0] + self.lado * (4/5), self.esq_superior_izq[1] + self.lado / 5,
                                self.esq_superior_izq[0] + self.lado / 5, self.esq_superior_izq[1] + self.lado * (4/5), fill = "black", width = self.lado / 5)
            self.estado = 1
            self.tablero.update() 

            ##Cambia turno en et_turno:
            turno = 2
            cambia_turno()

            ##Procesa tablero
            self.al_cambiar()
            
        def crear_circulo(self):
            global turno
            self.tablero.create_oval(self.esq_superior_izq[0] + self.lado / 6, self.esq_superior_izq[1] + self.lado / 6, 
                                self.esq_superior_izq[0] + self.lado * (5/6), self.esq_superior_izq[1] + self.lado * (5/6), fill = "red")
            self.tablero.create_oval(self.esq_superior_izq[0] + self.lado / 6 + self.lado / 5, self.esq_superior_izq[1] + self.lado / 6 + self.lado / 5, 
                                self.esq_superior_izq[0] + self.lado * (5/6) - self.lado/5, self.esq_superior_izq[1] + self.lado * (5/6) - self.lado / 5, fill = "white")
            self.estado = 2

            self.tablero.update() 

            ##Cambia turno en et_turno:
            turno = 1
            cambia_turno()

            ##Procesa tablero
            self.al_cambiar()

        def dibujar_casilla(self):
            global turno
            casilla: int = self.tablero.create_rectangle(self.esq_superior_izq[0], self.esq_superior_izq[1], self.esq_superior_izq[0] + self.lado, self.esq_superior_izq[1] + self.lado, fill="white", outline="black")
            self.tablero.tag_bind(
                casilla,
                "<Button-1>",
                lambda event: ((self.crear_cruz() if (turno == 1) else self.crear_circulo()) if (self.estado == 0) else print("No puedes hacer esto."))) #cambiar esto en un futuro

    class Tablero:
        def __init__(self, raiz, M, N, al_regresar : Callable):
            self.tablero: tk.Canvas = tk.Canvas(raiz, width = M, height = M, background="black")
            self.tablero.place(x = 150, y = 100)
            self.tablero.update()
            self.N = N
            self.lado: int = M
            self.al_regresar = al_regresar
            self.casillas: List[List[Casilla]] = []
            self.dibujar_tablero()

        def dibujar_tablero (self):
            self.crear_boton_regresar()
            j: int = 0
            while (j < self.N):
                self.casillas.append([])
                i: int = 0
                while (i < self.N):
                    self.casillas[j].append(Casilla(self.tablero, (i * (self.lado / self.N), j * (self.lado / self.N)), self.procesar_tablero))
                    i += 1
                j += 1

        def eliminar_tablero (self):
            self.tablero.place_forget()
            self.al_regresar()

        def procesar_tablero (self):

            empate : int = 1
            #Verifica filas
            for fila in self.casillas:
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
                self.ganar_tablero()
                empate = 0
            else:
                pass
            
            global partida
            #Verifica que no estén llenas las casillas:
            if  all( all(j.estado != 0 for j in i) for i in self.casillas) and empate == 1:
                texto_displayer("> ¡Empate!")
                partida += 1
                self.reiniciar_tablero()

        
        def ganar_tablero (self):
            global partida
            global turno
            if (turno == 2): #El ganador fue el jugador 1
                texto_displayer(f" > ¡{jugador_1} ha ganado!")
                puntuacion[0] += 1
                if partida % 2 == 1: 
                    turno = 1
                    cambia_turno()
                partida += 1
                actualizar_puntuacion(puntuacion)
                self.reiniciar_tablero()
            else:
                texto_displayer(f" > ¡{jugador_2} ha ganado!")
                puntuacion[1] += 1
                if partida % 2 == 0: 
                    turno = 2
                    cambia_turno()
                partida += 1
                actualizar_puntuacion(puntuacion)
                self.reiniciar_tablero()

        
        def reiniciar_tablero (self):
            self.tablero.place_forget()
            tablero = Tablero(raiz, M, dimensiones, self.al_regresar)

        ##Boton regresar:
        def crear_boton_regresar(self):
            def cambio_color_1(evento):
                self.boton_regresar['bg']= 'black'
                self.boton_regresar['fg']= 'white'

            def cambio_color_2(evento):
                self.boton_regresar['bg']= 'white'
                self.boton_regresar['fg']= 'black'

            self.boton_regresar : tk.Button = tk.Button(raiz, text='Regresar', font= ('Arial Black', 10), background="white", foreground="black", command= self.eliminar_tablero)
            self.boton_regresar.place(x=460, y=400)

            self.boton_regresar.bind(
                '<Enter>',
                cambio_color_1
                )

            self.boton_regresar.bind(
                '<Leave>',
                cambio_color_2
                )

    
    #Funciones para botones#
    ##-------------------------------------------------------------------------------------#
     
    def eliminar_imagen():
        fondo_etiqueta.place_forget()
        et_turno.place_forget()
        lienzo_turno.delete(cruz_1)
        lienzo_turno.delete(cruz_2)
        lienzo_turno.place_forget()
        lienzo_display.delete(display)
        lienzo_display.place_forget()
        label_puntuacion.place_forget()
        label_display.place_forget()
        lienzo_cuadro.place_forget()
        menu_pre_juego.menu_pj(raiz)

    
    ##Declaración de elementos:
    #--------------------------------------------------------------------------------------#
    ##Fondo
    fondo = tk.PhotoImage(file='Fondo2.png')
    fondo_etiqueta = tk.Label(raiz, highlightthickness=0, image=fondo,)

    ## Display de Turno
    et_turno = tk.Label(
        raiz,
        text="Turno: ",
        font=("Arial Black", 20),
        background='white',
        highlightthickness=0,
    )

    ## Turno Lienzo
    lienzo_turno: tk.Canvas = tk.Canvas(raiz, width=30,height=30, background='white', highlightthickness=0)
    temp: List[int] = []

    ##Cruces
    cruz_1 : int = 0
    cruz_2 : int = 0

    ## Display de mensajes
    lienzo_display: tk.Canvas = tk.Canvas(raiz, width= 300, height= 45)
    temp_display: List[int] = []

    #text_displayer cero
    label_display: tk.Label = tk.Label(
        raiz,
        text= " > ",
        font= ('Arial Black', 10),
        fg='white',
        background='black'
    )

    ##Display
    display : int = 0

    # Display de contador
    temp_puntuacion: List[tk.Label] = []
    label_puntuacion: tk.Label = tk.Label(
        raiz,
        text= "0  -  0",
        font=("Arial Black", 20),
        background='white',
        highlightthickness=0
    )

    ##Cuadro negro superior
    lienzo_cuadro: tk.Canvas = tk.Canvas(raiz, width= 302, height= 20, background='black', highlightthickness=0)

    #--------------------------------------------------------------------------------------#

    ##Seteo de elementos
    def elementos_constantes():

        fondo_etiqueta.place(x=0, y=0)
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
        temp_display.append(label_display)

        ##Display
        display: int = lienzo_display.create_rectangle(0,0,300,45, outline="black", fill='black')

        # Display de contador
        label_puntuacion.place(x= 485,y= 5)
        temp_puntuacion.append(label_puntuacion)

        ##Cuadro negro superior
        lienzo_cuadro.place(x=150, y=80)

        tablero : Tablero = Tablero(raiz,M,dimensiones, eliminar_imagen)
        
    elementos_constantes()

    def cambia_turno ():
        if (turno == 1):
            for e in temp:
                lienzo_turno.delete(e)
            cruz_1: int = lienzo_turno.create_line(5, 5, 25,25, width=8, fill="black")
            temp.append(cruz_1)
            cruz_2: int = lienzo_turno.create_line(5, 25, 25, 5, width=8, fill="black")
            temp.append(cruz_2)
        else:
            for e in temp:
                lienzo_turno.delete(e)
            cruz_1: int = lienzo_turno.create_oval(3, 3, 27, 27, fill="red")
            temp.append(cruz_1)
            cruz_2: int = lienzo_turno.create_oval(10, 10, 20, 20, fill="white")
            temp.append(cruz_2)

    def texto_displayer (texto: str):
        texto_d: tk.Label = tk.Label(
            raiz,
            text= texto,
            font=("Arial Black", 10),
            fg='white',
            background='black'
        )
        temp_display[0].place_forget()
        temp_display.pop(0)
        temp_display.append(texto_d)
        texto_d.place(x=155, y=432)

    def actualizar_puntuacion (puntaje: List[int]):
        label_puntaje: tk.Label = tk.Label(
            raiz,
            text= f"{puntaje[0]}  -  {puntaje[1]}",
            font= ("Arial Black", 20),
            background='white',
            highlightthickness=0
        )
        temp_puntuacion[0].place_forget()
        temp_puntuacion.pop(0)
        temp_puntuacion.append(label_puntaje)
        label_puntaje.place(x= 485,y= 5)


    raiz.mainloop()

