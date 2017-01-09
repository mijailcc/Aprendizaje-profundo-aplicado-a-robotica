from Camara import Camara 
from random import randint
import numpy as np

def crear():
    objetos = ['esponja', 'haki', 'dador', 'dadov', 'dadoa', 'cubo']
    camara = Camara()
    arreglo = None
    p = False
    for i in np.arange(6):
        obj = objetos[i]
        for j in np.arange(1299):
            k = j + 1
            img = camara.cargar('imagenes/' + obj + str(k) + '.jpg')
            print 'imagenes/' + obj + str(k) + '.jpg'
            (y, x, z) = img.shape
            nmin = min(x, y)
            corte = 0
            if nmin == x:
                img = camara.redimensionar(img, ancho = 256.0/x, alto = 1)
                corte = (y - 256) / 2
                img = camara.recortar(img, 0, 256, corte, y - corte)
            else:
                img = camara.redimensionar(img, ancho = 1, alto = 256.0/y)
                corte = (x - 256) / 2
                img = camara.recortar(img, corte, x - corte, 0, 256)
            (y, x, z) = img.shape
            if y > 257 or x > 257:
                img = camara.recortar(img, 0, 256, 0, 256)
            xcorte = randint(0, 32)
            ycorte = randint(0, 32)
            img = camara.recortar(img, xcorte, 256 - (32 - xcorte), ycorte, 256 - (32 - ycorte))
            salida = np.zeros(6)
            salida[i] = 1
            camara.guardar(img, 'entrena/' + obj + str(k))
            nuevo = np.array([img, salida])
            if not(p):
                arreglo = nuevo
                p = True
            else:
                arreglo = np.vstack((arreglo, nuevo))

    arreglo = np.random.permutation(arreglo)
    arreglo = np.random.permutation(arreglo)
    ent = int(1299 * 6 * 0.7)
    entrenamiento = arreglo[ : ent]
    prueba = arreglo[ent : ]
    np.save('entrenamiento.npy', entrenamiento)
    np.save('prueba.npy', prueba)

if __name__ == '__main__':
    crear()																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																	
