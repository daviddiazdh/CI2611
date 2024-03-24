import tkinter as tk
import creador_raiz

##Fondo
fondo : tk.PhotoImage = tk.PhotoImage(file='images/Fondo3.png')
fondo_etiqueta : tk.Label = tk.Label(creador_raiz.raiz, highlightthickness=0, image=fondo)

def cambio_color_1(e) -> None:
    """
    Cambia de color el botón jugar.
    Pasa el color a magenta en el fondo y negro a las letras.

    ### Parámetros:
    * `evento`: Nombre de referencia para que tkinter identifique el evento.

    ### Retorno: 
    * `None`: No devuelve nada.
    """
    boton_jugar['bg'] = 'magenta3'
    boton_jugar['fg'] = 'black'

def cambio_color_2(e) -> None:
    """
    Cambia de color el botón inicio.
    Pasa el color a negro en el fondo y blanco a las letras.

    ### Parámetros:
    * `evento`: Nombre de referencia para que tkinter identifique el evento.

    ### Retorno: 
    * `None`: No devuelve nada.
    """
    boton_jugar['bg'] = 'black'
    boton_jugar['fg'] = 'white'

def cambio_color_3(e) -> None:
    """
    Cambia de color el botón salir.
    Pasa el color a magenta en el fondo y negro a las letras.

    ### Parámetros:
    * `evento`: Nombre de referencia para que tkinter identifique el evento.

    ### Retorno: 
    * `None`: No devuelve nada.
    """
    boton_salir['bg'] = 'magenta3'
    boton_salir['fg'] = 'black'

def cambio_color_4(e) -> None:
    """
    Cambia de color el botón salir.
    Pasa el color a negro en el fondo y blanco a las letras.

    ### Parámetros:
    * `evento`: Nombre de referencia para que tkinter identifique el evento.

    ### Retorno: 
    * `None`: No devuelve nada.
    """
    boton_salir['bg'] = 'black'
    boton_salir['fg'] = 'white'

def ir_a_menu_pj() -> None:
    """
    Se prepara para ir al menú principal, borrando todo lo que se muestra en pantalla.

    ### Parámetros:
    * No recibe parámetros

    ### Retorno: 
    * `None`: No devuelve nada.
    """
    boton_jugar.place_forget()
    boton_salir.place_forget()
    creador_raiz.opcion_del_usuario = 1
    creador_raiz.raiz.quit()

def salir() -> None:
    """
    Destruye la venta y se sale del bucle while que está en el módulo de ejecución.

    ### Parámetros:
    * No recibe parámetros

    ### Retorno: 
    * `None`: No devuelve nada.
    """
    creador_raiz.raiz.destroy()
    creador_raiz.salir = True

##Botón de jugar
boton_jugar : tk.Button = tk.Button(creador_raiz.raiz, text='Jugar', font= ('Arial Black', 20), background="black", foreground="white", command=ir_a_menu_pj)

boton_jugar.bind(
    '<Enter>',
    cambio_color_1
)

boton_jugar.bind(
    '<Leave>',
    cambio_color_2
)

def iniciar() -> None:
    """
    Muestra los elementos del menú en pantalla. 

    ### Parámetros:
    * No recibe parámetros

    ### Retorno: 
    * `None`: No devuelve nada.
    """
    boton_salir.place(x=255, y=335)
    boton_jugar.place(x=248, y=255)

##Botón de salir
boton_salir : tk.Button = tk.Button(creador_raiz.raiz, text='Salir', font= ('Arial Black', 20), background="black", foreground="white", command= salir)

boton_salir.bind(
    '<Enter>',
    cambio_color_3
)

boton_salir.bind(
    '<Leave>',
    cambio_color_4
)

