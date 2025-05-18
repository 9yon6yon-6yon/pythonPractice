'''images are collection of arrays.
Gray scale image : only one color space with gray color between [0 - 255] where 0 means black and 255 means white ::: 1D
Colored image : Consists of 3 colors RGB (RED GREEN BLUE) ::: 3D
HSV color space: 3 channels (HUE SATURATION VALUE)
'''
import numpy as np
import cv2


img = cv2.imread('absolute-cinema.png')
# cv2.imwrite("newImage.png",img)
'''binarizing an image'''

grayImage = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

ret, thresh = cv2.threshold(grayImage, 0, 255, cv2.THRESH_BINARY)

'''numpy to show get the array value'''
# grayNP = np.array(grayImage)
# print(np.unique(grayNP))


'''rotating an image'''
# rotate = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)

vStack = np.vstack((grayImage, thresh))
vStack = np.array(vStack)
'''contours pre-processing'''

contours, h = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))

'''displaying an image in a window'''

cv2.imshow('window of image', vStack)
cv2.waitKey(0)
cv2.destroyAllWindows()
