import cv2
import numpy as np
import matplotlib.pyplot as plt
#roi is the object or region of object we need to find
roi = cv2.imread('/orange.png')
hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
#target is the image we search in
target = cv2.imread('/abhiyaan_opencv_qn1.png')
hsvt = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)
# Find the histograms using calcHist.
M = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )
I = cv2.calcHist([hsvt],[0, 1], None, [180, 256], [0, 180, 0, 256] )
h,s,v = cv2.split(hsvt)

R=M/I

B = R[h.ravel(),s.ravel()]
B = np.minimum(B,1)
B = B.reshape(hsvt.shape[:2])

# apply a convolution with a circular disc
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
cv2.filter2D(B,-1,disc,B)
B = np.uint8(B)
cv2.normalize(B,B,0,255,cv2.NORM_MINMAX)

# Use thresholding to segment out the region
ret,thresh = cv2.threshold(B,10,255,0)

# Overlay images using bitwise_and
thresh = cv2.merge((thresh,thresh,thresh))
res = cv2.bitwise_and(target,thresh)

t=np.array(target).copy()
r,c=100,100
for i in range(0,res.shape[0]-r,100):
    print("")
    for j in range(0,res.shape[1]-c,100):
        print(np.mean(res[i:i+r,j:j+c,:]))
        if(np.mean(res[i:i+r,j:j+c,:])>3):
            t[i:i+100,j:j+2,0]=255
            t[i:i+2,j:j+100,0]=255
            t[i:i+100,j+98:j+100,0]=255
            t[i+98:i+100,j:j+100,0]=255
plt.imshow(t)
