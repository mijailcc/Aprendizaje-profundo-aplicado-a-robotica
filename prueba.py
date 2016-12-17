import numpy as np
from Red import Red
from Camara import Camara
from random import randint

def iniciar():
    camara = Camara()
    ##imagen = camara.imagen()
    imagen = camara.cargar('imagen.jpg')
    (y, x, z) = imagen.shape
    nmin = min(x, y)
    if x > 224 and y > 224:
	corte = 0
    	if nmin == x:
        	imagen = camara.redimensionar(imagen, ancho = 256, alto = y)
        	corte = (y - 256) / 2
        	imagen = camara.recortar(imagen, 0, 256, corte, y - corte)
    	else:
        	imagen = camara.redimensionar(imagen, ancho = x, alto = 256)
        	corte = (x - 256) / 2
        	imagen = camara.recortar(imagen, corte, x - corte, 0, 256)
        (y, x, z) = imagen.shape
    	if y > 257 or x > 257:
        	imagen = camara.recortar(imagen, 0, 256, 0, 256)
    	xcorte = randint(0, 32)
    	ycorte = randint(0, 32)
    	imagen = camara.recortar(imagen, xcorte, 256 - (32 - xcorte), ycorte, 256 - (32 - ycorte))
    else:
       	imagen = camara.redimensionar(imagen, ancho = 224, alto = 224)
    red = Red(Pesos = True)
    opcion = red.alimentar(imagen)[0]
    print opcion
    if opcion[0] > 0.5:
        print "Esponja"
    if opcion[1] > 0.5:
        print "Haki"
    if opcion[2] > 0.5:
        print "Dado rojo"
    if opcion[3] > 0.5:
        print "Dado verde"
    if opcion[4] > 0.5:
        print "Dado azul"
    if opcion[5] > 0.5:
        print "Cubo"

if __name__ == '__main__':
    iniciar()
