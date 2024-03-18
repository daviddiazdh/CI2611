import tkinter as tk
from typing import List


##Declaración de la ventana
menu = tk.Tk()
alto_pantalla = menu.winfo_screenheight()
ancho_pantalla = menu.winfo_screenwidth()

alto_ventana = 600
ancho_ventana = 600

posicion_x= round((ancho_pantalla - ancho_ventana)/2)
posicion_y = round((alto_pantalla - alto_ventana)/2)

posicionraiz = str(ancho_ventana)+"x"+str(alto_ventana)+"+"+str(posicion_x)+"+"+str(posicion_y - 25)
menu.geometry(posicionraiz)
menu.resizable(0, 0)

menu.wm_iconbitmap('tres-en-raya1.ico')
menu.wm_title('N en Raya 3D')

##Título
lienzo_completo : tk.Canvas = tk.Canvas(menu, width= 400, height= 400)
lienzo_completo.place(x= 100, y=100)

etiqueta_datos : tk.Label = tk.Label(menu, text='Datos de juego:', font= ('Arial Black', 20))
etiqueta_datos.place(x=110, y=100)

##Entrada 1 Usuario:

etiqueta_1 : tk.Label = tk.Label(menu, text='Ingrese el nombre del jugador 1:', font= ('Arial Black', 10))
etiqueta_1.place(x=110, y=170)
nombre_jugador_1 : tk.Entry = tk.Entry(menu, font= ('Arial Black',10), width=28)
nombre_jugador_1.place(x= 110, y= 200)

##Entrada 1 Usuario:
etiqueta_2 : tk.Label = tk.Label(menu, text='Ingrese el nombre del jugador 2:', font= ('Arial Black', 10))
etiqueta_2.place(x=110, y=225)
nombre_jugador_2 : tk.Entry = tk.Entry(menu, font= ('Arial Black',10), width=28)
nombre_jugador_2.place(x= 110, y= 250)

##Entrada 3 Usuario:
etiqueta_3 : tk.Label = tk.Label(menu, text='Ingrese la dimensión del tablero:', font= ('Arial Black', 10))
etiqueta_3.place(x=110, y=275)
dimension : tk.Entry = tk.Entry(menu, font= ('Arial Black',10), width=28)
dimension.place(x= 110, y= 300)
retorno_g = ["", "", ""]

##Botón de inicio
boton_inicio : tk.Button = tk.Button(menu, text='Iniciar', font= ('Arial Black', 10), command= menu.destroy)
boton_inicio.place(x=400, y=350)

##Botón de regresar
boton_regresar : tk.Button = tk.Button(menu, text='Regresar', font= ('Arial Black', 10))
boton_regresar.place(x=80, y=350)

menu.mainloop()
