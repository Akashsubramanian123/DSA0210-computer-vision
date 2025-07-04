import cv2
img = cv2.imread('C:/Users/akash/downloads/master_vijay.jpg')
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_img.jpg',gray_img)