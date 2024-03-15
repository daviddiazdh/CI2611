import tkinter as tk

ventana = tk.Tk() #siempre debe haber ventana

tablero = tk.Canvas(ventana, width = 500, height = 500)
tablero.place(x = 433, y = 114)
rect_00 = tablero.create_rectangle(0,0,100,100, activeoutline= "green" , fill="white")
rect_01 = tablero.create_rectangle(100,0,200,100, activeoutline= "green" , fill="white")
rect_02 = tablero.create_rectangle(200,0,300,100, activeoutline= "green" , fill="white")
rect_03 = tablero.create_rectangle(300,0,400,100, activeoutline= "green" , fill="white")
rect_04 = tablero.create_rectangle(400,0,500,100, activeoutline= "green" , fill="white")

def crear_cruz(event):
    tablero.create_line(20,20,80,80, fill = "red", width = 5)
    tablero.create_line(80,20,20,80, fill = "red", width = 5)

def crear_círculo(event):
    tablero.create_oval(120,20,180,80, fill = "blue")


tablero.tag_bind(
    rect_00,
    "<Button-1>",
    crear_cruz

)

tablero.tag_bind(
    rect_01,
    "<Button-1>",
    crear_círculo

)


rect_10 = tablero.create_rectangle(0,100,100,200, activeoutline= "green" , fill="white")
rect_11 = tablero.create_rectangle(100,100,200,200, activeoutline= "green" , fill="white")
rect_12 = tablero.create_rectangle(200,100,300,200, activeoutline= "green" , fill="white")
rect_13 = tablero.create_rectangle(300,100,400,200, activeoutline= "green" , fill="white")
rect_14 = tablero.create_rectangle(400,100,500,200, activeoutline= "green" , fill="white")

rect_20 = tablero.create_rectangle(0,200,100,300, activeoutline= "green" , fill="white")
rect_21 = tablero.create_rectangle(100,200,200,300, activeoutline= "green" , fill="white")
rect_22 = tablero.create_rectangle(200,200,300,300, activeoutline= "green" , fill="white")
rect_23 = tablero.create_rectangle(300,200,400,300, activeoutline= "green" , fill="white")
rect_24 = tablero.create_rectangle(400,200,500,300, activeoutline= "green" , fill="white")

rect_30 = tablero.create_rectangle(0,300,100,400, activeoutline= "green" , fill="white")
rect_31 = tablero.create_rectangle(100,300,200,400, activeoutline= "green" , fill="white")
rect_32 = tablero.create_rectangle(200,300,300,400, activeoutline= "green" , fill="white")
rect_33 = tablero.create_rectangle(300,300,400,400, activeoutline= "green" , fill="white")
rect_34 = tablero.create_rectangle(400,300,500,400, activeoutline= "green" , fill="white")

rect_40 = tablero.create_rectangle(0,400,100,500, activeoutline= "green" , fill="white")
rect_41 = tablero.create_rectangle(100,400,200,500, activeoutline= "green" , fill="white")
rect_42 = tablero.create_rectangle(200,400,300,500, activeoutline= "green" , fill="white")
rect_43 = tablero.create_rectangle(300,400,400,500, activeoutline= "green" , fill="white")
rect_44 = tablero.create_rectangle(400,400,500,500, activeoutline= "green" , fill="white")

#2x + 500 = 1366             x= 258           
#2y + 480 = 768              y= 144
ventana.mainloop()