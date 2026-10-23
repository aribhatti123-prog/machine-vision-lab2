import cv2
import numpy as np

img = cv2.imread('Bismarck.jpg', cv2.IMREAD_GRAYSCALE)
blur_img = cv2.GaussianBlur(img,(3,3),0)

cv2.namedWindow("Image")
while True:
    cv2.imshow("Image", img)
    if cv2.waitKey(0) == ord('q'):
        break
    cv2.imshow("Image", blur_img)
    if cv2.waitKey(0) == ord('q'):
        break
cv2.destroyWindow("Image")

