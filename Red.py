## Clase con la arquitectura de red neuronal del articulo.
## 4824-imagenet-classification-with-deep-convolutional-neural-networks
## Se necesita tener cuda y tensorflow

import tensorflow as tf
import numpy as np

class Red:

    ##constantes

    PESOS_ARCHIVO = 'pesos.npy'
    ANCHO = 224
    ALTO = 224
    RGB = 3
    SALIDA = 6
    FILTRO1 = [11, 11, 3, 48]
    FILTRO2 = [5, 5, 48, 128]
    FILTRO3 = [3, 3, 128, 192]
    FILTRO4 = [3, 3, 192, 192]
    FILTRO5 = [3, 3, 192, 128]
    ULTIMA_CAPA = [6, 4 * 4 * 128]
    SANCADA1 = [1, 1, 1, 1]
    SANCADA2 = [1, 2, 2, 1]
    SANCADA3 = [1, 3, 3, 1]
    SANCADA4 = [1, 4, 4, 1]
    REDIMENSION = [1 , 4 * 4 * 128]
    BIAS_OMISION = 1.0
    DESVIACION_PESOS = 0.01
    RADIO = 5
    ALPHA = 0.001
    BETA = 0.75
    K = 2
    PROB_DES = 0.5
    TAZA_APRENDIZAJE = 0.01
    MOMENTO = 0.9
    DECAIMIENTO_PESOS = 0.0005
    


    def __init__(self, Pesos=None):
        if Pesos is None:
            self.iniciarPesos()
        else:
            self.cargarPesos()

    def iniciarPesos(self):
        self.peso0 = tf.Variable(tf.truncated_normal(self.FILTRO1, stddev = self.DESVIACION_PESOS))
        self.peso1 = tf.Variable(tf.truncated_normal(self.FILTRO2, stddev = self.DESVIACION_PESOS))
        self.peso2 = tf.Variable(tf.truncated_normal(self.FILTRO3, stddev = self.DESVIACION_PESOS))
        self.peso3 = tf.Variable(tf.truncated_normal(self.FILTRO4, stddev = self.DESVIACION_PESOS))
        self.peso4 = tf.Variable(tf.truncated_normal(self.FILTRO5, stddev = self.DESVIACION_PESOS))
        self.peso5 = tf.Variable(tf.truncated_normal(self.ULTIMA_CAPA, stddev = self.DESVIACION_PESOS))

    def cargarPesos(self):
        self.pesos = np.load(self.PESOS_ARCHIVO)
        self.peso0 = tf.Variable(self.pesos[0])
        self.peso1 = tf.Variable(self.pesos[1])
        self.peso2 = tf.Variable(self.pesos[2])
        self.peso3 = tf.Variable(self.pesos[3])
        self.peso4 = tf.Variable(self.pesos[4])
        self.peso5 = tf.Variable(self.pesos[5])

    def guardarPesos(self):
        pesos = np.array([self.sess.run(self.peso0), self.sess.run(self.peso1), self.sess.run(self.peso2), self.sess.run(self.peso3), self.sess.run(self.peso4), self.sess.run(self.peso5)]) 
        np.save(self.PESOS_ARCHIVO, pesos)

    def propagacionAdelante(self):

        ##se guarda espacio
        self.X = tf.placeholder(tf.float32, shape=[None, self.ALTO, self.ANCHO, self.RGB])
        self.deseado = tf.placeholder(tf.float32, shape=[None, self.SALIDA])
        
        ##Primera capa
        CAPA1 = self.convolucion(self.X, self.peso0, self.SANCADA4, 0.0, self.FILTRO1[3])
        NCAPA1 = self.normalizacion(CAPA1, self.RADIO, self.ALPHA, self.BETA)
        self.CAPA1 = self.maximo(NCAPA1, self.SANCADA3, self.SANCADA1)
        self.CAPA1 = tf.nn.dropout(self.CAPA1, self.PROB_DES)

        ##Segunda capa
        CAPA2 = self.convolucion(self.CAPA1, self.peso1, self.SANCADA2, 1.0, self.FILTRO2[3])
        NCAPA2 = self.normalizacion(CAPA2, self.RADIO, self.ALPHA, self.BETA)
        self.CAPA2 = self.maximo(NCAPA2, self.SANCADA3, self.SANCADA1)
        self.CAPA2 = tf.nn.dropout(self.CAPA2, self.PROB_DES)
        
        ##Tercera capa
        CAPA3 = self.convolucion(self.CAPA2, self.peso2, self.SANCADA2, 0.0, self.FILTRO3[3])
        self.CAPA3 = self.normalizacion(CAPA3, self.RADIO, self.ALPHA, self.BETA)
        
        
        ##Cuarta capa
        CAPA4 = self.convolucion(self.CAPA3, self.peso3, self.SANCADA1, 1.0, self.FILTRO4[3])
        self.CAPA4 = self.normalizacion(CAPA4, self.RADIO, self.ALPHA, self.BETA)
        
        ##Quinta capa
        CAPA5 = self.convolucion(self.CAPA4, self.peso4, self.SANCADA1, 1.0, self.FILTRO5[3])
        NCAPA5 = self.normalizacion(CAPA5, self.RADIO, self.ALPHA, self.BETA)
        self.CAPA5 = self.maximo(NCAPA5, self.SANCADA2, self.SANCADA4)
        
        ##Sexta capa
        CAPA6 = tf.reshape(self.CAPA5, self.REDIMENSION)
        bias = tf.Variable(tf.constant(value = 0.0, shape=[self.SALIDA]))
        self.Y = tf.nn.softmax(tf.matmul(CAPA6, tf.transpose(self.peso5)) + bias)
        

    def alimentar(self, dato):
        ndato = np.array([dato])
        self.propagacionAdelante()
        self.sess = tf.Session()
        self.sess.run(tf.initialize_all_variables())
        return self.sess.run(self.Y, feed_dict={self.X : ndato})

    def convolucion(self, X, W, SANCADA, BIAS, TAM):
        conv = tf.nn.conv2d(X, W, strides = SANCADA, padding = 'SAME')
        bias =tf.Variable(tf.constant(value = BIAS, shape = [TAM]))
        suma = tf.nn.bias_add(conv, bias)
        return tf.nn.relu(suma)

    def maximo(self, X, TAM, SANCADA):
        return tf.nn.max_pool(X, ksize = TAM, strides = SANCADA, padding='SAME')

    def normalizacion(self, X, radio, alp, bet):
        return tf.nn.local_response_normalization(X, radio, bias = self.K, alpha = alp, beta = bet)

    def error(self):
        self.propagacionAdelante()
        self.entropia = tf.nn.softmax_cross_entropy_with_logits(self.Y, self.deseado)
        self.perdida = tf.reduce_mean(self.entropia)

    def entrenamiento(self, DATOS):
        self.error()
        #self.op_entrenamiento = tf.train.MomentumOptimizer(self.DECAIMIENTO_PESOS, self.MOMENTO).minimize(self.perdida)
        self.op_entrenamiento = tf.train.AdamOptimizer(1e-5).minimize(self.perdida)
        #self.op_entrenamiento =  tf.train.GradientDescentOptimizer(1.0).minimize(self.perdida)
        prediccion_correcta = tf.equal(tf.argmax(self.Y, 1), tf.argmax(self.deseado, 1))
        exactitud = tf.reduce_mean(tf.cast(prediccion_correcta, tf.float32))
        self.sess = tf.InteractiveSession()
        self.sess.run(tf.initialize_all_variables())
        n = 0
        for i in range(2094):
            lote = DATOS
            if i % 1 == 0:
                exactitud_entrenamiento = exactitud.eval(feed_dict={self.X : np.array([lote[i][0]]), self.deseado : np.array([lote[i][1]])})
                print("Paso: %d, Exactitud entrenamiento %g"%(i, exactitud_entrenamiento))
                n += exactitud_entrenamiento
            self.op_entrenamiento.run(feed_dict={self.X : np.array([lote[i][0]]), self.deseado : np.array([lote[i][1]])})
        return n
