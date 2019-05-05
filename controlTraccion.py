#Created by Juan Jaminton Yate on 20/04/19.
#Copyright © 2019 Juan Jaminton Yate. All rights reserved.

import RPi.GPIO as GPIO                         #inicializo los pines GPIO de la RPi
import time                                     #inicializo los timers y contadores de la RPi
import pygame                                   #inicializo la librería para la lectura de los botones del control del PS3
#servos salidas GPIO
garra=17
carrete=26
#lado izquierdo PuenteH1 GPIO para motor DC
in1=18
in2=19
in3=20
in4=21
#lado derecho PuenteH2 GPIO para motor DC
in5=22
in6=23
in7=24
in8=25

GPIO.setmode(GPIO.BCM)                          #configuro las salidas de los GPIO con el nombre natural de los pines en vez del orden de  los mismos

#inicializacion servos
GPIO.setup(garra,GPIO.OUT)      #se marca como salida el puerto del PWM para la garra
GPIO.setup(carrete,GPIO.OUT)    #se marca salida el puerto del PWM para el servo del carrete de hilo
pwmgarra=GPIO.PWM(garra,50)     #se declara que la salida de la garra es un PWM y se guarda en pwmgarra con 50 Hz de frecuencia
pwmcarrete=GPIO.PWM(carrete,50) #se decalra que la salida del servo para el carrete de hilo es un PWM y se guarda en pwmcarrete con 50 Hz de frecuencia
pwmgarra.start(0)                               #se inicia el PWM de la garra con 0% de cilco de trabajo
pwmcarrete.start(7)                             #el servo de rotacion continua empieza parado cuando se le pone un PWM de 7%

#inicializacion motores traccion
GPIO.setup(in1,GPIO.OUT)        #se declaran todos los pines para las entradas de los Puente Hs como salidas
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(in5,GPIO.OUT)
GPIO.setup(in6,GPIO.OUT)
GPIO.setup(in7,GPIO.OUT)
GPIO.setup(in8,GPIO.OUT)
pwmin1=GPIO.PWM(in1,500)        #se declaran todas las salidas anteriores como PWM con una frecuencia de 500 Hz
pwmin2=GPIO.PWM(in2,500)
pwmin3=GPIO.PWM(in3,500)
pwmin4=GPIO.PWM(in4,500)
pwmin5=GPIO.PWM(in5,500)
pwmin6=GPIO.PWM(in6,500)
pwmin7=GPIO.PWM(in7,500)
pwmin8=GPIO.PWM(in8,500)
pwmin1.start(0)                                 #se inicilizan los PWM con un ciclo de trabajo de 0%
pwmin2.start(0)
pwmin3.start(0)
pwmin4.start(0)
pwmin5.start(0)
pwmin6.start(0)
pwmin7.start(0)
pwmin8.start(0)
pygame.init()
j = pygame.joystick.Joystick(0) #se guarda la libreria de JoyStick en j para no volver a escribir todos los comandos mas que poner con j
j.init()                                        #se inicializa la libreria
print('Jostick iniciado : %s' % j.get_name())                                                   # se imprime el control de PS3 que esté conectado
apertura=1                                                                                                                      #se inicializa el valor del ciclo de trabajo de la apertura la garra

try:

                while True:
                                pygame.event.pump()                                                                             #se empieza librería para poder hacer lectura de los botones del control del PS3 como eventos
                                if (j.get_axis(1) > 0.2) or (j.get_axis(1) < -0.2):             #adelante y atras, para que funcione solo cuando la palanca izquierda esté a más de 20% de la amplitud total
                                                if j.get_axis(1) < -0.2:                                        #para movimiento del eje Y hacia arriba
                                                                CicloDeTrabajo = j.get_axis(1)*(-100)           #multiplica el valor del la palanca por 100 para conseguir el cilco de trabajo de 0 a 100%
                                                                if CicloDeTrabajo>100:                                          #si se llegara a pasar de 100% se regresa a 100%
                                                                                CicloDeTrabajo=100
                                                                pwmin1.ChangeDutyCycle(0)                       #conjunto de ciclos de trabajo para que camione hacia adelante
                                pwmin2.ChangeDutyCycle(CicloDeTrabajo)
                                pwmin3.ChangeDutyCycle(0)
                                pwmin4.ChangeDutyCycle(CicloDeTrabajo)
                                pwmin5.ChangeDutyCycle(CicloDeTrabajo)
                                pwmin6.ChangeDutyCycle(0)
                                pwmin7.ChangeDutyCycle(CicloDeTrabajo)
                                pwmin8.ChangeDutyCycle(0)
                                if j.get_axis(1) > 0.2:                                                         #con el movimiento del eje y hacia abajo
                                                CicloDeTrabajo= j.get_axis(1)*(100)            #se multiplica por 100 para llegar al ciclo de trabajo de 0 a 100 %
                                if CicloDeTrabajo>100:                                          #si se llegara a pasar de 100% se regresa a 100%
                                                CicloDeTrabajo=100
                                pwmin1.ChangeDutyCycle(CicloDeTrabajo)          #conjunto de PWM para que camine hacia atras
                                pwmin2.ChangeDutyCycle(0)
                                pwmin3.ChangeDutyCycle(CicloDeTrabajo)
                                pwmin4.ChangeDutyCycle(0)
                                pwmin5.ChangeDutyCycle(0)
                                pwmin6.ChangeDutyCycle(CicloDeTrabajo)
                                pwmin7.ChangeDutyCycle(0)
                                pwmin8.ChangeDutyCycle(CicloDeTrabajo)
                                
                                if (j.get_axis(1)> -0.2) and (j.get_axis(1)<0.2) and (j.get_axis(2)<0.2) and (j.get_axis(2)>-0.2):#robot parado si la palanca se encuentra a menos del 20% de su amplitud para darle un juego sin que se mueva
                                                pwmin1.ChangeDutyCycle(0)                                       #conjunto de PWM para que el robot se pare completamente
                                pwmin2.ChangeDutyCycle(0)
                                pwmin3.ChangeDutyCycle(0)
                                pwmin4.ChangeDutyCycle(0)
                                pwmin5.ChangeDutyCycle(0)
                                pwmin6.ChangeDutyCycle(0)
                                pwmin7.ChangeDutyCycle(0)
                                pwmin8.ChangeDutyCycle(0)
                                
                                if (j.get_axis(2) > 0.2) or (j.get_axis(2) < -0.2):             #giro derecha e izquierda
                                                if j.get_axis(2) < -0.2:
                                                                CicloDeTrabajo = j.get_axis(2)*(-100)           #multiplica el valor del la palanca por 100 para conseguir el cilco de trabajo de 0 a 100%
                                                                if CicloDeTrabajo>100:                                          #si se llegara a pasar de 100% se regresa a 100%
                                                                                CicloDeTrabajo=100
                                pwmin1.ChangeDutyCycle(0)                       #conjunto de PWM para que el robot gire a la derecha
                                pwmin2.ChangeDutyCycle(CicloDeTrabajo)
                                pwmin3.ChangeDutyCycle(0)
                                pwmin4.ChangeDutyCycle(CicloDeTrabajo)
                                pwmin5.ChangeDutyCycle(0)
                                pwmin6.ChangeDutyCycle(CicloDeTrabajo)
                                pwmin7.ChangeDutyCycle(0)
                                pwmin8.ChangeDutyCycle(CicloDeTrabajo)
                                if j.get_axis(2) > 0.2:
                                                CicloDeTrabajo = j.get_axis(2)*(100)            #multiplica el valor del la palanca por 100 para conseguir el cilco de trabajo de 0 a 100%
                                if CicloDeTrabajo>100:                                          #si se llegara a pasar de 100% se regresa a 100%
                                                CicloDeTrabajo=100
                                pwmin1.ChangeDutyCycle(CicloDeTrabajo)          #conjunto de PWM para que el robot gire a la izquierda
                                pwmin2.ChangeDutyCycle(0)
                                pwmin3.ChangeDutyCycle(CicloDeTrabajo)
                                pwmin4.ChangeDutyCycle(0)
                                pwmin5.ChangeDutyCycle(CicloDeTrabajo)
                                pwmin6.ChangeDutyCycle(0)
                                pwmin7.ChangeDutyCycle(CicloDeTrabajo)
                                pwmin8.ChangeDutyCycle(0)
                                if j.get_button(15):                                                                            #cuadrado, esto es para mover la garra.El PWM de funcionamiento es de 1 a 4%
                                                apertura += 1                                                                           #PWM de 1 % es la garra completamente cerrada y conforme se va aumentando el porcentaje se va abriendo hasta llegar a 4% que es completamente abirto
                                time.sleep(0.1)                                                                         #delay para ruido de boton
                                #pwmgarra.ChangeDutyCycle(10)#abrir
                                if j.get_button(13):                                                                            #circulo, para cerrar la garra restandole valores
                                                apertura -= 1
                                time.sleep(0.1)#delay para ruido de boton
                                #pwmgarra.ChangeDutyCycle(1)#cerrar
                                if apertura <= 0.5:                                                                             #esto permite que el PWM no baje de 0.5% para evitar errores
                                                apertura = 1                                                                            #y se regresa a 1%
                                pwmgarra.ChangeDutyCycle(apertura)
                                #time.sleep(0.2)                                
                                if j.get_button(12):                                                                            #cuando se aprieta el trianngulo
                                                pwmcarrete.ChangeDutyCycle(6)                                   #sube la garra con el carrete
                                                time.sleep(0.25)                                                                #se espera medio segundo
                                                pwmcarrete.ChangeDutyCycle(7)                                   #se para el carrete
                                if j.get_button(14):                                                                            #cuando se aprieta el X
                                                pwmcarrete.ChangeDutyCycle(8)                                   #se baja la garra
                                                time.sleep(0.25)                                                                #se espera medio segundo
                                                pwmcarrete.ChangeDutyCycle(7)                                           #se para el carrete
                                if j.get_button(6):                                                                             #cuando se aprieta la flecha hacia abajo
                                                pwmcarrete.ChangeDutyCycle(7)                                   #se para el carrete

except KeyboardInterrupt:                                                                                       #se limpia todo el codigo si se interrumpe con Ctrl + C
                GPIO.cleanup()
                pwmin1.stop()
                pwmin2.stop()
                pwmin3.stop()
                pwmin4.stop()
                pwmin5.stop()
                pwmin6.stop()
                pwmin7.stop()
                pwmin8.stop()
                pwmgarra.stop()
                pwmcarrete.stop()

