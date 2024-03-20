import tkinter as tk
from typing import List
import juego
import menu_principal

jugador_1: str = ""
jugador_2: str = ""
N: str = ""

def menu_pj(menu):
    
    ##Prueba imagen
    fondo = tk.PhotoImage(file='Fondo.png')
    fondo_etiqueta = tk.Label(menu, highlightthickness=0, image=fondo)
    fondo_etiqueta.place(x=0, y=0)

    ##Título
    etiqueta_datos : tk.Label = tk.Label(menu, text='Datos de juego:', font= ('Arial Black', 20), background="white")
    etiqueta_datos.place(x=130, y=100)

    ##Entrada 1 Usuario:
    etiqueta_1 : tk.Label = tk.Label(menu, text='Ingrese el nombre del jugador 1:', font= ('Arial Black', 10), background="white")
    etiqueta_1.place(x=130, y=170)
    nombre_jugador_1 : tk.Entry = tk.Entry(menu, font= ('Arial Black',10), width=28)
    nombre_jugador_1.place(x= 130, y= 200)

    ##Entrada 1 Usuario:
    etiqueta_2 : tk.Label = tk.Label(menu, text='Ingrese el nombre del jugador 2:', font= ('Arial Black', 10), background="white")
    etiqueta_2.place(x=130, y=225)
    nombre_jugador_2 : tk.Entry = tk.Entry(menu, font= ('Arial Black',10), width=28)
    nombre_jugador_2.place(x= 130, y= 250)

    ##Entrada 3 Usuario:
    etiqueta_3 : tk.Label = tk.Label(menu, text='Ingrese la dimensión del tablero:', font= ('Arial Black', 10), background="white")
    etiqueta_3.place(x=130, y=275)
    dimension : tk.Entry = tk.Entry(menu, font= ('Arial Black',10), width=28)
    dimension.place(x= 130, y= 300)

    def iniciar():
        fondo_etiqueta.place_forget()
        etiqueta_datos.place_forget()
        etiqueta_1.place_forget()
        nombre_jugador_1.place_forget()
        etiqueta_2.place_forget()
        nombre_jugador_2.place_forget()
        etiqueta_3.place_forget()
        dimension.place_forget()
        boton_inicio.place_forget()
        boton_regresar.place_forget()

        global jugador_1
        global jugador_2
        global N

        jugador_1 = nombre_jugador_1.get()
        jugador_2 = nombre_jugador_2.get()
        N = dimension.get()

        juego.iniciar_juego(menu, N, jugador_1, jugador_2)
    
    def regresar():
        fondo_etiqueta.place_forget()
        etiqueta_datos.place_forget()
        etiqueta_1.place_forget()
        nombre_jugador_1.place_forget()
        etiqueta_2.place_forget()
        nombre_jugador_2.place_forget()
        etiqueta_3.place_forget()
        dimension.place_forget()
        boton_inicio.place_forget()
        boton_regresar.place_forget()
        menu_principal.menu_principal(menu)



    ##Botón de inicio
    boton_inicio : tk.Button = tk.Button(menu, text='Iniciar', font= ('Arial Black', 10), background="white" ,command= iniciar)
    boton_inicio.place(x=300, y=350)

    ##Botón de regresar
    boton_regresar : tk.Button = tk.Button(menu, text='Regresar', font= ('Arial Black', 10), background="white", command= regresar)
    boton_regresar.place(x=140, y=350)

    menu.mainloop()
