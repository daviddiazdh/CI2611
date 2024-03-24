import tkinter as tk
from typing import List
import creador_raiz

jugador_1: str = "David"
jugador_2: str = "Pedro"
N: str = ""


def iniciar_menu_pre_juego():

    ##Título
    etiqueta_datos : tk.Label = tk.Label(creador_raiz.raiz, text='Datos de juego:', font= ('Arial Black', 20), background="white")
    etiqueta_datos.place(x=130, y=100)

    ##Entrada 1 Usuario:
    etiqueta_1 : tk.Label = tk.Label(creador_raiz.raiz, text='Ingrese el nombre del jugador 1:', font= ('Arial Black', 10), background="white")
    etiqueta_1.place(x=130, y=170)
    nombre_jugador_1 : tk.Entry = tk.Entry(creador_raiz.raiz, font= ('Arial Black',10), width=28)
    nombre_jugador_1.place(x= 130, y= 200)

    ##Entrada 1 Usuario:
    etiqueta_2 : tk.Label = tk.Label(creador_raiz.raiz, text='Ingrese el nombre del jugador 2:', font= ('Arial Black', 10), background="white")
    etiqueta_2.place(x=130, y=225)
    nombre_jugador_2 : tk.Entry = tk.Entry(creador_raiz.raiz, font= ('Arial Black',10), width=28)
    nombre_jugador_2.place(x= 130, y= 250)

    ##Entrada 3 Usuario:
    etiqueta_3 : tk.Label = tk.Label(creador_raiz.raiz, text='Ingrese la dimensión del tablero:', font= ('Arial Black', 10), background="white")
    etiqueta_3.place(x=130, y=275)
    dimension : tk.Entry = tk.Entry(creador_raiz.raiz, font= ('Arial Black',10), width=28)
    dimension.place(x= 130, y= 300)

    def iniciar():
        
        global jugador_1
        global jugador_2
        global N
        
        jugador_1 = nombre_jugador_1.get()
        jugador_2 = nombre_jugador_2.get()
        N = dimension.get()

        contador : int = 0
        if jugador_1 != jugador_2 and jugador_1 != "" and jugador_2 != "":
            if N != "" and all( i.isdigit() == True for i in N) and int(N) > 2:
                etiqueta_datos.place_forget()
                etiqueta_1.place_forget()
                nombre_jugador_1.place_forget()
                etiqueta_2.place_forget()
                nombre_jugador_2.place_forget()
                etiqueta_3.place_forget()
                dimension.place_forget()
                boton_inicio.place_forget()
                boton_regresar.place_forget()
                if contador == 1:
                    etiqueta_error.place_forget()
                creador_raiz.opcion_del_usuario = 1
                creador_raiz.raiz.quit()


            else: 
                etiqueta_error : tk.Label = tk.Label(creador_raiz.raiz, text= "La dimensión de su tablero es incorrecta.", font= ('Arial Black', 8), background="white", foreground='red')
                etiqueta_error.place(x=130, y=320)
                contador = 1
        else: 
            ##Etiqueta Error: 
            etiqueta_error : tk.Label = tk.Label(creador_raiz.raiz, text= "Los nombres no pueden ser iguales.", font= ('Arial Black', 8), background="white", foreground='red')
            etiqueta_error.place(x=130, y=320)
            contador = 1

    def regresar():
        etiqueta_datos.place_forget()
        etiqueta_1.place_forget()
        nombre_jugador_1.place_forget()
        etiqueta_2.place_forget()
        nombre_jugador_2.place_forget()
        etiqueta_3.place_forget()
        dimension.place_forget()
        boton_inicio.place_forget()
        boton_regresar.place_forget()
        creador_raiz.opcion_del_usuario = 2
        creador_raiz.raiz.quit()

    ##Botón de inicio
    boton_inicio : tk.Button = tk.Button(creador_raiz.raiz, text='Iniciar', font= ('Arial Black', 10), background="white" ,command= iniciar)
    boton_inicio.place(x=300, y=350)

    ##Botón de regresar
    boton_regresar : tk.Button = tk.Button(creador_raiz.raiz, text='Regresar', font= ('Arial Black', 10), background="white", command= regresar)
    boton_regresar.place(x=140, y=350)



