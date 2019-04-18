import cv2

#读取图片，并改变图片大小
img =cv2.imread('me1.jpg')
img = cv2.resize(img,(500,660))
cv2.imwrite('img.jpg',img)

#同上
img1 = cv2.imread('me.jpg')
img1 = cv2.resize(img1,(500,660))
cv2.imwrite('img1.jpg',img1)

