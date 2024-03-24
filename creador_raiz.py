from typing import List, Tuple, Union
import tkinter as tk

opcion_del_usuario : int = 0
salir : bool = False

raiz = tk.Tk()
##Declaración de la ventana:
##-------------------------------------------------------------##
alto_pantalla : float = raiz.winfo_screenheight()
ancho_pantalla : float  = raiz.winfo_screenwidth()

alto_ventana : int = 500
ancho_ventana : int = 600

posicion_x : int = round((ancho_pantalla - ancho_ventana)/2)
posicion_y : int = round((alto_pantalla - alto_ventana)/2)

posicionraiz : str = str(ancho_ventana)+"x"+str(alto_ventana)+"+"+str(posicion_x)+"+"+str(posicion_y - 25)
raiz.geometry(posicionraiz)
raiz.resizable(0, 0)
raiz['bg'] = 'white'

raiz.wm_iconbitmap('images/tres-en-raya1.ico')

raiz.wm_title('N en Raya 3D')