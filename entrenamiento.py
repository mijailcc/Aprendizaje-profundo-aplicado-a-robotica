import numpy as np
from Red import Red
from Camara import Camara
import numpy as np

def iniciar():
    datos = np.load('datos.npy')
    img = datos[9][0]
    red = Red()
    camara = Camara()
    arreglo = np.zeros(10)
    for i in np.arange(10):
        arreglo[i] = red.entrenamiento(datos)
        red.guardarPesos()
        red = Red(Pesos = True)
    print red.alimentar(img)
    camara.guardar(img, 'prueba')
    np.savetxt('rendimiento.out', arreglo)

if __name__ == '__main__':
    iniciar()
