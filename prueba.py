import tkinter as tk
from typing import List, Tuple, Callable, Union

M : int = 400 #pixeles del tablero
N = int(input("Diga la dimensión de su tablero: "))
turno: int = 1          

class Casilla:
    def __init__(self,
                 tablero : tk.Canvas, 
                 posicion : Tuple[int, int]):
        self.tablero = tablero
        self.lado: int = M/N
        self.lienzo: tk.Canvas = tablero
        self.esq_superior_izq: Tuple[int, int] = posicion
        self.estado: int = 0 #estado varia entre 0,1 y 2 para indicar vacio, cruz y circunferencia, respectivamente.
        self.dibujar_casilla()

    def crear_cruz(self):
        global turno
        self.tablero.create_line(self.esq_superior_izq[0] + self.lado / 5, self.esq_superior_izq[1] + self.lado / 5, 
                            self.esq_superior_izq[0] + self.lado * (4/5), self.esq_superior_izq[1] + self.lado * (4/5), fill = "black", width = self.lado / 5)
        self.tablero.create_line(self.esq_superior_izq[0] + self.lado * (4/5), self.esq_superior_izq[1] + self.lado / 5,
                            self.esq_superior_izq[0] + self.lado / 5, self.esq_superior_izq[1] + self.lado * (4/5), fill = "black", width = self.lado / 5)
        self.estado = 1
        turno = 2

    def crear_circulo(self):
        global turno
        self.tablero.create_oval(self.esq_superior_izq[0] + self.lado / 6, self.esq_superior_izq[1] + self.lado / 6, 
                            self.esq_superior_izq[0] + self.lado * (5/6), self.esq_superior_izq[1] + self.lado * (5/6), fill = "red")
        self.tablero.create_oval(self.esq_superior_izq[0] + self.lado / 6 + self.lado / 5, self.esq_superior_izq[1] + self.lado / 6 + self.lado / 5, 
                            self.esq_superior_izq[0] + self.lado * (5/6) - self.lado/5, self.esq_superior_izq[1] + self.lado * (5/6) - self.lado / 5, fill = "white")
        self.estado = 2
        turno = 1

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
        self.tablero.place(x = 100, y = 100)
        self.tablero.update()

        self.estado: bool = False #False si está jugando, True si está ganado
        self.lado: int = M
        self.casillas: List[List[Casilla]] = []
        self.dibujar_tablero()

    def dibujar_tablero (self):
        j: int = 0
        while (j < N):
            self.casillas.append([])
            i: int = 0
            while (i < N):
                self.casillas[j].append(Casilla(self.tablero, (i * (self.lado / N), j * (self.lado / N))))
                i += 1
            j += 1

    # def eliminar_tablero ():
    # def ganar_tablero ():
    # def empatar_tablero ():
    # def reiniciar_tablero ():

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

raiz.wm_iconbitmap('tres-en-raya1.ico')
raiz.wm_title('N en Raya 3D')
tablero: Tablero = Tablero(raiz, M)
raiz.mainloop()