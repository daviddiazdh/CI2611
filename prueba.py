import tkinter as tk

ventana = tk.Tk() #siempre debe haber ventana

tablero = tk.Canvas(ventana)
tablero.pack(side="left", fill="both")
rect = tablero.create_rectangle(0,0,1920,1080, fill="green")

ventana.mainloop()