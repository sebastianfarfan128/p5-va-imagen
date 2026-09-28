import cv2
# leer la imagen con cv2 = computer vision
img = cv2.imread('conejo.jpg')
# determinar el tipo de imagen numpy.ndarray
print(type(img))
# mostrar pixeles (254, 338, 3)
print(img.shape)
# mostrando imagen en ventana barra de titulo conejo0043
cv2.imshow('conejo0043', img)
## tiempo de espera
cv2.waitKey(0)
# destruir todas las ventanas
cv2.destroyAllWindows()