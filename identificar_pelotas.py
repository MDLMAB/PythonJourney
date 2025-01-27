import cv2 as cv
import numpy as np


colores_hsv = {
    'rojo': (np.array([0, 120, 70]), np.array([10, 255, 255])),
    'amarillo': (np.array([20, 100, 100]), np.array([40, 255, 255]))
}
tamanio_pelota_lab = 100
tamanio_minimo = 10

def detectar_pelota(frame):
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    kernel = np.ones((3, 3), np.uint8)     
    pelota_detectada = frame.copy()

    for color, (bajo, alto) in colores_hsv.items():
        
        mascara = cv.inRange(hsv, bajo, alto)
        mascara_filtrada = cv.morphologyEx(mascara, cv.MORPH_OPEN, kernel)
        mascara_filtrada = cv.morphologyEx(mascara_filtrada, cv.MORPH_CLOSE, kernel)

        
        contornos, _ = cv.findContours(mascara_filtrada, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        for contorno in contornos:
            
            area = cv.contourArea(contorno)
            if area < tamanio_pelota_lab:  
                continue


            ((x, y), radio) = cv.minEnclosingCircle(contorno)
            if radio > tamanio_minimo:
                
                circularidad = (4 * np.pi * area) / (cv.arcLength(contorno, True) ** 2)
                if circularidad < 0.65:  
                    continue


                cv.circle(pelota_detectada, (int(x), int(y)), int(radio), (0, 255, 0), 2)
                cv.putText(
                    pelota_detectada,
                    color,
                    (int(x) - 20, int(y) - 20),
                    cv.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2,
                )


    return pelota_detectada



camera = cv.VideoCapture(0)
if not camera.isOpened():
    exit()

while True:

    ret, frame = camera.read()
    
    img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    procesar_frame = detectar_pelota(frame)
    cv.imshow('frame', procesar_frame)

    if cv.waitKey(1) == ord('q'):
        break
     
camera.release()
cv.destroyAllWindows()
