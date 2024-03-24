import tkinter as tk
import creador_raiz


def iniciar_menu_principal():

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
        creador_raiz.opcion_del_usuario = 1
        creador_raiz.raiz.quit()

    def salir():
        creador_raiz.raiz.destroy()
        creador_raiz.salir = True

    ##Botón de jugar
    boton_jugar : tk.Button = tk.Button(creador_raiz.raiz, text='Jugar', font= ('Arial Black', 20), background="white", foreground="black", command=ir_a_menu_pj)
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
    boton_salir : tk.Button = tk.Button(creador_raiz.raiz, text='Salir', font= ('Arial Black', 20), background="white", foreground="black", command= salir)
    boton_salir.place(x=233, y=320)

    boton_salir.bind(
        '<Enter>',
        cambio_color_3
    )

    boton_salir.bind(
        '<Leave>',
        cambio_color_4
    )

