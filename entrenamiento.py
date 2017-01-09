import numpy as np
from Red import Red
from Camara import Camara
import numpy as np

def iniciar():
    datos = np.load('entrenamiento.npy')
    red = Red(Pesos = True)
    camara = Camara()
    arreglo = np.zeros(10)
    for i in np.arange(30):
        arreglo[i] = red.entrenamiento(datos)
        red.guardarPesos()
        red = Red(Pesos = True)
    np.savetxt('rendimiento.txt', arreglo)

if __name__ == '__main__':
    iniciar()
