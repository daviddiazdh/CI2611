import tkinter as tk
import menu_pre_juego


##Fondo
def inicializar_fondo_menu_p(raiz):
    fondo = tk.PhotoImage(file='images/Fondo3.png')
    fondo_etiqueta = tk.Label(raiz, highlightthickness=0, image=fondo)
    fondo_etiqueta.place(x=0, y=0)

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

def ir_a_menu_pj():
    boton_jugar.place_forget()
    boton_salir.place_forget()
    fondo_etiqueta.place_forget()
    menu_pre_juego.menu_pj(raiz)

def salir():
    raiz.destroy()

##Botón de jugar
boton_jugar : tk.Button = tk.Button(raiz, text='Jugar', font= ('Arial Black', 20), background="white", foreground="black", command=ir_a_menu_pj)
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

