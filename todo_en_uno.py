from typing import List, Tuple, Union
import tkinter as tk


##Declaración de la ventana:
##-------------------------------------------------------------##
raiz = tk.Tk()

def crear_raiz():
    alto_pantalla = raiz.winfo_screenheight()
    ancho_pantalla = raiz.winfo_screenwidth()

    alto_ventana = 500
    ancho_ventana = 600

    posicion_x= round((ancho_pantalla - ancho_ventana)/2)
    posicion_y = round((alto_pantalla - alto_ventana)/2)

    posicionraiz = str(ancho_ventana)+"x"+str(alto_ventana)+"+"+str(posicion_x)+"+"+str(posicion_y - 25)
    raiz.geometry(posicionraiz)
    raiz.resizable(0, 0)
    raiz['bg'] = 'white'

    raiz.wm_iconbitmap('images/tres-en-raya1.ico')

    raiz.wm_title('N en Raya 3D')
##-----------------------------------------------------------##

