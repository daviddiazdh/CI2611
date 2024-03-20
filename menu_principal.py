import tkinter as tk

##Declaración de la ventana
raiz = tk.Tk()
alto_pantalla = raiz.winfo_screenheight()
ancho_pantalla = raiz.winfo_screenwidth()

alto_ventana = 500
ancho_ventana = 600

posicion_x= round((ancho_pantalla - ancho_ventana)/2)
posicion_y = round((alto_pantalla - alto_ventana)/2)

posicionraiz = str(ancho_ventana)+"x"+str(alto_ventana)+"+"+str(posicion_x)+"+"+str(posicion_y - 25)
raiz.geometry(posicionraiz)
raiz.resizable(0, 0)

raiz.wm_iconbitmap('tres-en-raya1.ico')
raiz.wm_title('N en Raya 3D')

##---------------------------------------------------##

def cambio_color_1(e):
    boton_jugar['bg'] = 'black'
    boton_jugar['fg'] = 'white'

def cambio_color_2(e):
    boton_jugar['bg'] = 'white'
    boton_jugar['fg'] = 'black'

##Botón de jugar
boton_jugar : tk.Button = tk.Button(raiz, text='Jugar', font= ('Arial Black', 10), background="white", foreground="black")
boton_jugar.place(x=270, y=220)


boton_jugar.bind(
    '<Enter>',
    cambio_color_1
)

boton_jugar.bind(
    '<Leave>',
    cambio_color_2
)







raiz.mainloop()
