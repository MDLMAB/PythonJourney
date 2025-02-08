import cv2

# Cargar una imagen
imagen = cv2.imread("ejemplo.jpg")
# Convertir la imagen a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
# Aplicar un desenfoque gaussiano
desenfoque_gaussiano = cv2.GaussianBlur(gris, (15,15), 0)
# Aplicar un filtro bilateral
filtro_bilateral = cv2.bilateralFilter(gris, 9,75 ,75 )
# Mostrar las imágenes
cv2.imshow("Original", imagen)
cv2.imshow("Gris", gris)
cv2.imshow("Desenfoque Gaussiano", desenfoque_gaussiano)
cv2.imshow("Filtro Bilateral",filtro_bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()