## Clase que trabaja con cv2 para tomar una imagen o video.
## requiere de numpy y cv2

import Image
import numpy as np
import cv2

class Camara:

    ##constantes
    NOMBRE = 'video'
    VIDEO_ANCHO = 640
    VIDEO_ALTO = 480
    FPS = 20
    ANCHO = 224
    ALTO = 224
    RGB = 3

    def __init__(self, nombre = None):
        self.cap = cv2.VideoCapture(0)
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        if not(nombre is None):
            self.out = cv2.VideoWriter(nombre + '.avi',self.fourcc, self.FPS, (self.VIDEO_ANCHO, self.VIDEO_ALTO))
        else:
            self.out = cv2.VideoWriter(self.NOMBRE + '.avi',self.fourcc, self.FPS, (self.VIDEO_ANCHO, self.VIDEO_ALTO))


    def imagen(self):
        ret, imagen = self.cap.read()
        if ret:
            return imagen
        return None

    def grabarVideo(self, imagen = None):
        if imagen is None:
            imagen = self.imagen()
        if not(imagen is None):
            self.out.write(imagen)
        else:
            print 'Error imagen nula'

    def recortar(self, imagen = None, corteXI = 0, corteXD = 1, corteYI = 0, corteYD = 1):
        if imagen is None:
            imagen = self.imagen()
        (y, x, z) = imagen.shape
        if corteXI >= 0 and corteXI < corteXD and corteXD <= x and corteYI >= 0 and corteYI < corteYD and corteYD <= y:
            return imagen[corteYI : corteYD, corteXI : corteXD, : ]
        print 'Error cortes no validos'
        return None

    def guardar(self, imagen, nombre, tipo='png'):
        cv2.imwrite(nombre + '.' + tipo, imagen) 

    def redimensionar(self,imagen = None, ancho = 1, alto = 1):
        if imagen is None:
            imagen = self.imagen()
        return cv2.resize(imagen, None, fx = ancho, fy = alto, interpolation = cv2.INTER_CUBIC)

    def rotacion(self, imagen = None, puntRotacion = None, grados = 0):
        if imagen is None:
            imagen = self.imagen()
        (y, x, z) = imagen.shape
        if puntRotacion is None:
                puntRotacion = (x / 2, y / 2)
        matriz = cv2.getRotationMatrix2D(puntRotacion, grados, 1.0)
        return cv2.warpAffine(imagen, matriz, (x, y))

    def voltear(self, imagen = None, tipo = 0):
        if imagen is None:
            imagen = self.imagen()
        return cv2.flip(imagen, tipo)

    def filtroGaus(self, imagen = None, x = 5, y = 5):
        if imagen is None:
            imagen = self.imagen()
        return cv2.GaussianBlur(imagen, (x, y), 0)

    def cargar(self, nombre):
        return cv2.imread(nombre)
