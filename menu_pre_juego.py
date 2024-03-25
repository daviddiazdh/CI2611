import tkinter as tk
from typing import List
import creador_raiz

jugador_1: str = ""
jugador_2: str = ""
N: str = "0"
##Funciones para botones: 
def cambio_color_1(e) -> None:
    """
    Cambia de color el botón inicio.
    Pasa el color a magenta en el fondo y negro a las letras.

    ### Parámetros:
    * `evento`: Nombre de referencia para que tkinter identifique el evento.

    ### Retorno: 
    * `None`: No devuelve nada.
    """
    boton_inicio['bg'] = 'magenta3'
    boton_inicio['fg'] = 'black'

def cambio_color_2(e) -> None:
    """
    Cambia de color el botón inicio.
    Pasa el color a negro en el fondo y blanco a las letras.

    ### Parámetros:
    * `evento`: Nombre de referencia para que tkinter identifique el evento.

    ### Retorno: 
    * `None`: No devuelve nada.
    """
    boton_inicio['bg'] = 'black'
    boton_inicio['fg'] = 'white'

def cambio_color_3(e) -> None:
    """
    Cambia de color el botón regresar.
    Pasa el color a magenta en el fondo y negro a las letras.

    ### Parámetros:
    * `evento`: Nombre de referencia para que tkinter identifique el evento.

    ### Retorno: 
    * `None`: No devuelve nada.
    """
    boton_regresar['bg'] = 'magenta3'
    boton_regresar['fg'] = 'black'

def cambio_color_4(e) -> None:
    """
    Cambia de color el botón regresar.
    Pasa el color a negro en el fondo y blanco a las letras.

    ### Parámetros:
    * `evento`: Nombre de referencia para que tkinter identifique el evento.

    ### Retorno: 
    * `None`: No devuelve nada.
    """
    boton_regresar['bg'] = 'black'
    boton_regresar['fg'] = 'white'


##Fondo
fondo = tk.PhotoImage(file='images/Fondo.png')
fondo_etiqueta = tk.Label(creador_raiz.raiz, highlightthickness=0, image=fondo)

##Título
etiqueta_datos : tk.Label = tk.Label(creador_raiz.raiz, text='Datos de juego:', font= ('Arial Black', 20), background="white")

##Entrada 1 Usuario:
etiqueta_1 : tk.Label = tk.Label(creador_raiz.raiz, text='Ingrese el nombre del jugador 1:', font= ('Arial Black', 10), background="white")
nombre_jugador_1 : tk.Entry = tk.Entry(creador_raiz.raiz, font= ('Arial Black',10), foreground='magenta3',  width=28)

##Entrada 1 Usuario:
etiqueta_2 : tk.Label = tk.Label(creador_raiz.raiz, text='Ingrese el nombre del jugador 2:', font= ('Arial Black', 10), background="white")

nombre_jugador_2 : tk.Entry = tk.Entry(creador_raiz.raiz, font= ('Arial Black',10), foreground='magenta3', width=28)

##Entrada 3 Usuario:
etiqueta_3 : tk.Label = tk.Label(creador_raiz.raiz, text='Ingrese la dimensión del tablero:', font= ('Arial Black', 10), background="white")

dimension : tk.Entry = tk.Entry(creador_raiz.raiz, foreground='magenta3', font= ('Arial Black',10), width=28)

##Etiqueta Error:
texto_SV : tk.StringVar = tk.StringVar() 
etiqueta_error : tk.Label = tk.Label(creador_raiz.raiz, textvariable= texto_SV, font= ('Arial Black', 8), background="white", foreground='magenta3')

def iniciar() -> None:
    """
    Coloca todos los elementos que se mostrarán en pantalla. 

    ### Parámetros:
    * No recibe parámetros.

    ### Retorno: 
    * `None`: No devuelve nada.
    """   
    etiqueta_datos.place(x=130, y=100)

    etiqueta_1.place(x=130, y=170)
    nombre_jugador_1.place(x= 130, y= 200)

    etiqueta_2.place(x=130, y=225)
    nombre_jugador_2.place(x= 130, y= 250)

    etiqueta_3.place(x=130, y=275)
    dimension.place(x= 130, y= 300)

    etiqueta_error.place(x=130, y=320)

    boton_inicio.place(x=300, y=350)
    boton_regresar.place(x=140, y=350)

##Mensaje Error:
def mostrar_error(texto) -> None:
    """
    Muestra un mensaje de error en la interfaz.

    ### Parámetros:
    * `texto`: Texto que se quiere mostrar como error.

    ### Retorno: 
    * `None`: No devuelve nada.
    """  
    texto_SV.set(texto)

def iniciar_juego() -> None:
    """
    Se prepara para entrar en el módulo juego, borrando todo lo que se muestra en pantalla.

    ### Parámetros:
    * No recibe parámetros.

    ### Retorno: 
    * `None`: No devuelve nada.
    """ 
    global jugador_1
    global jugador_2
    global N
    
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
            creador_raiz.opcion_del_usuario = 1
            creador_raiz.raiz.quit()

        else: 
            mostrar_error("La dimensión escogida es incorrecta.")
    else: 
        mostrar_error("No puedes jugar contra ti mismo.")

def regresar() -> None:
    """
    Se prepara para entrar en el módulo menu principal, borrando todo lo que se muestra en pantalla.

    ### Parámetros:
    * No recibe parámetros.

    ### Retorno: 
    * `None`: No devuelve nada.
    """ 
    etiqueta_datos.place_forget()
    etiqueta_1.place_forget()
    nombre_jugador_1.place_forget()
    etiqueta_2.place_forget()
    nombre_jugador_2.place_forget()
    etiqueta_3.place_forget()
    dimension.place_forget()
    boton_inicio.place_forget()
    boton_regresar.place_forget()
    etiqueta_error.place_forget()
    creador_raiz.opcion_del_usuario = 2
    creador_raiz.raiz.quit()

##Botón de inicio
boton_inicio : tk.Button = tk.Button(creador_raiz.raiz, text='Iniciar', font= ('Arial Black', 10), background="black", foreground="white" ,command= iniciar_juego)

boton_inicio.bind(
    '<Enter>',
    cambio_color_1
)

boton_inicio.bind(
    '<Leave>',
    cambio_color_2
)

##Botón de regresar
boton_regresar : tk.Button = tk.Button(creador_raiz.raiz, text='Regresar', font= ('Arial Black', 10), background="black", foreground="white", command= regresar)

boton_regresar.bind(
    '<Enter>',
    cambio_color_3
)

boton_regresar.bind(
    '<Leave>',
    cambio_color_4
)


