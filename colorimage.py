import cv2 as cv
import sys
import numpy as np

src = cv.imread(sys.argv[1], cv.IMREAD_COLOR)
cv.namedWindow("Original image", cv.WINDOW_AUTOSIZE)
cv.imshow( "Original image", src)
px=src[20,25]
print(px)
r,g,b=cv.split(src)
cv.imshow("Red",   r)
cv.imshow("Green", g)
cv.imshow("Blue", b)

ycrcb_image=cv.cvtColor(src,cv.COLOR_BGR2YCrCb)
px=ycrcb_image[20,25]
print(px)
y,Cb,Cr= cv.split(ycrcb_image)
cv.imshow("Y",   y);
cv.imshow("Cb",  Cb);
cv.imshow("Cr",  Cr);

hsv_image=cv.cvtColor(src, cv.COLOR_BGR2HSV)
px=hsv_image[20,25]
print(px)
h,s,v= cv.split(hsv_image)
cv.imshow("hue",        h);
cv.imshow("Saturation", s);
cv.imshow("Value",      v);

cv.waitKey(0)

