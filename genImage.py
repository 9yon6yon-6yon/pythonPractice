import cv2
import numpy as np
from numpy.random import default_rng

# img = np.random.default_rng().integers(2,size=(200,200),dtype=np.uint8)
# img = np.array(img*255)


img1 = np.zeros((40, 40), np.uint8)
img2 = np.full((40, 40), 0, np.uint8)
img3 = np.zeros((40, 40), np.uint8)
stackVer = np.vstack((img1, img2, img3))
stackVer = np.array(stackVer, np.uint8)


cv2.imshow('Image', stackVer)
cv2.waitKey(0)
cv2.destroyAllWindows()

