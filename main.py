import imageio
import numpy as np
import matplotlib.pyplot as plt


def pasar_a_YIQ(img):
    r = img[:, :, 0]/255
    g = img[:, :, 1]/255
    b = img[:, :, 2]/255

    Y = (r*0.299+g*0.587+b*0.114)
    I = (r*0.595716-g*0.274453-b*0.321263)
    Q = (r*0.211456-g*0.522591+b*0.311135)

    return(Y, I, Q)


def pasar_a_RGB(Y, I, Q):
    Y = np.clip(Y, 0.0, 1.0)
    I = np.clip(I, -0.5957, 0.5957)
    Q = np.clip(Q, -0.5226, 0.5226)

    r = (Y+0.9563*I+0.621*Q)*255
    g = (Y-0.2721*I-0.6474*Q)*255
    b = (Y-1.1070*I+1.7046*Q)*255

    img = np.zeros((np.shape(Y)[0], np.shape(Y)[1], 3), dtype='uint8')
    img[:, :, 0] = r
    img[:, :, 1] = g
    img[:, :, 2] = b

    return(img)


def graficar_resultados(img, modIluminancia, modSauracion, combinados, a, b):
    fig, ax = plt.subplots(2, 2)
    fig.set_size_inches(10, 10)
    ax[0, 0].imshow(img)
    ax[0, 1].imshow(modIluminancia)
    ax[1, 0].imshow(modSauracion)
    ax[1, 1].imshow(combinados)
    ax[0, 0].set_title("Original")
    ax[0, 1].set_title("Iluminacia modificada. a = " + str(a))
    ax[1, 0].set_title("Saturacion modificada. b = " + str(b))
    ax[1, 1].set_title("Valores Combinados")


def modifcar_valores(a, b, Y, I, Q):
    modIluminancia = pasar_a_RGB(a*Y, I, Q)
    modSauracion = pasar_a_RGB(Y, b*I, b*Q)
    combinados = pasar_a_RGB(a*Y, b*I, b*Q)
    graficar_resultados(img, modIluminancia, modSauracion, combinados, a, b)


img = imageio.imread('chip.bmp')

Y, I, Q = pasar_a_YIQ(img)

a = 0.6
b = 1.7

modifcar_valores(a, b, Y, I, Q)
