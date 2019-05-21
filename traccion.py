#Created by Juan Jaminton Yate on 20/04/19.
#Copyright © 2019 Juan Jaminton Yate. All rights reserved.

import RPi.GPIO as GPIO                         #inicializo los pines GPIO de la RPi
import time                                     #inicializo los timers y contadores de la RPi
import pygame                                   #inicializo la librería para la lectura de los botones del control del PS4
GPIO.setwarnings(False)
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
#motobomba PuenteH3 GPIO para motor DC
in9=2
in10=3
in11=4
in12=5

GPIO.setmode(GPIO.BCM)                          #configuro las salidas de los GPIO con el nombre natural de los pines en vez del orden de  los mismos
#inicializacion motores traccion
GPIO.setup(in1,GPIO.OUT)        #se declaran todos los pines para las entradas de los Puente Hs como salidas
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(in5,GPIO.OUT)
GPIO.setup(in6,GPIO.OUT)
GPIO.setup(in7,GPIO.OUT)
GPIO.setup(in8,GPIO.OUT)
GPIO.setup(in9,GPIO.OUT)
GPIO.setup(in10,GPIO.OUT)
GPIO.setup(in11,GPIO.OUT)
GPIO.setup(in12,GPIO.OUT)
pwmin1=GPIO.PWM(in1,20)        #se declaran todas las salidas anteriores como PWM con una frecuencia de 500 Hz
pwmin2=GPIO.PWM(in2,20)
pwmin3=GPIO.PWM(in3,20)
pwmin4=GPIO.PWM(in4,20)
pwmin5=GPIO.PWM(in5,20)
pwmin6=GPIO.PWM(in6,20)
pwmin7=GPIO.PWM(in7,20)
pwmin8=GPIO.PWM(in8,20)
pwmin9=GPIO.PWM(in9,20)
pwmin10=GPIO.PWM(in10,20)
pwmin11=GPIO.PWM(in11,20)
pwmin12=GPIO.PWM(in12,20)
pwmin1.start(0)                                 #se inicilizan los PWM con un ciclo de trabajo de 0%
pwmin2.start(0)
pwmin3.start(0)
pwmin4.start(0)
pwmin5.start(0)
pwmin6.start(0)
pwmin7.start(0)
pwmin8.start(0)
pwmin9.start(0)
pwmin10.start(0)
pwmin11.start(0)
pwmin12.start(0)
pygame.init()
j = pygame.joystick.Joystick(0) #se guarda la libreria de JoyStick en j para no volver a escribir todos los comandos mas que poner con j
j.init()                                        #se inicializa la libreria
print('Jostick iniciado : %s' % j.get_name())                                                   # se imprime el control de PS3 que esté conectado
apertura=1                                                                                                                      #se inicializa el valor del ciclo de trabajo de la apertura la garra
CicloDeTrabajo=0
try:
    while True:
        pygame.event.pump()                                                                             #se empieza librería para poder hacer lectura de los botones del control del PS3 como eventos
        if (j.get_axis(5) > -0.8) or (j.get_axis(2) > -0.8):             #giro derecha e izquierda
            if j.get_axis(5) > -0.8:
                CicloDeTrabajo = (j.get_axis(5)+1)*(50)            #multiplica el valor del la palanca por 100 para conseguir el cilco de trabajo de 0 a 100%
                pwmin1.ChangeDutyCycle(0)                       #conjunto de ciclos de trabajo para que camione hacia adelante
                pwmin2.ChangeDutyCycle(CicloDeTrabajo)
                pwmin3.ChangeDutyCycle(0)
                pwmin4.ChangeDutyCycle(CicloDeTrabajo)
                pwmin5.ChangeDutyCycle(CicloDeTrabajo)
                pwmin6.ChangeDutyCycle(0)
                pwmin7.ChangeDutyCycle(CicloDeTrabajo)
                pwmin8.ChangeDutyCycle(0)
                print(CicloDeTrabajo)
            if j.get_axis(2) > -0.8:
                CicloDeTrabajo = (j.get_axis(2)+1)*(50)            #se multiplica por 100 para llegar al ciclo de trabajo de 0 a 100 %
                pwmin1.ChangeDutyCycle(CicloDeTrabajo)          #conjunto de PWM para que camine hacia atras
                pwmin2.ChangeDutyCycle(0)
                pwmin3.ChangeDutyCycle(CicloDeTrabajo)
                pwmin4.ChangeDutyCycle(0)
                pwmin5.ChangeDutyCycle(0)
                pwmin6.ChangeDutyCycle(CicloDeTrabajo)
                pwmin7.ChangeDutyCycle(0)
                pwmin8.ChangeDutyCycle(CicloDeTrabajo)
                print(CicloDeTrabajo)
        elif (j.get_axis(0) > 0.2) or (j.get_axis(0) < -0.2):             #adelante y atras, para que funcione solo cuando la palanca izquierda esté a más de 20% de la amplitud total
            if j.get_axis(0) < -0.2:                                        #para movimiento del eje Y hacia arriba
                CicloDeTrabajo = j.get_axis(0)*(-100)          #multiplica el valor del la palanca por 100 para conseguir el cilco de trabajo de 0 a 100%
                pwmin1.ChangeDutyCycle(0)                       #conjunto de PWM para que el robot gire a la derecha
                pwmin2.ChangeDutyCycle(CicloDeTrabajo)
                pwmin3.ChangeDutyCycle(0)
                pwmin4.ChangeDutyCycle(CicloDeTrabajo)
                pwmin5.ChangeDutyCycle(0)
                pwmin6.ChangeDutyCycle(CicloDeTrabajo)
                pwmin7.ChangeDutyCycle(0)
                pwmin8.ChangeDutyCycle(CicloDeTrabajo)
                print(CicloDeTrabajo)
            if j.get_axis(0) > 0.2:                                                         #con el movimiento del eje y hacia abajo
                CicloDeTrabajo= j.get_axis(0)*(100) 
                pwmin1.ChangeDutyCycle(CicloDeTrabajo)          #conjunto de PWM para que el robot gire a la izquierda
                pwmin2.ChangeDutyCycle(0)
                pwmin3.ChangeDutyCycle(CicloDeTrabajo)
                pwmin4.ChangeDutyCycle(0)
                pwmin5.ChangeDutyCycle(CicloDeTrabajo)
                pwmin6.ChangeDutyCycle(0)
                pwmin7.ChangeDutyCycle(CicloDeTrabajo)
                pwmin8.ChangeDutyCycle(0)
                print(CicloDeTrabajo)
        if (j.get_axis(4) < -0.2):             #adelante y atras, para que funcione solo cuando la palanca izquierda esté a más de 20% de la amplitud total
            CicloDeTrabajo = j.get_axis(4)*(-100)          #multiplica el valor del la palanca por 100 para conseguir el cilco de trabajo de 0 a 100%
            pwmin9.ChangeDutyCycle(0)                       #conjunto de PWM para que el robot gire a la derecha
            pwmin10.ChangeDutyCycle(CicloDeTrabajo)
            pwmin11.ChangeDutyCycle(0)
            pwmin12.ChangeDutyCycle(CicloDeTrabajo)
            print(CicloDeTrabajo)
        else:
            pwmin1.ChangeDutyCycle(0)          #conjunto de PWM para que el robot gire a la izquierda
            pwmin2.ChangeDutyCycle(0)
            pwmin3.ChangeDutyCycle(0)
            pwmin4.ChangeDutyCycle(0)
            pwmin5.ChangeDutyCycle(0)
            pwmin6.ChangeDutyCycle(0)
            pwmin7.ChangeDutyCycle(0)
            pwmin8.ChangeDutyCycle(0)
            pwmin9.ChangeDutyCycle(0)
            pwmin10.ChangeDutyCycle(0)
            pwmin11.ChangeDutyCycle(0)
            pwmin12.ChangeDutyCycle(0)
            
        

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
                
