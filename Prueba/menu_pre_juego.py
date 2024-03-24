import tkinter as tk
from typing import List
import creador_raiz

jugador_1: str = "David"
jugador_2: str = "Pedro"
N: str = "0"
contador_error : int = 0

##Fondo
fondo = tk.PhotoImage(file='images/Fondo.png')
fondo_etiqueta = tk.Label(creador_raiz.raiz, highlightthickness=0, image=fondo)

##Título
etiqueta_datos : tk.Label = tk.Label(creador_raiz.raiz, text='Datos de juego:', font= ('Arial Black', 20), background="white")

##Entrada 1 Usuario:
etiqueta_1 : tk.Label = tk.Label(creador_raiz.raiz, text='Ingrese el nombre del jugador 1:', font= ('Arial Black', 10), background="white")
nombre_jugador_1 : tk.Entry = tk.Entry(creador_raiz.raiz, font= ('Arial Black',10), width=28)

##Entrada 1 Usuario:
etiqueta_2 : tk.Label = tk.Label(creador_raiz.raiz, text='Ingrese el nombre del jugador 2:', font= ('Arial Black', 10), background="white")

nombre_jugador_2 : tk.Entry = tk.Entry(creador_raiz.raiz, font= ('Arial Black',10), width=28)

##Entrada 3 Usuario:
etiqueta_3 : tk.Label = tk.Label(creador_raiz.raiz, text='Ingrese la dimensión del tablero:', font= ('Arial Black', 10), background="white")

dimension : tk.Entry = tk.Entry(creador_raiz.raiz, font= ('Arial Black',10), width=28)

##Etiqueta Error:
lista_errores : List[tk.Label] = [] 
etiqueta_error : tk.Label = tk.Label(creador_raiz.raiz, text= "", font= ('Arial Black', 8), background="white", foreground='red')


def iniciar():
    
    etiqueta_datos.place(x=130, y=100)

    etiqueta_1.place(x=130, y=170)
    nombre_jugador_1.place(x= 130, y= 200)

    etiqueta_2.place(x=130, y=225)
    nombre_jugador_2.place(x= 130, y= 250)

    etiqueta_3.place(x=130, y=275)
    dimension.place(x= 130, y= 300)

    etiqueta_error.place(x=130, y=320)
    lista_errores.append(etiqueta_error)

    boton_inicio.place(x=300, y=350)
    boton_regresar.place(x=140, y=350)

##Mensaje Error:
def mostrar_error(texto):
    lista_errores[0].place_forget()
    lista_errores.pop(0)
    etiqueta_error : tk.Label = tk.Label(creador_raiz.raiz, text= texto, font= ('Arial Black', 8), background="white", foreground='red')
    etiqueta_error.place(x=130, y=320)
    lista_errores.append(etiqueta_error)

def iniciar_juego():
    
    global jugador_1
    global jugador_2
    global N
    global contador_error
    
    jugador_1 = nombre_jugador_1.get()
    jugador_2 = nombre_jugador_2.get()
    N = dimension.get()

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
            if contador_error == 1:
                lista_errores[0].place_forget()
                lista_errores.pop(0)
            creador_raiz.opcion_del_usuario = 1
            creador_raiz.raiz.quit()

        else: 
            mostrar_error("La dimensión escogida es incorrecta.")
            contador_error = 1
    else: 
        mostrar_error("No puedes jugar contra ti mismo.")
        contador_error = 1

def regresar():

        global contador_error
        
        etiqueta_datos.place_forget()
        etiqueta_1.place_forget()
        nombre_jugador_1.place_forget()
        etiqueta_2.place_forget()
        nombre_jugador_2.place_forget()
        etiqueta_3.place_forget()
        dimension.place_forget()
        boton_inicio.place_forget()
        boton_regresar.place_forget()
        if contador_error == 1:
            lista_errores[0].place_forget()
            lista_errores.pop(0)

        creador_raiz.opcion_del_usuario = 2
        creador_raiz.raiz.quit()

##Botón de inicio
boton_inicio : tk.Button = tk.Button(creador_raiz.raiz, text='Iniciar', font= ('Arial Black', 10), background="white" ,command= iniciar_juego)

##Botón de regresar
boton_regresar : tk.Button = tk.Button(creador_raiz.raiz, text='Regresar', font= ('Arial Black', 10), background="white", command= regresar)

    



