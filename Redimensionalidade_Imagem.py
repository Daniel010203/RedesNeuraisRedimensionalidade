import cv2
#mudança
# Read Image
img = cv2.imread('entrada.jpg')
# Display Image
cv2.imshow('Escala de Cinzas', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Applying Grayscale filter to image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh1 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY, 199, 5)

thresh2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY, 199, 5)

cv2.imshow('Média da vizinhança (Adaptive Mean)', thresh1)
cv2.waitKey(0)
cv2.imwrite('Media_Vizinhanca.jpg', thresh1)
cv2.imshow('Soma Ponderada (Adaptive Gaussian)', thresh2)
cv2.waitKey(0)
cv2.imwrite('Soma_Ponderada.jpg', thresh2)
cv2.destroyAllWindows()

# Saving filtered image to new file
cv2.imwrite('Escala_de_Cinzas.jpg', gray)
