import cv2

# Cargar la imagen original
imagen = cv2.imread("ejemplo.jpg")
# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
# Detectar bordes usando el algoritmo Canny
bordes = cv2.Canny(gris, 100, 200)
# Convertir los bordes a una imagen de 3 canales
bordes_color = cv2.cvtColor(bordes, cv2.COLOR_GRAY2BGR)
# Superponer los bordes sobre la imagen original
resaltada = cv2.addWeighted(imagen,  0.6,bordes_color, 0.4, 0)
# Mostrar las imágenes
cv2.imshow("Original", imagen)
cv2.imshow("Bordes", bordes)
cv2.imshow("Resaltada",resaltada )
cv2.waitKey(0)
cv2.destroyAllWindows()