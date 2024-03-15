import tkinter as tk

ventana = tk.Tk() #siempre debe haber ventana

etiqueta = tk.Label(
    ventana,
    text="diversion pura aqui"
)

def saludo ():
    print("hola")
    return


etiqueta.place(x=10,y=10)

cuadrito = tk.Canvas(ventana, width=500, height=500)
cuadrito.place(x=120,y=120)
#etiqueta.pack()
rect = cuadrito.create_rectangle(500, 500, 0, 0, fill="blue")

def cambiar_color():
    cuadrito.itemconfig(rect, fill="red")


# cuadrito.tag_bind(
# rect, 
# "<Button-1>", 
# cambiar_color
# )

botón = tk.Button(
    ventana,
    text="da click aqui para ganar 1BT",
    command=cambiar_color
)

botón.place(x=80,y=80)


ventana.mainloop()