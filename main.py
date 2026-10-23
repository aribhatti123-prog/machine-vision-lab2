import cv2
import numpy as np

img = cv2.imread('Bismarck.jpg', cv2.IMREAD_GRAYSCALE)
blur_img = cv2.GaussianBlur(img,(9,9),0)
box_img = cv2.boxFilter(img, -1, (9,9))

high_blur = img - blur_img
high_box = img - box_img

cv2.namedWindow("Image")
while True:
    cv2.imshow("Image", img)
    if cv2.waitKey(0) == ord('q'):
        break
    cv2.imshow("Image", high_blur)
    if cv2.waitKey(0) == ord('q'):
        break
    cv2.imshow("Image", high_box)
    if cv2.waitKey(0) == ord('q'):
        break
cv2.destroyWindow("Image")

