import cv2
image = cv2.imread("img1.png")
print(image.shape)
print(image[10, 744])
print(image[744, 10])
cv2.imshow("Image", image)
cv2.waitKey(0)
