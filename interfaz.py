import imageio
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import ttk
from prueba2 import pasar_a_RGB, pasar_a_YIQ

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


def obtener():
    obtener = Toplevel()
    img = combo1.get()
    a = float(combo2.get())
    b = float(combo3.get())
    RGB = imageio.imread(img)
    RGB = np.clip(RGB / 255., 0., 1.)
    YIQ = pasar_a_YIQ(RGB)
    nueva = pasar_a_RGB(YIQ[:, :, 0], YIQ[:, :, 1], YIQ[:, :, 2])
    imageio.imwrite("nueva.png", nueva.astype(np.uint8))
    
    mostrar = tkinter.


ventana = Tk()
ventana.title('Practica 1')
ventana.geometry('250x300')

texto1 = StringVar()
texto1.set("Seleccione una imágen")

texto2 = StringVar()
texto2.set("Seleccione un valor de a")

texto3 = StringVar()
texto3.set("Seleccione un valor de b")

etiqueta1 = Label(ventana, textvariable=texto1).place(x=50, y=28)
combo1 = ttk.Combobox(ventana)
combo1.place(x=50, y=50)
combo1["values"] = ('chip.bmp', 'lena.png')

etiqueta2 = Label(ventana, textvariable=texto2).place(x=50, y=78)
combo2 = ttk.Combobox(ventana)
combo2.place(x=50, y=100)
combo2["values"] = ('0.4', '0.6', '0.8', '1.2', '1.4')

etiqueta3 = Label(ventana, textvariable=texto3).place(x=50, y=128)
combo3 = ttk.Combobox(ventana)
combo3.place(x=50, y=150)
combo3["values"] = ('0.4', '0.6', '0.8', '1.2', '1.4')

boton = Button(ventana, command=obtener, text="Calcular").place(x=75, y=250)

ventana.mainloop()
