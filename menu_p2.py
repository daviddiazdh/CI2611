from typing import List, Tuple, Union
import tkinter as tk
import todo_en_uno

todo_en_uno.raiz

boton_jugar : tk.Button = 0
lista_boton : List[tk.Button] = []
bandera :int = 0

def crear_fondo_menu_p(raiz):
    fondo = tk.PhotoImage(file='images/Fondo3.png')
    fondo_etiqueta = tk.Label(raiz, highlightthickness=0, image=fondo)
    fondo_etiqueta.place(x=0, y=0)

def crear_botones(raiz):
    
    def cambio_color_1(e):
        boton_jugar['bg'] = 'black'
        boton_jugar['fg'] = 'white'

    def cambio_color_2(e):
        boton_jugar['bg'] = 'white'
        boton_jugar['fg'] = 'black'
    
    def cambio_color_3(e):
        boton_salir['bg'] = 'black'
        boton_salir['fg'] = 'white'

    def cambio_color_4(e):
        boton_salir['bg'] = 'white'
        boton_salir['fg'] = 'black'
    
    ##Botón de jugar
    boton_jugar : tk.Button = tk.Button(raiz, text='Jugar', font= ('Arial Black', 20), background="white", foreground="black", command= cambiar_condicion_para_menu)
    boton_jugar.place(x=225, y=220)

    boton_jugar.bind(
        '<Enter>',
        cambio_color_1
    )

    boton_jugar.bind(
        '<Leave>',
        cambio_color_2
    )

    ##Botón de salir
    boton_salir : tk.Button = tk.Button(raiz, text='Salir', font= ('Arial Black', 20), background="white", foreground="black", command= salir)
    boton_salir.place(x=233, y=320)

    boton_salir.bind(
        '<Enter>',
        cambio_color_3
    )

    boton_salir.bind(
        '<Leave>',
        cambio_color_4
    )

    lista_boton.append(boton_jugar)
    lista_boton.append(boton_salir)

def cambiar_condicion_para_menu():
    global bandera
    bandera = 1

def eliminar_boton(lista):
    for e in lista:
        e.place_forget()

    global lista_boton
    lista_boton = []

def salir(raiz):
    raiz.destroy()
