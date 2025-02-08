import cv2
import numpy as np

# Imagen en blanco para dibujar
canvas = np.zeros((500, 500, 3), dtype='uint8')
# Función de callback para manejar el clic del ratón
def dibujar(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Dibujar un círculo donde se hizo clic
        cv2.circle(canvas,(x,y),20,(255,0,0),-1)
        
# Configurar ventana y callback
cv2.namedWindow("Dibuja con el ratón")
cv2.setMouseCallback("Dibuja con el ratón", dibujar)

while True:
    cv2.imshow("Dibuja con el ratón", canvas)
    if cv2.waitKey(1) & 0xFF == 27: # Presiona ESC para salir
        break
cv2.destroyAllWindows()
