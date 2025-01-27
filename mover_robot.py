# Incorporar la funcion que dota de movimiento al robot
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
    ball_positions = []

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
                ball_positions.append((int(x), int(y), color))

    return pelota_detectada, ball_positions

def move_robot(offset_x, offset_y):
    # Example logic to move the robot based on the offsets
    if abs(offset_x) > 20:  # Threshold to avoid small movements
        if offset_x > 0:
            print("Mover derecha")
            # Send command to move derecha
        else:
            print("Mover izquierda")
            # Send command to move izquierda

    if abs(offset_y) > 20:  # Threshold to avoid small movements
        if offset_y > 0:
            print("Mover abajo")
            # Send command to move down
        else:
            print("Mover arriba")
            # Send command to move up

camera = cv.VideoCapture(0)
if not camera.isOpened():
    exit()

current_ball = None

while True:
    ret, frame = camera.read()
    if not ret:
        break

    procesar_frame, ball_positions = detectar_pelota(frame)

    if current_ball is None and ball_positions:
        current_ball = ball_positions[0]
    elif current_ball:
        # Check if the current ball is still visible
        visible = False
        for pos in ball_positions:
            if pos[2] == current_ball[2]:  # Check if the color matches
                current_ball = pos
                visible = True
                break
        if not visible:
            current_ball = ball_positions[0] if ball_positions else None

    if current_ball:
        cv.circle(procesar_frame, (current_ball[0], current_ball[1]), 10, (255, 0, 0), -1)
        frame_center_x = frame.shape[1] // 2
        frame_center_y = frame.shape[0] // 2
        ball_x, ball_y = current_ball[0], current_ball[1]
        offset_x = ball_x - frame_center_x
        offset_y = ball_y - frame_center_y
        move_robot(offset_x, offset_y)

    cv.imshow('frame', procesar_frame)

    if cv.waitKey(1) == ord('q'):
        break

camera.release()
cv.destroyAllWindows()