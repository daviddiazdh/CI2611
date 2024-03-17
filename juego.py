import tkinter as tk
from typing import List, Tuple, Callable, Union
import winsound
from time import sleep

##windsound 
def play(path):
    winsound.PlaySound(path, winsound.SND_ASYNC)

##Código base
M : int = 300 #pixeles del tablero
N = int(input("Diga la dimensión de su tablero: "))
turno: int = 1          
puntuacion: List[int] = [0,0]

class Casilla:
    def __init__(self,
                 tablero : tk.Canvas, 
                 posicion : Tuple[int, int],
                 al_cambiar: Callable[[], None]):
        self.tablero = tablero
        self.lado: int = M/N
        self.lienzo: tk.Canvas = tablero
        self.esq_superior_izq: Tuple[int, int] = posicion
        self.estado: int = 0 #estado varia entre 0,1 y 2 para indicar vacio, cruz y circunferencia, respectivamente.
        self.al_cambiar = al_cambiar
        self.dibujar_casilla()

    def crear_cruz(self):
        global turno
        play('mouse-click.wav')
        self.tablero.create_line(self.esq_superior_izq[0] + self.lado / 5, self.esq_superior_izq[1] + self.lado / 5, 
                            self.esq_superior_izq[0] + self.lado * (4/5), self.esq_superior_izq[1] + self.lado * (4/5), fill = "black", width = self.lado / 5)
        self.tablero.create_line(self.esq_superior_izq[0] + self.lado * (4/5), self.esq_superior_izq[1] + self.lado / 5,
                            self.esq_superior_izq[0] + self.lado / 5, self.esq_superior_izq[1] + self.lado * (4/5), fill = "black", width = self.lado / 5)
        self.estado = 1
        self.tablero.update() 
        sleep(0.5)
        ##Procesa tablero
        self.al_cambiar()

        ##Cambia turno en et_turno:
        turno = 2
        cambia_turno()
        
    def crear_circulo(self):
        global turno
        play('mouse-click.wav')
        self.tablero.create_oval(self.esq_superior_izq[0] + self.lado / 6, self.esq_superior_izq[1] + self.lado / 6, 
                            self.esq_superior_izq[0] + self.lado * (5/6), self.esq_superior_izq[1] + self.lado * (5/6), fill = "red")
        self.tablero.create_oval(self.esq_superior_izq[0] + self.lado / 6 + self.lado / 5, self.esq_superior_izq[1] + self.lado / 6 + self.lado / 5, 
                            self.esq_superior_izq[0] + self.lado * (5/6) - self.lado/5, self.esq_superior_izq[1] + self.lado * (5/6) - self.lado / 5, fill = "white")
        self.estado = 2

        self.tablero.update() 
        sleep(0.5)
        ##Procesa tablero
        self.al_cambiar()

        ##Cambia turno en et_turno:
        turno = 1
        cambia_turno()
        
    def dibujar_casilla(self):
        global turno
        casilla: int = self.tablero.create_rectangle(self.esq_superior_izq[0], self.esq_superior_izq[1], self.esq_superior_izq[0] + self.lado, self.esq_superior_izq[1] + self.lado, fill="white", outline="black")
        self.tablero.tag_bind(
            casilla,
            "<Button-1>",
            lambda event: ((self.crear_cruz() if (turno == 1) else self.crear_circulo()) if (self.estado == 0) else print("No puedes hacer esto."))) #cambiar esto en un futuro

class Tablero:
    def __init__(self, raiz, M):
        self.tablero: tk.Canvas = tk.Canvas(raiz, width = M, height = M, background="black")
        self.tablero.place(x = 150, y = 150)
        self.tablero.update()

        self.lado: int = M
        self.casillas: List[List[Casilla]] = []
        self.dibujar_tablero()

    def dibujar_tablero (self):
        j: int = 0
        while (j < N):
            self.casillas.append([])
            i: int = 0
            while (i < N):
                self.casillas[j].append(Casilla(self.tablero, (i * (self.lado / N), j * (self.lado / N)), self.procesar_tablero))
                i += 1
            j += 1

    # def eliminar_tablero ():
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
        for i in range(N):
            contador = 0
            for j in range(N - 1):
                if (self.casillas[j][i].estado == 0 or self.casillas[j][i].estado != self.casillas[j + 1][i].estado):
                    contador = 0
                elif (self.casillas[j][i].estado != 0 and self.casillas[j][i].estado == self.casillas[j + 1][i].estado):
                    contador += 1
                else:
                    contador = 0
            if (contador == N - 1):
                self.ganar_tablero()
                empate = 0
            else:
                pass
        #Verifica diagonal
        
        if (all((self.casillas[i][i].estado != 0 and self.casillas[0][0].estado == self.casillas[i][i].estado) for i in range(N))):
            self.ganar_tablero()
            empate = 0
        else:
            pass

        #Verifica diagonal secundaria

        if (all((self.casillas[i][N - 1 - i].estado != 0 and self.casillas[0][N - 1].estado == self.casillas[i][N - 1 - i].estado) for i in range(N))):
            self.ganar_tablero()
            empate = 0
        else:
            pass

        #Verifica que no estén llenas las casillas:
        if  all( all(j.estado != 0 for j in i) for i in self.casillas) and empate == 1:
            texto_displayer("¡Empate!")
            self.reiniciar_tablero()

            
    def ganar_tablero (self):
        if (turno == 1): #El ganador fue el jugador 1
            texto_displayer("¡Jugador 1 ha ganado!")
            puntuacion[0] += 1
            actualizar_puntuacion(puntuacion)
            cancion = 'level.wav'
            play(cancion)
            self.reiniciar_tablero()
        else:
            texto_displayer("¡Jugador 2 ha ganado!")
            puntuacion[1] += 1
            actualizar_puntuacion(puntuacion)
            cancion = 'level.wav'
            play(cancion)
            self.reiniciar_tablero()
    
    def reiniciar_tablero (self):
        self.tablero.place_forget()
        tablero = Tablero(raiz, M)

##Declaración de la ventana y llamada a la primera clase padre Tablero
raiz = tk.Tk()
alto_pantalla = raiz.winfo_screenheight()
ancho_pantalla = raiz.winfo_screenwidth()

alto_ventana = 600
ancho_ventana = 600

posicion_x= round((ancho_pantalla - ancho_ventana)/2)
posicion_y = round((alto_pantalla - alto_ventana)/2)

posicionraiz = str(ancho_ventana)+"x"+str(alto_ventana)+"+"+str(posicion_x)+"+"+str(posicion_y - 25)
raiz.geometry(posicionraiz)
raiz.resizable(0, 0)

## Display de Turno

et_turno = tk.Label(
    raiz,
    text="Turno: ",
    font=("Arial Black", 20)
)

et_turno.place(x=30, y=5)

lienzo_turno: tk.Canvas = tk.Canvas(raiz, width=30,height=30)
lienzo_turno.place(x=135,y=13)

temp: List[int] = []

# Jugador 1 Cruz
cruz_1: int = lienzo_turno.create_line(5, 5, 25,25, width=8, fill="black")
temp.append(cruz_1)
cruz_2: int = lienzo_turno.create_line(5, 25, 25, 5, width=8, fill="black")
temp.append(cruz_2)

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
        circ_1: int = lienzo_turno.create_oval(3, 3, 27, 27, fill="red")
        temp.append(circ_1)
        circ_2: int = lienzo_turno.create_oval(10, 10, 20, 20, fill="white")
        temp.append(circ_2)


## Display de mensajes
lienzo_display: tk.Canvas = tk.Canvas(raiz, width= 300, height= 45)
lienzo_display.place(x=150, y=480)

temp_display: List[int] = []

#text_displayer cero
label_display: tk.Label = tk.Label(
    raiz,
    text= " "
)
label_display.place(x=155, y=488)
temp_display.append(label_display)

display: int = lienzo_display.create_rectangle(0,0,300,45, outline="black")

def texto_displayer (texto: str):
    texto_d: tk.Label = tk.Label(
        raiz,
        text= texto,
        font=("Arial Black", 15)
    )
    temp_display[0].place_forget()
    temp_display.pop(0)
    temp_display.append(texto_d)
    texto_d.place(x=155, y=488)


# Display de contador
temp_puntuacion: List[tk.Label] = []
label_puntuacion: tk.Label = tk.Label(
    raiz,
    text= "0  -  0",
    font=("Arial Black", 20)
)
label_puntuacion.place(x= 250,y= 5)
temp_puntuacion.append(label_puntuacion)

def actualizar_puntuacion (puntaje: List[int]):
    label_puntaje: tk.Label = tk.Label(
        raiz,
        text= f"{puntaje[0]}  -  {puntaje[1]}",
        font= ("Arial Black", 20)
    )
    temp_puntuacion[0].place_forget()
    temp_puntuacion.pop(0)
    temp_puntuacion.append(label_puntaje)
    label_puntaje.place(x= 250,y= 5)


raiz.wm_iconbitmap('tres-en-raya1.ico')
raiz.wm_title('N en Raya 3D')
tablero: Tablero = Tablero(raiz, M)
raiz.mainloop()