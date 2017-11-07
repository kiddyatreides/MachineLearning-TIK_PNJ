# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 09:46:39 2017

@author: kiddyatreides
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 08:56:00 2017

@author: kiddyatreides
"""

import cv2
import pylab as pl
from PIL import Image
from numpy import array

im = array(Image.open('orang.jpg'))
pl.imshow(im) #plot image

x = [100, 100, 400,400]
y = [200, 500, 200, 500]

#plot titik dengan penanda garis merah
pl.plot(x,y,'r*')

#line plot
pl.plot(x[:2],y[:2])

#mengubah title
pl.title('Plot: "orang.jpg"')
pl.show()

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread('orang.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=1,
        minSize =(30,30),
        flags = cv2.CASCADE_SCALE_IMAGE
        )
		

print("Found {0} face(s)!".format(len(faces)))

#Draw rectangle
for(x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h),(0,255,0),2)
cv2.imshow("Faces found",img)
cv2.waitKey(0)