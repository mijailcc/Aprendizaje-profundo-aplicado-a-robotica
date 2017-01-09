import numpy as np
from Red import Red

def iniciar():
    datos = np.load('prueba.npy')
    objetos = ['esponja', 'haki', 'dador', 'dadov', 'dadoa', 'cubo']
    red = Red(Pesos = True)
    red.iniciar()
    aciertos = 0
    for i in range(2339):
        opcion = red.alimentar(datos[i][0])[0]
    	if opcion[0] > 0.5:
            if datos[i][1][0] == 1:
               aciertos += 1
               print 1
            else:
               print 0
    	if opcion[1] > 0.5:
            if datos[i][1][1] == 1:
               aciertos += 1
               print 1
            else:
               print 0
    	if opcion[2] > 0.5:
            if datos[i][1][2] == 1:
               aciertos += 1
               print 1
            else:
               print 0
    	if opcion[3] > 0.5:
            if datos[i][1][3] == 1:
               aciertos += 1
               print 1
            else:
               print 0
    	if opcion[4] > 0.5:
            if datos[i][1][4] == 1:
               aciertos += 1
               print 1
            else:
               print 0
    	if opcion[5] > 0.5:
            if datos[i][1][5] == 1:
               aciertos += 1
               print 1
            else:
               print 0
    print "aciertos: " + str(aciertos)

if __name__ == '__main__':
    iniciar()
