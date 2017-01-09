from Camara import Camara
import time

def tomar():
    camara = Camara()
    for i in range(76):
        imagen = camara.imagen()
	camara.guardar(imagen, "nuevo1/dador" + str(i + 25), "jpg")	
	time.sleep(1)

if __name__ == '__main__':
    tomar()
