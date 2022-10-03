import cv2
print("Package imported")

img = cv2.imread("resources/lena.jpg")

cv2.imshow("Output", img)
cv2.waitKey(0)
#print(img)
