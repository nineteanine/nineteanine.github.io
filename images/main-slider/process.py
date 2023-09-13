import cv2
import numpy as np

image = cv2.imread('pattern-10.jpg')
h,w,c = image.shape
image_new = np.zeros((h,w,c+1), np.uint8)
#image_new[:,:,3] = 255

#for i in range(h):
#    for j in range(w):
#        image_new[i,j,:3] = image[i,j]
#        a = np.mean(image[i,j])
#        if a == 35:
#            continue
#        a = np.max(image[i,j])
#        image_new[i,j,3] = a #min(255,a+35)
        #if image[i,j,0]<=38 and image[i,j,1]<=38:
        #    image_new[i,j,3] = 0


image = image[:, 128:-256]

cv2.imshow('image', image)

cv2.waitKey()

cv2.imwrite('pattern-10.png', image)