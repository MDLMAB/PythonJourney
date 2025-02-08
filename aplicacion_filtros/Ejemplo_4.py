import cv2

# Cargar la imagen
imagen = cv2.imread("ejemplo.jpg", cv2.IMREAD_GRAYSCALE)
# Binarizar la imagen
_, binaria = cv2.threshold(imagen,128 ,255 , cv2.THRESH_BINARY)
# Encontrar contornos
contornos,_ = cv2.findContours(binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Cargar la imagen original en color
imagen_color = cv2.imread("ejemplo.jpg")
# Dibujar contornos en la imagen original
cv2.drawContours(imagen_color, contornos, -1, (255,0 ,0 ), 2)
# Mostrar la imagen resultante
cv2.imshow("Contornos", imagen_color)
cv2.waitKey(0)
cv2.destroyAllWindows()