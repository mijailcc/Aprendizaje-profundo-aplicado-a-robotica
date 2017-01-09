from Camara import Camara 
import numpy as np

def crear():
    objetos = ['esponja', 'haki', 'dador', 'dadov', 'dadoa', 'cubo']
    camara = Camara()
    for i in np.arange(6):
        obj = objetos[i]
        inicio = 100
        for j in np.arange(100):
            k = j + 1
            inicio -= 1
            img = camara.cargar('imagenes/' + obj + str(k) + '.jpg')
            for t in np.arange(3):
                imgd = camara.filtroGaus(imagen = img)
                camara.guardar(imgd, 'imagenes/' + obj + str(k + inicio), tipo = 'jpg')
                inicio += 1
                imgd = camara.rotacion(imagen = img, grados = 90)
                camara.guardar(imgd, 'imagenes/' + obj + str(k + inicio), tipo = 'jpg')
                inicio += 1
                imgd = camara.rotacion(imagen = img, grados = 180)
                camara.guardar(imgd, 'imagenes/' + obj + str(k + inicio), tipo = 'jpg')
                inicio += 1
                imgd = camara.rotacion(imagen = img, grados = 270)
                camara.guardar(imgd, 'imagenes/' + obj + str(k + inicio), tipo = 'jpg')
                inicio += 1
                img = camara.voltear(imagen = img, tipo = t)


if __name__ == '__main__':
    crear()
