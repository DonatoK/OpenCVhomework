
import cv2 as cv
import sys
import numpy as np

src = cv.imread(sys.argv[1], 0)
imgcpy = cv.imread(sys.argv[1], 0)
cv.namedWindow("Original image", cv.WINDOW_AUTOSIZE)
cv.imshow("Original image", src)

mean = 0
sigma = 50
cv.randn(imgcpy,mean,sigma)        
imgcpy=cv.add(imgcpy,src)
cv.imshow("Gaussian Noise",   imgcpy)


boximg=cv.blur(imgcpy,(3,3))
cv.imshow("Box Filter",   boximg)

blurimg= cv.GaussianBlur(imgcpy,(3,3),1.5)
cv.imshow("Gaussian Filter",   blurimg)

medimg=cv.medianBlur(imgcpy,3)
cv.imshow("Median Filter",   medimg)

a=0.01          
pb=0.01 
info=src.shape
#source returns ( rows, columns,channels)
amount1=int(info[0]*info[1]*a)
amount2=int(info[0]*info[1]*pb)

#cv.randu(dst,low,high)
for val in range(0, amount1):
  holder1=int(np.random.uniform(0,info[0]))
  holder2=int(np.random.uniform(0,info[1]))
  src.itemset((holder1, holder2), 0)
  for val in range(0, amount2):
        holder3=int(np.random.uniform(0,info[0]))
        holder4=int(np.random.uniform(0,info[1]))
        src.itemset((holder3, holder4) , 255)

cv.imshow("Salt and Pepper Noise",   src)   

boximg=cv.blur(src,(3,3))
cv.imshow("Box Filter2",   boximg)

blurimg= cv.GaussianBlur(src,(3,3),1.5)
cv.imshow("Gaussian Filter2",   blurimg)

medimg=cv.medianBlur(src,3)
cv.imshow("Median Filter2",   medimg)

cv.waitKey(0)

