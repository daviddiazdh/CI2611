import creador_raiz
import menu_principal
import menu_pre_juego
import juego

def colocar_fondo(fondo):
    fondo.place(x=0, y=0)

def eliminar_fondo(fondo_etiqueta):
    fondo_etiqueta.place_forget()

condicion : bool = True

def terminar_while():
    global condicion
    condicion = False

while condicion:
    colocar_fondo(menu_principal.fondo_etiqueta)
    menu_principal.iniciar()
    creador_raiz.raiz.mainloop()

    if creador_raiz.salir == True:
        break
    
    eliminar_fondo(menu_principal.fondo_etiqueta)

    if creador_raiz.opcion_del_usuario == 1:
        colocar_fondo(menu_pre_juego.fondo_etiqueta)

        menu_pre_juego.iniciar()

        creador_raiz.raiz.mainloop()

        eliminar_fondo(menu_pre_juego.fondo_etiqueta)

    if creador_raiz.opcion_del_usuario == 1:
        colocar_fondo(juego.fondo_etiqueta)

        juego.iniciar()

        creador_raiz.raiz.mainloop()

        eliminar_fondo(juego.fondo_etiqueta)
        

