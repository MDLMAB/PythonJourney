import cv2 as cv                                                       # OpenCV
import numpy as np                                                     # Numpy
import RPi.GPIO as GPIO                                                # GPIO
import time                                                            # Time
from collections import deque                                          # Deque

colores_hsv = {
    'rojo': (np.array([0, 120, 70]), np.array([10, 255, 255])),
    'amarillo': (np.array([20, 100, 100]), np.array([40, 255, 255]))
}                                                                       # Definir los colores en HSV
tamanio_pelota_lab = 100                                                # Tamaño de la pelota
tamanio_minimo = 10                                                     # Tamaño mínimo de la pelota

last_positions = deque(maxlen=5)                                        # Deque para almacenar las últimas posiciones de la pelota

GPIO.setwarnings(False)                                                 # Desactivar advertencias
GPIO.setmode(GPIO.BCM)                                                  # Modo BCM

TRIG = 22                                                               # Definir los pines
ECHO = 27
BUZZER_PIN = 4 

AIN1 = 12 
AIN2 = 13 
ENA = 6 

BIN1 = 20 
BIN2 = 21 
ENB = 26 

GPIO.setup(TRIG,GPIO.OUT,initial=GPIO.LOW)                           # Configurar los pines
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(AIN1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(AIN2,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(ENA,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(BIN1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(BIN2,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(ENB,GPIO.OUT,initial=GPIO.LOW)

pwm_izquierdo = GPIO.PWM(ENA,500)                                   # Configurar los pines PWM
pwm_derecho = GPIO.PWM(ENB,500) 
pwm_izquierdo.start(40)                                             # Iniciar la velocidad PWM
pwm_derecho.start(40) 

def medir_distancia():                                              # Función para medir la distancia con el ultrasonido
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)  
    GPIO.output(TRIG, GPIO.LOW)
    
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start
    distancia = (pulse_duration * 34300) / 2
    
    return distancia

def retroceder():                                                  # Función para mover el robot hacia atrás
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(BIN1, GPIO.HIGH)
    GPIO.output(BIN2, GPIO.LOW)
    
def avanzar():                                                     # Función para mover el robot hacia adelante
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.HIGH)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.HIGH)
    
def detener():                                                     # Función para detener el robot
    pwm_izquierdo.ChangeDutyCycle(0)
    pwm_derecho.ChangeDutyCycle(0)
    
def girar_izquierda():                                              # Función para girar el robot hacia la izquierda
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.HIGH)

def girar_derecha():                                                # Función para girar el robot hacia la derecha
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.HIGH)
    GPIO.output(BIN1, GPIO.HIGH)
    GPIO.output(BIN2, GPIO.LOW)

def detectar_pelota(frame):                                         # Función para detectar la pelota en el frame de la cámara
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)                      # Convertir el frame a HSV
    kernel = np.ones((3, 3), np.uint8)                              # Kernel para el filtro morfológico
    pelota_detectada = frame.copy()                                 # Copiar el frame para dibujar la pelota detectada
    ball_positions = []                                             # Lista para almacenar las posiciones de la pelota

    for color, (bajo, alto) in colores_hsv.items():                # Iterar sobre los colores definidos
        mascara = cv.inRange(hsv, bajo, alto)
        mascara_filtrada = cv.morphologyEx(mascara, cv.MORPH_OPEN, kernel)
        mascara_filtrada = cv.morphologyEx(mascara_filtrada, cv.MORPH_CLOSE, kernel)
        contornos, _ = cv.findContours(mascara_filtrada, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        for contorno in contornos:                               # Iterar sobre los contornos
            area = cv.contourArea(contorno)
            if area < tamanio_pelota_lab:  
                continue

            ((x, y), radio) = cv.minEnclosingCircle(contorno)   # Encontrar el círculo mínimo que rodea el contorno
            if radio > tamanio_minimo:
                circularidad = (4 * np.pi * area) / (cv.arcLength(contorno, True) ** 2) # Calcular la circularidad
                if circularidad < 0.65:                        # Filtrar por circularidad
                    continue

                cv.circle(pelota_detectada, (int(x), int(y)), int(radio), (0, 255, 0), 2) # Dibujar el círculo
                cv.putText(
                    pelota_detectada,
                    color,
                    (int(x) - 20, int(y) - 20),
                    cv.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2,
                )
                ball_positions.append((int(x), int(y), color)) # Almacenar la posición de la pelota

    return pelota_detectada, ball_positions

def move_robot(offset_x, offset_y):                           # Función para mover el robot en el plano X, no se usa el Y
    if abs(offset_x) > 20:  
        if offset_x > 0:
            print("Mover derecha")
            girar_derecha()
        else:
            print("Mover izquierda")
            girar_izquierda()

    else:
        print("Adelante")
        avanzar()

camera = cv.VideoCapture(0)                                    # Iniciar la cámara con instancia 0
if not camera.isOpened():
    exit()

current_ball = None                                            # Iniciar Pelota actual

while True:                                                      # Loop principal
    ret, frame = camera.read()
    if not ret:
        break

    procesar_frame, ball_positions = detectar_pelota(frame)     # Detectar la pelota en el frame

    if current_ball is None and ball_positions:                 # Si no hay pelota actual, seleccionar la primera pelota detectada
        current_ball = ball_positions[0]                        # como la pelota actual
    elif current_ball:                                          # Si hay una pelota actual, verificar si sigue siendo visible
        visible = False                                         # en el frame actual
        for pos in ball_positions:                              # Iterar sobre las posiciones de la pelota detectadas
            if pos[2] == current_ball[2]:                       # Si el color de la pelota actual es el mismo que el color de la pelota detectada
                current_ball = pos                              # Actualizar la pelota actual
                visible = True                                  # Marcar la pelota como visible
                break                                            # Salir del bucle
        if not visible:
            current_ball = ball_positions[0] if ball_positions else None

    if current_ball:                                           # Si hay una pelota actual, dibujar un círculo en su posición
        cv.circle(procesar_frame, (current_ball[0], current_ball[1]), 10, (255, 0, 0), -1)
        frame_center_x = frame.shape[1] // 2
        frame_center_y = frame.shape[0] // 2
        ball_x, ball_y = current_ball[0], current_ball[1]
        offset_x = ball_x - frame_center_x
        offset_y = ball_y - frame_center_y
        
        distancia = medir_distancia()                    # Medir la distancia con el sensor ultrasonido
        if distancia < 2:                                # Si la distancia es menor a 2 cm, detener el robot y hacer sonar el buzzer
            detener()                                 
            GPIO.output(BUZZER_PIN, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(BUZZER_PIN, GPIO.LOW)
            time.sleep(3)
            avanzar()
        else:
            move_robot(offset_x, offset_y)

    if ball_positions:                                  # Almacenar las últimas posiciones de la pelota
        last_positions.append(ball_positions[0])        # para suavizar el movimiento del robot

    if last_positions:                                  # Calcular la posición promedio de la pelota
        avg_x = int(np.mean([pos[0] for pos in last_positions]))
        avg_y = int(np.mean([pos[1] for pos in last_positions]))
        current_ball = (avg_x, avg_y, 'amarillo')

    cv.imshow('frame', procesar_frame)                  # Mostrar el frame procesado

    if cv.waitKey(1) == ord('q'):                       # Salir del loop si se presiona la tecla 'q'
        break

camera.release()                                        # Liberar la cámara
cv.destroyAllWindows()                                  # Cerrar todas las ventanas